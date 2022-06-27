import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = "mongodb+srv://J0hn1975:N1k0nD750@myfirstcluster.0yzye.mongodb.net/lyric_finder?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.errorhandler(404)
def page_not_found(error) -> object:
    """
    This function renders the error 404 page
    if incorrect url entered
    :param id: error indentifier
    :return render_template 404.html
    """
    return render_template('404.html'), 404


@app.route("/")
@app.route("/home")
def home() -> object:
    """
    This function renders the home page.
    :return render_template of index.html
    """
    return render_template("index.html")


@app.route("/get_lyrics")
def get_lyrics() -> object:
    """
    This function renders the lyrics page.
    :return render_template of lyrics.html
    """
    lyric = list(mongo.db.lyric_finder.find())
    return render_template("lyrics.html", lyric=lyric)


@app.route("/search", methods=["GET", "POST"])
def search() -> object:
    """
    This function allows the user to
    search the lyrics based on a search criteria
    :return render_template of lyrics.html
    """
    query = request.form.get("query")
    lyric = list(mongo.db.lyrics.find({"$text": {"$search": query}}))
    return render_template("lyrics.html", lyric=lyric)


@app.route("/register", methods=["GET", "POST"])
def register() -> object:
    """
    This function allows a new user to the site to register
    :return redirect to register page
    :return render_template register.html
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        mongo.db.users.insert_one({
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        })

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login() -> object:
    """
    This function allows the user to login.
    Checks if user and password already exist in database
    :return redirect to login page
    :return render_template login.html
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username) -> object:
    """
    This fucntion displays the user profile when they are logged on
    :param id: username
    :return render_template profile.html
    :return redirect to login page
    """
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout() -> object:
    """
    This function allows the user to logout and remove the user session cookie
    :return redirect to login page
    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_lyrics", methods=["GET", "POST"])
def add_lyrics() -> object:
    """
    This function allow the user to add lyrics using a predefined criteria
    :return redirect to get_lyrics
    :return render_template add_lyrics.html
    """
    if request.method == "POST":
        # add lyrics to the database
        lyrics = {
            "music_genre": request.form.get("music_genre"),
            "artist_name": request.form.get("artist_name"),
            "song_title": request.form.get("song_title"),
            "song_lyrics": request.form.get("song_lyrics"),
            "song_composer": request.form.get("song_composer"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.lyrics.insert_one(lyrics)
        flash("Lyrics Sucessfully Added")
        return redirect(url_for("get_lyrics"))

    genre = mongo.db.genre.find().sort("music_genre", 1)
    return render_template("add_lyrics.html", genre=genre)


@app.route("/edit_lyrics/<lyrics_id>", methods=["GET", "POST"])
def edit_lyrics(lyrics_id) -> object:
    """
    This function allows the lyrics to be edited by the user
    :param id: lyrics indentifier
    :return render_template edit_lyrics.html
    """
    if request.method == "POST":
        # pulls exisintg lyrics from the datebase to edit
        submit = {
            "music_genre": request.form.get("music_genre"),
            "artist_name": request.form.get("artist_name"),
            "song_title": request.form.get("song_title"),
            "song_lyrics": request.form.get("song_lyrics"),
            "song_composer": request.form.get("song_composer"),
            "image_url": request.form.get("image_"),
            "created_by": session["user"]
        }
        mongo.db.lyrics.update({"_id": ObjectId(lyrics_id)}, submit)
        flash("Lyrics Sucessfully Updated")

    lyric = mongo.db.lyrics.find_one({"_id": ObjectId(lyrics_id)})
    genre = mongo.db.genre.find().sort("music_genre", 1)
    return render_template("edit_lyrics.html", lyric=lyric, genre=genre)


@app.route("/delete_lyrics/<lyrics_id>")
def delete_lyrics(lyrics_id) -> object:
    """
    This function deletes the lyrics and all
    associated headings and album artwork
    :return redirect to get_lyrics
    """
    mongo.db.lyrics.remove({"_id": ObjectId(lyrics_id)})
    flash("Lyrics Successfully Deleted")
    return redirect(url_for("get_lyrics"))


@app.route("/get_genre")
def get_genres() -> object:
    """
    This function calls all the genres stored in the database
    :return render_template of genres.html
    """
    # adds genres to the database
    genre = list(mongo.db.genre.find().sort("music_genre", 1))
    return render_template("genres.html", genre=genre)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genres() -> object:
    """
    This function allows the admin user to add genres to the database
    :return redirect to get_genres page
    :return render_template add_genre.html
    """
    if request.method == "POST":
        genre = {
            "music_genre": request.form.get("music_genre")
        }
        mongo.db.genre.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id) -> object:
    """
    This function allows the genres to be edited by an admin user only
    :param id: genre indentifier
    :return redirect to get_genres
    :return render_template edit_genre.html
    """
    if request.method == "POST":
        submit = {
            "music_genre": request.form.get("music_genre")
        }
        mongo.db.genre.update({"_id": ObjectId(genre_id)}, submit)
        flash("Genre Successfully Updated")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genre.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id) -> object:
    """
    This function allows the genres to be deleted by an admin user only
    :param id: genre indentifier
    :return redirect to get_genres
    """
    mongo.db.genre.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_genres"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

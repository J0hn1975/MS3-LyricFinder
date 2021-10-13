# Santorini
![Responsive Mockup](docs/Mockups/AmIResponsive.PNG)

[You can visit the live site here](https://j0hn1975.github.io/MS2-Santorini/)

## Table of Contents
> 1. [Target Audience](#target-audience)
> 2. [Project Goals](#project-goals)
> 3. [The 5 Planes of UX](#the-5-planes-of-ux)  
    3.1 [Strategy](#strategy)  
    3.2 [Scope](#scope)  
          - i [User Stories](#user-stories)   
          - ii  [Site Owner Goals](#site-owner-goals)    
    3.3 [Structure](#structure)  
    3.4 [Skeleton](#skeleton)  
          - i [Wireframes](#wireframes)   
    3.5 [Surface](#surface)  
          - i [Colours](#colours)  
          - ii [Typography](#typography)  
          - iii [Imagery](#imagery)
> 4. [Features](#features)  
> 5. [Technolgies Used](#technolgies-used)
> 6. [Testing](#testing)  
>   6.1 [Code Validation](#code-validation)  
    6.2 [Device Tests](#device-tests)  
    6.3 [Browser Tests](#browser-tests)  
    6.4 [User Story Tests](#user-story-tests)  
> 7. [Bugs Fixes](#bugs)
> 8. [Deployment](#deployment)
> 10. [Credits](#credits)
> 11. [Acknowledgements](#acknowledgements)

## Target Audience
The audience ideally targerted are music lovers who enjoy finding out the lyrics to their favourite songs. 
On this site they will be view existing lyrics, as well as add and edit their own lyrics.


# The 5 Planes of UX
## Strategy
## Project Goals - Delete?
---
The primary business goals of this site are:
> * To promote the island of Santorini
> * Increase the number of vistors to the island
> * Provide inspiration for Santorini as a holiday destination

The primary cusomter goals of this site are:
> * Learn more about the island before visting
> * Contact the site owner with any additional questions or queries
> * Be inspired to choose Santorini as a viable holiday destination

## Scope
## User Stories
As a new or returning visitor I would like to see:
> 1. A site that is easy and clear to navigate
> 2. External social media links
> 3. A site that responds and provides feedback on my interactions
> 4. A site that I can interact with
> 5. As a user I would like to see a responsive site that can be used on mobile devices
> 6. An error page to show if I have enterted an incorrect URL
> 7. The ability to edit and delete lyrics added by the user
> 8. A site that has clear login and registration pages

## Admin/Site owner goals
The main goal of this site is to present song lyrics on a website that is easy to navigate
> 9. A way of contact the site owner with any issues related to the site
> 10. Present the end user with a clear and simple navigaion menu
> 11. The ability to add, edit and delete lyrics
> 12. Provide a quiz where the user can test their knowledge
> 13. Make a site that is responsive across all devices.
> 14. A site that provides feedback and validation.
> 15. On the 404 page the user shouldn't use the broswer back but instead the nav bar.
---

## Structure
The website has been structured with 4 web pages. Each page is cleary designed, easy to navigate, and with well layed out information. With a mobile first approach in mind I have used bootstrap throughout to make the site respoinsive on mobile devices.

> The 4 pages are:
> 1. Home Page: A welcome message, brief description of the island greet the user, as well as a map of where the island is located and the current weather forecast
> 2. Quiz Page: A 10 question quiz on Santorini, with progess indicators for each question, right and wrong answers are higlighted, with a table at the end showing overall progress
> 3. Contact Page: A contact page to allow the user to contact the site owner, warnings if the incorrect information has been entered and alert then the form is submitted.
> 4. 404: This alerts users if they have entered an incorrect URL for the site. The user is presented with warning message, navbar and footer.
---

## Skeleton
To design and develop the wireframes I first used Balsamiq, then used Snipping Tools to create PNG versions. The wireframes images are designed to collaspe.

## Wireframes
> <details><summary>Home Page</summary>
> <img src="https://github.com/J0hn1975/MS2-Santorini/blob/main/docs/Wireframes/Home/Home.PNG">
></details>
>
> <details><summary>Quiz Page</summary>
> <img src="https://github.com/J0hn1975/MS2-Santorini/blob/main/docs/Wireframes/Quiz/Quiz.PNG">
> </details>
> 
> <details><summary>Contact Page</summary>
> <img src="https://github.com/J0hn1975/MS2-Santorini/blob/main/docs/Wireframes/Contact/Contact.PNG">
> </details>
---

## Surface
## Colours
Each page is design with very simple colours and images to showcase the island. The colours I have used are as follows:
> - #FFCC51 - used as a background color for the footer and navbar
> - #050505 - used for the site brand and nav links
> - #009688 - used to style the quiz text.

## Typography
For the most part of I have used the Titilium Web Google font, with a fallback of Sans Serif should Titilium Web not work.

## Imagery
Througout the site I have used clear images showcasing Santorini's natural beauty.

## Design
> The site is made up of three pages, using a simple and clean design. 
> 

# Features
## Existing Features
### Feature 1: The Nav Bar
A boostrap and fully responsive nav bar, that has links to Home, Quiz and Contact pages. As part of it bootstrap functionality the nav bar displays as a burger menu on mobile devices. 
> ![Navbar](docs/Features/navbar.PNG)
> ![MobileNav](docs/Features/navbar_mobile.PNG)  
> User stories feature relates to:
> * 1.1 A site that is easy and clear to navigate
> * 1.12 As a user I would like to see a responsive site that can be used on mobile devices
> * 1.15 Present the end user with a clear and simple navigaion menu

### Feature 2: Weather Widget API
Weather Widget display the current weather for Santorini on the Home Page. When the widget is clicked it takes you to the Forcast7.com website for a more detailed forecast.
> ![Weather Widget](docs/Features/weatherwidget.PNG)
> 24hr Forecast  
> ![Weather Widget 24hr](docs/Features/weather24.PNG)  
> 7 Day Forecast  
> ![Weather Widget 7Day](docs/Features/weather7days.PNG)  
> User stories feature realtes to:  
> * 2.3 The current weather conditions in Santorini
> * 2.13 Display the current weather in Santorini

### Feature 3: Google Maps API
Google maps API to that shows the exact location of Sanitorini.
> ![Google Maps API](docs/Features/map.PNG)  
> User stories feature relates to:
> * 3.2 A map of where Santorini is located
> * 3.18 Display a map of Santorini

### Feature 4: Footer
Footer that displays the site name and two social links; one to youtube and one to Tripadvisor
> ![Footer](docs/Features/footer.PNG)  
> User stories feature relates to:
> * 4.4 External social media links to find out more about the island

### Feature 5: Home Page
Home page that displays a welcome message and short description of the island. A nav bar, footer, google map and weather forecast are displayed to
> ![Home Page](docs/Features/homepage.PNG)  
> USer stories this feature relates to:
> * 5.1 A site that is easy and clear to navigate
> * 5.3 The current weather conditions in Santorini

### Feature 6: Quiz Page
A quiz to that the knowledge of the end user, that responds to and validates user input
> ![Quiz Page](docs/Features/quizpage.PNG)   
> ![Quiz Started](docs/Features/quiz.PNG)  
The quiz displays the right and or wrong answer  
> ![RightWrongAnswer](docs/Features/right_wrong_answer.PNG)  
At the end of the quiz an table displays overall progress with buttons to leave table or start quiz again  
> ![Quiz Results](docs/Features/quiz_result.PNG)  
> User stories the features relates to:  
> * 6.5 An informative quiz where I can test my knowledge on Santorini
> * 6.6 Feedback on which answers I have got right
> * 6.7 A final page that displays how well did on the quiz
> * 6.17 Provide a quiz where the user can test their knowledge
> * 6.19 A site that provides feedback and validation.

### Feature 7: Contact Page
A contact page to allow user to contact site owner. Form also displays validation, and message when form is submitted.
> ![Contact](docs/Features/contactpage.PNG)
Name Validation  
> ![Name Validation](docs/Features/namevalidation.PNG)   
Subject Validation       
> ![Subject Validation](docs/Features/subjectvalidation.PNG)  
Email Validation   
> ![Email Validation](docs/Features/emailvalidation.PNG)  
Message Validation      
> ![Message Validation](docs/Features/messagevalidation.PNG)  
Form Submitted      
> ![Form Submitted](docs/Features/formsubmitted.PNG)  
User stories the features relates to:   
> * 7.9 A contact page to get in touch with the site owner
> * 7.14 Display a contact form so the user can get in touch with the site owner
> * 7.19 A site that provides feedback and validation.  

### Feature 8: 404 Error Page
404 error page for when a user enters a incorrect URL
> ![404](docs/Features/404.PNG)  
User stories the features relates to:
> * 7.19 A site that provides feedback and validation.
> * 7.20 On the 404 page the user shouldn't use the broswer back but instead the nav bar
> * 8.13 An error page to show if I have enterted an incorrect URL
---

## Technolgies Used
> * HTML5
> * CSS3
> * Javascript
> * Google Maps Api
> * Weather Widget
> * Balsamiq

## Testing
## Code Validation
### CSS Validation
I have used the W3C CSS Validation Service - Jigsaw to check that my CSS is valid

|    Page     |               Result                |                       Screenshot                       |
| :---------: | :---------------------------------: | :----------------------------------------------------: |
| Entire Site | CSS Validation passed with 0 Errors | [View Results](docs/CSS-Validation/CSS_Validation.PNG) |
---

### HTML Validation
I have used the W3C Markup Validation Service to check my HTML is valid

|   Page       |  Result              |                      Screenshot                      |
|:------------:|:--------------------:|:----------------------------------------------------:|
|   Home       | 0 errors             | [View Results](docs/HTML-Validation/Home_Page.PNG)   |
|   Quiz       | 0 errors             | [View Results](docs/HTML-Validation/Quiz_Page.PNG)   |
|  Contact     | 0 errors             | [View Results](docs/HTML-Validation/Contact_Page.PNG)|
---

### Javascript Validation
I have used JS Hint to validate my Javascript.

|     Page     |        Result        |                         Screenshot                          |
|:------------:|:--------------------:|:-----------------------------------------------------------:|
|    form.js   | 0 errors, 0 warnings | [View Results](docs/Javascript-Validation/form.js.PNG)      |
|    map.js    | 0 errors, 0 warnings | [View Results](docs/Javascript-Validation/map.js.PNG)       |
|  question.js | 0 errors, 0 warnings | [View Results](docs/Javascript-Validation/question.js.PNG)  |
|    quiz.js   | 0 errors, 0 warnings | [View Results](docs/Javascript-Validation/quiz.js.PNG)      |
| sendemail.js | 0 errors, 0 warnings | [View Results](docs/Javascript-Validation/SendEmail.js.PNG) |
---

### WAVE Accessibilty
I have used the WAVE Web Accessibilty Evaluation Tool to ensure site is accessible

|   Page  |            Result           | Screenshot |
|:-------:|:---------------------------:|:----------:                                                                 
|   Home  | 0 errors, 0 contrast errors | [View results](/docs/WAVE-Accessibilty/index.html_Wave_Validation.PNG)      |
|   Quiz  | 0 errors, 0 contrast errors | [View results](/docs/WAVE-Accessibilty/quiz.html_Wave_Validation.PNG)       |
| Contact | 0 errors, 0 contrast errors | [View results](assets/docs/WAVE-Accessibilty/quiz.html_Wave_Validation.PNG) |
--- 

### Lighthouse Performance
I have used Google Lighthouse (in Google Dev tools) to measure the performance the site

|       Page        |                            Result                            |                        Screenshot                        |
| :---------------: | :----------------------------------------------------------: | :------------------------------------------------------: |
|  Home (Desktop)   | 97 Performance, 95 Accessibility, 87 Best Practices, 100 SEO |  [View Results](docs/Lighthouse/Desktop/index.html.PNG)  |
|  Quiz (Desktop)   | 99 Performance, 96 Accessibility, 93 Best Practices, 100 SEO |  [View Results](docs/Lighthouse/Desktop/quiz.html.PNG)   |
| Contact (Desktop) | 99 Performance, 96 Accessibility, 93 Best Practices, 100 SEO | [View Results](docs/Lighthouse/Desktop/contact.html.PNG) |
|   Home (Mobile)   | 77 Performance, 97 Accessibility, 87 Best Practices, 100 SEO |  [View Results](docs/Lighthouse/Mobile/index.html.PNG)   |
|   Quiz (Mobile)   | 84 Performance, 97 Accessibility, 93 Best Practices, 100 SEO |   [View Results](docs/Lighthouse/Mobile/quiz.html.PNG)   |
| Contact (Mobile)  | 88 Performance, 97 Accessibility, 93 Best Practices, 100 SEO | [View Results](docs/Lighthouse/Mobile/contact.html.PNG)  |
--- 

### Device Tests
The site has been tested on the following physical devices
> - Huawei P30 Pro
> - HP Envy 17 Laptop
> - Samsung Galaxy A31

Actual tests:
> 1. Home, Quiz, Contact nav links all go to the correct pages. Clicking the Santorini brand logo navigates back to the Home page from each page.
> 2. The nav collaspses to a burger menu, which pushes the content down when clicked on. All nav links work as expected here too.
> 3. The weather widget on the home page is responsive and when clicked on goes to the Forecast7.com website as expected.
> 4. The map of Santorini has a location pin showing its location on the island.
> 5. The text and images are clearly displayed.
> 6. Contact page does not allow user to move forward until all fields are completed. Error messages display if a field has not been filled out.
> 7. All pages are responsive.
> 8. The quiz page on mobile displays clearly. The correct and incorrect answers are easy to see.
> 9. The desription of the island does not display on mobiles, as it makes the Home page too cluttered.
> 10. Each nav link and logo brand text color change to white when clicked on.
> 11. A 404 error page will be displayed in the event of a incorrect URL being entered. The standard nav can be used to navigate back to the site pages.
> 12. The two social links both go to Youtube and Tripadvisor respectively, both open in separate pages.

Overall results:
> * The above physical tests passed on each device they were tested on. On the mobile version of Chrome however, the Aladin font used on the hero text falls back to cursive.

### Browser Tests
> * Firefox Developer Edition - All nav links, features and website work as expected
> * Google Chrome - All nav links, features and website work as expected
> * Firefox Developer Edition - All nav links, features and website work as expected

### User story tests
> 1. A site that is easy and clear to navigate

|                    Feature                    |             Test Steps             |           Expected            |       Actual       |
| :-------------------------------------------: | :--------------------------------: | :---------------------------: | :----------------: |
| A website that is easy and clear to navigate. | Clicked on nav links for each page | Pages to load when clicked on | Works as expected |

[User story screenshot](docs/Features/homepage.PNG)  

> 2. A map of where Santorini is located

|                   Feature                    |                          Test Steps                          |    Expected    |      Actual       |
| :------------------------------------------: | :----------------------------------------------------------: | :------------: | :---------------: |
| Display a map of where Santorini is located. | Navigate to home page where is map is clearly and prominently displayed | Map to display | Works as expected |  

[User story screen shot](docs/Features/homepage.PNG)  

> 3. The current weather conditions in Santorini

|                           Feature                           |       Test Steps        |               Expected                |      Actual       |
| :---------------------------------------------------------: | :---------------------: | :-----------------------------------: | :---------------: |
|       Display current weather conditions in Santorini       | Navigate to home page.  |       Weather Widget to display       | Works as expected |
| More detailed weahter forecast for the next 24hr and 7 days | Click on Weather Widget | Pass through to Forecast7.com website | Works as expected |

[User story screen shot](docs/Features/weatherwidgettest.PNG)

> 4. External social media links to find out more about the island

|                Feature                 |                          Test Steps                          |               Expected                |      Actual       |
| :------------------------------------: | :----------------------------------------------------------: | :-----------------------------------: | :---------------: |
| Social media links to external content | Click on Youtube and Tripadvisor social media links display in footer | Youtube Video and Tripadvisor to load | Works as expected |

> 5. An informative quiz where I can test my knowledge on Santorini

|                         Feature                         |                     Test Steps                      |           Expected            |      Actual       |
| :-----------------------------------------------------: | :-------------------------------------------------: | :---------------------------: | :---------------: |
| Find an informative quiz to test knowledge on Santorini | Navigate to quiz page, clicked on Start Quiz button | Quiz to start as question one | Works as expected |

[User story screen shot](docs/Features/quiztest.PNG)  

> 6. Feedback on which answers I have got right

|             Feature              |          Test Steps           |             Expected             |      Actual       |
| :------------------------------: | :---------------------------: | :------------------------------: | :---------------: |
| Show feedback on correct answers | Answered a question correctky | Correct answer to be highlighted | Works as expected |

[User story screen shot](docs/Features/right_wrong_answer.PNG)  

> 7. A final page that displays how well did on the quiz

|                  Feature                   |   Test Steps   |               Expected               |      Actual       |
| :----------------------------------------: | :------------: | :----------------------------------: | :---------------: |
| Display overall summay page at end of quiz | Completed quiz | Overall quiz summary to be displayed | Works as expected |

[User story screen shot](docs/Features/quiz_result.PNG)

> 8. An option to close out of the final page or play quiz again

|                    Feature                     |   Test Steps   |                    Expected                     |      Actual       |
| :--------------------------------------------: | :------------: | :---------------------------------------------: | :---------------: |
| Buttons to close out of quiz or start it again | Completed quiz | 'Try again' and 'Go to home' buttons to display | Works as expected |

[User story screen shot](docs/Features/endofquizbuttons.PNG)  

> 9. A contact page to get in touch with the site owner

|                   Feature                   |      Test Steps      |             Expected             |      Actual       |
| :-----------------------------------------: | :------------------: | :------------------------------: | :---------------: |
| Contact page for user to contact site owner | Clicked on quiz page | Contact form page to be displyed | Works as expected |

[User story screen shot](docs/Features/contactpage.PNG) 

> 10. A site that responds and provides feedback on my interactions

|                       Feature                       |             Test Steps              |                           Expected                           |      Actual       |
| :-------------------------------------------------: | :---------------------------------: | :----------------------------------------------------------: | :---------------: |
| Features that respond and provide feed back to user | Completed contact form, played quiz | User validation displyed on contact form. User progress on quiz displayed | Works as expected |

[User story screen shot](docs/Features/examplesofvalidation.PNG) 

> 11. A site that I can interact with

|              Feature              |               Test Steps                |                       Expected                       |      Actual       |
| :-------------------------------: | :-------------------------------------: | :--------------------------------------------------: | :---------------: |
| Interactive features on webs site | User can complete contact form and quiz | Contact form and quiz page for user to interact with | Works as expected |  

[User story screen shot](docs/Features/interactivefeatures.PNG)

> 12. As a user I would like to see a responsive site that can be used on mobile devices

|                   Feature                   |          Test Steps          |                           Expected                           |      Actual       |
| :-----------------------------------------: | :--------------------------: | :----------------------------------------------------------: | :---------------: |
| A site that is responsive on mobile devices | View site from mobile device | Site is responsive. Nav bar collapses to burger menu. Test each link. | Works as expected |

[User story screen shot](docs/Features/responsiveness.PNG)  

> 13. An error page to show if I have enterted an incorrect URL

|                         Feature                          |     Test Steps      |        Expected        |      Actual       |
| :------------------------------------------------------: | :-----------------: | :--------------------: | :---------------: |
| An error 404 will be displayed if incorrect URL entered. | Enter incorrect URL | Error 404 page to load | Works as expected |  

[User story screen shot](docs/Features/404.PNG)  

> 14. Display a contact form so the user can get in touch with the site owner

|                           Feature                            |        Test Steps         |                Expected                 |      Actual       |
| :----------------------------------------------------------: | :-----------------------: | :-------------------------------------: | :---------------: |
| Contact form for the user to get in touch with site owner with questions or queries | Navigated to contact page | Contact form to display on contact page | Works as expected |  

[User story screen shot](docs/Features/contact.PNG)  

> 15. Present the end user with a clear and simple navigaion menu

|                           Feature                            |                     Test Steps                     |            Expected             |      Actual       |
| :----------------------------------------------------------: | :------------------------------------------------: | :-----------------------------: | :---------------: |
| Present the end user with a clear and simple navigation menu | Loaded site where the nav bar is clearly layed out | Nav bar to display on each page | Works as expected |

[U er story screen shot](docs/Features/navbar.PNG)

> 16. Display the current weather in Santorini

|                       Feature                        |    Test Steps    |                   Expected                    |      Actual       |
| :--------------------------------------------------: | :--------------: | :-------------------------------------------: | :---------------: |
| Weather Widget displays current weather of Santorini | Loaded home page | Weather widget with daily forecast to display | Works as expected |

[User story screen shot](docs/Features/weatherwidget.PNG)

> 17. Provide a quiz where the user can test their knowledge

|                   Feature                    |    Test Steps    |           Expected           |      Actual       |
| :------------------------------------------: | :--------------: | :--------------------------: | :---------------: |
| Quiz page that contains informative question | Loaded quiz page | Quiz to display on page load | Works as expected |

[User story screen shot](docs/Features/quizpage.PNG)

> 18. Make a site that is responsive across all devices.

|                Feature                 |                   Test Steps                   |       Expected        |      Actual       |
| :------------------------------------: | :--------------------------------------------: | :-------------------: | :---------------: |
| Site created with mobile first in mind | Test across different devices (emulators used) | Site to be responsive | Works as expected |

[User story screen shot](docs/Features/deviceresponsivenness-2.png)

> 19. A site that provides feedback and validation.

|                   Feature                   |               Test Steps                |              Expected               |      Actual       |
| :-----------------------------------------: | :-------------------------------------: | :---------------------------------: | :---------------: |
| Site that provides feed back and validation | Completed quiz with provides validation | Validation to provided on questions | Works as expected |

[User story screen shot](docs/Features/right_wrong_answer.PNG)  

> 20. On the 404 page the user shouldn't use the broswer back but instead the nav bar.

|                         Feature                         |                         Test Steps                         |           Expected            |      Actual       |
| :-----------------------------------------------------: | :--------------------------------------------------------: | :---------------------------: | :---------------: |
| 404 page with nav bar for user to navigate back to site | Entered incorrect URL and used nav bar to get back to site | To be directed back main site | Works as expected |

[User story screen shot](docs/Features/404nav.PNG)  

> 21. Display a map of Santorini

|         Feature          |          Test Steps           |         Expected         |      Actual       |
| :----------------------: | :---------------------------: | :----------------------: | :---------------: |
| Display map of Santorini | Map of Santorini on home page | To find map on home page | Works as expected |  

[User story screen shot](docs/Features/map.PNG)  

---

# Bugs
> **Bug** Contact form initially didn't push down when using mobile nav  
> **Fix** Changed **poistion: absolute;** to **postion: relative**. Changed **top:50%** to **top:25%**. Changed **transform: translate(-50%,50%);** to **transform: translate(-50%,25%);**
>
> **Bug** Small gap at top of page between bottom of nav bar and top of quiz.  
> **Fix** Changed **margin: 40px auto;** to **margin: auto;** on .custom box CSS class  
>
> **Bug** Content map, heading-left doesn't push down on mobile nav  
> **Fix** Changed **position : absolute;** to **position: relative;** on .hero-text CSS class  

# Deployment

I have deployed this site to GitHub pages

> 1. Log in to git hub and find the respositry you wish to deploy
> 2. On the respository click on **Settings**
> 3. From left the hand menue click on **Pages**
> 4. Click on the **Source** option
> 5. From the dropdown change **none** to **master branch**
> 6. The deplyment will take a few moments to finalise
> 7. The live site URL is now displayed under Github Pages

Clone site locally

> 1. Log in to Github and navigate to main page of repository
> 2. Click on **Code** above the list of files
> 3. Copy the link under clone to https
> 4. Open Git bash
> 5. If required change the directory to where you would like repo cloned to
> 6. Type git clone and then copy in repo URL
> 7. Press enter and repo will go through short cloning process

---

# Credits
> * Quiz and JS credited to The Webshala - https://www.youtube.com/watch?v=J8QbjXdVl9c
> * Contact form and validation JS credited to Coding Market https://www.youtube.com/watch?v=WY4rvU4ImgE

# Acknowledgements
> * Mo Shami for his external patience and guidance
> * My partner who has not seen that much of me during MS2

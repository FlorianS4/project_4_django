# Gamecrit blog post site

You like video games and you want to share your experience you gained from them with others.
Then gamecrit is the perfect site for you!

![Gamecrit image](/docs/readme-images/gamecrit-pic-for-readme.png)

Leave your review.

Like other reviews.

Engage in the comment section with other users!

Bookmark your favorite reviews, for inspiration.

Then you will maybe you find the next game you want to play through a review on our site, who knows!

Visit Gamecrit [here](https://project-4-django-34f4c5eeb5b8.herokuapp.com/)!!




## Content
- [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
    - [User Stories](#user-stories)
        - [First Time User](#first-time-user)
        - [Returning User](#returning-user)
        - [Frequent User](#frequent-user)
- [Design](#design)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Color Scheme](#color-scheme)
- [Wireframes](#wireframes)
- [Relationship Models](relationship-models)
- [Agil Methology](#agil-methology)
- [Features](#features)
    - [Common Features](#common-features)
      - [Navbar](#navbar)
      - [Footer](#footer)
    - [Main Page](#main-page)
      - [Gamecrit Banner](#gamecrit-banner)
      - [Gamecrit Post Cards](#gamecrit-post-cards)
      - [Pagination](#pagination)
    - [Display Game Review Page](#display-game-review-page)
    - [Add Gamecrit Post Page](#add-gamecrit-post-page)
    - [Edit Gamecrit Post Page](#edit-gamecrit-post-page)
    - [Delete Gamecrit Post Page](#delete-gamecrit-post-page)
    - [Gamecrit Contact Page](#gamecrit-contact-page)
    - [Bookmark Page](#bookmark-page)
    - [Signup Page](#signup-page)
    - [Login Page](#login-page)
    - [Logout Page](#logout-page)
    - [404 Page](#404-page)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Programs Used - Frameworks - Libraries - Databases](#programs-used---frameworks---libraries---databases)
- [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [Running the project locally](#running-the-project-locally)
    - [Heroku set up](#heroku-set-up)
- [Credits](#credits)
    - [Code](#code)
    - [Similar students projects](#similar-students-projects)
    - [Resources Used](#resources-used)
    - [Media](#media)
- [Fixed Bugs](#fixed-bugs)
- [Future Content](#future-content)
- [Acknowledgments](#acknowledgments)


## Site Owner Goals
- to provide the user with a blog site about video games.
- to provide the user with the ability to create their post about a video game with their opinion.
- to provide the user with the ability to leave a comment underneath a blog post.
- to provide the user with the ability to edit or delete the post or a comment they created.
- to provide the user with the ability to like and bookmark a post.
- to provide the user with a bookmark section, where they can see their bookmarked posts.
- to provide the user with a possibility to get in contact with the side owner.

## User Experience
### User Stories
#### First Time User
- I want to read reviews about games I'm interested in.
- I want to read what other people think about my favorite game.
- I want to play a new game and hope to find inspiration.

#### Returning User
- I want to write my own reviews and provide my own thoughts about a game I like.
- I want to like good reviews.
- I want to write comments with my own thoughts about a game that somebody wrote a blog post for.

#### Frequent User
- I want to bookmark good reviews so I can come back to the post after I finish the game.

## Design
### Typography

[Google Fonts](https://fonts.google.com/) was used for the following font:
- ![Lato font image](/docs/readme-images/font-image-navbar.png)

    [Lato](https://fonts.google.com/specimen/Lato?preview.text=Gamecrit)
- Lato font was picked because I like the look of it for the Gamecrit header in the Navbar.

- ![Stencil font image](/docs/readme-images/font-image-banner.png)

    [Stencil](https://fonts.google.com/specimen/Stardos+Stencil?preview.text=GAMECRIT&query=Stencil)
- Stencil was picked as font for my hero image heading.

- Sans Serif was chosen as a backup font, in case the main font is not imported into the website, or there is a problem with the browser.

### Imagery

All Images were taken from different websites. I give credit to them in the [credits](#credits) section. I only needed two pictures, one as a default picture if people forgot or didn't want to include a picture for their blog post. The other picture is for the Gamecrit Banner.

### Color Scheme

* I have used `#FFFFFF` and `#000000` as the primary color for text used on the site.
* I have used `#910C07` as the text color for the "crit" in the navbar header.
* I have used `#C2B329` as the background color for the navbar and the author display.
* I have used `#D3D3D3` as the background color for the blog text field and for the comment section.
* I have used `#2CFF05` as the color for for the buttons on my site.

![Gamecrit Site color palette](/docs/readme-images/color-palette-project-4.png)

## Wireframes
<details>

<summary>Desktop Wireframe</summary>
Main Page:

![Wireframe Main Page](/docs/wireframes-images/home-page-desktop.png)

Gamecrit Contact Page:

![Gamecrit Contact Page](/docs/wireframes-images/contact-page-desktop.png)

Create your own review Page:

![Create review Page](/docs/wireframes-images/create-post-desktop.png)

Bookmark Page:

![Bookmark Page](/docs/wireframes-images/bookmark-page-desktop.png)

Login Page:

![Login Page](/docs/wireframes-images/login-page-desktop.png)

Register Page:

![Register Page](/docs/wireframes-images/register-page-desktop.png)

404 Page:

![404 Page](/docs/wireframes-images/404-page-desktop.png)

</details>

<details>

<summary>Mobile Wireframe</summary>
Main Page:

![Wireframe Main Page mobile](/docs/wireframes-images/home-page-mobile.png)

Gamecrit Contact Page:

![Gamecrit Contact Page mobile](/docs/wireframes-images/contact-page-mobile.png)

Create your own review Page:

![Create review Page mobile](/docs/wireframes-images/create-post-mobile.png)

Bookmark Page:

![Bookmark Page mobile](/docs/wireframes-images/bookmark-page-mobile.png)

Login Page:

![Login Page mobile](/docs/wireframes-images/login-page-mobile.png)

Register Page:

![Register Page mobile](/docs/wireframes-images/register-page-mobile.png)

404 Page:

![404 Page mobile](/docs/wireframes-images/404-page-mobile.png)

</details>

## Relationship Models

I used [LucidChart](https://www.lucidchart.com/) to create a relationship diagram of my models.

![ERD Diagram](/docs/readme-images/erd-diagram-gamecrit.png)

- This diagram shows the relationships in my models and beetween one another.
- I used the [Django AllAuth](https://docs.allauth.org/en/latest/) library for user authentification, which created my user model for me.

## Agil Methology

This project was designed with the Agile methodology, using the Project Board and Issues sections in GitHub.

>[Project Board](https://github.com/users/FlorianS4/projects/8)

## Features
### Common Features

#### Favicon

![Favicon](/docs/readme-images/favicon.png)

#### Navbar

![Navbar desktop login view](/docs/readme-images/navbar-login-desktop.png)

![Navbar desktop logged in view](/docs/readme-images/navbar-loggedin-desktop.png)

- The navbar gives the user menu options depending if they are already logged in or not.

![Navbar mobile view](/docs/readme-images/navbar-mobile.png)

- The navbar on mobile view has a drop down menu.

#### Footer

![Footer desktop view](/docs/readme-images/footer-desktop.png)

![Footer mobile view](/docs/readme-images/footer-mobile.png)

- The footer has a link to my GitHub as well as links to popular social media sites.

### Main Page
#### Gamecrit Banner
 
![Banner desktop login view](/docs/readme-images/banner-desktop-login.png)
![Banner desktop logged in view](/docs/readme-images/banner-desktop-loggedin.png)

- In the banner the user has options of buttons depending if they are logged in or not.
- The same options exists on mobile.

![Banner mobile view](/docs/readme-images/banner-mobile-view.png)

#### Gamecrit Post Cards

![Gamecrit post cards desktop view](/docs/readme-images/desktop-blog-cards-view.png)

![Gamecrit post cards mobile view](/docs/readme-images/mobile-blog-cards-view.png)

The Site displays the written blogs with a picture in smaller cards. If the user added an image him-/herself it will be here, otherwise it picks the default picture.
- The author and the date when the blog post was created is also displayed.
- The user can click on a card to see the gamecrit post.

#### Pagination

![Pagination](/docs/readme-images/pagination.png)

### Display Game Review Page

![Game Review section](/docs/readme-images/blog-post-video-and-blog-section.png)

- In the top part of the Game Review the user can see the trailer and the review for the game.

![Edit and delete buttons for author](/docs/readme-images/edit-and-delete-button-for-post-author.png)

- The author of the post also has the option to edit or delete the post.

![Game Like and Comment section](/docs/readme-images/blog-post-like-comment-section.png)

- In the bottom part of the Game Review the user can like the post, see how many comments there are and read and leave their own comment.
- Users can edit or delete their own comments.

### Add Gamecrit Post Page

![Add Gamecrit Blog Post Page](/docs/readme-images/add-gamecrit-blog-post.png)

- The user can add his/her own post on this site.
- The title, text about the game and a video link are mandatory, the picture is not.
- If the user chooses to not upload a picture, the site will automaticly pick the default picture.
- After uploading the post, the superuser has to verify the post and set it to public, so other people can see it.

### Edit Gamecrit Post Page

![Edit Gamecrit Blog Post Page](/docs/readme-images/edit-gamecrit-blog-post.png)

- On the edit page the author of the post can edit the post.

### Delete Gamecrit Post Page

![Delete Gamecrit Blog Post Page](/docs/readme-images/delete-gamecrit-blog-post.png)

- On the delete page the author of the post can delete the post.

### Gamecrit Contact Page

![Gamecrit Contact Page](/docs/readme-images/gamecrit-contact-page.png)

- On the gamecrit contact page a user can get in contact with the gamecrit team.

### Bookmark Page

![Gamecrit Bookmark Page](/docs/readme-images/gamecrit-bookmark-page.png)

- On the bookmark page the user can see his bookmarked blog post.

### Signup Page

![Signup Page](/docs/readme-images/sign-up-page.png)

- A standard sign up page with validation.

### Login Page

![Login Page](/docs/readme-images/sign-in-page.png)

- A standard login page.

### Logout Page

![Logout Page](/docs/readme-images/logout-page.png)

- A standard logout page.

### 404 Page
![404 Page](/docs/readme-images/404-page.png)
- When an error occurs or a wrong input is given to the url the 404-page will show up with the information on how to be redirected to the landing page.

## Testing
See the testing results in the [TESTING.md](TESTING.md) file.

## Technologies Used
### Languages
HTML, CSS, JavaScript, Python

### Programs Used - Frameworks - Libraries - Databases
- [Google Fonts](https://fonts.google.com/) - to import  fonts used on website.
- [FontAwesome](https://fontawesome.com/) - for footer's and navbar's icon.
- [Google Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools)- for troubleshooting, debugging, inspecting page's elements, testing responsiveness and styling elements.
- [Gitpod](https://gitpod.io/) - IDE to develop the website.
- [GitHub](https://GitHub.com/) - for version control and hosting.
- [Balsamiq](https://balsamiq.com/wireframes/)- to create wireframes.
- [Coolors](https://coolors.co/) - to create color palette.
- [Wave](https://wave.webaim.org/) to test accessibility.
- [Google Chrome's Lighthouse](https://developers.google.com/web/tools/lighthouse) - to test performance and accessibility.
- [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code.
- [W3C HTML Markup Validator](https://validator.w3.org/) to validate HTML code.
- [JShint JavaScript Validator](https://jshint.com/) to validate JS code.
- [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) to validate Python code.
- [TinyPNG](https://tinypng.com/) - to compress images to reduce file size without a reduction in quality.
- [LucidChart](https://www.lucidchart.com/) - was used to make the ERD Diagram.
- [Django](https://www.djangoproject.com/) - used for the project's web framework. Is a Python framework.
- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction//) - used as a CSS framework.
- [Cloudinary](https://cloudinary.com/) - online static file storage used for uploaded pictures.
- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) - Postgres database.



## Deployment

How to setup your PostgreSQL database:
- got to [CI Database Maker](https://dbs.ci-dbs.net/)
- input your LMS email address
- create your PostgreSQL database
- press on Info and copy the Database URL to your env.py file.

How to setup your Cloudinary database.
- Go to [Cloudinary](https://cloudinary.com/) and sing up for free.
- Go to your cloudinary dashboard and copy your API key.
- Add the cloudinary API key to your env.py file. 

This site was deployed to GitHub pages.
Instructions:

- Login to Github.
- Go to the GitHub repository: FlorianS4/Project_4_django, navigate to the Settings tab.
- Select the Pages tab on the menu on the left side.
- Under Source, choose main from the Branch dropdown menu. Save it.
- The page will refresh itself and the website is now deployed with a text indicating such.

### Heroku Deployment

- Log into your [Heroku](https://www.heroku.com/) account or create an account.
- Select the New button on the right at the top and select "Create New App".
- Enter a application name.
- Select a region.
- Click "Create App".
- Go to the deploy option.
- Select GitHub as your deployment option.
- Confirm the connection to Github and choose the correct repository.
- Select "Enable Automatic" and "Deploy branch" with the selection main.
- Select "view" to see the live website.

### Heroku set up

- In your GitPod workspace create an env.py file and add it to .gitignore.
- Add your SECRET_KEY value and the DATABASE_URL to the env.py file.
- Add your CLOUDINARY_URL to the env.py file if you use cloudinary.
- In the settings.py file import the env.py file and add the SECRET_KEY and DATABASE_URL file paths.
- Add cloudinary to the INSTALLED_APPS and to the static files in the settings.py file.
- Add TEMPLATES_DIR in settings.py file and change the templates directory to TEMPLATES_DIR.
- Add these Config Vars in Heroku:
    - `CLOUDINARY_URL` (Your Cloudinary API key)
    - `DATABASE_URL` (Your Postgres SQL API key)
    - `SECRET_KEY` (Your secret key)
- Additional Heroku Files:
    - Requirements.txt file
    - Create Procfile via gunicorn

        ```python
        web: gunicorn codestar.wsgi
        ```

### Running the project locally
Additional files needed for installation of dependencies:
    Requirements.txt file

How to Fork:
- Login to Github
- Go to the GitHub repository: Project_4_django
- Select the Fork button on the right at the top

How to clone:
- Login to Github
- Go to the GitHub repository: Project_4_django
- Select the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
- Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
- Type 'git clone' into the terminal and then paste the link you copied in step 3. and enter.
- A clone will be created.

## Credits
### Code

This project was based on the Code Institute - I think therefore I Blog walkthrough.
The walkthrough provided a base for a standard blog. I customised a lot of the layouts and styling of this base with Bootsrap and custom CSS.

For help with creating a blog post and for different models I used [Codemy.com](https://www.youtube.com/@Codemycom/featured) on YouTube and [Dee Mc](https://www.youtube.com/@IonaFrisbee) aswell on YouTube.

- I used [this video](https://www.youtube.com/watch?v=vXMTp_1_L7Y) for help with creating a post.
- I used [this video](https://www.youtube.com/watch?v=nFa3lC105dM) for help with deleting a post.
- I used [this video](https://www.youtube.com/watch?v=JzDBCZTgVyw&t=1s) for help with editing a post.
- I used [this video](https://www.youtube.com/watch?v=e49QSMHXM5k&list=PLCC34OHNcOtoQCR6K4RgBWNi3-7yGgg7b&index=17) for help with storing and displaying likes correctly.

- I used the way [AliOKeeffe](https://github.com/AliOKeeffe) handled her project's bookmarking section in [this project](https://github.com/AliOKeeffe/PP4_My_Meal_Planner) as a reference and built on it for my own bookmarks.

### Similar students projects

When I browsed through the peer review slack channel I found [this project](https://github.com/nazar0309/Game-Glance) by [nazar0309](https://github.com/nazar0309) and I really enjoyed the topic as my main hobby always has been gaming. So I took it as an inspiration for my own project.

### Resources Used
- Code Institute's lessons (I think therefore I Blog)
- [Stack Overflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/)
### Media
- [Banner](https://www.pexels.com/photo/close-up-photo-of-gaming-keyboard-2115257/)
- [Default Image](https://www.pexels.com/photo/low-light-photo-of-nes-controller-1637436/) - This Image is used when the user doesn't upload a image for the review themself.
- [Favicon](https://icons8.de/icons/set/controller)

## Fixed Bugs
- Gamecrit contact error: Does not appear to have any url path in it.

    * Added a s to "urlpattern" as there was a spelling mistake.

- My Project wasn't deploying to Heroku.

    * Wrong naming for project in procfile.

- Delete Gamecrit Post class wasn't working correctly in views.py.

    * Deleted form_class from views.py as it was added by mistake.

- Gamecrit Contact Form wasn't showing up because of wrong naming conventions and beeing wired up incorrect.

    * Wired up urls and HTML template correctly to display form and added Meta class for ordering and __ str __ method for the admin panel.

- Wrong field reference in Post model so the view and later on the templates could not use it.

    * Changed reference fields names and added missing fields. 

- Wrong field reference in Comment model so the view and later on the templates could not use it.

    * Changed reference fields names and added missing fields.

- My signup page wasn't working correctly. 

    * Added correct code institute sign up page template.

## Future Content
- User should be able to like comments from other users.
- A search function. 

## Acknowledgments
My mentor Jubril Akolade for his guidance, input and support.

The Slack community on Code Institute for reviewing my project and for support.

Code Institute for informational courses.

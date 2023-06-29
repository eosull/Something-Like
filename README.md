# Something Like

| ![Screen Size Responsiveness](/assets/readme_images/screen_size_mock_ups.png) |
|:--:|
|Something Like...|

**Something Like** is a forum website that allows users to share recommendations and discuss works of art they enjoy. The target audience is people who want personalised recommendations and discussion about books, tv shows, albums or films they enjoy.

Once a user sign up, they can create posts about something they enjoyed which serves as an invitation for others to leave comments underneath recommending similar works. They can also comment underneath other users' posts which, once approved by the site admin, will join the conversation underneath each post.

Unregistered users can view content on the site, but are unable to create or edit any content. Posts can be found on the 'Explore' page which shows a list of posts on the site, with a filter feature allowing users to filter the posts by date, category or both.

The live site can be found [here](https://something-like-pp4.herokuapp.com/)

# Table of Contents
- [About](#something-like)
- [Features](#features)
- [Design](#design)
- [Agile](#agile-implementation)
- [Tools and Technologies](#tools-and-technologies)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)

# Features
## Navigation
A navbar is present at the top of all pages, allowing users to move between pages on the site at all stages. The navbar shows 'login' and 'register' for unauthorised users and 'logout' if user is authorised.

| ![Unauthorised Navbar](/assets/readme_images/navbar_unauthorised.png) |
|:--:|
|Unauthorised Navbar|

| ![Authorised Navbar](/assets/readme_images/navbar_authorised.png) |
|:--:|
|Authorised Navbar|

This menu turns into an expandable hamburger icon on smaller screens.

| ![Mobile Navbar](/assets/readme_images/navbar_mobile.png) |
|:--:|
|Mobile Navbar|

## Landing Page
The landing page has an animation that shows all post categories as well as a link to create a new post. Unauthorised users are shown a link to sign up.

| ![Landing Page New Post](/assets/readme_images/landing_page_new_post.png) |
|:--:|
|Landing Page New Post|

The landing page also provides links to posts of specific categories and gives a preview of the 3 most recent posts, inviting the user to explore posts further.

| ![Landing Page Explore](/assets/readme_images/landing_page_explore.png) |
|:--:|
|Landing Page Explore|

## Explore
The Explore page has a list of posts, ordered by date of posting with newest at the top. Each post has coloured dashes beside the category and amount of comments/likes.

| ![Explore Post List](/assets/readme_images/explore_post_list.png) |
|:--:|
|Explore Post List|

This list can also be filtered by date and category using the filter form at the top of the page.

| ![Explore Filter](/assets/readme_images/explore_filter.png) |
|:--:|
|Explore Filter|

## Post Details
Each post has a detailed view including information such as user (with avatar generated using [Boring Avatars](https://github.com/boringdesigners/boring-avatars-service)), date of posting and like count. Authorised users can add a like to the post. Comments are displayed underneath the post and authorised users can also add to these comments.

| ![Post Detail](/assets/readme_images/post_detail.png) |
|:--:|
|Post Detail|

## Creating/Editing Post
Authorised users can create new posts on the site, this consists of filling out a form that asks for a title, category and some information.

| ![New Post Page](/assets/readme_images/new_post.png) |
|:--:|
|New Post Page|

Authorised users can also edit posts they have created with a similar form that is pre-populated with post information. If the user clicks 'delete', they are sent to a confirmation page where they must confirm they want to delete the post.

| ![Edit Post Page](/assets/readme_images/edit_post.png) |
|:--:|
|Edit Post Page|

## Account Registration/Login
Users can register and login to access features only accesible to authorised users using front-end forms, shown below.

| ![Login Page](/assets/readme_images/signin_page.png) |
|:--:|
|Login Page|

| ![Register Page](/assets/readme_images/signup_page.png) |
|:--:|
|Register Page|

# Design
The design process was structured using the five planes of UX - **Strategy, Scope, Structure, Skeleton & Surface**. Each Section is discussed more in depth in the Design document in the repository, which can be found [here](DESIGN.md). A summary will be outlined below.

From brainstorming sessions and using design thinking a central site goal emerged:
-  **Provide a platform for users looking for film, tv, music or book recommendations to share personalised recommendations with one another**.

It is hoped by developing an intuitive and responsive site where users can create and interact with content this goal will be acheived. There are two main pieces of content on the site that users can contribute to. These are posts and comments which serve as conversation starters, invitations to discuss and opportunities to share recommendations.

The colour palette (seen below) which was combined with neutral black, grey and off-white was used to mark categories of posts, create user avatars and accentuate animations. 

| ![Final Color Palette](/assets/readme_images/color_palette_final.png) |
|:--:|
|Colour Palette|

The central goal of the site, sharing recommendations, was kept in mind throughout the design process. This means significant work was put into making sure the process of creating posts and interacting with other users was made as simple as possible. In the [design document](DESIGN.md) you can see how these core features developed from wireframes through 4 iterations making sure these features are as intuitive and enjoyable to use as possible.

# Agile Implementation
An Agile methodology was used in the development of this site, structuring and scheduling the workflow. This was my first time working in this way, so it took roughly a month for me to find out the most productive way to use this way of working.

At the beginning my focus was on completing tasks so that User Stories would be completed within a Sprint timeframe. After a month or so of working this way, I decided to move to working in iterations instead. This meant lengthening the Sprints and reducing the specificity of the tasks attached to User Stories.

By iteration 4 (sprint finishing submission date) I had found a more efficient way of working. This went as follows:
- 2 Week Sprints
- Working MVP iteration at the end of each sprint
- Themed Epics for most important aspects of project
- Iteration-Specific User Stories mapped to themed Epics
- Clear tasks and MoSCoW prioritization assigned to each User Story
- Acceptance Criteria included for most

The implementation of this process can be seen clearly on my [GitHub project board](https://github.com/users/eosull/projects/7). Below is the details of User Stories and Sprints from the project, clicking on Epic or Sprint titles will bring you to the associated page on GitHub to see info in more detail.

## User Stories

| **EPIC**          | **User Story**                                                                                                        | **Completed** |
|-------------------|-----------------------------------------------------------------------------------------------------------------------|---------------|
|**_Iteration 1_**|
| [**Project Setup**](https://github.com/eosull/Something-Like/issues/1) |                                                                                                                       | &check; |
|                   | As a Developer I want to Set up my workspace So that I can begin working on the code                                  | &check; |
|                   | As a Developer I want access to design and prep work so that I can reference it and structure the development process | &check; |
|                   | As a Developer I want to deploy my Django project to Heroku to ensure that everything has been set up correctly       | &check; |
| [**Data Models and Django Admin Site**](https://github.com/eosull/Something-Like/issues/5) |                                                                                                                       | &check; |
|                   | As a Site Admin I want to create a database so that I can begin to consider implementing CRUD functionality.          | &check; |
|                   | As a Site Admin I want to Access the admin panel so that I can Interact with database models and edit content.        | &check; |
| [**Site Navigation and Base Templates**](https://github.com/eosull/Something-Like/issues/8) |                                                                                                                       | &check; |
|                   | As a Developer I want to create a base template so that I can extend this across all pages on site.                   | &check; |
|                   | As a User I want to arrive on a landing page that previews content so that I can get a sense of what the site is about.                                                                                                                     | &check; |
|                   | As a User I want to visit a page on the site where all posts are displayed so that I can view all posts and select to view in more detail if desired.                                                                                                                   | &check; |
|                   | As a User I want to click on a post and be taken to a post detail page so that I can View the post in more detail and see data not available in preview.                                                                                                                   | &check; |
|                   | As a Registered User I want to visit the login page so that I can login to my account.                                | &check; |
|                   | As an Unregistered User I want to visit the registration page so that I can register to create an account.            | &check; |
|                   | As a User I want the links on the site to take me to where I want to go so that I can navigate intuitively throughout the site and not get confused.                                                                                                                                   | &check; |
| [**CRUD Functionality**](https://github.com/eosull/Something-Like/issues/16) |                                                                                                                       | &check; |
|                   | As an Authorised User I want to Create, Read, Update and Delete Posts So that I can Create Content for other users to engage with.                                                                                                                       | &check; |
| [**Front End Design**](https://github.com/eosull/Something-Like/issues/23) |                                                                                                                       | &check; | 
|                   | As A User I want to Use a site that meets accessibility guidelines, UX design principles, is intuitive and evokes a positive emotional response so that the site is simple and enjoyable to use.                                                                                                | &check; |       
|**_Iteration 2_**|
| [**Post Creation, display and navigation**](https://github.com/eosull/Something-Like/issues/30) |                                                                                                                       | &check; |
|                   | As a User I want to create engaging posts so that I can begin conversations with other users about art that I enjoy                                 | &check; |
|                   | As a User I want to Arrange the content shown to me on the explore page so that I can View categories of posts that interest me                                  | &check; |
| [**Comment Creation, Display and Editing**](https://github.com/eosull/Something-Like/issues/32) |                                                                                                                       | &check; |
|                   | As an Authorised User I want to Create and Read comments So that I can Create Content for other users to engage with.                                 | &check; |
|                   | As a User I want to comment underneath posts so that I can engage with other users' content on the site                               | &check; |
| [**UX and Front End Design**](https://github.com/eosull/Something-Like/issues/34) |                                                                                                                       | &check; |
|                   | As a User I want to receive feedback anytime the database of the site is engaged with so that I am aware of the consequences of actions and am alerted to actions taken                                | &check; |
|                   | As a User I want to be met with dynamic and engaging content so that I can enjoy the site content and am motivated to add to it                               | &check; |
| [**Site Testing**](https://github.com/eosull/Something-Like/issues/37) |                                                                                                                       | &check; |
|                   | As a Site Admin I want to test my code so that I can ensure it meets accessibility, functionality, usability, responsiveness and data management standards as well as meeting project MVP targets                             | &check; |
|**_Iteration 3_**|
| [**Post Creation, display and navigation**](https://github.com/eosull/Something-Like/issues/30) |                                                                                                                       | &check; |
|                   | As a User I want to Intuitively navigate and create posts so that I can create and engage with content on the site                                  | &check; |
| [**Comment Creation, Display and Editing**](https://github.com/eosull/Something-Like/issues/32) |                                                                                                                       | &check; |
|                   | As a User I want to intuitively read and contribute comments so that I can join in the conversation                                | &check; |
| [**UX and Front End Design**](https://github.com/eosull/Something-Like/issues/34) |                                                                                                                       | &check; |
|                   | As a User I want to be met with content that evokes a positive emotional response so that I enjoy navigating and interacting with the site                              | &check; |
| [**Site Testing**](https://github.com/eosull/Something-Like/issues/37) |                                                                                                                       | &check; |
|                   | As a Site Admin I want to test my code so that I can ensure it meets accessibility, functionality, usability, responsiveness and data management standards as well as meeting project MVP targets                             | &check; |
| [**Clean and Prestentable Code**](https://github.com/eosull/Something-Like/issues/68) |                                                                                                                       | &check; |
|                   | As a Site Admin I want my code and documentation to be clean and readable so anyone viewing the code can understand and navigate the code easily                             | &check; |
|**_Iteration 4_**|
| [**UX and Front End Design**](https://github.com/eosull/Something-Like/issues/34) |                                                                                                                       | &check; |
|                   | As a Site User I want to experience a positive response when using the site, navigating easily and adding to content easily so that I can enjoy the content on the site and interact with other users                            | &check; |
| [**Site Testing**](https://github.com/eosull/Something-Like/issues/37) |                                                                                                                       | &cross; |
|                   | As a Site Developer I want to Manually and Automatically Test My code so that any changes made in this iteration meet accessibility, functionality, usability, responsiveness and project goals                            | &cross; |
| [**Clean and Prestentable Code**](https://github.com/eosull/Something-Like/issues/68) |                                                                                                                       | &cross; |
|                   | As a Developer I want to refactor and tidy up my code so that my code is as efficient and readable as possible                        | &cross; |
|                   | As a Site Admin I want to Write a clear and well-structured ReadMe so that I can Document the development process and explain the motivations of the project                      | &cross; |
|**Unfinished User Stories**|
|                   | As a User I want to See a set number of posts on a page and click to see more so that the page does not contain too many posts and become very long                           | &cross; |
|                   | As an Authorised User I want to Edit and Delete comments so I can manage content I have created                           | &cross; |
|                   | As a User I want to see suggested posts related to the content I'm viewing so that I can explore and engage with the content further                          | &cross; |
|                   | As a Site Admin I want to be able to access admin features without accessing back-end admin panel so that I can approve comments and manage content from the main site                          | &cross; |

- These unfinished User Stories were categorised as 'Would be Nice to Have' and considered extras to the MVP. They will be developed on in future iterations.

## Sprints

### Sprint 1 (17/04/2023-23/04/2023) - [Design](#design)
This sprint consisted of brainstorming sessions, project requirement consideration and research. Emerging from this was a site concept, basic wireframes, ERD and Epics with user stories.

### Sprint 2 (24/04/2023-30/04/2023) - [Project Setup](https://github.com/eosull/Something-Like/milestone/1)
This sprint consisted of setting up the requirements to develop a full-stack project using an agile methodology. This included setting up a repository, workspace and project board.

### Sprint 3 (01/05/2023-02/05/2023) - [Admin Site/Database Build Sprint](https://github.com/eosull/Something-Like/milestone/2)
This Sprint covered the creation of database models for the site and the building of the administration site. This included adding the data models for users, comments, posts and categorys. The creation of a superuser and building of an admin site to edit database was also included.

### Sprint 4 Site Navigation and Templates (02/05/2023-05/05/2023) - [Site Navigation and Templates](https://github.com/eosull/Something-Like/milestone/3)
This sprint covered the creation of views, templates and navigation links in order to create a navigable structure to the site. The end goal of this sprint was to have a site structure where content could be displayed and navigated through.

### Sprint 5 Front End CRUD Functionality (04/05/2023-09/05/2023) - [CRUD Functionality](https://github.com/eosull/Something-Like/milestone/4)
This sprint covered the implementation of CRUD functionality for authorised users via front-end forms. This includes the creation, editing and deleting of posts and comments. Full CRUD functionality for posts was acheived, comment editing and deleting is still to be acheived.

### Sprint 6 Front End Styling Iteration 1 (11/05/2023-16/05/2023) - [Front End Iteration 1](https://github.com/eosull/Something-Like/milestone/5)
This sprint covered the front end design for the first working iteration of the site. This will include structuring, mobile responsiveness, colour schemes and typogrophy.

### Sprint 7 Iteration 2 Sprint (19/05/2023-02/06/2023) - [Iteration 2 Sprint](https://github.com/eosull/Something-Like/milestone/6)
After Sprint 6, the decision was taken to broaden the scope of Sprints, Epics and User Stories. This included a lengthening of sprint time and less rigid tasks in User Stories. The focus has now shifted from individual functionality and structural elements to an iteration based workflow. The core structure of the site has been completed and from this point on the working sprints will be with the next iteration in mind. The first iteration was focused on functionality and meeting core MVP targets. This iteration builds on this, adds features and aims to create a more engaging product.

### Sprint 8 Iteration 3 Sprint (07/06/2023-19/06/2023) - [Iteration 3 Sprint](https://github.com/eosull/Something-Like/milestone/7)
Iteration 3 Sprint. This sprint inherits Epics from iteration 2 that deals with core site content and adds iteration specific user stories to these. New epics that deal with submission preparation are also created as the project comes into the final month of development. Included in this sprint is development on the automated tested started in iteration 2 and continuing manual testing.  It also includes work on the core site content of posts and comments (creation and display). The Front end development will continue and a code tidy up including refactoring, commenting and structuring will begin.

### Sprint 9 Iteration 4 Sprint (19/06/2023-03/07/2023) - [Iteration 4 Sprint](https://github.com/eosull/Something-Like/milestone/8)
Iteration 4 Sprint, finishes on project submission. This sprint also deals with the Epics laid out in Iteration 2, adding user stories specific to the development stage. This includes writing a clear and concise ReadMe file, Ensuring the site is up to accessibility and code structuring standards. Also included is a final front-end development phase, polishing up where possible and ensuring site is responsive and meets the core project goals. Refactoring and commenting with finish in this sprint, ready for the code to be graded.

# Tools and Technologies
- [HTML5](https://en.wikipedia.org/wiki/HTML): Markup Language
- [CSS3](https://en.wikipedia.org/wiki/CSS): Styling
- [Javascript](https://en.wikipedia.org/wiki/JavaScript): Dynamic site content
- [Python](https://www.python.org/): Used in conjunction with Django to render site
- [Django 4.2](https://docs.djangoproject.com/en/4.2/): Database-orientated framework to build site
  - [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/): Django application to handle account management
  - [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): Django application to handle form rendering
  - [Django Summernote](https://pypi.org/project/django-summernote/): Text formatting in Django admin panel
  - [Django Nose](https://pypi.org/project/django-nose/): Automated testing
- [Bootstrap](https://getbootstrap.com/): Front-end toolkit
- [Elephantsql](https://www.elephantsql.com/): PostgreSQL database hosting
- [Cloudinary](https://cloudinary.com/): Hosting of Media and Static files
- [Coverage](https://coverage.readthedocs.io/en/7.2.7/): Monitoring automated Python testing coverage
- [Psycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter for Python
- [Google Fonts](https://fonts.google.com/): Import fonts to use on site
- [Bootstrap Icons](https://icons.getbootstrap.com/) Icons on the site
- [LucidChart](https://www.lucidchart.com/): Diagrams, flowcharts and wireframes 
- [Code Institute Student Template](https://github.com/Code-Institute-Org/gitpod-full-template): Template for repository

# Testing
Testing was completed throughout the development of the site as can be seen in the [Testing](TESTING.md) file. This included manual and automated tests for functionality, accessibility, code validation and site goals.

## Manual Testing
Accesibility testing completed using Chrome Developer Tools [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) feature. HTML code was validated using [W3 Validation](https://validator.w3.org/) and [Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate CSS code. Javascript code was tested using [JSHint](https://jshint.com/) while Python code formatting was tested tested continuously during development using [pycodestyle](https://pypi.org/project/pycodestyle/) extenstion in VS code for Gitpod.

# Bugs
Deployment to Heroku: build was failing on Heroku and I was met with the following error: *ERROR: Could not build wheels for backports.zoneinfo, which is required to install pyproject.toml-based projects*. A search on slack [found a student](https://code-institute-room.slack.com/archives/CHDVDV2Q4/p1681717148021239) who had faced a similar issue, the cause being heroku is using a new version of Python and needs to be told to use an older version for backports.zoneinfo to run. Good info and possible solution found on [Stack Overflow](https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta). Added runtime.txt file in directory and specified use of python-3.11.3 to resolve. This didn't work as I was getting the same error. Found more people facing the same issue on Slack and avoiding the install of backports if python version is greater that 3.9 [was suggested](https://code-institute-room.slack.com/archives/C026PTF46F5/p1677505066005429). This worked and project was successfully deployed to Heroku.

Custom User Model: The initial plan for development was to create a custom user model that would allow for further customation as the project developed. This was created in a separate accounts app. Upon trying to implement login/register functionality this was creating problems with connecting urls, views and templates as well as taking up a lot of development time. The decision was taken to remove this accounts app and stick to the perfectly adequete Django default user model and use AllAuth for authentication in order to keep development moving and to reach the MVP sooner.

Commenting: When trying to submit a comment I kept getting a Django error message telling me the comment form field 'author_id' was null and this violated not-null constraint. To resolve this I added the following line in the post method of blog/views.py to use the id in the request to fill this field: comment_form.instance.author_id = request.user.id .

Editing: I used 2 auto-generated time-stamps (one set at creation and one that changes with each edit) and a comparison function to find out whether or not posts had been edited. These were never equal so would never display as not edited. Using the console to inspect values I figured out the issue was with microsecond DateTimeField value (see image below). I used .replace(microsecond=0) in the comparison function to only make the comparison between date and hour/minute/seconds and the edited functionality worked.

| ![Microsecond Discrepancy](/assets/readme_images/bug_microsecond_timestamp.png) |
|:--:|
|Microsecond Discrepancy For Created Time and Edited Time|

Static File Heroku Delivery: Static files not being delivered to Heroku, so live site appears with no styling. Disable collect static config var on Heroku deleted and code with Debug set to False deployed, Static files now being served with live site showing styling.

# Deployment

**Heroku Deployment**
1. Create Heroku App
2. Create database (I used Elephant SQl)
3. Configure Cloudinary for media and static hosting
4. Link database/cloudinary to app in Heroku config vars
5. Add Django secret key to Heroku config vars
6. Link Heroku to GitHub Repository
7. Set up Automatic deployments or make manual deployments

**Forking**
1. Navigate to the [GitHub Repository](https://github.com/eosull/Something-Like) and click 'fork' in the top right of the page

**Cloning**
1. Navigate to the [GitHub Repository](https://github.com/eosull/Something-Like) and click the green 'code' dropdown
2. Choose your format from HTTPS, SSH or GitHub CLI and copy
3. Open your terminal in your IDE and use git clone followed by this link


# Credits

## Code/Resource References
- Commit messages formatted based on [Conventional Commit Standards](https://www.conventionalcommits.org/en/v1.0.0/#summary) - useful cheatsheet for formatting these messages by Github user Zekfad [Here](https://gist.github.com/Zekfad/f51cb06ac76e2457f11c80ed705c95a3)
- Creation of Entity Relationship Diagram was completed using LucidChart resources [Youtube tutorial](https://www.youtube.com/watch?v=QpdhBUYk7Kk&ab_channel=LucidSoftware) and [associated article](https://www.lucidchart.com/pages/how-to-draw-ERD).
- Rolodex Effect on site homepage was based on code [posted on codepen.io](https://codepen.io/orchard/pen/LoNdQZ?page=1) by user Adam Orchard.
- Custom Login/Register Forms created with help from [this post by Adam Wiener](https://gavinwiener.medium.com/modifying-django-allauth-forms-6eb19e77ef56)

## Media
- User Avatars generated using [Boring Avatars](https://github.com/boringdesigners/boring-avatars-service) by Boring Designers
- Site colour palette generated using [Colormind](http://colormind.io/)
- Site Favicon generated using [Favicon.io](assets/favicon/favicon.ico)
- Site responsiveness mock up generated using [Am I Responsive](https://ui.dev/amiresponsive)

## Acknowledgments
Many thanks to my Code Institute mentor Adegbenga Adeye who provided feedback and support throughout the development of this project.

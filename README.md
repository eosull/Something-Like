# Table of Contents
- [About](#about)
- [Design](#design)
- [Agile](#agile-implementation)
- [Features](#features)
- [Tools and Technologies](#tools-and-technologies)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)

# About
This is some info about this project.

# Design
This section provides information on the design process of the project. It will be outlined using the five planes of UX; **Strategy, Scope, Structure, Skeleton & Surface**.

## Strategy
The strategy plane focuses on what the project aims to acheive, and for whom. Following design thinking practices a problem statement was generated to summarise the needs of a user:

- *I, Eoin, as a lover of music/books/film am trying to find new recommendations for each of these. I find it difficult to connect with works that are algorithmically suggested via streaming apps because so many options are presented. This can feel overwhelming and can lead what is being recommended to feel somewhat disposable. I do not feel the connection I did to the work when for example: a friend gives me a book or an older family member gives me an album.*

Considering how these needs could be met was key in developing the strategy for this project. In this statement, the user is overwhelmed by choices provided by streaming sites and is searching for the connection they feel to media they encounter as a result of a personalised recommendation. Therefore, the central goal of the site is to **provide a platform for users looking for film, music or book recommendations to share personalised recommendations with one another**.

## Scope
Building on from the strategy and the goal outlined above, the scope of the project is concerned with the features to be included in the project.

### User Experience
The site should be:
- Intuitive and easily navigable
- Provide feedback to user actions
- Responsive to different screen sizes
- Accessible

### Functionality
The main functionalities of the site are as follows:
- A user can register and login, becoming authorised.
- An unauthorised user can view posts and comments on the site.
- An authorised user can create a categorised post detailing a piece of work they like. This post serves as an invitation for recommendations from other users.
- An authorised user can comment on a post.
- An authorised user can edit and delete their posts and comments.

### Content
The site should contain the following core content:
- Post previews, post details and categorised posts.
- Comments underneath posts

The implementation of these features successfully is the MVP for this project and are intended to be built on once they have been acheived. Implemented features and future additions will be detailed further in [Features Section](#features).

## Structure
The structure of the site was designed with two parts in mind; information design and the interaction design. Information design is concerned with how the information is structured on the site and the interaction design is concerned with how the user navigates this.

The site is designed so the home page is the hub from where the user can access all other features. Certain features are only accessible to authorised users. Unauthorised users will have access to read functionality, whereas create, edit and delete functionality will be limited to users with an account.

The nav elements will always be accessible via the header on the site. Feedback is provided for any action that creates or alters content via the use of confirmation messages.

| ![Information Design Flowchart](/assets/readme_images/information_design_flowchart.png) |
|:--:|
|Information Design Flowchart|

An entity relationship diagram was created for the purpose of meeting the MVP of the project, providing data models for: **Users**, **Posts** and **Comments**. Each of these have a primary ID key and multiple foreign keys. The relationships are as follows, outlined as well in diagram below:
- User to Posts = Only One to Zero or Many
- User to Comments = Only One to Zero or Many
- Posts to Comments = Only One to Zero or Many

| ![Data Model ERD mk.1](/assets/readme_images/erd.png) |
|:--:|
|Data Model ERD 1st design|

After 1st Mentor meeting (project inception stage), a few alterations were suggested for the data model. The alterations can be seen in the model below. They consist of the creation of a categories model to be used for storing category information and mapped to multiple posts and the addition of an edited key in the post and comment model to show if they have been edited.

| ![Data Model ERD mk.2](/assets/readme_images/erd_2.png) |
|:--:|
|Data Model ERD 2nd design|

Upon revision of ERD and Django data models, the decision was made to implement a custom data model that extends the in built Django User model. This decision was made in order to allow extra fields to be added with greater ease in future development of the data model. Additional fields were also added to the Category and Comments model.

| ![Data Model ERD mk.3](/assets/readme_images/erd_3.png) |
|:--:|
|Data Model ERD 3rd design|

After facing difficulties implementing login/register functionality, the decision was taken to drop the current user model and to use the default Django user model combined with AllAuth for authentication. Updated ERD is below.

| ![Data Model ERD mk.4](/assets/readme_images/erd_4.png) |
|:--:|
|Data Model ERD 4rd design|

This model may evolve as the project develops and MVP targets are met, any development will be detailed here.

## Skeleton
A simple wireframe of the site was created to visualise navigation, layout and design. Some features included in the wireframe are not mandatory and would be considered nice to have. If these are not included a rationale will be included in the [User Stories](#user-stories) section. This wireframe can be seen below.

| ![Homepage Wireframe](/assets/readme_images/wireframe_home.png) |
|:--:|
|Homepage|

| ![Login Wireframe](/assets/readme_images/wireframe_login.png) |
|:--:|
|Login|

| ![Register Wireframe](/assets/readme_images/wireframe_register.png) |
|:--:|
|Register|

| ![Categories Wireframe](/assets/readme_images/wireframe_categories.png) |
|:--:|
|Categories/All Posts|

| ![Post Detail Wireframe](/assets/readme_images/wireframe_postdetail.png) |
|:--:|
|Post Detail|

| ![My Posts Wireframe](/assets/readme_images/wireframe_myposts.png) |
|:--:|
|My Posts|

| ![New Post Wireframe](/assets/readme_images/wireframe_newpost.png) |
|:--:|
|New Post|

| ![Edit Post Wireframe](/assets/readme_images/wireframe_editpost.png) |
|:--:|
|Edit Post|

## Surface
The surface level of the project, including color schemes, font styling and images will be developed as the site is built. This will be documented here.

# Agile Implementation
This is some info about the implementation of Agile processes in the project.

## User Stories
Below is a table containing project epics and associated user stories. Clicking on the epic title will take you to the Github epic page where you can investigate user stories further and see their tasks and acceptance criteria.


| **EPIC**          | **User Story**                                                                                                        | **Completed** |
|-------------------|-----------------------------------------------------------------------------------------------------------------------|---------------|
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
| [**CRUD Functionality**](https://github.com/eosull/Something-Like/issues/16) |                                                                                                                       | &cross; |
|                   | As an Authorised User I want to Create, Read, Update and Delete Posts So that I can Create Content for other users to engage with.                                                                                                                       | &check; |
|                   | As an Authorised User I want to Create, Read, Update and Delete Comments So that I can Create Content for other users to engage with.                                                                                                                       | &cross; |

## Sprints
Working sprints were undertaken with the MVP of the project in mind to complete the development. They are as follows:

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

# Features
These are some of the features of the project.

# Tools and Technologies
These are the tools and technologies used in the development of the project.

# Testing
These are the testing processes that were carried out.

# Bugs
Deployment to Heroku: build was failing on Heroku and I was met with the following error: *ERROR: Could not build wheels for backports.zoneinfo, which is required to install pyproject.toml-based projects*. A search on slack [found a student](https://code-institute-room.slack.com/archives/CHDVDV2Q4/p1681717148021239) who had faced a similar issue, the cause being heroku is using a new version of Python and needs to be told to use an older version for backports.zoneinfo to run. Good info and possible solution found on [Stack Overflow](https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta). Added runtime.txt file in directory and specified use of python-3.11.3 to resolve. This didn't work as I was getting the same error. Found more people facing the same issue on Slack and avoiding the install of backports if python version is greater that 3.9 [was suggested](https://code-institute-room.slack.com/archives/C026PTF46F5/p1677505066005429). This worked and project was successfully deployed to Heroku.

Custom User Model: The initial plan for development was to create a custom user model that would allow for further customation as the project developed. This was created in a separate accounts app. Upon trying to implement login/register functionality this was creating problems with connecting urls, views and templates as well as taking up a lot of development time. The decision was taken to remove this accounts app and stick to the perfectly adequete Django default user model and use AllAuth for authentication in order to keep development moving and to reach the MVP sooner.

Commenting: When trying to submit a comment I kept getting a Django error message telling me the comment form field 'author_id' was null and this violated not-null constraint. To resolve this I added the following line in the post method of blog/views.py to use the id in the request to fill this field: comment_form.instance.author_id = request.user.id .


# Deployment
This is how the project was deployed.

# Credits

Many thanks to my Code Institute mentor Adegbenga Adeye who provided feedback and support throughout the development of this project.

Repository created using the [Code Institute Student Template](https://github.com/Code-Institute-Org/gitpod-full-template)

Commit messages formatted based on [Conventional Commit Standards](https://www.conventionalcommits.org/en/v1.0.0/#summary) - useful cheatsheet for formatting these messages by Github user Zekfad [Here](https://gist.github.com/Zekfad/f51cb06ac76e2457f11c80ed705c95a3)

Diagrams, flowcharts and wireframes created using [LucidChart](https://www.lucidchart.com/). Of particular use for creation of Entity Relationship Diagram was their [Youtube tutorial](https://www.youtube.com/watch?v=QpdhBUYk7Kk&ab_channel=LucidSoftware) and [associated article](https://www.lucidchart.com/pages/how-to-draw-ERD).

Resources used in the creation of the data model include:
- [UUID as Primary Key](https://tech.serhatteker.com/post/2020-01/uuid-primary-key/)
- [Custom User Model Using Django Default User](https://learndjango.com/tutorials/django-custom-user-model#:~:text=There%20are%20two%20modern%20ways,know%20what%20you're%20doing.)
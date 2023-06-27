# Something Like Design Process

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

| ![Information Design Flowchart mk.1](/assets/readme_images/information_design_flowchart.png) |
|:--:|
|Information Design Flowchart MK.1|

| ![Information Design Flowchart mk.2](/assets/readme_images/information_flowchart_2.png) |
|:--:|
|Information Design Flowchart MK.2|

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
|Data Model ERD 4th design|

Likes have been added to both the Comment and Post data model while edited time has been added to Post data model.

| ![Data Model ERD mk.5](/assets/readme_images/erd_5.png) |
|:--:|
|Data Model ERD 5th design|

No further changes have been made to the data model.

## Skeleton
A simple wireframe of the site was created to visualise navigation, layout and design. This wireframe was developed on with each iteration of the site, this development can be seen below.

| ![Homepage Wireframe](/assets/readme_images/wireframe_home.png) |
|:--:|
|Homepage Wireframe|

| ![Homepage Iteration 1](/assets/readme_images/iteration_1_home.png) |
|:--:|
|Homepage Iteration 1|

| ![Homepage Iteration 2](/assets/readme_images/iteration_2_home.png) |
|:--:|
|Homepage Iteration 2|

| ![Homepage Iteration 3](/assets/readme_images/iteration_3_home.png) |
|:--:|
|Homepage Iteration 3|

| ![Homepage Iteration 4](/assets/readme_images/iteration_4_home.png) |
|:--:|
|Homepage Iteration 4|

| ![Register Wireframe](/assets/readme_images/wireframe_register.png) |
|:--:|
|Register Wireframe|

| ![Homepage Iteration 1](/assets/readme_images/iteration_1_register.png) |
|:--:|
|Register Iteration 1|

| ![Homepage Iteration 2](/assets/readme_images/iteration_2_register.png) |
|:--:|
|Register Iteration 2|

| ![Homepage Iteration 3](/assets/readme_images/iteration_3_register.png) |
|:--:|
|Register Iteration 3|

| ![Homepage Iteration 4](/assets/readme_images/iteration_4_register.png) |
|:--:|
|Register Iteration 4|

| ![Categories/Explore Wireframe](/assets/readme_images/wireframe_categories.png) |
|:--:|
|Explore Wireframe|

| ![Explore Iteration 1](/assets/readme_images/iteration_1_explore.png) |
|:--:|
|Explore Iteration 1|

| ![Explore Iteration 2](/assets/readme_images/iteration_2_explore.png) |
|:--:|
|Explore Iteration 2|

| ![Explore Iteration 3](/assets/readme_images/iteration_3_explore.png) |
|:--:|
|Explore Iteration 3|

| ![Explore Iteration 4](/assets/readme_images/iteration_4_explore.png) |
|:--:|
|Explore Iteration 4|

| ![Post Detail Wireframe](/assets/readme_images/wireframe_postdetail.png) |
|:--:|
|Post Detail Wireframe|

| ![Post Detail Iteration 1](/assets/readme_images/iteration_1_details.png) |
|:--:|
|Post Detail Iteration 1|

| ![Post Detail Iteration 2](/assets/readme_images/iteration_2_details.png) |
|:--:|
|Post Detail Iteration 2|

| ![Post Detail Iteration 3](/assets/readme_images/iteration_3_details.png) |
|:--:|
|Post Detail Iteration 3|

| ![Post Detail Iteration 4](/assets/readme_images/iteration_4_detail.png) |
|:--:|
|Post Detail Iteration 4|

| ![Edit Post Wireframe](/assets/readme_images/wireframe_editpost.png) |
|:--:|
|Edit Post Wireframe|

| ![Edit Post Iteration 1](/assets/readme_images/iteration_1_edit_post.png) |
|:--:|
|Edit Post Iteration 1|

| ![Edit Post Iteration 2](/assets/readme_images/iteration_2_edit_post.png) |
|:--:|
|Edit Post Iteration 2|

| ![Edit Post Iteration 3](/assets/readme_images/iteration_3_edit.png) |
|:--:|
|Edit Post Iteration 3|

| ![Edit Post Iteration 4](/assets/readme_images/iteration_4_edit.png) |
|:--:|
|Edit Post Iteration 4|

## Surface
The surface level of the project, including color schemes, font styling and images will be developed as the site is built. This will be documented here.

### Colour Scheme
The site has core colouring of an off-white and black for background and text, with pops of colour in dynamic and interactive elements. The colour palette for these elements were generated using [Colormind](http://colormind.io/) and can be seen in the image below. Each of these colours are assigned to a category. In addition, the avatars generated using [Boring Avatars](https://github.com/boringdesigners/boring-avatars-service) provide nice colour on the post detail page. This will be customised to be generated from the site colour palette in future iterations.

| ![Colormind Color Palette](/assets/readme_images/color_pallete_iteration_2.png) |
|:--:|
|Colormind Colour Palette|

Colour Scheme was altered as part of Iteration 4, in order to increase contrast between elements and improve accessibility. The colour scheme is as follows:
- White: #fdf2f2
- Grey: #a8a4a464
- Black: #100f0f
- Dark blue: #3f5673
- Dark blue opaque: #3f567396
- Light blue: #2b7f78
- Green: #45703e
- Orange: #bc5201
- Red: #c52f36

The main colours on the site can be seen below.

| ![Final Color Palette](/assets/readme_images/color_palette_final.png) |
|:--:|
|Final Colour Palette|

### Font Styling
Google Fonts was used to import fonts. A striking Bebas Neue was used for headings and important content with Montserrat used for body text and site content.
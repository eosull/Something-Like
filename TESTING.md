# Manual Testing

Below are the manual tests carried out on Iteration 4 and the results of the tests. These tests were carried out to test the core functionality of the site.

| Page  | HTML Validation | Accesibility Score | Links functioning | Forms Functioning
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Index  | &check; | 100 | &check; | NA |
| Explore  | &check; | 100 | &check; | &check; |
| Login  | &check; | 100  | &check; | &check; |
| Register  | &check; | 100 | &check; | &check; |
| Post Detail  | &check; | 100 | &check; | &check; |
| New Post  | &check; | 100 | &check; | &check; |
| Edit Post  | &check; | 100 | &check; | &check; |

**Note** - HTML validation presents errors on some pages due to extension from Django base template or rendering of forms. Any errors shown that could be fixed were.

Using Code validation tools detailed in [README](README.md#testing) the following results were acheived:

| CSS  | Python | Javascript |
| ------------- | ------------- | ------------- |
| &check; | &check; | &check; |

Python manual functionality testing is detailed below:
- **admin.py**
  - Post register function:
    - Posts showing on admin panel, all fields present as expected
  - Comment register function:
    - Comments showing on admin panel, all fields present as expected
    - Comment approval function works as expected
  - Category register function:
    - Categories showing on admin panel

- **forms.py**
  - New Post Form:
    - Fields and help text showing correctly
    - Placeholder text showing as expected
    - Title autofocused on page loading
    - Custom classes added to inputs successfully
    - Does not submit with empty fields
    - Post displaying correctly after submission
  - New Comment Form:
    - Fields showing correctly
    - Placeholder showing correctly
    - Custom classes added to inputs successfully
    - Does not submit with empty fields
    - Comment approval message showing on submission
    - Comment showing once approved
  - Post Filter Form:
    - Fields showing correctly
    - Date filtering works as expected
    - Category filtering works as expected
  - Register Form:
    - Custom classes added successfully
  - Login Form:
    - Custom classes added successfully
- **models.py**
  - Category Model:
    - Fields showing correctly
    - String return working correctly
  - Post Model:
    - Fields showing correctly
    - Cascade deletion working for user and category
    - String return working correctly
    - Like count return working
    - Created and Edited time comparison working
  - Comment Model:
    - Fields showing correctly
    - Cascade delete working for user and post
    - String return working correctly
    - Like count return working
- **blog/urls.py**
  - Index URL functioning
  - Explore URL functioning
  - Post Detail URL functioning
  - New Post URL functioning
  - Edit Post URL functioning
  - Delete Post URL functioning
  - Post Like URL functioning
  - Comment Like URL functioning
- **views.py**
  - Index View:
    - Post list showing as expected
    - Template rendering correctly
  - Explore View:
    - Filtering working as expected
    - Content Showing as expected
    - Template rendering correctly
  - New Post View:
    - Form rendered and working correctly
    - Edit Post Form rendered and working correctly
    - Delete Post Form rendered and working correctly
  - Post Detail View:
    - Post rendering all information correctly
    - Comments rendering correctly
    - Likes rendering correctly
    - Comment posting functioning correctly
    - Like posting functioning correctly
  - Post Like View:
    - Post liking functioning correctly
  - Comment Like View:
    - Comment liking functioning correctly
- **something_like/urls.py**
  - Admin site URL functioning
  - Summernote URL functioning
  - Blog URL functioning
  - AllAuth URL functioning

Manual testing carried out during each iteration is detailed here:

<details>
<summary>Iteration 1</summary>

### Accessibility 

Lighthouse Testing was conducted on the first iteration of the site to detect accessibility issues with the initial design. A score of 100 was acheived with nothing to address at this stage of development.

| ![Iteration 1 Lighthouse](/assets/readme_images/iteration_1_lighthouse.png) |
|:--:|
|Iteration 1 Lighthouse Test|

### HTML 

The code at this stage of development was passed into the [W3 HTML Validator](https://validator.w3.org/), with 2 solvable issues being presented - button hierarchy on Edit Post page and form action on Delete Post page. Both of these issues were resolved.

| ![Iteration 1 HTML Button Error](/assets/readme_images/iteration1_button_html_error.png) |
|:--:|
|Iteration 1 HTML Button Error|

| ![Iteration 1 HTML Form Action Error](/assets/readme_images/iteration1_form_action_error.png) |
|:--:|
|Iteration 1 HTML Form Action Error|

The other issues highlighted by the validator were related to the use of Django templating in the HTML files.
</details>

<details>

<summary>Iteration 2</summary>

### Python

Manual testing was completed to ensure views, urls and templates were hooked up properly. Forms were also tested to ensure they functioned as intended.

### Javascript

Javascript automated testing using Jest was not implemented in this Iteration due to the minimal amount of JS present (One function to time out messages). This was manually tested and further JS added will be subject to automated testing.

### HTML 

The code at this stage of development was passed into the [W3 HTML Validator](https://validator.w3.org/), some small issues were presented such as extra closing tags and unecessary closing slash on input elements. These were resolved and no issues currently showing. 

### CSS

CSS code was passed into the [Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/). No errors were found.

### Accessibility 

Running lighthouse test on the site at this stage produced a score of 100 for accessibility.

| ![Iteration 2 Lighthouse](/assets/readme_images/iteration_2_lighthouse.png) |
|:--:|
|Iteration 2 Lighthouse Test|

### Site Goal testing

#### User Experience
The site should is intuitive and easily navigable, provides feedback to user actions, responsive to different screen sizes and accessible.

#### Functionality
A user can register and login, becoming authorised. They can then create a categorised post detailing a piece of work they like. They can also comment on other posts as well as edit and delete their posts and comments. Unauthorised users can view posts and comments on the site.

#### Content
The site contains core content of post previews, post details categorised posts and comments underneath posts

</details>

<details>

<summary>Iteration 3</summary>

### Python

Manual testing was again performed to ensure views, urls and templates were hooked up properly. Forms were also tested to ensure they still functioned as intended.

No additional automated testing was added in this iteration.

### Javascript

JS functionality tested manual and functioning. No automated tests developed.

### HTML 

The code at this stage of development was passed into the [W3 HTML Validator](https://validator.w3.org/), no issues were found.

### CSS

CSS code was passed into the [Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/). The following error was presented, where 'center' had been used as a value for float when this is not a valid value. Removing this line removed the error and meant the code passed.

| ![Iteration 3 CSS](/assets/readme_images/iteration_3_CSS_error.png) |
|:--:|
|Iteration 3 CSS Error|

### Accessibility 

Running lighthouse test on the site at this stage produced a score of 97 for accessibility. The failing issues were related to contrast ratio between background and foreground elements. This will be addressed in Iteration 4 development.

| ![Iteration 3 Lighthouse](/assets/readme_images/iteration_3_lighthouse.png) |
|:--:|
|Iteration 3 Lighthouse Test|

### Site Goal testing

The site still meets the goals set out at the beginning of development, as laid out in Iteration 2 Site Goal Testing.

</details>

# Automated Testing

The [Django testing modules](https://docs.djangoproject.com/en/4.2/topics/testing/overview/) were used to automate testing of python code. These use the Python standard library module unittest. A separate testing database is used while test cases are run and then deleted. For testing the views the django Client module was used simulating get and post requests. I used a [combination of coverage and django-nose](https://django-testing-docs.readthedocs.io/en/latest/coverage.html) to measure test coverage for my app as I built the tests.

The first tests were built for the models in the test_models.py file, testing methods like string return and counting functionality. Then the basic functionality for the views such as redirects and correct template usage were built in test_views.py.

These tests were developed during iteration 2 development but were not prioritised during iteration 3 & 4 so final coverage for code is at 77%.

| ![Coverage Report](/assets/readme_images/coverage_report.png) |
|:--:|
|Python Testing Coverage|

# Site Goals & User Story testing

As can be seen in [Readme User Story section](README.md#user-stories), User story completion was tracked in a table as well on the [project board](https://github.com/users/eosull/projects/7). On review of these records, it can be seen that the site hits the goal of providing a platform for users looking for film, tv, music or book recommendations to share personalised recommendations with one another.

The User stories not completed were considered to be features that were extra or 'nice to have'. 
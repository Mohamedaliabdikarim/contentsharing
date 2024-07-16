# CONTETSHARING

This project aims to create a comprehensive social media application using Django. The core functionalities of the application include user profile management, categorization of posts, image processing, and social interactions such as likes, comments, and following.
This is the back-end repository for the Django Rest Framework web API of Contentsharing. For the React frontend of the project, please refer to the repository located [here](https://github.com/Mohamedaliabdikarim/contentsharingcode).


# Planning

Planning began with the creation of epics and user stories for the frontend application, aligned with the project's goals. These user stories guided the development of wireframes that outlined the intended functionality. For more details, refer to the frontend React app repository [here](https://github.com/Mohamedaliabdikarim/contentsharingcode).

The user stories needed to achieve a minimum viable product (MVP) were mapped to the API endpoints on the back-end necessary to support the desired functionality.

## Data Models

# Django Models Documentation

This document provides an overview of the Django models used in our application. Below, you'll find descriptions of each model along with their fields and relationships.

## Profile Model

- **Profile**: Extends the default Django `User` model to include additional fields like `name`, `content`, and `image`.
  - `owner`: A one-to-one relationship with the `User` model.
  - `created_at`: Timestamp for when the profile is created.
  - `updated_at`: Timestamp for when the profile is last updated.
  - `name`: An optional field for the profile name.
  - `content`: An optional field for profile content.
  - `image`: An image field with a default profile picture.
  - `Meta`: Orders profiles by creation date in descending order.

- **create_profile**: A signal that creates a `Profile` instance whenever a new `User` is created.

## Category Model

- **Category**: Represents different categories a post can belong to.
  - `name`: A unique name for the category, chosen from predefined options.

## Post Model

- **Post**: Represents a blog post or article.
  - `owner`: A foreign key linking to the `User` model.
  - `category`: A foreign key linking to the `Category` model, with a default value.
  - `created_at`: Timestamp for when the post is created.
  - `updated_at`: Timestamp for when the post is last updated.
  - `title`: The title of the post.
  - `content`: The content of the post, optional.
  - `image`: An optional image field with a default image.
  - `image_filter`: A choice field for selecting an image filter, with a default value.
  - `Meta`: Orders posts by creation date in descending order.

## Like Model

- **Like**: Tracks likes on posts.
  - `owner`: A foreign key linking to the `User` model.
  - `post`: A foreign key linking to the `Post` model.
  - `created_at`: Timestamp for when the like is created.
  - `Meta`: Orders likes by creation date in descending order.
  - `unique_together`: Ensures a user cannot like the same post more than once.

## Follower Model

- **Follower**: Represents the relationship of one user following another user.
  - `owner`: A foreign key linking to the `User` model, representing the follower.
  - `followed`: A foreign key linking to the `User` model, representing the followed user.
  - `created_at`: Timestamp for when the follow relationship is created.
  - `Meta`: Orders followers by creation date in descending order.
  - `unique_together`: Ensures a user cannot follow the same user more than once.

## Comment Model

- **Comment**: Represents comments on posts.
  - `owner`: A foreign key linking to the `User` model.
  - `post`: A foreign key linking to the `Post` model.
  - `created_at`: Timestamp for when the comment is created.
  - `updated_at`: Timestamp for when the comment is last updated.
  - `content`: The content of the comment.
  - `Meta`: Orders comments by creation date in descending order.

## API endpoints

| **URL** | **Notes** | **HTTP Method** | **CRUD operation** | **View type** | **POST/PUT data format** |
|---|---|---:|---|---:|---|
|  |  |  |  |  |  |
| **Comment endpoints** |  |  |  |  |  |
| /comments | List comments or create a comment if logged in. | GET, POST | Read, Create | List | {<br>    "content": "string",<br>    "post": "integer"<br>} |
| /comments/id | Retrieve a comment, or update or delete it by id if you own it. | GET, PUT, DELETE | Read, Update, Delete | Detail | {<br>    "content": "string"<br>} |
| **Follower endpoints** |  |  |  |  |  |
| /followers | List all followers, i.e. all instances of a user following another user.<br>Create a follower, i.e. follow a user if logged in. | GET, POST | Read, Create | List | {<br>    "followed": "integer"<br>} |
| /followers/id | Retrieve a follower.<br>No Update view, as we either follow or unfollow users.<br>Destroy a follower, i.e. unfollow someone if owner. | GET, DELETE | Read, Delete | Detail | N/A |
| **Like endpoints** |  |  |  |  |  |
| /likes | List likes or create a like if logged in. | GET, POST | Read, Create | List | {<br>    "post": "integer"<br>} |
| /likes/id | Retrieve a like or delete it by id if you own it. | GET, DELETE | Read, Delete | Detail | N/A |
| **Post endpoints** |  |  |  |  |  |
| /posts | List posts or create a post if logged in.<br>The perform_create method associates the post with the logged in user. | GET, POST | Read, Create | List | {<br>    "title": "string",<br>    "content": "string",<br>    "category": "integer"<br>} |
| /posts/id | Retrieve a post and edit or delete it if you own it. | GET, PUT, DELETE | Read, Update, Delete | Detail | {<br>    "title": "string",<br>    "content": "string",<br>    "category": "integer"<br>} |
| /posts/category/category_name | List posts filtered by category. | GET | Read | List | N/A |
| **Category endpoints** |  |  |  |  |  |
| /categories | List all categories or create a new one. | GET, POST | Read, Create | List | {<br>    "name": "string"<br>} |
| /categories/id | Retrieve, update, or delete a category by id. | GET, PUT, DELETE | Read, Update, Delete | Detail | {<br>    "name": "string"<br>} |
| **Profile endpoints** |  |  |  |  |  |
| /profiles | List all profiles.<br>No create view as profile creation is handled by Django signals. | GET | Read | List | N/A |
| /profiles/id | Retrieve or update a profile if you're the owner. | GET, PUT | Read, Update | Detail | {<br>    "name": "string",<br>    "content": "string",<br>    "image": "string"<br>} |



# Frameworks, libraries and dependencies

# Contentsharing API

The contentsharing API is implemented in Python using Django and Django Rest Framework.

The following additional utilities, apps, and modules were also used:

- **django-cloudinary-storage**
  - Enables Cloudinary integration for storing user profile images in Cloudinary.
  - [Link](https://pypi.org/project/django-cloudinary-storage/)

- **dj-allauth**
  - Used for user authentication. While not currently utilized, this package enables registration and authentication using a range of social media accounts. This may be implemented in a future update.
  - [Link](https://django-allauth.readthedocs.io/en/latest/)

- **dj-rest-auth**
  - Provides REST API endpoints for login and logout. The user registration endpoints provided by dj-rest-auth are not utilized by the contentsharing frontend, as custom functionality was required and implemented by the Contentsharing API.
  - [Link](https://dj-rest-auth.readthedocs.io/en/latest/introduction.html)

- **djangorestframework-simplejwt**
  - Provides JSON Web Token (JWT) authentication.
  - [Link](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

- **dj-database-url**
  - Creates an environment variable to configure the connection to the database.
  - [Link](https://pypi.org/project/dj-database-url/)

- **psycopg2**
  - Database adapter to enable interaction between Python and the PostgreSQL database.
  - [Link](https://pypi.org/project/psycopg2/)


- **django-cors-headers**
  - This Django app adds Cross-Origin Resource Sharing (CORS) headers to responses, to enable the API to respond to requests from origins other than its own host. contentsharing is configured to allow requests from all origins, to facilitate future development of a native mobile app using this API.
  - [Link](https://pypi.org/project/django-cors-headers/)


  # Deployment


The Contentsharing API is deployed to Heroku, using an ElephantSQL Postgres database. To replicate this deployment, follow these steps:

1. **Fork or clone this repository in GitHub.**

2. **Set Up Cloudinary for User Profile Images:**
    - Create a Cloudinary account if you don't have one.
    - Log in to Cloudinary.
    - Go to the 'dashboard'.
    - Copy the 'API Environment variable' (starts with `cloudinary://`). You may need to click the eye icon to see the full variable. Save this temporarily.

3. **Create a New Heroku App:**
    - Log in to Heroku.
    - Select 'Create new app' from the 'New' menu at the top right.
    - Enter a name for your app and choose the appropriate region.
    - Click 'Create app'.

4. **Set Up ElephantSQL:**
    - Log in to ElephantSQL.
    - Click 'Create new instance'.
    - Name your plan and select the 'Tiny Turtle (free)' plan.
    - Choose the nearest data center to your location.
    - Click 'Review' and then 'Create instance'.
    - Go to the ElephantSQL dashboard, click on your new instance name, and copy the 'URL' (starts with `postgres://`).

5. **Configure Heroku:**
    - Go back to your Heroku dashboard.
    - Go to the 'Settings' tab.
    - Click 'Reveal Config Vars'.
    - Enter the following config variables:
        - `CLOUDINARY_URL`: your Cloudinary URL
        - `DATABASE_URL`: your ElephantSQL URL
        - `SECRET_KEY`: your Django secret key
        - `ALLOWED_HOST`: your Heroku app URL (without the `https://` prefix)

6. **Deploy from GitHub:**
    - In Heroku, go to the 'Deploy' tab.
    - Select 'GitHub' as the deployment method and connect your GitHub account if prompted.
    - Search for your repository and click 'Connect'.
    - Under 'Automatic Deploys', optionally enable automatic deploys from the `main` branch.
    - Under 'Manual Deploy', select the `main` branch and click 'Deploy Branch'.

7. **Final Steps:**
    - Wait for the deployment process to complete.
    - Once finished, you will get a link to your deployed API.

Your API will now be deployed to Heroku, and you can access it using the provided link.

# Credits
- code 
[drf-api](https://github.com/Code-Institute-Solutions/drf-api/tree/e3c785ad9f0dfaae57766e948b722f0db49ef4dd)
- image uploads [cloudinary](https://cloudinary.com/)

# Python validation
All files with custom Python code were subsequently validated using the [Code Institute Python Linter:](https://pep8ci.herokuapp.com/), no errors found

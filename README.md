# Welcome to Hiker's Guide!

The purpose of this website is to help hikers find the best hiking trails that Sweden has to offer, the website is targeted towards people who enjoy hiking and want to read more about the different hiking trails in Sweden. 

Information such as difficulty or distance of a trail is easily navigated to and available to the user. Users can also create an account with the website and sign in, this will allow them to interact with the website by liking or posting a comment on an individual blog post.
The admin users of the site can add new hiking trails, delete current ones, or edit/update hiking trails that you are the author of.

The website is fully responsive, providing users with the possibility of accessing the website on desktop, tablet or phone.

![Screenshot_20230203_033410](https://user-images.githubusercontent.com/114813115/216629918-c7499734-a0ea-41d9-b85a-f2bf34ab0d98.png)

## Index - Table of Contents

* [User Experience](#user-experience-(UX))
* [Entity Relationship Diagram](#entity-relationship-diagram)
* [Wireframes](#wireframes)
* [Features](#Features)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credits](#Credit)

Link to deployed project: https://hiking-spots.herokuapp.com/ 

## User Experience (UX)

**Epic: User Interactivity**

**User Stories**: 
- Site User - View post list
As a **Site user** I can **view a list of posts** so that **I can select one to read**.

- Site User - Liking Posts
As a **Site User** I can **like a post** so that **I can provide positive feedback to the author**.

- Site User/Admin - View likes
As a **Site User or Admin** I can **view the number of likes on each post** so that **I can see how popular or trending a post is**.

- Site User/Admin - View comments
As a **Site User or Admin** I can **view the comments on an individual post** so that **I can read the conversation**.

- Site User - Comment on a post
As a Site User I can comment on a post so that I can be involved in the conversation.

- Site User - Google Static Map
As a **Site user** I can **view an image of a map for an individual trail** so that **I can see where the trail is located**.

- Site User - Message Handling
As a **Site user** I can **get a message when logging in or out** so that **I can get clear visual feedback**.

**Epic: Admin capabilities**

**User Stories**: 
- Admin - Post management
As a **Site Owner** I can **create, read, update and delete posts** so that **I can manage my blog content**.

- Admin - Create drafts
As a **Site owner** I can **create draft posts** so that **I can finish writing the content later**.

- Admin - Approve comments
As a **Site owner** I can **approve or disapprove comments** so that **I can filter out objectionable comments**.

- Admin - Adding posts
As a **Admin** I can **add posts through the dashboard** so that **I can add posts without having to access the admin panel**.

- Admin - Deleting posts
As a **Site Admin** I can **delete my blog post when viewing them individually** so that **I can delete posts without accessing the admin panel**.

- Admin - Editing posts
As a **Site Admin** I can **Edit a blog post** so that **I can manage my blog content without accessing the Admin Panel**.

**Epic: Account Management**

**User Stories**: 
- Site User - Account registration
As a Site **user** I can **register an account** so that **I can like and comment posts**.

- Site User - Log in
As a **user** I can **log in to an already existing account** so that **I can post comments and like posts**.

- Site User - Logout
As a **Site user/admin** I can **log out of my account** so that **I am no longer logged in**.

**Epic: Site Navigation**

- Site User - About us Page
As a **Site user** I can **Read about the website in the "about us" section** so that **I can get information about the website**.

- Site User - Difficulty levels
As a **Site user** I can **view a page explaining how difficulty levels are calculated** so that **I can understand the different difficulty levels**.

- Site User - Google Static Map
As a **Site user** I can **view an image of a map for an individual trail** so that **I can see where the trail is located**.

User stories are being tracked using GitHub Projects. All User Stories have been divided into Acceptance Criteria and Tasks. 

### Wireframes
When designing the layout of the website I created Wireframes for the landing page, the blog post page, and the about page.
![Screenshot_20230124_064438](https://user-images.githubusercontent.com/114813115/216374043-3b2a89fd-d16a-4fe1-a4b6-2ab8263bb8e2.png)
![Screenshot_20230124_070553](https://user-images.githubusercontent.com/114813115/216374093-c632812a-37d8-46be-ba68-317159c719f1.png)
![Screenshot_20230124_070630](https://user-images.githubusercontent.com/114813115/216374135-f9f82142-d50e-4e1d-b4ec-35f02aa5a2cd.png)
![Screenshot_20230124_071014](https://user-images.githubusercontent.com/114813115/216374164-4b049bc7-8814-471f-8125-f4bc583a6a74.png)

### Entity Relationship Diagram
I created an Entity Relationship Diagram (ERD) showing the relationship between the Post model, Comment model and the Default Django User Model. In the diagram the Fields latitude and longitude is missing. This is because I added these fields later in the project and could not change the diagram since my free trial with the drawing platform had ended. 
Both the latitude and longitude has a FloatField and should be included in the Post model.

![ERD PP4](https://user-images.githubusercontent.com/114813115/216373254-05b4a2c4-4920-4e08-9a77-b2998f89a9f3.png)

## Features

## Existing Features

### Navigation bar
  - The navigation bar features a Logo in the middle, that acts as a link to the home page. The navigation bar has a consistent placement on each page making the website easy to navigate. The navigation bar is responsive, logo size, text and icons adapts to different screen sizes.
The left dropdown menu features links to the Home, About us, and Difficulty Scale pages. The right icon representing a user has links to the Home, Register and Login pages if the user is not logged in. If the user is logged in however, the dropdown menu will include links to the Home and Logout pages.

![Screenshot_20230202_124957](https://user-images.githubusercontent.com/114813115/216375112-2ab21afc-a0f2-485d-ae0f-fbb0dbfc9e54.png)
![Screenshot_20230202_125015](https://user-images.githubusercontent.com/114813115/216375148-b003dce7-5f6c-4af1-82fd-6a8505708882.png)
![Screenshot_20230202_124934](https://user-images.githubusercontent.com/114813115/216375215-38d89104-a1f6-437a-bbff-1a7b76c50b98.png)

## The Landing Page
  - The landing page consists of the different hiking trails that the admin has posted, sorted by the most recent posts first. Each hiking trail on the landing page has an image, Title, name of the author, an excerpt for the post and also the difficulty level of the trail. 
The date and time that the post was created, as well as the number of likes on each post is also visible to the user. If a user has admin capabilities they will also see a button labeled “Add post”, which gives admin the possibility to add posts without having to access the admin panel.
![Screenshot_20230202_010106](https://user-images.githubusercontent.com/114813115/216375613-a9529c11-b5c2-4349-9007-8a77cc9bccdc.png)
![Screenshot_20230202_010047](https://user-images.githubusercontent.com/114813115/216375632-8ee30d60-8e0b-47b6-9e3d-56584d4abab9.png)

## The Blog Post Page
- The individual blog posts include individual images, titles, content and map, but they are all built using the same form. When viewing an individual blog post as a user who is not logged in, all content, the map rendered as an image, number of likes and the comments on the post will be rendered. 
When viewing an individual blog post as a user who is logged in, the possibility to like a blog post will be available, as will the possibility to leave a comment. 
When viewing an individual blog post as a superuser/admin, two extra buttons will appear underneath the title of the blog post. These are links to the Edit post and Delete post pages, providing the Admin with full CRUD functionality without accessing the admin panel. 
The map is rendered by taking the latitude and longitude provided in the add_post form and using them to provide coordinates to Google Maps Static API. This will create an image with a marker on the coordinates provided. 
I used Bootstrap to hide the post image and the image of the map along with its header on medium and small devices to provide better responsiveness. 
![Screenshot_20230202_050257](https://user-images.githubusercontent.com/114813115/216376657-c0d23238-c0af-426f-ae73-9409c8d72268.png)
![Screenshot_20230202_011212](https://user-images.githubusercontent.com/114813115/216376239-7a8caedf-5c33-49c6-9de7-7c8e8f9305a1.png)
![Screenshot_20230202_011304](https://user-images.githubusercontent.com/114813115/216376270-87df8793-9f4a-40e1-b412-5299c8667994.png)

## The Register Page
  - The Register page allows the user to sign up for an account. It also provides a link redirecting them to the login page if they already have an account.
  
![Screenshot_20230202_011636](https://user-images.githubusercontent.com/114813115/216378265-24558034-5fb4-4ad1-a8ed-67eda122b3a1.png)
  
## The Login Page
  - The login page allows users to sign in to their accounts. There is also a link redirecting them to the Register page if they do not have an account already. The user also has the possibility to select a 'Remember Me' option, so that the user’s login data will be stored in order to auto-fill the fields next time they return to the page.
  
![Screenshot_20230202_012426](https://user-images.githubusercontent.com/114813115/216378308-0a59e1ff-3a34-45eb-80ae-6c5ae55549bc.png)

## The Logout Page
  - The log out page allows users to sign out of their account, it confirms that the user wants to sign out, and also provides a button labeled “Back” that redirects users to the previous page without signing out of their account. 

![Screenshot_20230202_014821](https://user-images.githubusercontent.com/114813115/216378443-cacc7d0d-6207-44b2-a384-bfee47fe71a7.png)

## The About us Page
  - This page provides users with information about the website, reasons why the website exists and goals with the website can be found here. The page also includes links to the Login page and Register page, reminding users to sign up in order to be able to interact with the content.

![Screenshot_20230202_051204](https://user-images.githubusercontent.com/114813115/216379052-90cd96b3-b447-4bce-affa-0ff98f4bad98.png)

## The Difficulty Scale Page
  - The Difficulty Scale page explains how the website defines the different difficulty levels used to determine the difficulty of an individual trail. The page also includes links to the Login page and Register page, reminding users to sign up in order to be able to interact with the content.
  
![Screenshot_20230202_051303](https://user-images.githubusercontent.com/114813115/216379296-2dbae28b-f5c7-4d40-ab1f-f668191992d3.png)

## The Add Post Form
  - This form provides admin with the possibility to add a post from the website itself, the Add Post form includes all fields defined in the Post model. The form includes a button labeled “Submit” to add a new blog post, as well as a button labeled “Back” that will redirect the admin to the Home page without creating a post.

![Screenshot_20230202_051452](https://user-images.githubusercontent.com/114813115/216379990-936a35da-eb5c-42b6-84b6-b00d03dbdb44.png)

## The Delete Post Form
  - This form allows admins to delete a post from the website, given that they are the author of the blog post. By clicking the “Delete” button from the post_detail card, they are brought to the Delete page, where they can confirm that they want to delete the post by clicking “Delete”, they also have the option to click a button labeled “Back”, if they wish to keep the post.

![Screenshot_20230202_015118](https://user-images.githubusercontent.com/114813115/216378660-d59c9b94-20ad-4b58-b3f9-68b552c9340c.png)
  
  
## The Edit Post Form
  - This form is similar to the Add Post form, it allows admin to edit a post that is already created, since there can be many admins on the website, an admin also needs to be the author of the post in order to be able to edit it on the website. The form will open pre-loaded with the content from when it was created, allowing admins to easily change misspellings or any other content. The title or the author of the post can’t be changed.
  
![Screenshot_20230202_015136](https://user-images.githubusercontent.com/114813115/216378782-a0b47232-e566-4384-9e59-00dcd777b11a.png)
  
## Validation Messages
  - A validation message is shown to the user whenever they Sign in/out or register an account. They are also shown to admins whenever they successfully add a new hiking trail, delete a current one, or edit an existing one.

![Screenshot_20230202_015306](https://user-images.githubusercontent.com/114813115/216380229-dd5bc035-6457-4065-90e9-9708ec715ec9.png)

## Testing

I have written automatic tests for views, models and forms. They all pass.
![Screenshot_20230202_051758](https://user-images.githubusercontent.com/114813115/216381745-049099b1-99f5-4372-9821-38e2008a89cd.png)


### Manual testing:
- I have tested that this website works appropriately in the following browsers: Chrome, Firefox and Safari.
- I confirmed that this website looks good and functions the way it should on all standard screen sizes using the devtools device toolbar.
- I have confirmed that all headers and sections are legible in terms of positioning and readability.
- No elements are distracted by background-colors, and no images are stretched when viewed on different devices.
- I have made sure that all functions work properly and the website works as intended.
- I have made sure that all buttons work as intended.
- I have made sure that the register an account, login and logout features work as intended.
- I have made sure that the website is responsive to all devices, using bootstrap and CSS to make website adapt to different screen sizes.

### Manual testing - General Users

![Screenshot_20230202_054027](https://user-images.githubusercontent.com/114813115/216386497-bb35c305-b51b-49ca-a712-ade78d2e290f.png)
![Screenshot_20230202_054102](https://user-images.githubusercontent.com/114813115/216386595-aae3b81e-d44d-48e5-b2a2-a7ce1273ff0e.png)

### Manual testing - Logged in Users

![Screenshot_20230202_054234](https://user-images.githubusercontent.com/114813115/216387027-9dd64447-7c83-4828-b0fb-e02333a1ac69.png)

### Manual testing - Superusers

![Screenshot_20230202_054410](https://user-images.githubusercontent.com/114813115/216387393-ac030d54-bc33-40ea-ae06-3fb919db6bb2.png)

### Manual testing - Admin Panel

![Screenshot_20230202_054438](https://user-images.githubusercontent.com/114813115/216387548-c372eccf-1ff6-4475-9b78-04ee970cb42b.png)

- Lighthouse Testing 
I tested the landing page using DevTools Lighthouse test, this is the report i received.

![Screenshot_20230202_064300](https://user-images.githubusercontent.com/114813115/216401195-8e278109-d1b1-439e-bef0-7dc05818d27c.png)

- HTML Validator 

- I validated the HTML of the landing page through the View Source functionality, since the code is using non HTML elements that won't be visible when at the source-view. I received errors because my img elements did not have any alt attribute, after adding that I received no errors. 

![Screenshot_20230202_063748](https://user-images.githubusercontent.com/114813115/216400195-9735a155-4c64-4a73-bb73-a22399b061a6.png)

- CSS Validator 

- The CSS was validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator), and all code passed without any issues.

![Screenshot_20230202_064423](https://user-images.githubusercontent.com/114813115/216402171-5400c578-d407-4b11-8a04-a6582bc85278.png)

- Validator Testing - Python

Admin.py

![admin py python linter](https://user-images.githubusercontent.com/114813115/216402971-6e2e47d3-c480-4cab-b8ed-1fc49d8e3770.png)

Apps.py

![Screenshot_20230202_065229](https://user-images.githubusercontent.com/114813115/216403238-b38915f1-d92d-49f0-b619-6a9b091e18f1.png)

Forms.py

![Screenshot_20230202_065329](https://user-images.githubusercontent.com/114813115/216403429-d4a3657f-f741-4b1e-8403-45bbae78bfb1.png)

Models.py

![Screenshot_20230202_065440](https://user-images.githubusercontent.com/114813115/216403686-679e9c4e-577a-4011-8285-3244b31ca2fa.png)

test_forms.py

![Screenshot_20230202_065549](https://user-images.githubusercontent.com/114813115/216403979-64466b05-0577-4382-bb0f-2ed1af2aba91.png)

test_models.py

![Screenshot_20230202_065640](https://user-images.githubusercontent.com/114813115/216404151-c708eda9-ffd7-4318-aec9-b5e74c92f96e.png)

test_views.py 

![Screenshot_20230202_065746](https://user-images.githubusercontent.com/114813115/216404385-10e2f095-9c53-4bbf-b7b5-09788d762b46.png)

urls.py (blog)

![Screenshot_20230202_065830](https://user-images.githubusercontent.com/114813115/216404555-0725059f-8d5e-47ff-bace-dc4b2d1b0778.png)

views.py 

![image](https://user-images.githubusercontent.com/114813115/216415298-77f6e64e-e71a-4831-a474-70964d593938.png)

asgi.py

![Screenshot_20230202_071538](https://user-images.githubusercontent.com/114813115/216411041-a98fa828-2f4d-47e5-b4f6-741709b84dda.png)

Settings.py

![Screenshot_20230202_072703](https://user-images.githubusercontent.com/114813115/216415607-b1cbc880-4352-4a23-a265-e83407ec71dc.png)

urls.py (hikingspots)

![Screenshot_20230202_072045](https://user-images.githubusercontent.com/114813115/216413200-f6a994dd-a413-4123-a01e-6ee8c88fe79d.png)

wsgi.py

![Screenshot_20230202_072155](https://user-images.githubusercontent.com/114813115/216413522-614bf2bb-5b70-4f47-bd48-cbc0e13e11fc.png)

## Bugs
- There are no unfixed bugs.

## Deployment

### Local Deployment

To preview the project in the development environment, run the following command in the terminal:
```python3 manage.py runterminal```. This will open port 8000. Click *Open Browser* when the popup window appears.
To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/KarlPreisler/hiking-spots-blog.git`

### Preparing File for Deployment
If you have not already set up Postgres for use in the deployed application, complete the following steps:
- In the terminal, type `pip3 install psycopg2-binary` and press enter.
- Install gunicorn, which will act as the web server. Type `pip3 install gunicorn` in the terminal and press enter.
- You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, which I did, then the requirements file needs to be updated using: `pip3 freeze --local > requirements.txt`:
  - In the terminal, type `pip3 freeze --local > requirements.txt`. This will create or update a file called `requirements.txt`, with a list of all the packages that Heroku will need to install to run our app.
- Create a Procfile in the root folder of your project, and add this code to the Procfile: `web: gunicorn <app_name>.wsgi:application`.

### ElephantSQL Deployment
I have used ElephantSQL to host my database. 
The instructions to create a new account can be[found here](https://code-institute-students.github.io/deployment-docs/02-elephantsql/elephantsql-01-sign-up). 
Once you have created an account:
- Log in to ElephantSQL to access your dashboard.
- Click *Create New Instance*.
- Give your plan a name (usually the name of the project, in this case hiking-spots-blog*).
- Select the Tiny Turtle (Free) plan.
- Leave the Tags field blank.
- Click *Select Region* and choose a data center near you.
- Click *Review*, then, if everything looks correct, *Create Instance*.
- Go back to your dashboard and click on the name of the project. 
- Copy the database URL for your project, and use it in two places:
  - In your `env.py` file, create a new key called `DATABASE_URL` and give it the value of the ElephantSQL database URL, as follows: ` os.environ.setdefault("DATABASE_URL", "my_copied_database_url")`.
    - Before deploying the project, create a file called `env.py` (if it hasn't been created already), and complete the following steps:
      - In `settings.py`: At the top of the file, add the following import:
      ```python
      import os
      if os.path.isfile("env.py"):
          import env
      ```
      - Replace the pasted-in database url with the following code:
      ```python
      os.environ.get("DATABASE_URL")
      ```
  - Paste the database URL into the config vars section of your project on Heroku - instructions are in the *Heroku Deployment* section below. 

### Heroku deployment
This project uses [Heroku](https://www.heroku.com), a cloud based platform that enables developers to build and run applications.

I used the [Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) for this project. Here is the [Heroku documentation](https://devcenter.heroku.com/articles/heroku-cli) for the most up-to-date installation instructions. 

To log in to the Heroku CLI:

- In the terminal, type heroku login -i. 
- Enter your username and password in the terminal.
- If you have Multi-Factor Authentication turned on:
  - Click on Account Settings on the Heroku Dashboard.
  - Copy the key by scrolling down to the API Key section and click Reveal. 
  - Use the login command: heroku login -i
  - Enter your Heroku username.
  - Enter the API key.

To deploy the project from the Heroku dashboard:

- Select New in the top-right corner of your Heroku Dashboard, and select Create new app from the dropdown menu.
- Enter a name for your app. The app name must be unique.
- From the dropdown menu, select the region closest to you, and select Create App.
- From the Settings, click Reveal Config Vars. Add a new config var and add the KEY to 'PORT', and the value to '8000'.
- Add another Config Var with the KEY set to 'DATABASE_URL' and the value to the ElephantSQL database URL you copied above.
- Additional Config Vars:
  - 'CLOUDINARY_URL' copied from [Cloudinary](https://cloudinary.com/), used to store images.
  - 'SECRET_KEY' containing the secret key.
  - 'HEROKU_POSTGRESQL_COBALT_URL' with the Heroku postgres database URL. 

To connect your GitHub repository to the newly created app in Heroku:

- At the top of the screen on Heroku, select Deploy.
- Next to Deployment method select GitHub, then scroll down and click Connect to GitHub to confirm you want to connect.
- In the repo-name field, search for the name of the GitHub repository to deploy.
- Click Connect to connect the GitHub repository with Heroku. 
- Deploy Branch in the Manual deploy section, or enable automatic deploys.

Once the project is deployed, add the URL of the website to the ALLOWED_HOSTS in settings.py, using the following code:
- ALLOWED_HOSTS = ['<project_url>']

Push changes to GitHub and project will now be live on Heroku.

## Credits

## Content
- [Code Institute's Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used as the starting workspace template for this project.
- [Code Institute's README Template](https://github.com/Code-Institute-Solutions/readme-template) was used to structure this README.

## Acknowledgements
- Special thanks to my mentor Brian Machiara for helping me throughout the project. With everything from styling and responsiveness, to understanding the logical aspects such as building functions etc.  







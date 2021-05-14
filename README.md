# Contact-App-Project

For my third milestone project, I have decided to create a contact app for users so that they get to keep their information about his or her contact. 
The application is created to ensure that users can create, edit, update and delete their contacts. This is to address the information Architecture for processing, 
storing, retrieving, and updating data.

# Table of Contents
1. [UX](#UX)
2. [Target Audience](#Target-Audience)
3. [Wireframe](#Wireframe)
4. [Database](#Database)
5. [Features](#Features)
6. [Technologies Used](#Technologies-Used)
7. [External Hosting](#External-Hosting)
8. [Testing](#Testing)
9. [Testing User Stories](#Testing-User-Stories)
10. [Deployments](#Deployments)
11. [Credits](#Credits)

 
# UX

## UX Design
The main color scheme for the project was a mainly green and white background. It also consists of
the black text so that the users can easily see their contacts. Also, the navigation is placed orderly
to provide a user experience better.

## User Stories

### Users
- As a first-time user, I would like to create my account with the option to log in and log out so nobody else can access it.
- As a first-time user, I want to navigate easily to find the content and be able to see my contacts.
- As a user, I want to add my contact.
- As a user, I want to edit or delete my contact.

### Owner
- As an owner, I want my users to be able to have access to their contacts
- As an owner, I would like my users to navigate easily.
- As an owner, I would like to ensure users that they can keep their contacts.

## Target Audience
The main purpose of the application is to provide users with the functionality to create, 
edit, update and delete their contacts. This application aims to attract users who would like to keep their information easily so that they can get in touch with the person
that they know.

## Wireframe
I used Balsamiq to create the Wireframe for the project. This Wireframe contains
the schematics for the ideal project:

[Link to the Final Version of the Wireframe](/workspace/contact-app-project/wireframe/contact-app-wireframe-project.pdf)

## Database
I used MongoDB Atlas as a non-relational database to contain information
about the contacts. Here is the link to the database model that I designed:

[Database Model Design](/workspace/contact-app-project/database-designs/database-design.png)

## Data Design
This data shows it only contains two things: the users and the contacts. 
The functionality is structured to the following CRUD: Create, Read, Update, and Delete.
[Image of the Data Design](/workspace/contact-app-project/database-designs/database-diagram.png)

# Features

## Existing Features

### Structure
- Navbar - I used Materialize with the basic navbar with the title and mobile navbar with the
links to sections: Home, Profile, Add Contact, Log Out. When the navbar is resized, 
you will see that the links on the right turn into a hamburger icon, an effect of class=sidenav-trigger functionality.

### Forms
- Register form: This provides the interface to new users for sign-up.

- Login form: a form that enables users to sign into an already created account.

- Add Contact form: contain fields that enable users to add a new review to the website.

- Edit Contact form: This form retrieves existing review data for revise.

- Log out the form: This form allows users to sign out from their account.

### Home
- The Home page will display collapsible; accordion elements that expand when clicked on.
It also has a welcoming title. The collapsible header with delete and edit buttons for reviews while the collapsible body encapsulates 
the set of data stored about a particular instance of an entity.

### Profile
- The Profile section features exclusively for a user session. 
  All collections per user are stored in their respective profile Page and secure to only be available to the owner.

### Add New Contact
- This section will have the form where the user will put their contacts full name, telephone, and email.

### Security
- To make the user authentication more secure, the login form integrates werkzeug security features namely:
"generate_password_hash" and "check_password_hash". it is difficult to crack the passwords.

## Features Left to Implement
- To add some background.
- To add a search bar. 
- To add recovery options.
- To restrict access to unknown users

# Technologies Used

## Languages
- [HTML](https://html.com/)
- [CSS](https://www.w3schools.com/css/)
- [Javascript](https://www.w3schools.com/js/DEFAULT.asp)
- [Python](https://www.python.org/)

## Tools and Libraries
- [Materialize](https://materializecss.com/)
    - It was used to create the grid layout and styling various features such as navbar accordion, cards, buttons, and form to render a responsive website.
- [PEP8 Python Validator](http://pep8online.com/)
    - To validate the python code
- [JQuery](https://jquery.com)
    - It was used to simplify JavaScript.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - This is a web application framework used to create functions with Python that are injected into HTML templates.
- [Git](https://git-scm.com/)
    - It was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [Jshint](https://jshint.com/)
    - To validate my JavaScript code.
- [HTML Validator](https://validator.w3.org/)
    - To validate my HTML code.
- [CSS Validator](https://jigsaw.w3.org/css-validator/)
    - To validate my CSS code.
- [drawio](https://app.diagrams.net/)
    - Used to create the database schema and data manipulation operations diagrams.
- [dbdiagramio](https://dbdiagram.io/home)
    - Used to create the database schema diagram online.
- [font awesome](https://fontawesome.com/)
    - It was used to create the grid layout and styling various features such as navbar accordion, 
      cards, buttons, forms, and footer to render a responsive website.

# External Hosting
- [MongoDB](https://www.mongodb.com/)
    - a document-oriented cloud database used to store manage, query, and retrieve data set for the app.
- [Heroku](http://heroku.com/)
    - It was used to deploy, manage, and scale the app.
- [GitHub](https://github.com/)
    - The project used the GitHub hosting service to save the project in a repository.

# Testing

I have struggled a lot when it comes to testing. However, I was able to use some necessary measures to test my app with various resources. 
The Database Creation with MongoDB Atlas and Heroku deployment was very easy because I followed the well-implemented course in Code Institute Module. 
I used Chrome DevTools lighthouse to test the app to see how is it functioning well.

[Screenshot of lighthouse testing](/workspace/contact-app-project/images/ligthouse-dev tools-screenshot.png)

# Testing User Stories from User Experience (UX) Section

### Users:
1. As a first-time user, I would like to create my account with the option to log in and log out so nobody else can access it.
  - The user will see the Register form for first-time users to sign up.
  - Also the user will be able to log in at the Log in the form if their account is already created.
  - The user can log out at the Log Out form if they want to leave their account.
  - For security measures, the form will have the werkzeug security features such as 
    "generate_password_hash" and "check_password_hash". These hashing passwords will be good to keep their information secured.

2. As a first-time user, I want to navigate easily to find the content and be able to see my contacts.
    - At the top of each page there is a clean navigation bar, each link describes at what section they will end up at clearly.
    - The user will be able to see their contacts with the collapsible. It behaves as expected and each collapsible header has the name 
    and the details of the contact including which user created by.

3. As a user, I want to add my contact.
    - The users can make use of the Add Contact form by clicking Add Contact tab in the navbar menu.

4. As a user, I want to edit or delete my contact.
    - Each relevant section provides Edit/Delete buttons that allow users to revise or delete contacts that they added.

### Owner:
1. As an owner, I want my users to be accessible to their contacts
    - The composition of the app is clear and simple. Already at the home page, the users will be able
    to see their contacts easily including the information that they created

2. As an owner, I would like to ensure users that they can keep their contacts.
    - There is enough security for the users to keep their contacts safe. In the future, I hope
    to make more tough security on the contacts where the collapsible is accessed to each user.

## Bugs

### Fixed
- I have fixed the link between the contact.py and the base.html with '{{ url_for(edit_contacts)}}'
- I have fixed the contacts.html because I was having trouble with the wrapping of the contacts.

### Unfixed
- The validation for the forms because I failed to have the validation function when the user clicks 
if the form is not complete or incorrect.

### Further Testing
- All the links were tested. They all work perfectly.
- I have tested my app with Google Chrome, Microsoft Edge, and Safari.
- All Codes passed through their respective Validators to erase syntax errors.
- The button links work as expected.
- To prevent arbitrary code from running and security flaw, after the development stage, 
  I specify the debug=False before submission.
- I have tested it with my iPhone and IPad.

# Deployment

## Github
The app was developed on GitPod, using git and GitHub to host the repository as it cannot host a Python project on GitHub Page which only allows for static websites. 
Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

Note: It's important to contain our environment variables within a hidden env.py file 
which should never be pushed to GitHub by ensuring .gitignore has it secured.

# Heroku
Here are the following steps to take when to deploy using Heroku:

1. Create Heroku App
- Go to the Heroku website
- Go to sign up and create your account.
- Select Python as your primary language.
- Fill in your unique name and select your corresponding region.
- Click Create App.

2. Add requirements.txt file

- Type "pip3 freeze --local > requirements.txt"
- After that, I type "git add -A"
- Then type git commit -m "Add requirements.txt file" 
- Finally, type git push.

3. Add Procfile
- Type echo web: python contact.py > Profile
- Then type git add -A
- Then type git commit -m "Add Procfile"
- Finally, git push

4. Creating default environment variables
- Click Settings on the Heroku dashboard
- Click on Reveal Config Vars.
- Add the key of "IP" and the value of "0.0.0.0", and click on Add.
- Add the key of "PORT" and the value of "5000", then click Add.
- Add the key of "SECRET_KEY" and the value of "your secret key string here", then click Add.
- Add the key of "MONGO_URI" and the value of "mongo URI string here"
- Finally, add the key of "MONGO_DBNAME" and the value of "the name of your database here".

5. Setting-up Automatic Deployment from GitHub
- Click Deploy on the dashboard.
- Click Connect to GitHub.
- Ensure that my GitHub profile is displayed, then add my repository name (same as my Heroku App), 
  and then click search.
- Click connect once it finds the repository.
- Then safely click Enable Automatic Deployment.
- Select Branch and then click Deploy Branch.
- The message will say "Your App was successfully deployed"
- Click View to launch the app.

## Credits

### Code 
- The code came from the Code Institute mini project which inspired me to do something
different. I made some modifications to fit my needs.

### Acknowledgements

- I would like to thank Aaron for helping and supporting me with this project.
- I would like to thank the Tutor Support for their maximum effort to assist me.
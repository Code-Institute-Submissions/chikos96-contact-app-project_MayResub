# Contact-App-Project

For my third milestone project, I have decided to create a contact app 
for users so that they get to keep their information about his 
or her contact. 
 
# UX

## UX Design
The main color scheme for the project was mainly green and white background.

## User Stories

### Users
- As a first time user, I would like to create my own account with the option to login and logout 
  so nobody else can access it.
- As a first time user, I want to navigate easily in order to find the content and be able to see my contacts.
- As a user, i want to add my contact.
- As a user, i want to edit or delete my contact.

### Owner
- As a owner, I want my users to be able to have access to their contacts
- As a owner, I would like my users to navigate easily.
- As a owner, I would like to ensure users that they are able to keep their contacts.

## Target Audience
The main purpose for the application is to provide users with the functionality to create, 
edit, update and delete their own contacts. This application aims to attract users who 
would like to keep their information easily so that they can get in touch with the person
that they know.

## Wireframe
I used Balsamiq to create the Wireframe for the project. This Wireframe contains
the schematics for the ideal project:

[Link to the Final Version of the Wireframe](/workspace/contact-app-project/wireframe/contact-app-wireframe-project.pdf)

## Database
I used MongoDB Atlas as a non relational database to contain information
about the contacts. Here is the link to the database model that i designed:

[Database Model Design](/workspace/contact-app-project/database-designs/database-model-design.png)

## Data Design
This data shows it only contains two things: the users and the contacts. 
The functionality is structured to following CRUD: Create, Read, Update, and Delete.
[Image of the Data Design](/workspace/contact-app-project/database-designs/database-diagram.png)

# Features

## Existing Features

### Structure
- Navbar - I used Materialize with the basic navbar with the title and mobile-navbar with the
links to sections: Home, Profile, Add Contact, Log Out. When the nav bar is resized, 
you will see that the links on the right turn into a hamburger icon, an effect of class=sidenav-trigger functionality.

### Forms
- Register form: This provides interface to new users for sign up.

- Log In form: form that enable users to sign into already created account.

- Add Contact form: contain fields that enable users to add new review to the website.

- Edit Contact form: This form retrieves existing review data for revise.

- Log out form: This form allows users to sign out from their account.

### Home
- The Home page will display collapsibles; accordion elements that expand when clicked on.
It also has a welcoming title. The collapsible-header with delete and edit buttons for reviews while the 
collapsible-body encapsulates the set of data stored about a particular instance of an entity.

### Profile
- The Profile section features exclusively for a user session. 
  All collections per user are stored in their respective profile Page and secure to only be available to the owner.

### Add New Contact
- This section will have the form where the user will put theur contacts full name, telephone and email.

### Security
- To make the user authentication more secure, the Log In form integrates werkzeug security features namely:
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
- [PEP8 Python Validator](http://pep8online.com/)
- [JQuery](https://jquery.com)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Git](https://git-scm.com/)
- [Jshint](https://jshint.com/)
- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://jigsaw.w3.org/css-validator/)

# External Hosting
- [MongoDB](https://www.mongodb.com/)
- [Heroku](http://heroku.com/)
- [GitHub](https://github.com/)

## Testing

I have struggled a lot when it comes to testing. However i was able to use some necessary measures to test 
my app with various resources. The Database Creation with MongoDB Atlas and Heroku deployment was very easy 
because I followed the well implemented course in Code Institute Module.

# Testing User Stories from User Experience (UX) Section

### Users:
1. As a first time user, I would like to create my own account with the option to login and logout 
  so nobody else can access it.
  - The user will see the Register form for first time user to sign up.
  - Also the user will be able to log in at the Log in form if their account is already created
  - For security measures, the form will have the werkzeug security features such as 
    "generate_password_hash" and "check_password_hash". These hashing passwords will be good to keep their 
    information secured.

2. As a first time user, I want to navigate easily in order to find the content and be able to see my contacts.
    - At the top of each page there is a clean navigation bar, each link describes at what section 
    they will end up at clearly.
    - The user will be able to see their contacts with the collaspible. It behaves as expected and each
    collaspible-header has the name and the details of the contact including which user created by.

3. As a user, i want to add my contact.
    - The users can make use of the Add Contact form by clicking Add Contact tab in the navbar menu.

4. As a user, i want to edit or delete my contact.
    - Each relevant section provides Edit/Delete buttons which allow users to revise or delete contacts that they added.

### Owner:
1. As a owner, I want my users to be accessible to their contacts
    - The composition of the app is clear and simple. Already at the home page, the users will be able
    to see their contacts easily including the information that they created

2. As a owner, I would like to ensure users that they are able to keep their contacts.
    - There is enough security for the users to keep their contacts safe. In the future, i hope
    to make more tough security on the contacts where the collaspible is accessed to each user.

## Bugs

### Fixed
- I have fixed the link between the contact.py and the base.html with '{{ url_for(edit_contacts)}}'
- I have fixed the contacts.html because i was having trouble with the wrapping of the contacts.

### Unfixed
- The validation for the forms because i failed to have the validation function when the user clicks 
if the form is not complete.

### Further Testing
- All links were tested. Internal links all work. External links all work and open in new window.
- All Codes passed through their respective Validators to erase syntax error.
- To prevent arbitrary code from running and security flaw, after the development stage, 
  I specify the debug=False before submission.

## Deployment

# Github
The app was developed on GitPod, using git and GitHub to host the repository 
as it cannot host a Python project on GitHub Page which only allows for static websites. 
Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

Note: It's important to contain our environment variables within a hidden env.py file 
which should never be pushed to GitHub by ensuring .gitignore has it secured.

# Heroku
Here are the following steps to take when to deploy using Heroku:

1. Create Heroku App
- Go to Heroku website
- Go to sign up and create your own account.
- Select Python as your primary language.
- Fill in your unique name and select your corresponding region.
- Click Create App.

2. Add requirements.txt file

- Type "pip3 freeze --local > requirements.txt"
- After that, I type "git add -A"
- Then type git commit -m "Add requirements.txt file" 
- Finally, type git push.

3. Add Procfile
- Type echo web: python contact.py > Procfile
- Then type git add -A
- Then type git commit -m "Add Procfile"
- Finally git push

4. Creating default environment variables
- Click Settings on Heroku dashboard
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
- Click View to launch app.

## Credits

### Code 
- The code came from the Code Institute mini project which inspired me to do something
different. I made some modifications to definitely fit my needs.

### Acknowledgements

- I would like to thank Aaron for helping and supporting me with this project.
- I would like to thank the Tutor Support for their maximum effort to assist me.
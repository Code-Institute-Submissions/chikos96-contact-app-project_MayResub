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
the schematics for the ideal project

## Database
I used MongoDB Atlas as a non relational database to contain information
about the contacts.

## Data Design
This data shows it only contains two things: the users and the contacts. 
The functionality is structured to following CRUD: Create, Read, Update, and Delete.

# Features

## Existing Features

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
my app with various resources.

# Testing User Stories from User Experience (UX) Section

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
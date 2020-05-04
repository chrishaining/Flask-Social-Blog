# Social Blog App


Project to build a social blog app using Flask. The project is part of the [Python and Flask Bootcamp](https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/learn/lecture/11440740#content) course taught by Jose Portilla.

<p>
  <img src="./puppycompanyblog/static/profile_pics/default_profile.png" title="Fox" alt="A fox is like a puppy" width="400" height="300"/>
</p>


## About the app
The premise of the app is for users to create and view blog posts. The theme of the app is puppies (which seems to be a favourite topic of Jose's).

Aside from the learning aspect, the main goal of the app is to enable a user to:
* register as a user
* login
* view their own account details and update them
* create a blog post
* update and delete their own blog posts
* view their own blog posts as well as the blog posts of others.
It is also important that users can only update and delete their own details and blogs.

[Try the app on Heroku](https://flask-puppy-blog.herokuapp.com)

## Tech stack
The app was written in Python 3.8, using Flask 1.1.2, SQLite and SQLAlchemy. I've used pip for installing packages, and set up the app using a virtual environment. See `requirements.txt` for the list of packages used.

## What I learned
* how to upload a file to an app
* use of WTForms - takes some of the heavy lifting out of HTML forms
* registration and login management
* using `url_for` to link to other parts of the app
* use of __blueprints__ to structure a multi-component app
* how to deploy a Python app to Heroku

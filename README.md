
This is a python script to loop through all your repos from your API token and update review counts and enforce admins off the master branch

Creating this to mass update all of our repos settings.

First you need to create a personal token using the steps here https://github.com/settings/tokens, give all repo access except the delete repo access.

Then install the PyGitHub Python library to access the GitHub REST API.

$ pip install PyGithub

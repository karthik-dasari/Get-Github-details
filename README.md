# Get-Github-details

## Get Github details is a project in which you will enter the username of a person and the details related to that person will be shown.

#### I have used GitHub API to fetch the data.
#### This entire application was build using flask framework.

#### When an user enters a username and click Submit button then the username, profile picture, name, bio, last updated, number of followers and number of following will be displayed followed by number of repo's and details of that repo's will be displayed.
#### The data will be displayed without refreshing the page.
#### The history will be also stored, the user can retrive the his search history.
#### You can also delete the history.


https://user-images.githubusercontent.com/67855672/115133348-1f0b4b00-a025-11eb-98ba-4d851f666d71.mp4

## How to access this web application in your local machine?

#### ->Download or clone my repo.
#### ->Install python3, flask, flask_mysqldb. After installing python3 to install flask and flask_mysqldb run this commands "pip install flask" and "pip install flask_mysqldb".
#### ->You need to setup a database in your mySql server.
#### ->Download MySQL server and open Phpmyadmin page. Now create a database with name "githubdetails" and then create a table with name "data". Now create the columns id and username.
#### ->open cmd in the folder location and run the command "flask run".
#### ->open http://127.0.0.1:5000/ in our browser.

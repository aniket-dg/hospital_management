# hospital_management
Simple Hospital Management System for add, view, delete, search patient data

## Installation
```
git clone https://github.com/aniket-dg/hospital_management.git
```
Create a VirtualEnv for Python3 and Activate it

Go to the Project Folder
```
cd hospital_management
```
Install all required Libraries
```
pip install -r requirements.txt
```
## Database Configuration
  1. Create database 'hospital' using pgAdmin.

## Environment File
1. Create .env file in root folder (i.e. inside hospital_management/) using vscode terminal or using git bash.
1. Open .env file, Create following 3 variables. 
     <br> SECRET_KEY = 'create new secret key using online tool'<br>
      USER = 'your database user name'<br>
      PASSWORD = 'your database password'<br>
 2. Save file.
 
 Apply Migrations
```
python manage.py migrate
```
 Create Super User
 Remember your username and password.
```
python manage.py createsuperuser
```
Start the Project
```
python manage.py runserver
```
Go to the [localhost](http://127.0.0.1:8000/)

Add Some data for working properly
  1. Go to [localhost](http:127.0.0.1:8000/)
  2. Enter your credentials you created in the previous step
  3. Add some Patient data
  
## Your app is ready :)

# Backend-For-Twitter-Clone

This is a scaled down Twitter Clone built using django rest framework with postgres as the database

**You should generate your own secret key in order to access it**

To get your own key, RUN **python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'**

Store the printed key in your .env file

API Features:

 - User can **register** their accounts 
 - User can login and logout 
 - **Authenticated User** can see other people tweets,and can post their own tweet
 - Users can make **comments** on the tweets
 - Users can **like** tweets
 - Users can see other fellow registered Users on the platform
 - Users have separate **bookmark section** where they can add tweets as bookmark
 - Users can **follow** other accounts on the platform
 
 
 
 ## Packages 
 
 List of Packages used to build this API
 
  - **Corsheaders**
  - **dj-rest-auth**
  - **dj-allauth**
  - **drf-spectacular**
  - **drf-yasg**

## Usage

**If you want to try it on your local machine , Just update the Databases section on settings.py**

Creae a .env file in the root directory with the following details

- **SECRET_KEY**
- **DEBUG**
- **DB_NAME**
- **DB_USER**
- **DB_PASSWORD**
- **DB_HOST**

All DB details are based on your postgres instance

## Running container Instance

To run it as a docker container , Just update the Environment section in docker-compose.yml.Note that DB details in web and db service should be the same.
After updating (Passing the environment variables) , DO **sudo docker compose up**

After that , You can access the api running inside the container

## Documentation

**Go to /swagger/ Endpoint for Documwntation**



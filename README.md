# Playdate

Playdate is an application designed to simplify the process of arranging playdates for parents. As any parent knows, it can often take hours or even days to coordinate schedules and respond to text messages amidst the chaos of daily life. This app aims to alleviate the challenges associated with scheduling playdates, making it easier for parents to connect and organize opportunities for their children to socialize and play together.

![Am I Responsive](documentation/drf_api.png)

Link to API:
[Link to playdate drf-api](https://playdate-drf-api-a577c80fbeb8.herokuapp.com/)

Link to front-end site connected to the API:
[Link to Playdate](https://playdate-184e33ed70de.herokuapp.com/)
[Link to Playdate README.md](https://github.com/LindaAPersson/playdate/blob/main/README.md)

## Agile Workflow

Agile Methodology was used to help prioritize and organize tasks for the hole webpage. I used Project Boards on Github.

* User stories were created by looking at epics and added on as the project was advancing.
* Project Board was used to track progression of the task through the Todo, In progress and Done columns.

<details>
<summary> Userstories / Project board
</summary>

![issues.png](documentation/readme/issues.png)
![projectboard.png](documentation/readme/kanBan.png)
</details>

To see the Epic and user stroies in full: [Project Board](https://github.com/users/LindaAPersson/projects/8).

## User storie

### Admin user
The back-end section of the project focuses on its administrative side, so that's the only user story I will focus on:

As an admin, I want to be able to create, edit, and delete users, playdates, comments, and reviews so that I can have control over the content of the application and remove any potential inappropriate content. Additionally, I want to be able to read all the contact forms that users send.

## Database Design
The following models were created to represent the database model structure of the application:
![database diagram](documentation/readme/databsaDiagram.png)

### Models

#### User Model
The User model contains information about the user. It is part of the Django allauth library.
* ForeignKey relation with the Playdate model owner field
Fo* reignKey relation with the Comment model owner field
* ForeignKey relation with the Review model owner field

#### Playdate Model
The Playdate model contains the following fields: title, image, location, description, organizor, prize, created_at, parent_stay_required, time, suitable_age.
* ForeignKey relation with the Comment model post field
* ForeignKey relation with the Review model post field

#### Comment Model
The Comment model contains the following fields: user, playdate_post, created_on, content.
* ForeignKey relation between the user field and the User model id field.
* ForeignKey relation between the Playdate field and the User model playdate_post field.

#### Review Model
The Review model contains the following fields: user, playdate_post, created_on, comment, attendance, bring_this, age_recommendation.
* ForeignKey relation between the user field and the User model id field.
* ForeignKey relation between the Playdate field and the User model playdate_post field.

#### Contact Model
The Contact model contains the following fields: name, email, subject, message, created_on.

## Features

### Future features
In DEV:

<details>
<summary> Start page
</summary>

![Root](documentation/readme/features/root.png)
</details>

<details>
<summary> Playdate
</summary>

![playdate](documentation/readme/features/playdate.png)
</details>

<details>
<summary> Playdate Filter
</summary>

![playdate](documentation/readme/features/playdateFilter.png)
</details>

<details>
<summary> Playdate Detail
</summary>

![playdate](documentation/readme/features/playdateDetail.png)
</details>

<details>
<summary> Add, Edit, Delete Playdate (signed in)
</summary>

![Add playdate](documentation/readme/features/addPlaydate.png)
![Edit playdate](documentation/readme/features/editPlaydate.png)
![Delete playdate](documentation/readme/features/deletePlaydate.png)
</details>

<details>
<summary> Comment
</summary>

![comment](documentation/readme/features/comments.png)
</details>

<details>
<summary> Comment Filter
</summary>

![comment filter](documentation/readme/features/commmentsFilter.png)
</details>

<details>
<summary> Comment Detail
</summary>

![comment detail](documentation/readme/features/commentDetail.png)
</details>

<details>
<summary> Add, Edit, Delete Commment (signed in)
</summary>

![Add comment](documentation/readme/features/addComment.png)
![Edit Delete comment](documentation/readme/features/deletEditComment.png)
</details>

<details>
<summary> Review
</summary>

![Review](documentation/readme/features/review.png)
</details>

<details>
<summary> Review Filter
</summary>

![Review filter](documentation/readme/features/reviewFilter.png)
</details>

<details>
<summary> Review Detail
</summary>

![Review detail](documentation/readme/features/reviewDetail.png)
</details>

<details>
<summary> Add, Edit, Delete Review (signed in)
</summary>

![Add Review](documentation/readme/features/addReview.png)
![Edit Review](documentation/readme/features/editReviiew.png)
![Delete Review](documentation/readme/features/deleeteReview.png)
</details>

<details>
<summary> Contact
</summary>

![contact](documentation/readme/features/contact.png)
![contact form](documentation/readme/features/contactForm.png)
</details>

<details>
<summary> Contact Detail
</summary>

![contact detail](documentation/readme/features/contactDetail.png)
</details>

<details>
<summary> Edit, Delete Contact (signed in)
</summary>

![Edit contact](documentation/readme/features/editContact.png)
![Delete contact](documentation/readme/features/deleteContact.png)
</details>

Deployed version:

<details>
<summary> Start page
</summary>

![Root](documentation/readme/featuresDeployed/root.png)
</details>

<details>
<summary> Playdate
</summary>

![playdate](documentation/readme/featuresDeployed/playdate.png)
</details>


<details>
<summary> Playdate Detail
</summary>

![playdate detail](documentation/readme/featuresDeployed/playdateDetaiil.png)
</details>

<details>
<summary> Comment
</summary>

![comment](documentation/readme/featuresDeployed/comments.png)
</details>

<details>
<summary> Comment Detail
</summary>

![comment detail](documentation/readme/featuresDeployed/commentsDetail.png)
</details>

<details>
<summary> Review
</summary>

![Review](documentation/readme/featuresDeployed/reiew.png)
</details>

<details>
<summary> Review Detail
</summary>

![Review detail](documentation/readme/featuresDeployed/reviewDetail.png)
</details>

<details>
<summary> Contact
</summary>

![contact](documentation/readme/featuresDeployed/contact.png)
</details>

<details>
<summary> Contact Detail
</summary>

![contact detail](documentation/readme/featuresDeployed/contactDetail.png)
</details>

## Testing

To see all testing done, please see: [TESTING.md](TESTING.md)

## Technologies used

### Languages & Frameworks
* Python
* Django

### Libraries & Tools
* Cloudinary to store static files
* Dbdiagram.io used for the database schema diagram
* Git was used for version control via Gitpod terminal to push the code to GitHub
* GitHub was used as a remote repository to store project code
* Gitpod - a virtual IDE workspace used to build this site
* Django REST Framework was used to build the back-end API
* Django AllAuth was used for user authentication
* Pillow was used for image processing and validation
* Psycopg2 was used as a PostgreSQL database adapter for Python
* ElephantSQL – deployed project on Heruko uses a ElephantSQL database

## Deployment

### Set up JSON Web Tokens (steps 1-17)
1. Firstly, to install JSON Web Token authentication run terminal command pip install dj-rest-auth

2. Add 'rest_framework.authtoken' and 'dj_rest_auth' to the list of INSTALLED_APPS in settings.py as below:

```bash 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'location_field.apps.DefaultConfig',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'dj_rest_auth',
```
3. Add the dj-rest-auth urls paths to the main urls.py file as below:
```bash 
urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
```
4. Migrate the database with terminal command python manage.py migrate

5. For users to be able to register, install Django AllAuth with terminal command pip install 'dj-rest-auth[with_social]'

6. Add the following INSTALLED_APPS to settings.py:
```bash 
'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
```

7. Set SITE_ID in settings.py to 1
8. Add the registration urls below to the main urls.py file:
```bash 
path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
```
9. To install the JSON tokens, run terminal command pip install djangoframework-simplejwt
10. Set [DEV] to 1 in the env.py file:
```bash 
os.environ['DEV'] = '1'
```

11. This value can be used to check if project is in development or production. Add the following if/else statement to settings.py:
```bash 
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
```
12. To enable token authentication, set REST_USE_JWT to True. To ensure tokens are sent over HTTPS only, set JWT_AUTH_SECURE to True. Cookie names must also be declared. To do all of this, add the following code below the if/else statement just added to settings.py:
```bash 
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
```
13. Create serializers.py file in the drf_api directory, and copy UserDetailsSerializer code from Django documentation as follows:
```bash 
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """Serializer for Current User"""
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """Meta class to to specify fields"""
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
```
14. Overwrite the default user detail serializer in settings.py with the following:
```bash 
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
}
```
15. Migrate the database again with terminal command python manage.py migrate

16. Update requirements.txt file with new dependencies by running terminal command pip freeze > requirements.txt

17. Add, commit and push changes.

### Prepare API for deployment to Heroku (steps 18-24)

18. To add a custom message to the root_route, create a views.py file in the drf_api directory and add the following code:
```bash 
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to The Winding Path drf API!"
    })
```
19. Import to the main urls.py file, and add to the top of the urlpatterns list as follows:
```bash 
from .views import root_route

urlpatterns = [
    path('', root_route),
```
20. To set up page pagination, add the following to settings.py (inside REST_FRAMEWORK):
```bash 
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```
21. Set the default renderer to JSON for the production environment in settings.py:
```bash 
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```
22. To set up DATETIME_FORMAT, add the following to settings.py (inside REST_FRAMEWORK, under DEFAULT_PAGINATION_CLASS):
```bash 
'DATETIME_FORMAT': '%d %b %y',
```
23. For comments, set DATETIME format to show how long ago a comment was created. To do this, add the following code to any serializers.py files within comment apps:

```bash 
from django.contrib.humanize.templatetags.humanize import naturaltime

created_on = serializers.SerializerMethodField()

    def get_created_on(self, obj):
        """Method to display when comment was posted"""
        return naturaltime(obj.created_on)
```
24. Add, commit and push changes

### Deploy to Heroku (steps 25-50 )

25. Log into Heroku and create a new app.

26. Go to 'Resources' to search for Heroku Postgres in the Add-Ons section, and select the free plan.

27. Go to 'Settings' and click on 'Reveal Config Vars' to confirm DATABASE_URL is present.

28.  Go back to Git workspace and run terminal command pip install dj_database_url psycopg2 to install the relevant libraries needed to use a Heroku postgres database.

29. Import dj_database_url to settings.py
30. Go to DATABASES in settings.py and separate development and production environments:
```bash 
DATABASES = {
    'default': ({
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    ))
}
```
31. Install Gunicorn library by running terminal command pip install gunicorn

32. Add a Procfile to the top level of the directory and add the following code to the file:
```bash 
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drf_api.wsgi
```
33. Set ALLOWED_HOSTS in settings.py:
```bash 
ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),
    'localhost',
]
```
34. Install Cors Headers library by running terminal command pip install django-cors-headers

35. Add 'corsheaders' to INSTALLED_APPS list in settings.py (underneath 'dj_rest_auth.registration')

36. Add to the top of the MIDDLEWARE list in settings.py as follows:
```bash 
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
37. Set allowed origins for network requests in settings.py:
```bash 
if 'CLIENT_ORIGIN' in os.environ:
     CORS_ALLOWED_ORIGINS = [
         os.environ.get('CLIENT_ORIGIN'),
         os.environ.get('CLIENT_ORIGIN_DEV')
    ]

else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https://.*\.gitpod\.io$",
    ]

CORS_ALLOW_CREDENTIALS = True
```
38. Set JWT_AUTH_SAMESITE to 'None' in settings py as follows:
```bash
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
```
39. In env.py, set SECRET_KEY value to a random value:
```bash
os.environ['SECRET_KEY'] = 'random value here'
```
40. In settings.py, replace the default SECRET_KEY variable as follows:
```bash
SECRET_KEY = os.environ.get('SECRET_KEY')
```
41. In settings.py, set DEBUG as follows:
```bash
DEBUG = 'DEV' in os.environ
```
42. Copy the CLOUDINARY_URL and SECRET_KEY values from env.py and add them to Heroku config vars.

43. Add config var COLLECT_STATIC and set to 1.

44. Update requirements.txt file with new dependencies by running terminal command pip freeze > requirements.txt

45. Add, commit and push changes.

46. Go back to Heroku and click on 'Deploy'. Go to 'Deployment Method' and click on GitHub.

47. Connect to the DRF repository.

48. In 'Manual Deploy' select Main branch and click 'Deploy Branch'.

49. Monitor build log and deployment blog to ensure no error messages display. If build is successful, the app is now deployed.

50. Click on 'Open app' to access deployed app.

### dj-rest-auth bug fix (steps 51-54)
dj-test-auth currently has a bug that does not allow users to log out. To fix this, follow these steps:

51. In the drf_api views.py file, imort JWT_AUTH settings from settings.py:
```bash
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)
```
then, add the following log out view code:
```bash
@api_view(['POST'])
def logout_route(request):
    """dj-rest-auth-logout-view-fix"""
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
```
52. In the main urls.py file, import the logout_route:
```bash
from .views import root_route, logout_route
```
then, add to the urlpatterns list. The logout_route must be placed above the dafault dj-rest-urls, as follows:
```bash
path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
```
53. Add, commit and push changes.

54. Return to Heroku and manually deploy again.

### Adding extra required environment variables - required to use API with Frontend part of project (steps 55-62)
55. In settings.py, add heroku app url to ALLOWED_HOSTS:
```bash
ALLOWED_HOSTS = [
    '....herokuapp.com'
    'localhost',
]
```
56. Go to Heroku deployed app, and go to 'Settings' then 'Reveal config vars'.

57. Add the new ALLOWED_HOST key with the value of your deployed URL (as added to ALLOWED_HOSTS).

58. Go back to settings.py and replace the url string with the ALLOWED_HOST environment variable"
```bash
ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),
    'localhost',
]
```
59. In order to make application more secure by changing the workspace url regularly, import the regular expression module at the top of settings.py"
```bash
import re
```
60. Replace the if/else statement for CLIENT_ORIGIN with the following:
```bash
if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
61. Add, commit and push changes.

62. Return to Heroku and manually deploy branch for a final time.

## Credits
* The Code Institute DRF-API walkthrough was used as an invaluable guide on how to build a DRF-API.
* Code Institute Tutor Support for help with the filter sections. 
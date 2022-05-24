# Simchi_Resume_Django
 This is a project to create resume using Django frame work in python and show how to deploy it on Horaku

# How to deploy Django model on Heroku
    1) using this lines before going to the next part :
        https://github.com/akjasim/codeband-django-heroku

    2) Install this and then freeze into the repository:
        pip install whitenoise
        pip freeze > requirements.txt
    3) Go to the MIDDLEWARE (settings.py) and add this :
        'whitenoise.middleware.WhiteNoiseMiddleware'

    4) Also add these into the settings.py :
        import os
        STATIC_ROOT = os.path.join(BASE_DIR, 'statics')
        STATIC_URL = '/static/'

        # Extra places for collectstatic to find static files.
        STATICFILES_DIRS = (
            os.path.join(BASE_DIR, 'static'),
        )
    5) Also, do this :  
        heroku config:set DISABLE_COLLECTSTATIC=1
    6) Finally:
        git add .
        git commit -m "...."
        git push heroku main

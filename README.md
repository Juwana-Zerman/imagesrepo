# Images Repo

This project is an image repository app built with Python using the Django framework. The App will allow the user to add images to the site from their computer and delete those images.

Due to initial time constraints the following aspects will need to be added in the future:
* Continuous Integration and Delivery
* Unit and Function tests

To further enhance and build upon this app other features that could be added include:
- ADD and DELETE images in bulk
- SEARCH function to filter images
- SELL/BUY images
- Authenticate users

![Homepage Snippet](https://i.imgur.com/B56IYOx.png)

### To Run This App:
1. Ensure Python and Pip are installed: check version with ```python -V``` and ```pip -V```
2. Fork, Clone, or Download this repository
3. Change into the venv directory with ```cd venv```
4. Run ```pip install -r requirements.txt``` to install dependencies
5. Change into the django_app directory with ```cd django_app```
6. Next changes will need to be made to the ```settings.py```file in the next django_app directory. You can run the command ```python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'``` in the terminal to generate your own SECRET_KEY and input it into the ```settings.py``` file.
7. The last thing to do in the ```settings.py```file would be to add a user name and password under the database section of this file.
8. If you are still in the ```venv/django_app``` directory where the ```manage.py``` file resides you can run ```python manage.py runserver``` and the app should start.
9. You can add images from your local computer and watch them appear on the page. You can then delete them to try the functionality of the app.

## Dependencies
- Python
- Django
- Bootstrap
- HTML
- CSS
- MySQL
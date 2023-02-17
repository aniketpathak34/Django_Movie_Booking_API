
# Django_Movie_Booking_API
The Django movie_booking API is a RESTful API that enables users to book movie tickets online. It allows registered users to view a list of available movies, book a ticket, and pay for it online. The API also allows theater owners to register their theaters and halls, manage show timings, and update movie schedules.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Python Version: This Django application requires Python 3.6 or later versions to be installed on your system.

Steps to Run the Django Application:


1> Clone the repository or download the project files to your local machine. 2> Open a terminal window and navigate to the project directory. 3> Create a new virtual environment and activate it:

bash python3 -m venv env source env/bin/activate # For Linux or macOS env\Scripts\activate # For Windows

Install the required packages from the requirements.txt file:

bash pip install -r requirements.txt

Apply the database migrations:

bash python manage.py migrate

Create a superuser for accessing the Django admin panel: bash python manage.py createsuperuser

Start the development server: bash python manage.py runserver Open a web browser and go to http://127.0.0.1:8000 to access the Django application.

To access the admin panel, go to http://127.0.0.1:8000/admin and login with the superuser credentials.

That's it! You can now use the Django application and make changes to the code as per your requirements.


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

how to access CRUD operations in this project

To See the details of movies  : http://127.0.0.1:8000/movies/

To see the details of theaters   : http://127.0.0.1:8000/theaters/

To see the details of Halls : http://127.0.0.1:8000/halls/
      
To see the details of Shows   : http://127.0.0.1:8000/shows/
      
To see the details of Seats   : http://127.0.0.1:8000/seats/ 

To see the details of Bookings   : http://127.0.0.1:8000/bookings/ 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if you know then use or you can change the database to default settings

go to settings.py file and find database there

postgresql  database :


                              DATABASES = {

                      'default': {
                          'ENGINE': 'django.db.backends.postgresql',
                          'NAME': 'name of the database',
                          'USER': 'user name',
                          'PASSWORD': 'password',
                      }
                  }     
     
   
django default Database ::

                                    
                                    DATABASES = {
                                        'default': {
                                            'ENGINE': 'django.db.backends.sqlite3',
                                            'NAME': BASE_DIR / 'db.sqlite3',
                                        }
                                    }

makemigrations and you are good to go 



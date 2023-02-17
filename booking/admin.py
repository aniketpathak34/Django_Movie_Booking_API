from django.contrib import admin
from .models import Movie, Theater, MovieHall, Show, Seat, Booking


#admin fill will create a interface of that fields you mentioned in modules



admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(MovieHall)
admin.site.register(Show)
admin.site.register(Seat)
admin.site.register(Booking)

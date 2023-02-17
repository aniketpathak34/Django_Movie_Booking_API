from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('movies/', views.MovieList.as_view()),
    path('movies/<int:pk>/', views.MovieDetail.as_view()),
    path('theaters/', views.TheaterList.as_view()),
    path('theaters/<int:pk>/', views.TheaterDetail.as_view()),
    path('halls/', views.HallList.as_view()),
    path('halls/<int:pk>/', views.HallDetail.as_view()),
    path('shows/', views.ShowList.as_view()),
    path('shows/<int:pk>/', views.ShowDetail.as_view()),
    path('seats/', views.SeatList.as_view()),
    path('seats/<int:pk>/', views.SeatDetail.as_view()),
    path('bookings/', views.BookingView.as_view()),
    path('bookings/<int:pk>/', views.BookingView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


#all URLS are here to access the given CRUD operations

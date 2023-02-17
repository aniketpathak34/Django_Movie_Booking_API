from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Movie, Theater, MovieHall, Show, Seat
from .serializers import (
    MovieSerializer,
    TheaterSerializer,
    HallSerializer,
    ShowSerializer,
    SeatSerializer
)


#this all class is CRUD operations of API


class MovieList(generics.ListCreateAPIView): #it will Return List of Movies
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):  #it can help to get the movie details with the id 
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class TheaterList(generics.ListCreateAPIView): #it will return list of theaters
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

class TheaterDetail(generics.RetrieveUpdateDestroyAPIView): #it can help to get the theater details with the id
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

class HallList(generics.ListCreateAPIView): #it will return hall of the theater
    queryset = MovieHall.objects.all()
    serializer_class = HallSerializer

class HallDetail(generics.RetrieveUpdateDestroyAPIView): #it will return hall screen based on id
    queryset = MovieHall.objects.all()
    serializer_class = HallSerializer

class ShowList(generics.ListCreateAPIView): #it can handle how many show will happen next the list of that show
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class ShowDetail(generics.RetrieveUpdateDestroyAPIView): # we can access specific details of show
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class SeatList(generics.ListCreateAPIView): #it can retur haw many seats are booked 
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class SeatDetail(generics.RetrieveUpdateDestroyAPIView):  # it can show that the id no is booked or not
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingView(generics.CreateAPIView): # it can help to book a ticket
    serializer_class = SeatSerializer

    def create(self, request, *args, **kwargs):
        seats = request.data.get('seats', [])
        show_id = request.data.get('show', None)

        if not show_id:
            return Response({'error': 'Show ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            show = Show.objects.get(id=show_id)
        except Show.DoesNotExist:
            return Response({'error': 'Invalid Show ID.'}, status=status.HTTP_400_BAD_REQUEST)

        # check if seats are available
        available_seats = show.get_available_seats()
        for seat in seats:
            if seat not in available_seats:
                return Response({'error': f'Seat {seat} is not available.'}, status=status.HTTP_400_BAD_REQUEST)

        # reserve seats
        reserved_seats = []
        for seat in seats:
            try:
                reserved_seat = Seat.objects.get(show=show, number=seat)
                reserved_seat.is_reserved = True
                reserved_seat.save()
                reserved_seats.append(reserved_seat)
            except Seat.DoesNotExist:
                return Response({'error': f'Invalid seat number {seat}.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SeatSerializer(reserved_seats, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

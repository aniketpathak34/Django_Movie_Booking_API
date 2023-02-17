from django.db import models

# Create your models here.



class Theater(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='posters/')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class MovieHall(models.Model):
    name = models.CharField(max_length=255)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    rows = models.IntegerField()
    columns = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.theater.name})"


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_hall = models.ForeignKey(MovieHall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.name} ({self.movie_hall.name})"





class Seat(models.Model):
    ROW_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
    ]
    column = models.PositiveSmallIntegerField()
    row = models.CharField(max_length=1, choices=ROW_CHOICES)
    movie_hall = models.ForeignKey(MovieHall, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('row', 'column', 'movie_hall')

    def __str__(self):
        return f"{self.row}{self.column} ({self.movie_hall.name})"


class Booking(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)

    def __str__(self):
        return f"{self.user_name} - {self.show}"


class Price(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='booking0.Price.movie+')
    movie_hall = models.ForeignKey(MovieHall, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('movie', 'movie_hall')

    def __str__(self):
        return f"{self.movie.name} ({self.movie_hall.name}): {self.price}"




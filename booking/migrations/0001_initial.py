# Generated by Django 3.2.10 on 2023-02-17 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('poster', models.ImageField(upload_to='posters/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='MovieHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('rows', models.IntegerField()),
                ('columns', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.movie')),
                ('movie_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.moviehall')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.PositiveSmallIntegerField()),
                ('row', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=1)),
                ('movie_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.moviehall')),
            ],
            options={
                'unique_together': {('row', 'column', 'movie_hall')},
            },
        ),
        migrations.AddField(
            model_name='moviehall',
            name='theater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.theater'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('user_email', models.EmailField(max_length=254)),
                ('seats', models.ManyToManyField(to='booking.Seat')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.show')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking0.Price.movie+', to='booking.movie')),
                ('movie_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.moviehall')),
            ],
            options={
                'unique_together': {('movie', 'movie_hall')},
            },
        ),
    ]

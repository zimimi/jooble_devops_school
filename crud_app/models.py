from django.db import models

class Film(models.Model):  
    name = models.CharField(max_length=100)
    kinopoisk_rating = models.FloatField()
    IMDb_rating = models.FloatField()
    RT_rating = models.IntegerField()
    year = models.IntegerField()
    duration = models.CharField(max_length=100)

    class Meta:
        db_table = "film_library"

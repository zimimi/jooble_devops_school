from django.db import models

class Film(models.Model):  
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=20)

    class Meta:
        db_table = "film_library"

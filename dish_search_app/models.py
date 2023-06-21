from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    items_available = models.JSONField()
    full_details = models.JSONField(default={})
    latitude_longitude = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @classmethod
    def search_dish(cls, query):
        return cls.objects.filter(items_available__icontains=query)



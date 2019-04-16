from django.db import models

class Search(models.Model):
    source = models.CharField(max_length=300)
    query = models.CharField(max_length=120)
    deep = models.IntegerField(default=0)

    def __str__(self):
        return self.query + " was searched on " + self.source
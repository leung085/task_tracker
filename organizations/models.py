from django.db import models
from django.utils import timezone

class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse('org_details', args=[str(self.id)])

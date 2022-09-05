import uuid

from django.db import models


class Technology(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    logo = models.FileField(null=False, upload_to="logos/technologies/")

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/projects/")
    technologies = models.ManyToManyField(Technology)
    link = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

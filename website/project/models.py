import uuid

from django.db import models


class Technology(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    tech_name = models.CharField(max_length=50, blank=False, null=False)
    tech_logo = models.FileField(null=False, upload_to="logos/technologies/")

    def __str__(self):
        return self.tech_name


class Project(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    project_name = models.CharField(max_length=50, blank=False, null=False)
    project_description = models.TextField()
    project_image = models.ImageField(null=True, upload_to="images/projects/")
    project_technologies = models.ManyToManyField(Technology)
    project_link = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.project_name

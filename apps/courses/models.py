from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['course']) < 5:
            errors['course'] = "The course name must be at least 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "The description must be at least 15 characters"
        
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Object Course, name: {}".format(self.name)

class Description(models.Model):
    description = models.TextField()
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
from django.db import models

from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    due_date = models.DateField()

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

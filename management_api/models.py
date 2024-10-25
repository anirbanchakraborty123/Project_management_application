from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .user_manager import CustomUserManager

# Customuser model
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

# Project model
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, related_name="owned_projects", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# Project Member model
class ProjectMember(models.Model):
    ADMIN = 'Admin'
    MEMBER = 'Member'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MEMBER, 'Member')
    ]

    project = models.ForeignKey(Project, related_name="members", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name="projects", on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

# Task model
class Task(models.Model):
    TODO = 'To Do'
    IN_PROGRESS = 'In Progress'
    DONE = 'Done'

    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done')
    ]

    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TODO)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default=LOW)
    assigned_to = models.ForeignKey(CustomUser, related_name="tasks", on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

# Comment model
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(CustomUser, related_name="comments", on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

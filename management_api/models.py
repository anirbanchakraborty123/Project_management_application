from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .user_manager import CustomUserManager

class CustomUser(AbstractBaseUser,PermissionsMixin):
    """
    Custom user model for managing application users.
    
    Attributes:
        username (str): Unique username for the user.
        email (str): Unique email for the user.
        password (str): Hashed password for authentication.
        first_name (str): User's first name.
        last_name (str): User's last name.
        date_joined (datetime): Timestamp of when the user joined.
    """
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

class Project(models.Model):
    """
    Project model representing a project with details and ownership.
    
    Attributes:
        name (str): Name of the project.
        description (str): Detailed description of the project.
        owner (User): The user who created/owns the project.
        created_at (datetime): Timestamp of when the project was created.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, related_name="owned_projects", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectMember(models.Model):
    """
    ProjectMember model to define user roles in projects.
    
    Attributes:
        project (Project): Associated project.
        user (User): User associated with the project.
        role (str): Role of the user in the project (Admin, Member).
    """
    ADMIN = 'Admin'
    MEMBER = 'Member'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MEMBER, 'Member')
    ]

    project = models.ForeignKey(Project, related_name="members", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name="projects", on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class Task(models.Model):
    """
    Task model representing tasks under a specific project.
    
    Attributes:
        title (str): Title of the task.
        description (str): Description of the task.
        status (str): Current status of the task (To Do, In Progress, Done).
        priority (str): Priority level (Low, Medium, High).
        assigned_to (User): User to whom the task is assigned.
        project (Project): Project under which the task falls.
        created_at (datetime): Creation timestamp of the task.
        due_date (datetime): Due date for task completion.
    """
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

class Comment(models.Model):
    """
    Comment model for storing comments on tasks.
    
    Attributes:
        content (str): Content of the comment.
        user (User): User who made the comment.
        task (Task): Task on which the comment is made.
        created_at (datetime): Creation timestamp of the comment.
    """
    content = models.TextField()
    user = models.ForeignKey(CustomUser, related_name="comments", on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

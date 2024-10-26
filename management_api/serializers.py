from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser, Project, Task, Comment

class UserSerializer(serializers.ModelSerializer):
    """Serializer for Custom User model."""
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']

class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project model."""
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at']

class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model."""
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date']

class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'task', 'created_at']

class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for serializing register data at Custom User model."""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        """ Returns user data after validationg """
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    """ Serializer to handle login for Custom User model """
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        """ Returns user data after validating else throws validation error"""
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
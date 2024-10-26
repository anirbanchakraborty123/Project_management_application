from rest_framework import viewsets, permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import CustomUser, Project, Task, Comment
from .serializers import (
    UserSerializer,
    ProjectSerializer,
    TaskSerializer,
    CommentSerializer,
    RegisterSerializer,
    LoginSerializer,
)

class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for managing User model operations."""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RegisterView(generics.CreateAPIView):
    """ Generics view to handle custom user registration """
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(APIView):
    """ APIView to handle login operation """
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        operation_description="Login with email and password",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            },
            required=['email', 'password']
        ),
        responses={
            200: openapi.Response(
                description="Successful login",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='JWT Refresh Token'),
                        'access': openapi.Schema(type=openapi.TYPE_STRING, description='JWT Access Token'),
                    }
                )
            ),
            400: openapi.Response(description="Invalid credentials"),
        }
    )
    def post(self, request):
        """ Returns JWT tokens if login is successfull"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        return Response(
            {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Generic view for managing Custom User (RUD) operations."""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
    permission_classes = [permissions.IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Project model operations."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Task model operations."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Comment model operations."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, TaskViewSet, CommentViewSet

router = DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

# urlpatterns = router.urls

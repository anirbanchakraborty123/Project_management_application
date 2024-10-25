from django.contrib import admin
from .models import Project,ProjectMember,CustomUser,Task,Comment
# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(CustomUser)
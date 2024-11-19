from django.contrib import admin
from .models import Ticket, UserStory, Company, CustomUser, Project


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('title', 'description')

@admin.register(UserStory)
class UserStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'nit', 'email')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'company')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'description')






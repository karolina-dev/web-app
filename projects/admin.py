from django.contrib import admin
from projects.models import Company, Project, UserStory, Ticket

admin.site.register(Company)
admin.site.register(Project)
admin.site.register(UserStory)
admin.site.register(Ticket)


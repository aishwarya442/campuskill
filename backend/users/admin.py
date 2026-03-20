from django.contrib import admin
from .models import User, AdminProfile, CompanyProfile, StudentProfile

# Since User extends AbstractUser, we can just register it.
admin.site.register(User)
admin.site.register(AdminProfile)
admin.site.register(CompanyProfile)
admin.site.register(StudentProfile)

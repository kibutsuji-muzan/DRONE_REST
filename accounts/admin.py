from django.contrib import admin
from django.contrib import admin
from accounts.models.userModel import User#, LoggedInUser
from accounts.models.profileModel import UserProfile, ProfileImage, ProfileType, ProfileUpdateRequest
from accounts.models.userOtp import VerificationDevice
from django.contrib.sessions.models import Session

class UpdateRequestInline(admin.StackedInline):
    model = ProfileUpdateRequest

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class VerificationDeviceInline(admin.StackedInline):
    model = VerificationDevice

class ProfileImageInline(admin.StackedInline):
    model = ProfileImage

@admin.register(User)
class Admin(admin.ModelAdmin):
    inlines = [UserProfileInline, VerificationDeviceInline]
    list_display = ('__str__',)

@admin.register(UserProfile)
class Admin(admin.ModelAdmin):
    inlines = [ProfileImageInline, UpdateRequestInline]

admin.site.register(Session)
admin.site.register(ProfileType)
admin.site.register(VerificationDevice)
from django.contrib import admin
from django.contrib import admin

from accounts.models.userModel import User, PassResetToken, UserType, UserUpdateRequest
from accounts.models.profileModel import UserProfile, ProfileImage
from accounts.models.userOtp import VerificationDevice
from django.contrib.sessions.models import Session


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
    inlines = [ProfileImageInline]

@admin.register(PassResetToken)
class PassRestTokenAdmin(admin.ModelAdmin):
    list_display = ('user',)

# @admin.register(VerificationDevice)
# class AdminVerDevice(admin.ModelAdmin):
#     list_display = ('unverified_phone',)

@admin.register(UserUpdateRequest)
class UpdateRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(Session)
admin.site.register(UserType)

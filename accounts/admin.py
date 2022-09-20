from django.contrib import admin
from django.contrib import admin

from accounts.models.userModel import User, PassResetToken, OrganizationType, UpdateRequest, UserUpdateFiles
from accounts.models.profileModel import UserProfile, ProfileImage
from accounts.models.userOtp import VerificationDevice


from django.contrib.sessions.models import Session


class UserProfileInline(admin.StackedInline):
    model = UserProfile

class VerificationDeviceInline(admin.StackedInline):
    model = VerificationDevice

class ProfileImageInline(admin.StackedInline):
    model = ProfileImage

class UpdateRequestInline(admin.StackedInline):
    model = UpdateRequest
    extra = 3

class UpdateFileInline(admin.TabularInline):
    model = UserUpdateFiles

@admin.register(User)
class Admin(admin.ModelAdmin):
    inlines = [UserProfileInline, VerificationDeviceInline, UpdateRequestInline]
    list_display = ('__str__',)

@admin.register(UserProfile)
class Admin(admin.ModelAdmin):
    inlines = [ProfileImageInline]

@admin.register(PassResetToken)
class PassRestTokenAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(UpdateRequest)
class AdminVerDevice(admin.ModelAdmin):
    inlines = [UpdateFileInline]

admin.site.register(Session)
admin.site.register(OrganizationType)

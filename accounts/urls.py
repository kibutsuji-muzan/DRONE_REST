from rest_framework.routers import DefaultRouter
from accounts.views.sign_up_in import SignUpInView
from accounts.views.profile import Profile

router = DefaultRouter()
router.register(r'sign', SignUpInView, basename='signup')
router.register(r'profile', Profile, basename='profile')

urlpatterns = router.urls
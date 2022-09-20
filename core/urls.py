from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


from accounts.views.accounts import AccountsManagement
from accounts.views.profile import Profile
from accounts.views.portfolio import PortfolioView


from droneshop.views.shop import Index, Others
from droneservice.views.homeService import ServiceIndex, ServiceOthers
from extras.views import HelpDesk


from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'drone-shop', Index, basename='drone_shop')
router.register(r'orders', Others, basename='drone_shop_orders')

router.register(r'drone-service', ServiceIndex, basename='drone_service')
router.register(r'orders-service', ServiceOthers, basename='drone_service_orders')

router.register(r'help-desk', HelpDesk, basename='help_desk')

router.register(r'accounts', AccountsManagement, basename='accounts')
router.register(r'profile', Profile, basename='profile')
router.register(r'portfolio', PortfolioView, basename='portfolio')

schemaview = get_schema_view(
    title="Drone E-Shop",
    description="Api for e-commerce next app",
    version="1.0.0",
    urlconf="core.urls",
)

urlpatterns = [
    re_path(r'api/auth/', include('knox.urls')),

    path('admin/', admin.site.urls,),
    path('schema/', schemaview),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
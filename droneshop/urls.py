from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from droneshop.views.shopHome import Index, SellersPage

router = DefaultRouter()
router.register(r'', Index, basename='home')

urlpatterns=[
    path('user-related/<slug:slug>/', SellersPage.as_view()),
]

urlpatterns += router.urls
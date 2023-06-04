from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import BankViewSet, BranchViewSet

router = routers.DefaultRouter()
router.register('banks', BankViewSet, basename="banks")
router.register('branches', BranchViewSet, basename="branches")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

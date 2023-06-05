from django import urls
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.views import *



router = routers.DefaultRouter()
router.register('banks', BankViewSet, basename="banks")
router.register('branches', BranchViewSet, basename="branches")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('import', import_data, name='import_data'),

]

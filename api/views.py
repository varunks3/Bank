from rest_framework import viewsets
from .models import Banks, Branches
from .serializers import BankSerializer, BranchSerializer
from django.http import HttpResponse


class BankViewSet(viewsets.ModelViewSet):
    queryset = Banks.objects.all()
    serializer_class = BankSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer



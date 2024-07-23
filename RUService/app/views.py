from rest_framework import generics
from .models import Home, Apartment, UtilityBill
from .serializers import HomeSerializer, ApartmentSerializer, HomeDetailSerializer
from .tasks import calculate_utility_bills
from django.views.generic import View
from django.http import JsonResponse


class HomeListCreate(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class ApartmentListCreate(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class ApartmentListByHome(generics.ListAPIView):
    serializer_class = ApartmentSerializer

    def get_queryset(self):
        home_id = self.kwargs['home_id']
        return Apartment.objects.filter(home__id=home_id)


class CalculateUtilityBillsView(View):
    def post(self, request):
        calculate_utility_bills.delay()
        return JsonResponse({'message': 'Задача по подсчету счетов запущена в фоне.'})


class UtilityBillsResultView(View):
    def get(self, request):
        utility_bills = UtilityBill.objects.all()
        data = [{'id': bill.id, 'amount': bill.amount} for bill in utility_bills]
        return JsonResponse({'utility_bills': data})

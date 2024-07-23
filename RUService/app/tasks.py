from celery import shared_task
from .models import Apartment, WaterMeter, Tariff, Billing
from datetime import datetime, timedelta


@shared_task
def calculate_utility_bills(month, water_tariff, area_tariff):
    for apartment in Apartment.objects.all():
        previous_reading = WaterMeter.objects.filter(apartment=apartment, month__lt=month).latest('month').readings
        current_reading = WaterMeter.objects.filter(apartment=apartment, month=month).latest('month').readings

        water_consumption = current_reading - previous_reading
        water_billing = water_tariff * water_consumption

        area = apartment.area
        area_billing = area_tariff * area

        Billing.objects.create(month=month, apartment=apartment, water_billing=water_billing, area_billing=area_billing)

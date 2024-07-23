from django.contrib import admin
from django.urls import path
from app.views import HomeListCreate, ApartmentListCreate, ApartmentListByHome, CalculateUtilityBillsView, UtilityBillsResultView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homes/', HomeListCreate.as_view(), name='home-list-create'),
    path('apartments/', ApartmentListCreate.as_view(), name='apartment-list-create'),
    path('homes/<int:home_id>/', ApartmentListByHome.as_view(), name='apartment-list-by-home'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('calculate-utility-bills/', CalculateUtilityBillsView.as_view(), name='calculate_utility_bills'),
    path('utility-bills-result/', UtilityBillsResultView.as_view(), name='utility_bills_result'),
]

from django.urls import path
from .views import CarView, car_detail
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', CarView.as_view(), name='car'),
    path('car_detail/<int:id>',car_detail),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
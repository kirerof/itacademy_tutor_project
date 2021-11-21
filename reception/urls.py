from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'reception'
urlpatterns = [
    path('', views.all_tutors, name='all_tutor'),
    path('<slug:slug>', views.create_reception, name='create_reception'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

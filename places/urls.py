from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.fetch_places_data, name='index'),
    path('places/<int:id>/', views.place_detail, name='place_detail'),
    path('tinymce/', include('tinymce.urls')),

]

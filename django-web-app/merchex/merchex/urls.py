from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', views.hello),
    path('about-us/', views.about),

    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('contact-us/', views.contact, name='contact'),
    path('bands/add/', views.band_create, name='band-create'),
]

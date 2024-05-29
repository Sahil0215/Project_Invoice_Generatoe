
# from django.contrib import admin
# from django.urls import path
# from app import views
# urlpatterns = [
#     path('', views.home,name="home"),
#     path('admin/', admin.site.urls),
#     path('pagea/',views.page_a, name="page_a"),
#     path('create_bill/', views.page_a, name='create_bill'),
# ]

# app/urls.py
from django.urls import path
from django.contrib import admin
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('generate/', views.generate, name='generate'),
    path('bill/', views.bill, name='bill'),
     path('404/', views.error_404, name='error_404'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('manager/<int:manager_id>/', views.get_manager, name='get_manager'),
    path('driver/<int:driver_id>/', views.get_driver, name='get_driver'),
    path('manager/<int:manager_id>/update/', views.update_manager, name='update_manager'),
    path('driver/<int:driver_id>/update/', views.update_driver, name='update_driver'),
    path('driver/register/', views.register_driver, name='register_driver'),
    # path('driver/login/', views.login, name='login'),
    # path('manager/login/', views.login, name='login'),
    path('manager/register/', views.register_manager, name='login'),
]
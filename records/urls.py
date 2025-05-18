from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),

    path('dashboard/', views.dashboard, name='dashboard'),  # ✅ Додано!

    path('animal/create/', views.create_animal, name='create_animal'),
    path('animal/<int:id>/edit/', views.update_animal, name='update_animal'),
    path('animal/<int:id>/delete/', views.delete_animal, name='delete_animal'),

    path('doctor/create/', views.create_doctor, name='create_doctor'),
    path('doctors/', views.list_doctors, name='list_doctors'),

    path('visit/create/', views.create_visit, name='create_visit'),
    path('visits/', views.list_visits, name='list_visits'),

    path('animal/<int:animal_id>/pdf/', views.generate_pdf, name='generate_pdf'),
]

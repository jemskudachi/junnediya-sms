from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('bonafide/<int:student_id>/', views.bonafide_view, name='bonafide'),
    path('hall_ticket/<int:student_id>/', views.hall_ticket_view, name='hall_ticket'),
    path('result/<int:student_id>/', views.result_view, name='result'),
    path('create-admin/', views.create_admin_user),
]

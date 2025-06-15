from django.urls import path
from . import views

urlpatterns = [
    path('bonafide/<int:student_id>/', views.bonafide_view, name='bonafide'),
    path('hall_ticket/<int:student_id>/', views.hall_ticket_view, name='hall_ticket'),
    path('result/<int:student_id>/', views.result_view, name='result'),
    path('create-admin/', views.create_admin_user),  # Temporary route to create admin
]

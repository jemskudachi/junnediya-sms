from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Student

def bonafide_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'school/bonafide.html', {'student': student})

def hall_ticket_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'school/hall_ticket.html', {'student': student})

def result_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'school/result.html', {'student': student})

def create_admin_user(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        return HttpResponse("✅ Superuser created successfully.")
    else:
        return HttpResponse("ℹ️ Admin user already exists.")

def home_view(request):
    return HttpResponse("""
        <h1>Welcome to Junnediya School Management System</h1>
        <p><a href='/admin/'>Go to Admin Panel</a></p>
        <p>Use <code>/bonafide/&lt;student_id&gt;/</code> for bonafide certificate.</p>
        <p>Use <code>/hall_ticket/&lt;student_id&gt;/</code> for hall ticket.</p>
        <p>Use <code>/result/&lt;student_id&gt;/</code> for result.</p>
    """)

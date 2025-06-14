
from django.shortcuts import render, get_object_or_404
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


from django.db import models

class Student(models.Model):
    SCHOOL_CHOICES = [
        ("JEMS", "Junnediya English Medium School Kudachi"),
        ("JEMHS", "Junnediya English Medium High School Kudachi"),
        ("JUMHPS", "Junnediya Urdu Medium Higher Primary School Kudachi"),
        ("JEMPPS", "Junnediya English Medium Pri-Primary School Kudachi"),
    ]

    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    class_name = models.CharField(max_length=50)
    dob = models.DateField()
    school = models.CharField(max_length=20, choices=SCHOOL_CHOICES)
    father_name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.roll_number} - {self.name}"

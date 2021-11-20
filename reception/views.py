from django.shortcuts import render
from . import models


def all_tutors(request):
    tutors = models.Tutor.objects.all()

    return render(request, 'tutor/all_tutors.html',
                  {'tutors': tutors})



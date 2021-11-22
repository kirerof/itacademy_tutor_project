from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from . import forms
from . import models
from django.http import HttpResponse


def all_tutors(request):
    tutors = models.Tutor.objects.all()

    return render(request, 'tutor/all_tutors.html',
                  {'tutors': tutors})


@login_required
def create_reception(request, slug):
    tutor1 = get_object_or_404(models.Tutor, slug=slug)
    if request.method == 'POST':
        reception_form = forms.ReceptionForm(request.POST)
        if reception_form.is_valid():
            cd = reception_form.cleaned_data
            new_reception = reception_form.save(commit=False)
            new_reception.date = cd['reception_date_time']
            new_reception.tutor = tutor1
            # условие для предотвращения записи на одно и то же время к одному репетитору
            if models.Reception.objects.filter(reception_date_time=cd['reception_date_time'],
                                               tutor=new_reception.tutor).count() == 0:
                models.Reception.objects.create(reception_date_time=new_reception.date,
                                                tutor=new_reception.tutor)

                return render(request, 'reception/reception_done.html')

            else:
                return HttpResponse('это время уже занято, вернись назад и выбери другое')
                
    else:
        reception_form = forms.ReceptionForm()

    return render(request, 'reception/tutor_reception.html',
                  {'tutor': tutor1,
                   'reception_form': reception_form})


@login_required
def create_feedback(request, slug):
    tutor = get_object_or_404(models.Tutor, slug=slug)

    if request.method == "POST":
        feedback_form = forms.CreateFeedbackForm(request.POST)
        if feedback_form.is_valid():
            new_feedback = feedback_form.save(commit=False)
            new_feedback.tutor = tutor
            new_feedback.save()

            return redirect('reception:see_feedback', slug)
    else:
        feedback_form = forms.CreateFeedbackForm()

    return render(request, 'tutor/create_feedback.html',
                  {'feedback_form': feedback_form,
                   'tutor': tutor})


def see_feedback(request, slug):
    tutor = get_object_or_404(models.Tutor, slug=slug)
    tutor_feedback = models.Feedback.objects.filter(tutor=tutor.id)

    return render(request, 'tutor/see_feedback.html',
                  {'tutor_feedback': tutor_feedback, 'tutor': tutor})


def registration(request):
    if request.method == 'POST':
        registration_form = forms.UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            cd = registration_form.cleaned_data
            new_user = registration_form.save(commit=False)
            new_user.set_password(cd['password1'])
            new_user.save()

            return redirect('reception:all_tutor')
    else:
        registration_form = forms.UserRegistrationForm()

    return render(request, 'registration/registration.html',
                  {'registration_form': registration_form})

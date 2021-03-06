from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from . import forms
from . import models
import datetime


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
            new_reception.user = request.user
            # условие для предотвращения записи на одно и то же время к одному репетитору
            if models.Reception.objects.filter(reception_date_time=cd['reception_date_time'],
                                               tutor=new_reception.tutor).count() == 0:
                models.Reception.objects.create(reception_date_time=new_reception.date,
                                                tutor=new_reception.tutor,
                                                user=new_reception.user)

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
            models.Profile.objects.create(user=new_user,
                                          email=cd['email'])

            return redirect('reception:login')
    else:
        registration_form = forms.UserRegistrationForm()

    return render(request, 'registration/registration.html',
                  {'registration_form': registration_form})


def user_profile(request):
    return render(request, "profile.html", {'user': request.user})


def edit_user_profile(request):
    if request.method == "POST":
        user_form = forms.UserEditForm(request.POST, instance=request.user)
        profile_form = forms.ProfileEditForm(request.POST,
                                             instance=request.user.profile)
        if all((user_form.is_valid(), profile_form.is_valid())):
            user_form.save()
            profile_form.save()

            return render(request, "profile.html", {'user': request.user})
    else:
        user_form = forms.UserEditForm(instance=request.user)
        profile_form = forms.ProfileEditForm(request.POST,
                                             instance=request.user.profile)

    return render(request, "edit_user_profile.html", {'user_form': user_form,
                                                      'profile_form': profile_form})


def my_receptions(request):
    receptions_set = models.Reception.objects.filter(user=request.user).order_by('reception_date_time')
    receptions = []
    delta = datetime.timedelta(hours=3)
    for reception in receptions_set:
        if reception.reception_date_time > datetime.datetime.now(datetime.timezone.utc) + delta:
            receptions.append(reception)
        else:
            reception.delete()

    return render(request, "reception/my_receptions.html", {'receptions': receptions})

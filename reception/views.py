from django.shortcuts import get_object_or_404
from django.shortcuts import render
from . import forms
from . import models
from django.http import HttpResponse


def all_tutors(request):
    tutors = models.Tutor.objects.all()

    return render(request, 'tutor/all_tutors.html',
                  {'tutors': tutors})


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

from django import forms
from . import models


class ReceptionForm(forms.ModelForm):
    class Meta:
        model = models.Reception
        fields = ('reception_date_time',)


class CreateFeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = ('feedback_text', )

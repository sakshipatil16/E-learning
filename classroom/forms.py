from django import forms
from .models import Studentsolution,Studentsolution_ass


class AssignmentForm(forms.ModelForm):
    class Meta:
        model=Studentsolution
        fields=('pdf',)


class AssignmentsolutionForm(forms.ModelForm):
    class Meta:
        model=Studentsolution_ass
        fields=('pdf',)



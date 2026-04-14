from django import forms
from ..models import School

class StudentForm(forms.Form):
    school = forms.ModelChoiceField(queryset=School.objects.all(), required=False)
    name = forms.CharField(label='Enter Name', max_length=50)
    age = forms.IntegerField(label="Enter Age")
    is_active = forms.BooleanField(label="Is Active?", required=False)

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 5:
            raise forms.ValidationError("Age must be greater than 5")
        return age
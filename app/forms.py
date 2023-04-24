from django import forms

def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('a character is not started in first')


def check_for_len(value):
    if len(value)<2:
        raise forms.ValidationError('len is less')


class StudentForm(forms.Form):
    Name=forms.CharField(max_length=100,validators=[check_for_a])
    Age=forms.IntegerField()
    url=forms.URLField(validators=[check_for_len])
    
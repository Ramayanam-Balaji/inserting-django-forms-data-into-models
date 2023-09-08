from django import forms
class StudentForm(forms.Form):
    sname=forms.CharField()
    sid=forms.IntegerField()
    semail=forms.EmailField()
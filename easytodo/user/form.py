from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Dashboard


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class DashboardForm(forms.Form):
    task = forms.CharField(label="   ",max_length=128)

    @staticmethod
    def save_task(task, user):
        t = Dashboard(tasks=task, user=user)
        t.save()

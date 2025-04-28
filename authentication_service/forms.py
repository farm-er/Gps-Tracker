from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from . import models



class ManagerRegistrationForm(forms.ModelForm):
    
    
    first_name = forms.CharField( label="First Name", max_length=50)
    last_name = forms.CharField( label="Last Name", max_length=50)
    email = forms.EmailField( label="Email")
    password = forms.CharField( label="Password", widget=forms.PasswordInput())
    verify_password = forms.CharField( label="Verify Password", widget=forms.PasswordInput())
    profile_picture = forms.ImageField( allow_empty_file=True, required=False)


    class Meta:
        model = models.Manager
        fields = ['first_name', 'last_name', 'email', 'password', 'verify_password', 'profile_picture']

    def clean_verify_password(self):
        verify_password = self.cleaned_data.get("verify_password")
        if self.cleaned_data.get("password") != verify_password:
            raise forms.ValidationError("Not the same password")
        return verify_password






class DriverRegistrationForm(forms.ModelForm):
    
    
    first_name = forms.CharField( label="First Name", max_length=50)
    last_name = forms.CharField( label="Last Name", max_length=50)
    email = forms.EmailField( label="Email")
    password = forms.CharField( label="Password", widget=forms.PasswordInput())
    verify_password = forms.CharField( label="Verify Password", widget=forms.PasswordInput())
    profile_picture = forms.ImageField( allow_empty_file=True, required=False)
    manager_email = forms.EmailField(label="Manager's Email")

    class Meta:
        model = models.Driver
        fields = ['first_name', 'last_name', 'email', 'password', 'verify_password', 'manager_email', 'profile_picture']
    
    def clean_manager_email(self):
        email = self.cleaned_data.get('manager_email')
        try:
            manager = models.Manager.objects.get(email=email)
        except models.Manager.DoesNotExist:
            raise forms.ValidationError("No manager with this email was found.")
        self.cleaned_data['manager'] = manager 
        return email
    
    def clean_verify_password(self):
        verify_password = self.cleaned_data.get("verify_password")
        if self.cleaned_data.get("password") != verify_password:
            raise forms.ValidationError("Not the same password")
        return verify_password


    def save(self, commit=True):
        driver = super().save(commit=False)
        driver.manager = self.cleaned_data['manager']
        if commit:
            driver.save()
        return driver

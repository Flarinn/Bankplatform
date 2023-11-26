from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import FileInput, ModelForm, NumberInput, TextInput, Textarea, PasswordInput, FileField, DateInput,DateField, HiddenInput

from .models import *


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['Sum', 'PrincipalCompany', 'BeneficiarCompany', 'Link', 'Months', 'Description']
        widgets = {
            'Sum': NumberInput(attrs={

                'class': 'form-control',
                'placeholder': 'Сумма БГ'
            }),
            "PrincipalCompany": TextInput(attrs={
                'id': 'party',
                'class': 'form-control',
                'placeholder': 'Компания принципала'
            }),
            "BeneficiarCompany": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Компания Бенефициара'
            }),
            "Link": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на закупку'
            }),
            "Months": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество месяцев'
            }),
            "Description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
        }

class ApplicationPrincipalCompanyForm(ModelForm):
    class Meta:
        model = PrincipalCompany
        fields = ['Name', 'INN', 'OGRN','Vlad']
        widgets = {
            "Name": TextInput(attrs={
                'id': 'party',
                'class': 'form-control',
                'placeholder': 'Компания принципала'
            }),
            'INN': NumberInput(attrs={

                'class': 'form-control',
                'placeholder': 'ИНН принципала',
                'maxlength': '2'
            }),
            'OGRN': NumberInput(attrs={

                'class': 'form-control',
                'placeholder': 'ОГРН принципала'
            }),
            'Vlad': HiddenInput
        }


class ApplicationBeneficiarCompanyForm(ModelForm):
    class Meta:
        model = BeneficiarCompany
        fields = ['Name', 'INN', 'OGRN', 'Vlad']
        widgets = {
            "Name": TextInput(attrs={
                'id': 'party',
                'class': 'form-control',
                'placeholder': 'Компания Бенефициара'
            }),
            'INN': NumberInput(attrs={

                'class': 'form-control',
                'placeholder': 'ИНН Бенефициара'
            }),
            'OGRN': NumberInput(attrs={

                'class': 'form-control',
                'placeholder': 'ОГРН бенефициара'
            }),
            'Vlad': HiddenInput(attrs={
                'required': 'False'
        })
        }


class AgentAccountFormmbsbss(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control'
            })
        }


class AgentAccountForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


class AgentAccountProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Name', 'LastName', 'Fam', 'Company', 'role')


class ApplicationInfoForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['Sum', 'PrincipalCompany', 'BeneficiarCompany', 'Link', 'Months', 'Description','Percent']
        widgets = {
            'Sum': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма БГ'
            }),
            "PrincipalCompany": TextInput(attrs={
                'id': 'party',
                'class': 'form-control',
                'placeholder': 'Компания принципала'
            }),
            "BeneficiarCompany": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Компания Бенефициара'
            }),
            "Link": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на закупку'
            }),
            "Months": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество месяцев'
            }),
            "Description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
            "Percent": TextInput(attrs={
               'class': 'form-control',
                'disabled': 'True',
            })
        }


class PersonApplicationInfoForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['id','Fam', 'Name', 'LastName', 'Rank', 'PassportSeria', 'PassportCode', 'Kem_Vid', 'Date_Vid','Birthday']
        widgets = {
            'Rank': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность',
                'initial': 'Владелец',
            }),
            'Fam': TextInput(attrs={

                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'Name': TextInput(attrs={

                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'LastName': TextInput(attrs={

                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            'PassportSeria': NumberInput(attrs={

                'class': 'form-control',
                'placeholder': 'Серия паспорта'
            }),
            'PassportCode': NumberInput(attrs={

                'class': 'form-control',
                'placeholder': 'код паспорта'
            }),
            'Kem_Vid': TextInput(attrs={

                'class': 'form-control',
                'placeholder': 'Кем выдан'
            }),
            'Date_Vid': DateInput(attrs={'class': 'form-control',
               'placeholder': 'Select a date',
               'type': 'date'}),
            'Birthday': DateInput(attrs={'class': 'form-control',
               'placeholder': 'Select a date',
               'type': 'date'}),
            'id': HiddenInput()
        }

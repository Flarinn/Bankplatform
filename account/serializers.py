from rest_framework import serializers

from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'Fam', 'Name', 'LastName', 'Birthday', 'PassportSeria', 'PassportCode', 'Kem_Vid', 'Date_Vid']


class ApplicationSerializer(serializers.ModelSerializer):
    created = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Application
        fields = ['id', 'ProductType', 'Description', 'Sum', 'Percent', 'Months', 'Link', 'PrincipalCompany', 'BeneficiarCompany', 'AgentWorker', 'PlatformWorkerId', 'BankWorkerId', 'AgentDecision', 'PlatformDecision', 'BankDecision', 'Status', 'UstavDoc', 'Buhotch']

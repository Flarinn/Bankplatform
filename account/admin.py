from django.apps import apps
from django.contrib import admin
from .models import Application

# admin.site.register(AgentAccount)
# admin.site.register(Application)

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

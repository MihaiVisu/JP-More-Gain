from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import get_models, get_app


for model in get_models(get_app('retrospective')):
    admin.site.register(model)

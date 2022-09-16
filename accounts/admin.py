from django.contrib import admin
from .models import Account, Mediator, Language, Qualification, Affiliation, Category

# Register your models here.

admin.site.register(Account)
admin.site.register(Mediator)
admin.site.register(Language)
admin.site.register(Qualification)
admin.site.register(Affiliation)
admin.site.register(Category)

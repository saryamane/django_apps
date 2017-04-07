from django.contrib import admin
from myapp.models import Topic, WebPage, AccessRecord

# Register your models here.

admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)

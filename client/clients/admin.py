from django.contrib import admin
from .models import Category_log, Recommendation_log

admin.site.register(Category_log)
admin.site.register(Recommendation_log)
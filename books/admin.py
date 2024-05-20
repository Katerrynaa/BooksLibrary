from django.contrib import admin
from .models import Books, Rating, WeeklyRecommendation

admin.site.register(Books)
admin.site.register(Rating)
admin.site.register(WeeklyRecommendation)



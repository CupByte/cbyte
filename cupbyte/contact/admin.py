from django.contrib import admin

# Register your models here.
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ('date', 'name')
    search_fields = ('name', 'email')

    class Meta:
        model = Feedback

admin.site.register(Feedback, FeedbackAdmin)
from django.contrib import admin
from Feedback.models import feedback

# Register your models here.

class feedbackAdmin(admin.ModelAdmin):
    list_display = ('fb_name','fb_phone','fb_comment')

admin.site.register(feedback,feedbackAdmin)

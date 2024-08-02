from django.contrib import admin
from .models import MailingList, SurveyQuestion, SurveyAnswer
# Register your models here.

admin.site.register(MailingList)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyAnswer)
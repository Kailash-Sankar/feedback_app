from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','sort_id')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('summary','created_date','user')
    search_fields = ('summary','user')
    list_filter = ('user','created_date')
    ordering = ('-created_date',)
    #filter_horizontal = ('tags')

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('user','question','created_date')

class RatingAdmin(admin.ModelAdmin):
	list_display = ('value','ico_name')

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('category','rating','user')

class TransportAdmin(admin.ModelAdmin):
	list_display = ('date','type')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Rating,RatingAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Transport,TransportAdmin)
admin.site.register(Location)
admin.site.register(Vendor)

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


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

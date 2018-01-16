from django.contrib import admin
from .models import Question,Choice
# Register your models here.
#注册模型

# admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date','question_text']  #注册显示内容
    list_display = ('question_text','pub_date') #列表显示 表头
    list_filter = ['pub_date']  #过滤器条件
    search_fields = ['question_text'] #搜索条件


    inlines = [ChoiceInline]  #添加关联对象
    # fields = [
    #     (None,      {'fields':['question_text']}),
    #     (u'时间信息',{'fields':['pub_date']}),
    # ]

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)
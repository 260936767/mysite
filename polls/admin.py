from django.contrib import admin
from .models import Question,Choice
# Register your models here.
#注册模型

# admin.site.register(Question)

# 多对一的多方
# StackedInline  堆放
class ChoiceInfo(admin.TabularInline):

    model = Choice
    extra = 2      #一次性创建几个模型


@admin.register(Question)  # 装饰器注册模型
class QuestionAdmin(admin.ModelAdmin):

    # 修改属性简短描述 设置页面列表名称
    def questionText(self): # 可以对属性进行拦截 做处理
        return self.question_text
    def pubDate(self):
        return self.pub_date
    def create_time(self):
        return self.create_time
    def last_time(self):
        return self.last_time
    questionText.short_description = "问题描述"
    pubDate.short_description = "提出时间"
    create_time.short_description = "创建时间"
    last_time.short_description = "更新时间"

    # 列表属性
    # list_display = ('question_text','pub_date') #列表显示 表头
    list_display = (questionText,pubDate,create_time,last_time) #列表显示 表头  传入函数名
    list_filter = ['pub_date']  #过滤器条件
    search_fields = ['question_text'] #搜索条件
    list_per_page = 10  #分页 5条为1页

    # 添加修改属性
    # fields = ['pub_date', 'question_text']  # 显示属性顺序内容  fields和fieldsets不能同时使用

    # 分组
    fieldsets = [
        (u'问题内容',      {'fields':['question_text']}),
        (u'提出时间',{'fields':['pub_date']}),
    ]

    inlines = [ChoiceInfo]  #添加关联对象  一个问题可以带出3个choice模型


    # 执行动作的位置 在顶部还是底部
    actions_on_bottom = True
    actions_on_top = False

# admin.site.register(Question,QuestionAdmin)  # 也可以使用装饰器注册
admin.site.register(Choice)
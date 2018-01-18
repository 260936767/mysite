from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    create_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        db_table = 'question'
        ordering = ['id']

#定义模型管理器 重写查询集方法，过滤
class ChoiceManager(models.Manager):

    def get_queryset(self):

        return super(ChoiceManager,self).get_queryset()


class Choice(models.Model):
    # 使用自定义的模型管理器
    choiceObject = ChoiceManager()

    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice_text

    class Meta:
        db_table = 'choice' #定义数据表明，推荐写小写字母，不写，默认为项目名_类名小写
        ordering = ['id'] # 对象的默认排序字段  -id 降序   id 升序

    @classmethod
    def createChoice(cls,question,choice_text,votes,create_time,last_time):
        question = Question.objects.get(pk = 5)
        choice = cls()
        choice.choice_text = choice_text
        choice.votes = votes
        choice.create_time = create_time
        choice.last_time = last_time
        choice.question = question
        return choice



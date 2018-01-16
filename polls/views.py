from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Choice
from django.template import RequestContext,loader
from django.core.urlresolvers import reverse
from django.views import generic  #使用通用视图
from django.utils import timezone

# Create your views here.

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    # output = ','.join([p.question_text for p in latest_question_list])
    # return HttpResponse("hello , world, this is my frist Django Project !")

    # context = RequestContext(request,
    #                          {'latest_question_list':latest_question_list,})
    # return HttpResponse(template.render(context))
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


'''
def detail(request,question_id):
    # return HttpResponse('you are detail at question %s.' %question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist!")
    # return render(request,'polls/detail.html',{'question':question})

    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
'''

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'



'''
def results(request,question_id):
    # response = 'you are results at question %s.'
    # return HttpResponse(response %question_id)
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'polls/results.html',{'question':question})
'''

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request,question_id):
    # return HttpResponse('you are voting on question %s.' %question_id)
    p = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = p.choice_set.get(pk = request.POST['choice'])   # choice html 标签的name
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':p,
            'error_message':"you didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))

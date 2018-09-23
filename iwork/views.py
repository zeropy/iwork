from django.shortcuts import render
from common.mymako import render_mako_context
from common.log import logger
from iwork.models import workRecord

# Create your views here.


def home(request):
    '''
    Home
    '''
    return render_mako_context(request, '/iwork/home.html')


def save_record(request):
    theme = request.POST.get('theme', '')
    content = request.POST.get('content', '')
    data = {
        'theme': theme,
        'content': content,
        'username': request.user.username,
    }

    result = workRecord.objects.save_record(data)
    return render_mako_context(result)


def record(request):
    pass

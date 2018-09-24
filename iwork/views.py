from django.shortcuts import render
from common.mymako import render_mako_context, render_json
from common.log import logger
from iwork.models import workRecord
from account.decorators import login_exempt
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@login_exempt
def home(request):
    '''
    Home
    '''
    return render_mako_context(request, '/iwork/home.html')


@csrf_exempt
@login_exempt
def save_record(request):
    theme = request.POST.get('theme', '')
    content = request.POST.get('content', '')
    print(theme)
    data = {
        'theme': theme,
        'content': content,
        'username': request.user.username,
    }

    result = workRecord.objects.save_record(data)
    return render_json(result)


@login_exempt
def record(request):
    record_list = workRecord.objects.all().order_by('-id')
    data = []
    for index, record in enumerate(record_list):
        data.append({
            'index': index,
            'theme': record.theme,
            'content': record.content,
        })
    return render_json({'code': 0, 'message': 'success', 'data': data})

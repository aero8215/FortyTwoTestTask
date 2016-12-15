# Create your views here.
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from apps.hello.models import Information


def index(request):
    data = Information.objects.all()[:1].get()
    context = {}
    if data:
        context['first_name'] = data.first_name
        context['last_name'] = data.last_name
        context['bio'] = data.bio
        context['birth_date'] = data.birth_date.date()
        context['skype'] = data.skype
        context['jabber'] = data.jabber
        context['other_contacts'] = \
            data.other_contacts.replace('\r\n\r\n', '<br>')
    return render(request, 'index.html', context)


def page_not_found(request):
    response = render_to_response(
        '400.html',
        context_instance=RequestContext(request)
    )
    response.status_code = 400
    return response

def bad_request(request):
    response = render_to_response(
        '500.html',
        context_instance=RequestContext(request)
    )
    response.status_code = 500
    return response
# Create your views here.
from django.shortcuts import render
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

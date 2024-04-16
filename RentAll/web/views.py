from django.http import HttpResponseNotFound
from django.template.loader import get_template
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'common/index.html'


class ContactsView(TemplateView):
    template_name = 'common/contacts.html'


def handle_404(request, exception):

    template = get_template('404.html')

    context = {}
    html = template.render(context, request)

    return HttpResponseNotFound(html)
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'common/index.html'


class ContactsView(TemplateView):
    template_name = 'common/contacts.html'
from apps.generic.views import EphemeralTemplateView
from apps.generic.forms import ContactForm

class ContactView(EphemeralTemplateView):
    template_name = "contact.html"

    def get(self, request, **kwargs):
        kwargs['contactForm'] = ContactForm()
        return EphemeralTemplateView.get(self, request, **kwargs)

    def post(self, request, **kwargs):
        kwargs['contactForm'] = ContactForm(request.POST)
        
        if kwargs['contactForm'].is_valid():
            kwargs['contactForm'].save()
            kwargs['message'] = 'Enviado com sucesso!'
            kwargs['contactForm'] = ContactForm()
        return EphemeralTemplateView.get(self, request, **kwargs)


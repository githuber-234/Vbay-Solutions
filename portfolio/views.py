from django.views.generic import TemplateView, FormView, ListView
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Project

class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

class ServicesView(TemplateView):
    template_name = 'portfolio/services.html'

class AboutView(FormView):
    template_name = 'portfolio/about.html'
    success_url = '/about/'

    def get_context_data(self, request):
        return {
            'contact_form': ContactForm(),
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(request))

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(request)

        if 'contact_submit' in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                send_mail(
                    "Message from Portfolio",
                    f"From: {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\nMessage:\n{form.cleaned_data['message']}",
                    settings.DEFAULT_FROM_EMAIL,
                    ['ad123eg456@gmail.com']
                )
                return redirect(self.success_url)
            else:
                context['contact_form'] = form

        return render(request, self.template_name, context)

class ProjectsView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'portfolio/projects.html'
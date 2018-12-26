from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from core.services import AnswerService, EmailService
from web.forms import AnswerForm


# Create your views here.
class AnswerView(FormView):
    form_class = AnswerForm
    template_name = 'answer/form.html'
    success_url = reverse_lazy('answer-form')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.answer_service = AnswerService()
        self.email_service = EmailService()

    def form_valid(self, form):
        data = form.cleaned_data
        name = data['name']
        email = data['email']
        university = data['university']
        answer = self.answer_service.create(name, email, university)
        self.email_service.send_answer(answer)
        messages.info(self.request, 'Thank you for answer!')
        return super().form_valid(form)

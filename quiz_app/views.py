from django.views.generic import TemplateView

from quiz_app.models import (
    TypePublicCatering,
    TypeRetail,
    AppointmentService,
    Quiz
)


class Page404View(TemplateView):
    """Страница 404"""
    
    template_name = 'page_404.html'

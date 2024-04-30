from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect, get_object_or_404

from quiz_app.forms import (
    QuizForm,
    TypePublicCateringForm,
    TypeRetailForm,
    TypeAppointmentServiceForm,
    SizePublicCateringForm,
    SizeRetailForm,
    SizeAppointmentServiceForm,
    ServicePublicCateringForm,
    ServiceRetailForm,
    ServiceAppointmentServiceForm
)
from quiz_app.models import (
    TypePublicCatering,
    TypeRetail,
    TypeAppointmentService,
    Quiz
)


class QuizFormView(FormView):
    """Представление для основы опроса"""

    form_class = QuizForm
    template_name = 'quiz_shop_main_create.html'

    def form_valid(self, form):
        quiz = form.save()
        return redirect(to='quiz_app:type_shop_new', pk=quiz.pk)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class TypeShopFormView(FormView):
    """Представление для опроса с типом бизнеса"""
    
    template_name = 'quiz_shop_type.html'

    def get_form_class(self, *args, **kwargs):
        if self.kwargs.get('pk'):
            quiz = Quiz.objects.get(id=self.kwargs.get('pk'))
            if quiz.type_business == 'ОБЩП':
                return TypePublicCateringForm
            elif quiz.type_business == 'РИТ':
                return TypeRetailForm
            elif quiz.type_business == 'УСПЗ':
                return TypeAppointmentServiceForm
            return None
        return None

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.quiz = Quiz.objects.get(id=self.kwargs.get('pk'))
        quiz.save()
        return redirect(to='quiz_app:size_shop_new', pk=self.kwargs.get('pk'))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class SizeShopFormView(FormView):
    """Представление для опроса с размером заведения"""
    
    template_name = 'quiz_shop_size.html'

    def get_form_class(self, *args, **kwargs):
        if self.kwargs.get('pk'):
            quiz = Quiz.objects.get(id=self.kwargs.get('pk'))
            if quiz.type_business == 'ОБЩП':
                self.kwargs['model_type_shop'] = TypePublicCatering
                return SizePublicCateringForm
            elif quiz.type_business == 'РИТ':
                self.kwargs['model_type_shop'] = TypeRetail
                return SizeRetailForm
            elif quiz.type_business == 'УСПЗ':
                self.kwargs['model_type_shop'] = TypeAppointmentService
                return SizeAppointmentServiceForm
            return None
        return None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.kwargs.get('pk'):
            quiz = Quiz.objects.get(id=self.kwargs.get('pk'))
            
            kwargs['instance'] = get_object_or_404(
                self.kwargs['model_type_shop'], 
                quiz=quiz
            )
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect(
            to='quiz_app:service_shop_new', 
            pk=self.kwargs.get('pk')
        )

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class ServiceShopFormView(FormView):
    "Представление для сервиса заведения"

    template_name = 'quiz_shop_service.html'

    def get_form_class(self, *args, **kwargs):
        if self.kwargs.get('pk'):
            quiz = Quiz.objects.get(id=self.kwargs.get('pk'))
            if quiz.type_business == 'ОБЩП':
                self.kwargs['model_type_shop'] = TypePublicCatering
                return ServicePublicCateringForm
            elif quiz.type_business == 'РИТ':
                self.kwargs['model_type_shop'] = TypeRetail
                return ServiceRetailForm
            elif quiz.type_business == 'УСПЗ':
                self.kwargs['model_type_shop'] = TypeAppointmentService
                return ServiceAppointmentServiceForm
            return None
        return None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.kwargs.get('pk'):
            quiz = Quiz.objects.get(id=self.kwargs.get('pk'))
            
            kwargs['instance'] = get_object_or_404(
                self.kwargs['model_type_shop'], 
                quiz=quiz
            )
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect(to='quiz_app:quiz_end')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class Page404View(TemplateView):
    """Представление для страницы 404"""
    
    template_name = 'page_404.html'


class QuizEndView(TemplateView):
    """Представление для завершающей анкету страницы"""
    
    template_name = 'quiz_end.html'

from django.contrib import admin
from quiz_app.models import (
    TypePublicCatering,
    TypeRetail,
    AppointmentService,
    Quiz
)


class QuizAdmin(admin.ModelAdmin):
    """
    Класс для настройки отображения полей модели
    """

    readonly_fields = ('created_at', )


admin.site.register(TypePublicCatering)
admin.site.register(TypeRetail)
admin.site.register(AppointmentService)
admin.site.register(Quiz, QuizAdmin)

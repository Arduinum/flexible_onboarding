from django.db import models


class Quiz(models.Model):
    """Модель опроса"""

    CHOICES_CITY = (
        ('ГМОС', 'Россия, г Москва'),
        ('ГНН', 'Россия, г Нижний Новгород'),
        ('ГСАМ', 'Россия, г Самара')
    )

    CHOICES_TYPES_BUSINESS = (
        ('ОБЩП', 'общепит'),
        ('РИТ', 'ритейл'),
        ('УСПЗ', 'услуга по записи')
    )

    email = models.EmailField(
        verbose_name='почта пользователя'
    )

    title = models.CharField(
        verbose_name='название заведения',
        max_length=200
    )

    type_business = models.CharField(
        verbose_name='тип бизнеса',
        choices=CHOICES_TYPES_BUSINESS,
        max_length=200
    )

    country_and_city = models.CharField(
        verbose_name='страна и город',
        choices=CHOICES_CITY,
        max_length=200,

    )

    address = models.TextField(
        verbose_name='адрес',
        blank=True,
        null=True
    )

    is_new_shop = models.BooleanField(
        verbose_name='новое заведение',
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='дата создания'
    )

    def __str__(self):
        return f'опрос {self.title}'

    class Meta:
       db_table = 'quiz'
       verbose_name = 'опрос'
       verbose_name_plural = 'опросы' 


class TypePublicCatering(models.Model):
    """Тип заведения общепит"""

    is_restaurant = models.BooleanField(
        verbose_name='ресторан',
        default=False
    )

    is_bar = models.BooleanField(
        verbose_name='бар',
        default=False
    )

    is_cafe = models.BooleanField(
        verbose_name='кафе',
        default=False
    )

    is_dining_room = models.BooleanField(
        verbose_name='столовая',
        default=False
    )

    room_area = models.FloatField(
        verbose_name='общая площадь помещения',
        blank=True,
        null=True
    )

    kitchen_area = models.FloatField(
        verbose_name='площадь кухни',
        blank=True,
        null=True
    )

    number_seats = models.IntegerField(
        verbose_name='колличество посадочных мест',
        blank=True,
        null=True
    )

    is_take_out = models.BooleanField(
        verbose_name='на вынос',
        default=False
    )

    is_in_room = models.BooleanField(
        verbose_name='в помещении',
        default=False
    )

    is_delivery = models.BooleanField(
        verbose_name='доставка',
        default=False
    )

    quiz = models.ForeignKey(
        to=Quiz,
        on_delete=models.CASCADE,
        verbose_name='опрос'
    )

    def __str__(self):
        return f'общепит {self.quiz.title}'
    
    class Meta:
       db_table = 'type_public_сatering'
       verbose_name = 'тип заведения общепит'
       verbose_name_plural = 'типы заведений общепиты'


class TypeRetail(models.Model):
    """Тип заведения ритейл"""

    is_clothing_store = models.BooleanField(
        verbose_name='магазин одежды',
        default=False
    )

    is_pharmacy = models.BooleanField(
        verbose_name='аптека',
        default=False
    )

    is_supermarket = models.BooleanField(
        verbose_name='супермаркет',
        default=False
    )

    is_book_shop = models.BooleanField(
        verbose_name='книжный магазин',
        default=False
    )

    room_area = models.FloatField(
        verbose_name='общая площадь помещения',
        blank=True,
        null=True
    )

    warehouse_area = models.FloatField(
        verbose_name='площадь склада',
        blank=True,
        null=True
    )

    number_shelving = models.IntegerField(
        verbose_name='колличество стиллажей',
        blank=True,
        null=True
    )

    is_take_out = models.BooleanField(
        verbose_name='на вынос',
        default=False
    )

    is_reservation = models.BooleanField(
        verbose_name='зарезервировать',
        default=False
    )

    is_delivery = models.BooleanField(
        verbose_name='доставка',
        default=False
    )

    quiz = models.ForeignKey(
        to=Quiz,
        on_delete=models.CASCADE,
        verbose_name='опрос'
    )

    def __str__(self):
        return f'ритейл {self.quiz.title}'
    
    class Meta:
       db_table = 'type_retail'
       verbose_name = 'тип заведения ритейл'
       verbose_name_plural = 'типы заведений ритейлы'


class TypeAppointmentService(models.Model):
    """Тип услуга по записи"""

    is_fitness_centre = models.BooleanField(
        verbose_name='фитнес центр',
        default=False
    )

    is_beauty_saloon = models.BooleanField(
        verbose_name='салон красоты',
        default=False
    )

    is_bowling = models.BooleanField(
        verbose_name='боулинг',
        default=False
    )

    is_clinic = models.BooleanField(
        verbose_name='клиника',
        default=False
    )

    room_area = models.FloatField(
        verbose_name='общая площадь помещения',
        blank=True,
        null=True
    )

    main_hall_area = models.FloatField(
        verbose_name='площадь основного зала',
        blank=True,
        null=True
    )

    number_staff = models.IntegerField(
        verbose_name='колличество персонала',
        blank=True,
        null=True
    )

    is_consultation = models.BooleanField(
        verbose_name='консультация',
        default=False
    )

    quiz = models.ForeignKey(
        to=Quiz,
        on_delete=models.CASCADE,
        verbose_name='опрос'
    )

    def __str__(self):
        return f'запись {self.quiz.title}'
    
    class Meta:
       db_table = 'type_appointment_service'
       verbose_name = 'тип услуга по записи'
       verbose_name_plural = 'типы услуги по записи'

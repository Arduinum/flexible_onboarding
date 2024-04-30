from django import forms
from quiz_app.models import (
    TypePublicCatering,
    TypeRetail,
    TypeAppointmentService,
    Quiz
)


class QuizForm(forms.ModelForm):
    """Форма для основы опроса"""

    class Meta:
        model = Quiz
        fields = (
            'email', 
            'title', 
            'type_business', 
            'country_and_city',
            'address',
            'is_new_shop'
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'id': 'email'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'id': 'title'
                }
            ),
            'type_business': forms.Select(
                attrs={
                    'class': 'form-select',
                    'required': True,
                    'id': 'type_business'
                }
            ),
            'country_and_city': forms.Select(
                attrs={
                    'class': 'form-select',
                    'required': False,
                    'id': 'country_and_city'
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'id': 'address',
                    'rows': 3
                }
            ),
            'is_new_shop': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_new_shop'
                }
            ),
        }
        labels = {
           'email': '* Электронная почта',
           'title': '* Название заведения',
           'type_business': '* Тип бизнеса',
           'country_and_city': 'Страна и город',
           'address': 'Адрес',
           'is_new_shop': 'Новое заведение'
        }


class TypePublicCateringForm(forms.ModelForm):
    """Форма для типа заведения общепит"""

    class Meta:
        model = TypePublicCatering
        fields = (
            'is_restaurant', 
            'is_bar', 
            'is_cafe', 
            'is_dining_room'
        )
        widgets = {
            'is_restaurant': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_restaurant'
                }
            ),
            'is_bar': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_bar'
                }
            ),
            'is_cafe': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_cafe'
                }
            ),
            'is_dining_room': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_dining_room'
                }
            ),
        }
        labels = {
           'is_restaurant': 'Ресторан',
           'is_bar': 'Бар',
           'is_cafe': 'Кафе',
           'is_dining_room': 'Столовая'
        }


class TypeRetailForm(forms.ModelForm):
    """Форма для типа заведения ретейл"""

    class Meta:    
        model = TypeRetail
        fields = (
            'is_clothing_store', 
            'is_pharmacy', 
            'is_supermarket', 
            'is_book_shop'
        )
        widgets = {
            'is_clothing_store': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_clothing_store'
                }
            ),
            'is_pharmacy': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_pharmacy'
                }
            ),
            'is_supermarket': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_supermarket'
                }
            ),
            'is_book_shop': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_book_shop'
                }
            ),
        }
        labels = {
           'is_clothing_store': 'Магазин одежды',
           'is_pharmacy': 'Аптека',
           'is_supermarket': 'Супермаркет',
           'is_book_shop': 'Книжный магазин'
        }


class TypeAppointmentServiceForm(forms.ModelForm):
    """Форма для типа услуга по записи"""

    class Meta:    
        model = TypeAppointmentService
        fields = (
            'is_fitness_centre', 
            'is_beauty_saloon', 
            'is_bowling', 
            'is_clinic'
        )
        widgets = {
            'is_fitness_centre': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_fitness_centre'
                }
            ),
            'is_beauty_saloon': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_beauty_saloon'
                }
            ),
            'is_bowling': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_bowling'
                }
            ),
            'is_clinic': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_clinic'
                }
            ),
        }
        labels = {
           'is_fitness_centre': 'Фитнес центр',
           'is_beauty_saloon': 'Салон красоты',
           'is_bowling': 'Боулинг',
           'is_clinic': 'Клиника'
        }


class SizePublicCateringForm(forms.ModelForm):
    """Форма для размеров заведения общепит"""

    class Meta:    
        model = TypePublicCatering
        fields = (
            'room_area', 
            'kitchen_area', 
            'number_seats'
        )
        widgets = {
            'room_area': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'placeholder': 'М²',
                    'step': '0.01',
                    'id': 'room_area'
                }
            ),
            'kitchen_area': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'placeholder': 'М²',
                    'step': '0.01',
                    'id': 'kitchen_area'
                }
            ),
            'number_seats': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'id': 'number_seats'
                }
            )
        }
        labels = {
           'room_area': 'Общая площадь помещения',
           'kitchen_area': 'Площадь кухни',
           'number_seats': 'Колличество посадочных мест'
        }


class SizeRetailForm(forms.ModelForm):
    """Форма для размеров заведения ритейл"""

    class Meta:    
        model = TypeRetail
        fields = (
            'room_area', 
            'warehouse_area', 
            'number_shelving'
        )
        widgets = {
            'number_shelving': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'placeholder': 'М²',
                    'step': '0.01',
                    'id': 'number_shelving'
                }
            ),
            'warehouse_area': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'placeholder': 'М²',
                    'step': '0.01',
                    'id': 'warehouse_area'
                }
            ),
            'number_shelving': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'id': 'number_shelving'
                }
            )
        }
        labels = {
           'room_area': 'Общая площадь помещения',
           'warehouse_area': 'Площадь склада',
           'number_shelving': 'Колличество стиллажей'
        }


class SizeAppointmentServiceForm(forms.ModelForm):
    """Форма для размеров заведения услуга по записи"""

    class Meta:    
        model = TypeAppointmentService
        fields = (
            'room_area', 
            'main_hall_area', 
            'number_staff'
        )
        widgets = {
            'room_area': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'placeholder': 'М²',
                    'step': '0.01',
                    'id': 'room_area'
                }
            ),
            'main_hall_area': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'placeholder': 'М²',
                    'step': '0.01',
                    'id': 'main_hall_area'
                }
            ),
            'number_staff': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'id': 'number_staff'
                }
            )
        }
        labels = {
           'room_area': 'Общая площадь помещения',
           'main_hall_area': 'Площадь основного зала',
           'number_staff': 'Колличество персонала'
        }


class ServicePublicCateringForm(forms.ModelForm):
    """Форма для сервиса заведение общепит"""

    class Meta:    
        model = TypePublicCatering
        fields = (
            'is_take_out', 
            'is_in_room', 
            'is_delivery'
        )
        widgets = {
            'is_take_out': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_take_out'
                }
            ),
            'is_in_room': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_in_room'
                }
            ),
            'is_delivery': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_delivery'
                }
            )
        }
        labels = {
           'is_take_out': 'На вынос',
           'is_in_room': 'В помещении',
           'is_delivery': 'Доставка'
        }


class ServiceRetailForm(forms.ModelForm):
    """Форма для сервиса заведение ритейл"""

    class Meta:    
        model = TypeRetail
        fields = (
            'is_take_out', 
            'is_reservation', 
            'is_delivery'
        )
        widgets = {
            'is_take_out': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_take_out'
                }
            ),
            'is_reservation': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_reservation'
                }
            ),
            'is_delivery': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_delivery'
                }
            )
        }
        labels = {
           'is_take_out': 'На вынос',
           'is_reservation': 'Зарезервировать',
           'is_delivery': 'Доставка'
        }


class ServiceAppointmentServiceForm(forms.ModelForm):
    """Форма для сервиса заведение услуга по записи"""

    class Meta:    
        model = TypeAppointmentService
        fields = (
            'is_consultation', 
        )
        widgets = {
            'is_consultation': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'required': False,
                    'id': 'is_consultation'
                }
            )
        }
        labels = {
           'is_consultation': 'Консультация'
        }

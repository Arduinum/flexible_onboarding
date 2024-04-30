from django.urls import path
from quiz_app.views import (
    Page404View, 
    QuizFormView, 
    TypeShopFormView,
    SizeShopFormView,
    ServiceShopFormView,
    QuizEndView
)


app_name = 'quiz_app'

urlpatterns = [
    path('main_shop/new/', QuizFormView.as_view(), name='main_shop_new'),
    path('main_shop/<int:pk>/type_shop/new', TypeShopFormView.as_view(), name='type_shop_new'),
    path('main_shop/<int:pk>/size_shop/new', SizeShopFormView.as_view(), name='size_shop_new'),
    path('main_shop/<int:pk>/service_shop/new', ServiceShopFormView.as_view(), name='service_shop_new'),
    path('page404/', Page404View.as_view(), name='page404'),
    path('quiz_end/', QuizEndView.as_view(), name='quiz_end')
]

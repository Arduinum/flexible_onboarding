from django.urls import path
from quiz_app.views import Page404View


app_name = 'quiz_app'

urlpatterns = [
    path('page404/', Page404View.as_view(), name='page404'),
]

from django.urls import path
from . import views
# from .views import line_chart, line_chart_json

app_name='contact'

urlpatterns = [
    path('', views.Contact,name='contact'), 
]

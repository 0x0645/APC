from django.urls import path
from . import views
# from .views import line_chart, line_chart_json

app_name='products'

urlpatterns = [
    path('', views.Product,name='productname'),
    path('<int:pk>', views.itemDetails.as_view() , name='itemDetails'),
    # path('chart', line_chart, name='line_chart'),
    # path('chartJSON', line_chart_json, name='line_chart_json'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),

]

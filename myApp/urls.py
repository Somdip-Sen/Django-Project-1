from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_page, name='search'),
    # 'url/' will redirect both url and url/ to the target where only 'url' will only redirect 'url' but not 'url/'
]

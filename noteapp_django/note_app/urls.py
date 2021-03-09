from django.urls import path
from . import views
from .views import Index_Detail

urlpatterns = [
    path('',views.index,name='index'),
    path('cat/',views.cat,name='category'),
    path('<int:pk>',Index_Detail.as_view(),name='detail'),
]
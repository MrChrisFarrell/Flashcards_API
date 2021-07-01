from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.CollectionList.as_view()),
]
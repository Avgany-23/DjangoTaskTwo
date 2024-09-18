from django.urls import path
from .views import Recipe, MainView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path(r'<str:dish>/', Recipe.as_view(), name='recipes'),
]

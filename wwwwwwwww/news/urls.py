from django.urls import path
from .views import NewsList, NewsSearch

urlpatterns = [
    path('', NewsList.as_view()),
    path('search', NewsSearch.as_view())
]

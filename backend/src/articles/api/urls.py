from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDestroyView,
)

from rest_framework.routers import DefaultRouter
from rest_framework import viewsets

"""urlpatterns = [
    path('', ArticleListView.as_view()),
    path('create/', ArticleCreateView.as_view()),
    path('<pk>/', ArticleDetailView.as_view()),
    path('<pk>/update/', ArticleUpdateView.as_view()),
    path('<pk>/delete/', ArticleDestroyView.as_view()),
]"""

router = DefaultRouter()
router.register(r'')
urlpatterns = router.urls

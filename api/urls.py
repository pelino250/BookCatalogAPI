from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import AuthorModelViewSet, AuthorList

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)

urlpatterns = [
    path("authors/", AuthorList.as_view()),
]
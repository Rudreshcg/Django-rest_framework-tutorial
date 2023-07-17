from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets/', views.SnippetList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)

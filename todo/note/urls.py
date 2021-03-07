from django.urls import path,include
from .views import NoteAPIView

urlpatterns = [
    path('',NoteAPIView.as_view()),
    path('<pk>',NoteAPIView.as_view())
]
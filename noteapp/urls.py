from django.urls import path
from .views import (
    NoteListCreateAPIView,
    NoteRetrieveUpdateDestroyAPIView,
    login_view
)

urlpatterns = [
    #path('register/',register_view, name="register"),
    path('login/',login_view, name="login"),
    #path('logout/',views.logoutUser, name = "logout"),
    path('notes/', NoteListCreateAPIView.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyAPIView.as_view())]

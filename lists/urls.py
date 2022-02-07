from django.urls import path
from . import views

app_name = "lists"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>/", views.ListDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.UpdateList.as_view(), name="edit"),
    path("create", views.CreateList.as_view(), name="create"),
    path("<int:pk>/delete/", views.DeleteView.as_view(), name="delete"),
]

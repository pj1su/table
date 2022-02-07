from django.db import models
from django.shortcuts import render, reverse, redirect


class ListModel(models.Model):
    title = models.CharField(max_length=20, default="enjoy")
    description = models.TextField(default="description List")
    host = models.ForeignKey(
        "users.User", related_name="list", on_delete=models.CASCADE, null=True
    )

    def get_absolute_url(self):
        return reverse("lists:detail", kwargs={"pk": self.pk})

from django.db import models


class Locomotive(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name="Наименование Марки Авто"
    )

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"

    def __str__(self):
        return self.name

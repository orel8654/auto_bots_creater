from django.db import models
from django.contrib.auth.models import User

class TelegramBotsTypes(models.Model):
    types_id = models.IntegerField(null=True, blank=True)
    types = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.types)

class TelegramBots(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True, verbose_name='Название бота')
    name_bot = models.CharField(max_length=255, blank=False, null=True, verbose_name='@')
    api_token = models.CharField(max_length=255, blank=False, null=True, verbose_name='Token')
    active = models.BooleanField(blank=True, null=True, default=False, verbose_name='Активный')
    type_bot = models.ForeignKey(TelegramBotsTypes, on_delete=models.CASCADE, verbose_name='Тип бота')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return str(self.name)

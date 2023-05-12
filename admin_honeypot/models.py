from django.db import models
from admin_honeypot import listeners


class LoginAttempt(models.Model):
    username = models.CharField("username", max_length=255, blank=True, null=True)
    ip_address = models.GenericIPAddressField("ip address", protocol='both', blank=True, null=True)
    session_key = models.CharField("session key", max_length=50, blank=True, null=True)
    user_agent = models.TextField("user-agent", blank=True, null=True)
    timestamp = models.DateTimeField("timestamp", auto_now_add=True)
    path = models.TextField("path", blank=True, null=True)

    class Meta:
        verbose_name = "login attempt"
        verbose_name_plural = "login attempts"
        ordering = ('timestamp',)

    def __str__(self):
        return self.username

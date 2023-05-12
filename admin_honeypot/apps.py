from django.apps import AppConfig

__all__ = ['AdminHoneypotConfig']


class AdminHoneypotConfig(AppConfig):
    name = 'admin_honeypot'
    label = 'admin_honeypot'
    verbose_name = 'Admin Honeypot'
    default_auto_field = 'django.db.models.AutoField'

import django

if django.VERSION < (3, 2):
    default_app_config = "django_health_check_prometheus.apps.HealthCheckConfig"

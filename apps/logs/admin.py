from django.contrib import admin
from apps.logs import models as m_logs
# Register your models here.

admin.site.register(m_logs.Log)
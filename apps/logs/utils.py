from apps.logs import models as m_logs


def create_log(e):
    m_logs.Log.objects.create(details=e)
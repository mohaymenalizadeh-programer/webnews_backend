from django.utils import timezone

def relative_time(dt):
    now = timezone.now()
    diff = now - dt
    seconds = diff.total_seconds()
    days = diff.days

    if seconds < 60:
        return "همین الان"
    elif seconds < 3600:
        return f"{int(seconds // 60)} دقیقه پیش"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} ساعت پیش"
    elif days == 1:
        return "دیروز"
    elif days < 7:
        return f"{days} روز پیش"
    elif days < 30:
        return f"{days // 7} هفته پیش"
    elif days < 365:
        return f"{days // 30} ماه پیش"
    else:
        return f"{days // 365} سال پیش"
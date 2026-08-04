from django.contrib import admin
from .models import Newsoftheday, NewsLifestyle, NewsDecoration, NewsTechnology , NewsArtculture , Slidertxt , Slidernews , Coment ,Visit, PageVideo , Portfolio
from django.utils import timezone
from datetime import timedelta
# Register your models here.

admin.site.register(Newsoftheday)
admin.site.register(NewsLifestyle)
admin.site.register(NewsDecoration)
admin.site.register(NewsTechnology)
admin.site.register(NewsArtculture)
admin.site.register(Slidertxt)
admin.site.register(Slidernews)

@admin.register(Coment)
class ComentAdmin(admin.ModelAdmin):
    list_display = ('coment_usernameandlastname', 'news_slug', 'publish_date', 'is_approved')
    list_filter = ('is_approved', 'publish_date')
    search_fields = ('coment_usernameandlastname', 'coment_title', 'news_slug')
    list_editable = ('is_approved',)








@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('device', 'created_at')

    def changelist_view(self, request, extra_context=None):
        today = timezone.now().date()
        yesterday = today - timedelta(days=1)
        week_ago = today - timedelta(days=7)

        today_visits = Visit.objects.filter(created_at__date=today)
        devices_today = list(today_visits.values_list('device', flat=True))

        extra_context = extra_context or {}
        extra_context['title'] = (
            f"امروز: {today_visits.count()} بازدید | "
            f"دستگاه‌های امروز: {', '.join(devices_today) if devices_today else 'هیچ'} | "
            f"دیروز: {Visit.objects.filter(created_at__date=yesterday).count()} | "
            f"این هفته: {Visit.objects.filter(created_at__date__gte=week_ago).count()}"
        )
        return super().changelist_view(request, extra_context=extra_context)

@admin.register(PageVideo)
class PageVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'created_at')




admin.site.register(Portfolio)    
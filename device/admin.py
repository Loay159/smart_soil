from django.contrib import admin
from .models import Zone, Zone_History

class ZoneHistoryAdmin(admin.ModelAdmin):
    list_filter = [
         "zone",
    ]
    list_display = ("zone", "level", "time",)
    search_fields = (
        "zone",
    )

class ZoneAdmin(admin.ModelAdmin):
    list_filter = [
         "name",
    ]
    list_display = ("name", "level",)
    search_fields = (
        "name",
    )
admin.site.register(Zone, ZoneAdmin)
admin.site.register(Zone_History, ZoneHistoryAdmin)

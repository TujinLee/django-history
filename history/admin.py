from django.contrib import admin
 
from .models import *


class HistoryEventAdmin(admin.ModelAdmin):
    date_hierarchy = 'event_timestamp'
    list_display = ('content_type', 'event_timestamp', 'publish_timestamp', 'object_id')
    search_fields = ['content_type', 'slug', 'desc']
    list_filter = ('content_type', 'is_internal', 'is_hidden')

    def related_object_admin(self, obj):
        """ Display link to related object's admin """
        try:
            if obj.content_type and obj.object_id:
                admin_url = reverse('admin:%s_%s_change' % (obj.content_type.app_label, obj.content_type.model), args=(obj.object_id,))
                return '%s: <a href="%s">%s</a>' % (obj.content_type.model.capitalize(), admin_url, obj.content_object.__unicode__())
        except Exception, ex:
            pass
        return _('No relative object')
    related_object_admin.allow_tags = True
    related_object_admin.short_description = _('Related object')



class HistoryAdmin(admin.ModelAdmin):
    list_display = ('owner', )


admin.site.register(HistoryEvent, HistoryEventAdmin)    
admin.site.register(History, HistoryAdmin)

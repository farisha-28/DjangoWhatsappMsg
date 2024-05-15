from django.contrib import admin
from .models import Message, MessageHandler

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'track_id']

class MessageHandlerAdmin(admin.ModelAdmin):
    list_display = ['message', 'email']


admin.site.register(Message, MessageAdmin)
admin.site.register(MessageHandler, MessageHandlerAdmin)
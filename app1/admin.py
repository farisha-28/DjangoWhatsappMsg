from django.contrib import admin
from .models import Users, MessageHandler, WhatsappSender

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email_address', 'track_id']

class MessageHandlerAdmin(admin.ModelAdmin):
    list_display = ['message', 'email']


admin.site.register(Users, UsersAdmin)
admin.site.register(MessageHandler, MessageHandlerAdmin)
admin.site.register(WhatsappSender)
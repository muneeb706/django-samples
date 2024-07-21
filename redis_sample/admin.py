from django.contrib import admin

from .models import Event, Ticket


class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "total_tickets", "available_tickets")


class TicketAdmin(admin.ModelAdmin):
    list_display = ("event", "customer_username")


admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)

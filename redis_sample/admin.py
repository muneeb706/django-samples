from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
# from django.utils.html import format_html

from .models import Event, Ticket


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "total_tickets", "available_tickets")

    # @admin.display(
    #     description='Formatted Name'
    # )
    # def formatted_name(self, obj):
    #     return format_html('<span style="color: red;">{}</span>', obj.name)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("event", "customer_username")


@admin.register(Event.history.model)
class HistoricalEventAdmin(SimpleHistoryAdmin):
    list_display = ("history_id", "history_date", "history_change_reason", "name", "total_tickets", "available_tickets")



@admin.register(Ticket.history.model)
class HistoricalTicketAdmin(admin.ModelAdmin):
    list_display = ("history_id", "history_date", "history_change_reason", "event", "customer_username")
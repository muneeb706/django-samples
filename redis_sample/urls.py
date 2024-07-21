from django.urls import path

from redis_sample import views

urlpatterns = [
    path("event/<int:event_id>/", views.event_detail, name="event_detail"),
    path(
        "event/<int:event_id>/purchase/",
        views.purchase_ticket_view,
        name="purchase_ticket",
    ),
]

from django.apps import AppConfig


class RedisSampleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "redis_sample"

    # def ready(self):
    #     """
    #     Makes sure the Redis cache is consistent with the database,
    #     initializes the ticket counts in Redis
    #     when the application starts.
    #     """
    #     from django_redis import get_redis_connection

    #     from .models import Event

    #     def initialize_redis(sender, **kwargs):
    #         redis_conn = get_redis_connection("default")
    #         events = Event.objects.all()
    #         for event in events:
    #             is_set_succcessful = redis_conn.set(
    #                 f"event:{event.id}:available_tickets", event.available_tickets
    #             )
    #             if is_set_succcessful:
    #                 print("Redis reconcilliation operation was successful.")
    #             else:
    #                 print("Redis reconcilliation operation failed.")

    #     initialize_redis(sender=self)

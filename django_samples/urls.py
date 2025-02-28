from django.contrib import admin
from django.urls import path, include
from fhir_to_parquet import urls as fhir_to_parquet_urls
from redis_sample import urls as redis_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fhir_to_parquet/', include(fhir_to_parquet_urls)),
    path('redis/', include(redis_urls))
]

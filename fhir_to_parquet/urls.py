from django.urls import path

from .views import FHIRToParquetAPIView

urlpatterns = [
    path("convert/", FHIRToParquetAPIView.as_view(), name="convert_fhir_to_parquet"),
]

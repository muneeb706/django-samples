from django.urls import path

from .views import upload_fhir_file

urlpatterns = [
    path("upload/", upload_fhir_file, name="upload_fhir_file"),
]

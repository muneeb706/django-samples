import json
import tempfile

import pandas as pd
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class FHIRToParquetAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("convert_fhir_to_parquet")

    def test_fhir_to_parquet_conversion(self):
        # Sample FHIR data
        fhir_data = {
            "resourceType": "Bundle",
            "type": "collection",
            "entry": [
                {
                    "resource": {
                        "resourceType": "Patient",
                        "id": "example",
                    }
                }
            ],
        }
        fhir_json = json.dumps(fhir_data)
        uploaded_file = SimpleUploadedFile(
            "fhir_file.json", fhir_json.encode("utf-8"), content_type="application/json"
        )

        # Make the POST request with the file
        response = self.client.post(
            self.url, {"file": uploaded_file}, format="multipart"
        )

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Save the response content to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".parquet") as tmp:
            # Write the streaming content to the temporary file
            for chunk in response.streaming_content:
                tmp.write(chunk)
            tmp.seek(0)  # Go back to the start of the file

            # Attempt to read the Parquet file
            try:
                df = pd.read_parquet(tmp.name)
                valid_parquet = True
            except Exception as e:
                print(f"Failed to read Parquet file: {e}")
                valid_parquet = False

            # Assert that the file is a valid Parquet file
            self.assertTrue(
                valid_parquet, "The response is not in a valid Parquet format."
            )

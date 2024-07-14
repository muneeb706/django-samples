import json
from io import BytesIO

import pandas as pd
from django.http import FileResponse
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView


class FHIRToParquetAPIView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file provided"}, status=400)

        try:
            # Read the uploaded FHIR file
            content = file.read()
            fhir_json = json.loads(content)

            # Assuming each entry in the 'entry' list can be directly converted to a row in a DataFrame
            # This might require customization based on the structure of your FHIR data
            entries = [
                self.flatten_resource(entry["resource"]) for entry in fhir_json["entry"]
            ]

            # Note: This simplistic approach assumes each resource can be directly mapped to a DataFrame row.
            # Complex nested structures will require more sophisticated flattening.
            df = pd.json_normalize(entries)

            # save the DataFrame to a Parquet file
            buffer = BytesIO()
            df.to_parquet(buffer)
            buffer.seek(0)

            # Return the Parquet file as a FileResponse
            return FileResponse(
                buffer,
                as_attachment=True,
                filename="converted.parquet",
                content_type="application/octet-stream",
            )

        except Exception as e:
            return Response({"error": str(e)}, status=400)

    def flatten_resource(self, data, prefix=""):
        flattened = {}
        for key, value in data.items():
            new_key = f"{prefix}{key}"
            if isinstance(value, dict):
                flattened.update(self.flatten_resource(value, f"{new_key}_"))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        flattened.update(self.flatten_resource(item, f"{new_key}_{i}_"))
                    else:
                        flattened[f"{new_key}_{i}"] = item
            else:
                flattened[new_key] = value
        return flattened

import tempfile
import json
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from fhir.resources import construct_fhir_element
import pyarrow as pa
import pyarrow.parquet as pq

class FHIRToParquetAPIView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file provided"}, status=400)

        try:
            # Read the uploaded FHIR file
            content = file.read()
            fhir_json = json.loads(content)

            # Assuming fhir_json is a dictionary that includes a 'resourceType' key
            element_type = fhir_json.get('resourceType')
            if element_type:
                # Parse FHIR JSON
                fhir_resource = construct_fhir_element(element_type=element_type, data=fhir_json)

                # Convert FHIR to a flat dictionary
                #  flattening FHIR data simplifies its complex, 
                # hierarchical structure, making it compatible with 
                # Parquet's columnar format and optimizing it for efficient 
                # storage, querying, and interoperability.
                flat_data = self.flatten_fhir(fhir_resource.dict())

                # Convert to PyArrow Table
                table = pa.Table.from_pydict(flat_data)

                # Write to Parquet file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".parquet") as temp_file:
                    pq.write_table(table, temp_file.name)

                # Return the Parquet file
                return FileResponse(open(temp_file.name, 'rb'), 
                                    as_attachment=True, 
                                    filename="converted.parquet")
            else:
                raise ValueError("The provided JSON does not contain a 'resourceType' field.")


        except Exception as e:
            return Response({"error": str(e)}, status=400)

    def flatten_fhir(self, data, prefix=''):
        flattened = {}
        for key, value in data.items():
            new_key = f"{prefix}{key}"
            if isinstance(value, dict):
                flattened.update(self.flatten_fhir(value, f"{new_key}_"))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        flattened.update(self.flatten_fhir(item, f"{new_key}_{i}_"))
                    else:
                        flattened[f"{new_key}_{i}"] = item
            else:
                flattened[new_key] = value
        return flattened

from django.http import HttpResponse
from django.shortcuts import render

from .forms import FHIRFileUploadForm


def upload_fhir_file(request):
    if request.method == "POST":
        form = FHIRFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Capture the uploaded file
            uploaded_file = form.cleaned_data["file"]

            # Process the file here (example: print file name)
            print(uploaded_file.name)

            # Redirect to a new URL or indicate success
            return HttpResponse("File uploaded successfully.")
    else:
        return render(request, "upload.html")

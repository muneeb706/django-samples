from django import forms


class FHIRFileUploadForm(forms.Form):
    file = forms.FileField(required=True)

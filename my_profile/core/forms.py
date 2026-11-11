from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    website = forms.CharField(required=False)  # honeypot: real users leave it empty

    class Meta:
        model = Inquiry
        fields = ["name", "email", "service", "budget", "message"]
        widgets = {"message": forms.Textarea(attrs={"placeholder": "What do you want to build or improve?"})}

    def clean_website(self):
        if self.cleaned_data["website"]:
            raise forms.ValidationError("Spam detected.")
        return ""

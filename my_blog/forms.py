from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(
        max_length=100,
        label="Full Name",
        error_messages={
            "required": "must not be empty",
            "max_length": "Please enter a shorter name",
        },
    )

    message = forms.CharField(max_length=300, label="Message", widget=forms.Textarea)
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)

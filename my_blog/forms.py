from django import forms


class ContactForm(forms.Form):
    firstname = forms.CharField(
        max_length=100,
        label="First Name",
        error_messages={
            "required": "is required",
            "max_length": "exceeded maximum characters",
        },
    )
    lastname = forms.CharField(
        max_length=100,
        label="Last Name",
        error_messages={
            "required": "must not be empty",
            "max_length": "Please enter a shorter name",
        },
    )

    message = forms.CharField(max_length=300, label="Message", widget=forms.Textarea)
    file = forms.FileField()

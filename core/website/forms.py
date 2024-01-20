from typing import Any
from django import forms
from .models import ContactModel,NewsLetter


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ["subject","full_name","email","phone_number","content"]
        
        error_messages = {
            'email': {
                'required': "فیلد ایمیل نمی تواند خالی باشد"
            },
            'content': {
                'required': "فیلد محتوا نمی تواند خالی باشد",
                'min_length': "طول محتوای وارد شده غیر مجاز است"
            },
            'subject': {
                'required': "فیلد  عنوان نمی تواند خالی باشد"
            },
            'full_name': {
                'required': "فیلد نام و نام خانوادگی نمی تواند خالی باشد"
            }
        }
    

class NewsLetterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=False)
    class Meta:
        model = NewsLetter
        fields = ['email',"first_name"]

    def clean_first_name(self):
        if len(self.cleaned_data['first_name']) > 0:
            raise forms.ValidationError("Please leave this field blank.")
        return self.cleaned_data['first_name']
    
    def save(self, commit=True):
        newsletter, created = NewsLetter.objects.get_or_create(email=self.cleaned_data.get("email"))
        return newsletter


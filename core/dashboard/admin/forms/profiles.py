from django.contrib.auth import forms as auth_forms
from django import forms
from django.utils.translation import gettext_lazy as _
from accounts.models import Profile


class AdminPasswordChangeForm(auth_forms.PasswordChangeForm):
    error_messages = {
        "password_incorrect": _(
            "پسورد قبلی شما اشتباه وارد شده است، لطفا تصحیح نمایید."
        ),
        "password_mismatch": _("دو پسورد ورودی با همدیگر مطابقت ندارند"),
    }
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control text-center'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control text-center'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control text-center'
        self.fields['old_password'].widget.attrs['placeholder'] = "پسورد قبلی خود را وارد نمایید"
        self.fields['new_password1'].widget.attrs['placeholder'] = "پسورد جایگزین خود را وارد نمایید"
        self.fields['new_password2'].widget.attrs['placeholder'] = "پسورد جایگزین خود را مجدد وارد نمایید"
    

class AdminProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields =[
            "first_name",
            "last_name",
            "phone_number"
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'نام خود را وارد نمایید'
        self.fields['last_name'].widget.attrs['class'] = 'form-control '
        self.fields['last_name'].widget.attrs['placeholder'] = 'نام خانوادگی را وارد نمایید'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control text-center'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'شماره همراه را وارد نمایید'
        
        
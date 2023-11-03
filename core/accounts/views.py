from django.contrib.auth import views as auth_views
from accounts.forms import AuthenticationForm

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    
    
class LogoutView(auth_views.LogoutView):
    pass
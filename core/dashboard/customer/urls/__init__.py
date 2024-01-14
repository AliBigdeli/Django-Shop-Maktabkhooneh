from django.urls import path,include

app_name = "customer"

urlpatterns = [
    path("",include("dashboard.customer.urls.generals")),
    path("",include("dashboard.customer.urls.profiles")),
]



from django.urls import path,include

app_name = "admin"

urlpatterns = [
    path("",include("dashboard.admin.urls.generals")),
    path("",include("dashboard.admin.urls.profiles")),
    path("",include("dashboard.admin.urls.products")),
    path("",include("dashboard.admin.urls.orders")),
    path("",include("dashboard.admin.urls.reviews")),
]



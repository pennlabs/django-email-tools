from django.urls import include, path


urlpatterns = [path("", include("email_tools.urls", namespace="email_tools"))]

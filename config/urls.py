from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

scheme_view = get_schema_view(
    openapi.Info(
        title="Swagger KinoEdge",
        default_version="v1",
        description="Swagger KinoEdge",
        terms_of_service="htthp://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@swagger.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("movie/", include("movie.urls")),
    path("user/", include("user.urls")),
    path("studio/", include("studio.urls")),
    path("actor/", include("actor.urls")),
    path("news/", include("news.urls")),
    path("", scheme_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", scheme_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

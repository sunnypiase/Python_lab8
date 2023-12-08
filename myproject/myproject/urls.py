from django.contrib import admin
from django.urls import path
from UniversityLib import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('lib/', views.lib_view, name='lib_view'),
]

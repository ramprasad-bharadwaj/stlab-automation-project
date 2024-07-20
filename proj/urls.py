from django.contrib import admin
from django.urls import path
from ap1.views import index, download_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index', index),
    path('download-pdf/<int:mod_no>/', download_pdf, name='download_pdf'),
]

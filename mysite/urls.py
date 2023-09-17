
from django.contrib import admin
from django.urls import path,include
from Practice import views,urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('Practice.urls'))
]

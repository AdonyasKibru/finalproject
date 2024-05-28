from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cost/<int:reservation_id>/', views.cost, name='cost'),
]

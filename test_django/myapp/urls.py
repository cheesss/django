from django.urls import path
from . import views

urlpatterns = [ path('', views.index, name = 'myapp'),
                path('create/',views.create),
                path('read/<id>/', views.read)
]    
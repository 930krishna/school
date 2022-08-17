from django.urls import path
from . import views

urlpatterns = [
    path('updsub/<id>',views.UpdateSub.as_view(),name='updsub'),
    path('delsub/<id>',views.DeleteSub.as_view(),name='delsub'),
]
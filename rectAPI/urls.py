from django.conf.urls import url
from rectAPI import views

urlpatterns=[
    url(r'^account/$',views.accountApi),
    url(r'^account/([0-9]+)$',views.accountApi)
]
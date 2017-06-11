from django.urls import url
import views

urlpatterns = [
    url('^login/$',views.login),
    url('^register/$',views.register),
]
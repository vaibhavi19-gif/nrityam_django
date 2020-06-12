from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name="gallery"),
    path('blog/', views.blog, name="blog"),
    path('about/', views.about, name="about"),
    path('pure/', views.pure, name="pure"),
    path('7styles/', views.styles, name="7styles"),
    path('shloka/', views.shloka, name="shloka"),
    path('semi/', views.semi, name="semi"),
    path('Features_of_Bharatanatyam/', views.featureB, name="featureB"),
    path('feedback/', views.feedback, name="feedback"),
    path('feedback_upload/', views.feedback_upload, name="feedback_upload"),
    path('Bharatanatyam/', views.Bharatanatyam, name="Bharatanatyam"),
    path('prarambhik/', views.prarambhik, name="prarambhik"),
    path('AsamayuktaMudra/', views.amudra, name="amudra")

]
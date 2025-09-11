from django.urls import path
from hello import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, kwargs={"name":"Dias","age":24}),
    path('contact', views.contact),
    path('anime', views.anime, name='anime')
]
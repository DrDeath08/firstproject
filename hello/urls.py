from django.urls import path
from hello import views

urlpatterns = [
    path(r'^about/contact', views.contact),
    path(r'^about', views.about, kwargs={"name":"Dias","age":24}),
    path('anime', views.anime, name='anime'),
    path('', views.index, name='home')
]
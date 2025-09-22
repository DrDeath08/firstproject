from django.urls import path
from hello import views

urlpatterns = [
    path(r'^about', views.about, kwargs={"name":"Dias","age":24}),
    path(r'^about/contact', views.contact),
    path('anime', views.anime, name='anime'),
    path('', views.index, name='home')
]
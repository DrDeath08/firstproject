from django.urls import path, re_path
from hello import views

urlpatterns = [
    re_path(r'^about/contact', views.contact),
    re_path(r'^about', views.about, kwargs={"name":"Dias","age":24}),
    path('anime', views.anime, name='anime'),
    path('', views.index, name='home')
]
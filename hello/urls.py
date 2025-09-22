from django.urls import path, re_path, include
from hello import views

about_patterns = [
    re_path(r'^about/contact', views.contact),
    re_path(r'^about', views.about, kwargs={"name":"Dias","age":24})
]

urlpatterns = [
    path('anime', views.anime, name='anime'),
    path('', views.index, name='home'),
    path('about/', include(about_patterns))
]
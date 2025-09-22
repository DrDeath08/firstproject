from django.urls import path, re_path, include
from hello import views

about_patterns = [
    path('', views.about, kwargs={"name":"Dias","age":24}),
    re_path('contact', views.contact)
]

urlpatterns = [
    path('anime', views.anime, name='anime'),
    path('', views.index, name='home'),
    path('about/', include(about_patterns))
]
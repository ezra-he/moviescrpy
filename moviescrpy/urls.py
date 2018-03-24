
from django.conf.urls import url, include


urlpatterns = [
    url(r'^movie/', include('movie.urls')),
]

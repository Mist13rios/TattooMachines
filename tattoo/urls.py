from django.conf.urls import url
from tattoo.view import index


urlpatterns = [
    url(r'^', index.as_view()),
]

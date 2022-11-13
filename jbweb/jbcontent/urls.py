from django.urls import path, include
from .views import Landing, EpisodePlayback, ShowContents

r'^(?P<review_req_identifier>.*)/detail$'

urlpatterns = [
    path('', Landing.as_view(), name='Landing'),
    path('<slug:show_title>/<int:episode_number>/', EpisodePlayback.as_view(), name='Episode'),
    path('<slug:show_title>/', ShowContents.as_view(), name='ShowContents'),

]
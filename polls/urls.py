from django.urls import path

from .views import (
    PollAllListView,
    PollDetailView,
    # PollListView
    vote
)

app_name = 'polls'

urlpatterns = [
    path('', PollAllListView.as_view(), name='all'),
    path('poll/<slug:slug>/', PollDetailView.as_view(), name='details'),
    # path('vote/<slug:slug>/', PollListView.as_view(), name='votes'),
    path('vote/<slug:slug>/', vote, name='votes'),
]

from django.urls import path

from .views import (
    PollListView,
    PollDetailView
)

app_name = 'polls'

urlpatterns = [
    path('', PollListView.as_view(), name='all'),
    path('poll/<slug:slug>/', PollDetailView.as_view(), name='details'),
]

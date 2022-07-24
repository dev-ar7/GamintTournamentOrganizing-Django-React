from django.urls import path
from .views import *

urlpatterns = [
    path('register-team/', TeamCreateView.as_view(), name='register-team'),
    path('view-teams/', TeamListView.as_view(), name='view-teams'),
    path('host-tournament/', TournamentCreateView.as_view(), name='host-tournament'),
    path('view-tournaments/', TournamentListView.as_view(), name='view-tournaments'),
    path('checkin/', CheckInCreateView.as_view(), name='checkin'),
    path('checkins-list/', CheckInListView.as_view(), name='checkins-list'),
    path('create-match-winner/', MatchWinnerCreateView.as_view(), name='create-match-winner'),
    path('match-winners-list/', MatchWinnerListView.as_view(), name='match-winners-list'),
    path('create-comment/', CommentCreateView.as_view(), name='create-comment'),
    path('comments-list/', CommentListView.as_view(), name='comments-list'),
]
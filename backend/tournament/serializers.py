from rest_framework import serializers
from .models import *


class TeamSerializers(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'team_name', 'player1', 'player1_role',
                'player2', 'player2_role', 'player3',
                'player3_role', 'player4', 'player4_role',
                'player5', 'player5_role')


class TournamentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'game', 'total_no_of_teams',
                'no_of_team_players_allowed', 'type', 'owner')


class CheckInSerializers(serializers.ModelSerializer):

    class Meta:
        model = CheckIn
        fields = ('id', 'player', 'tournament')


class MatchSerializers(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ('id', 'match_round', 'match_number', 
                'tournament', 'total_kills', 
                'position_points', 'winning_team')


class CommentSeializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'match', 'author', 'message', 'date')
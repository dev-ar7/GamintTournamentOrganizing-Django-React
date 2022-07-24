from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Team(models.Model):

    player_role = [
        ('IGL', 'In Game Leader'),
        ('ASSULTER', 'Assulter'),
        ('SYPPORTR', 'Supporter'),
        ('SNIPER', 'Sniper'),
        ('DMR', 'DMR'),
    ]

    team_name = models.CharField(max_length=250)
    player1 = models.CharField(max_length=250)
    player1_role = models.CharField(max_length=8, choices=player_role)
    player2 = models.CharField(max_length=250)
    player2_role = models.CharField(max_length=8, choices=player_role)
    player3 = models.CharField(max_length=250)
    player3_role = models.CharField(max_length=8, choices=player_role)
    player4 = models.CharField(max_length=250)
    player4_role = models.CharField(max_length=8, choices=player_role)
    player5 = models.CharField(max_length=250,blank=True, null=True) 
    player5_role = models.CharField(max_length=8, choices=player_role)


    def __str__(self):
        return self.team_name


class Tournament(models.Model):

    select_game = [
        ('BGMI', 'BGMI'),
        ('FREE FIRE', 'FREE FIRE'),
        ('CODM', 'CODM')
    ]

    tourni_type = [
        ('T', 'Tournament'),
        ('L', 'League'),
    ]

    name = models.CharField(max_length=255)
    game = models.CharField(max_length=10, choices=select_game)
    total_no_of_teams = models.PositiveBigIntegerField(default=0)
    no_of_team_players_allowed = models.PositiveBigIntegerField(default=4)
    type = models.CharField(max_length=1, choices=tourni_type)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} - {self.game} - {self.total_no_of_teams} - {self.type}'


class CheckIn(models.Model):

    player = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)


class Match(models.Model):

    match_round = models.CharField(max_length=50)
    match_number = models.PositiveBigIntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    total_kills = models.PositiveBigIntegerField(default=0)
    position_points = models.PositiveBigIntegerField(default=0)
    winning_team = models.ForeignKey(Team, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.match_round} - {self.match_number} - {self.winning_team}'


class Comment(models.Model):

    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=350)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.match} - {self.author} - {self.message}'

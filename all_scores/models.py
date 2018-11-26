# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from .fields import DateFromTimestampField
from django.conf import settings
from pytz import timezone
from datetime import datetime

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Division(models.Model):
    division_id = models.AutoField(primary_key=True)
    division_name = models.CharField(max_length=128)
    division_acronym = models.CharField(max_length=8)
    division_color = models.CharField(max_length=7)
    division_optimized = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'division'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    matchup = models.ForeignKey('Matchup', models.DO_NOTHING)
    slot = models.ForeignKey('Slot', models.DO_NOTHING, unique=True)
    game_completed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'game'


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=128)
    location_description = models.TextField()
    location_color = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'location'


class Matchup(models.Model):
    matchup_id = models.AutoField(primary_key=True)
    matchup_team1 = models.ForeignKey('Team', models.DO_NOTHING, related_name="team1")
    matchup_team2 = models.ForeignKey('Team', models.DO_NOTHING, related_name="team2")
    matchup_team1_score = models.IntegerField()
    matchup_team2_score = models.IntegerField()
    matchup_team1_timeouts = models.IntegerField()
    matchup_team2_timeouts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'matchup'


class Ranking(models.Model):
    ranking_id = models.AutoField(primary_key=True)
    team = models.ForeignKey('Team', models.DO_NOTHING, related_name="ranking_team")
    ranking_rank = models.IntegerField()
    ranking_round = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ranking'


class Scoreboardtext(models.Model):
    scoreboardtext_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, models.DO_NOTHING, related_name="scoreboard_location")
    scoreboardtext_text = models.TextField()
    scoreboardtext_start = models.IntegerField()
    scoreboardtext_end = models.IntegerField()
    scoreboardtext_color = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'scoreboardtext'


class Slot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    division = models.ForeignKey(Division, models.DO_NOTHING, related_name="slot_division")
    location = models.ForeignKey(Location, models.DO_NOTHING, related_name="slot_location")
    slot_start = models.IntegerField()
    slot_end = models.IntegerField()
    slot_round = models.IntegerField()

    def convert_time(self, i):
        "converts an int to a datetime object"
        result = datetime.fromtimestamp(i)
        result = result.replace(tzinfo=timezone(settings.TIME_ZONE))
        return result.strftime('%a %H:%M')

    @property
    def start_time(self):
        """Returns the slot's start time"""
        return self.convert_time(self.slot_start)

    @property
    def end_time(self):
        """Returns the slot's end time"""
        return self.convert_time(self.slot_end)


    class Meta:
        managed = False
        db_table = 'slot'


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    division = models.ForeignKey(Division, models.DO_NOTHING, related_name="team_division")
    team_name = models.CharField(max_length=128)
    team_acronym = models.CharField(max_length=8)
    team_color = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'team'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=32)
    user_password = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'user'

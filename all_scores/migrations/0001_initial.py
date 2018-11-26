# Generated by Django 2.1.3 on 2018-11-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('division_id', models.AutoField(primary_key=True, serialize=False)),
                ('division_name', models.CharField(max_length=128)),
                ('division_acronym', models.CharField(max_length=8)),
                ('division_color', models.CharField(max_length=7)),
                ('division_optimized', models.IntegerField()),
            ],
            options={
                'db_table': 'division',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_completed', models.IntegerField()),
            ],
            options={
                'db_table': 'game',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=128)),
                ('location_description', models.TextField()),
                ('location_color', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('matchup_id', models.AutoField(primary_key=True, serialize=False)),
                ('matchup_team1_score', models.IntegerField()),
                ('matchup_team2_score', models.IntegerField()),
                ('matchup_team1_timeouts', models.IntegerField()),
                ('matchup_team2_timeouts', models.IntegerField()),
            ],
            options={
                'db_table': 'matchup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('ranking_id', models.AutoField(primary_key=True, serialize=False)),
                ('ranking_rank', models.IntegerField()),
                ('ranking_round', models.IntegerField()),
            ],
            options={
                'db_table': 'ranking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Scoreboardtext',
            fields=[
                ('scoreboardtext_id', models.AutoField(primary_key=True, serialize=False)),
                ('scoreboardtext_text', models.TextField()),
                ('scoreboardtext_start', models.IntegerField()),
                ('scoreboardtext_end', models.IntegerField()),
                ('scoreboardtext_color', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'scoreboardtext',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('slot_start', models.IntegerField()),
                ('slot_end', models.IntegerField()),
                ('slot_round', models.IntegerField()),
            ],
            options={
                'db_table': 'slot',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=128)),
                ('team_acronym', models.CharField(max_length=8)),
                ('team_color', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=32)),
                ('user_password', models.CharField(max_length=1024)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
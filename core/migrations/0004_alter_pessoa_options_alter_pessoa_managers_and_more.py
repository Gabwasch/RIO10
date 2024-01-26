# Generated by Django 5.0.1 on 2024-01-26 11:04

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0003_pessoa_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pessoa',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='pessoa',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='senha',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='groups',
            field=models.ManyToManyField(related_name='pessoas', related_query_name='pessoa', to='auth.group'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='password',
            field=models.CharField(default=1, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='user_permissions',
            field=models.ManyToManyField(related_name='pessoas', related_query_name='pessoa', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nacionalidade',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]

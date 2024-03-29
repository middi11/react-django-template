# Generated by Django 5.0.1 on 2024-01-30 02:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('Role_id', models.AutoField(primary_key=True, serialize=False)),
                ('Role_name', models.CharField(max_length=1000)),
                ('Role_description', models.TextField(blank=True, default='N/A', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('User_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('Profile_picture', models.CharField(blank=True, max_length=1000, null=True)),
                ('First_name', models.CharField(default='N/A', max_length=1000)),
                ('Last_name', models.CharField(default='N/A', max_length=1000)),
                ('Date_of_birth', models.DateField(blank=True, null=True)),
                ('Address', models.CharField(default='N/A', max_length=1000)),
                ('Contact_number', models.CharField(default='N/A', max_length=1000)),
                ('Role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Account.role')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('User_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Account.userdetail')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Account.role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

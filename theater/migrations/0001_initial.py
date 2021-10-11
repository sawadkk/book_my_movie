# Generated by Django 3.1.2 on 2021-10-11 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.TextField()),
                ('poster_image', models.ImageField(blank=True, null=True, upload_to='thumbnails/')),
                ('summery', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.TextField(max_length=50)),
                ('seating_capacity', models.IntegerField()),
                ('entry_fee', models.IntegerField()),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('staus', models.CharField(blank=True, choices=[('Empty', 'empty'), ('Filling', 'filling'), ('Housefull', 'housefull'), ('Cancelled', 'cancelled')], max_length=300, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.movie')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.screen')),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='screen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.screen'),
        ),
    ]

# Generated by Django 2.2 on 2019-04-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('origin', models.ImageField(upload_to='photos/%y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('self_introduction', models.CharField(max_length=500)),
                ('sex', models.CharField(max_length=2)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('image', models.OneToOneField(on_delete=True, to='match.Image')),
            ],
        ),
    ]

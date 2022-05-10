# Generated by Django 3.2.8 on 2021-11-21 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_cumrap_phim'),
    ]

    operations = [
        migrations.CreateModel(
            name='NguoiDung',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('taiKhoan', models.CharField(max_length=20)),
                ('matKhau', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('soDt', models.PositiveIntegerField()),
                ('hoTen', models.CharField(max_length=50)),
            ],
        ),
    ]
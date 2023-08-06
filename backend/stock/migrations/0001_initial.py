# Generated by Django 4.1.4 on 2023-08-06 19:36

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
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(default='', max_length=10, null=True)),
                ('name', models.CharField(default='', max_length=255, null=True)),
                ('marketCap', models.DecimalField(decimal_places=5, default=0, max_digits=255, null=True)),
                ('exchange', models.CharField(default='', max_length=10, null=True)),
                ('postMarketChangePercent', models.DecimalField(decimal_places=5, default=0, max_digits=255, null=True)),
                ('regularMarketPrice', models.DecimalField(decimal_places=5, default=0, max_digits=255, null=True)),
                ('regularMarketChangePercent', models.DecimalField(decimal_places=5, default=0, max_digits=255, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

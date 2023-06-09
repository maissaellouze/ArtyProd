# Generated by Django 4.1.7 on 2023-05-14 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ArtyProd', '0007_remove_projet_utilisateur_personnel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=20)),
                ('additional_details', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArtyProd.projet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

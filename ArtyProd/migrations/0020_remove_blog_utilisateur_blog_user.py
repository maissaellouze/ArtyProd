# Generated by Django 4.1.7 on 2023-05-20 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ArtyProd', '0019_alter_blog_utilisateur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='utilisateur',
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.7 on 2023-05-13 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0003_detail_projet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='membres',
        ),
        migrations.AddField(
            model_name='personnel',
            name='Equipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ArtyProd.equipe'),
            preserve_default=False,
        ),
    ]

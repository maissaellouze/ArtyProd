# Generated by Django 4.1.7 on 2023-05-17 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0008_projetrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(default='Non définie')),
                ('statut', models.CharField(default='en_attente', max_length=20)),
                ('personne', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ArtyProd.personnel')),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArtyProd.projet')),
            ],
        ),
    ]

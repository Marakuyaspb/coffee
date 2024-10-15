# Generated by Django 5.1.1 on 2024-10-15 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallMe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заявка: перезвоните мне',
                'verbose_name_plural': 'Заявки: перезвоните мне',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='CallMeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('callme_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.callme')),
            ],
        ),
    ]
# Generated by Django 5.0.6 on 2024-05-15 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_books_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyRecomendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.TextField(max_length=255)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendation', to='books.books')),
            ],
        ),
    ]

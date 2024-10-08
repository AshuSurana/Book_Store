# Generated by Django 5.0.4 on 2024-05-16 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264)),
                ('author', models.CharField(max_length=264)),
                ('description', models.TextField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('publication_date', models.DateField()),
                ('cover_image', models.ImageField(upload_to='')),
            ],
        ),
    ]

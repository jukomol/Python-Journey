# Generated by Django 3.1.1 on 2020-09-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='catagory',
            field=models.CharField(default='', max_length=200),
        ),
    ]
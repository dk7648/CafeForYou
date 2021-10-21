# Generated by Django 3.2.8 on 2021-10-15 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0001_initial'),
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cafe',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='cafeapp.cafe'),
        ),
    ]

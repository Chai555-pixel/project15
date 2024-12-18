# Generated by Django 3.2.25 on 2024-12-18 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_auto_20241218_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compensation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='compensations',
            field=models.ManyToManyField(to='hr.Compensation'),
        ),
    ]
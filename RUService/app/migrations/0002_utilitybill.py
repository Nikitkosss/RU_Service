# Generated by Django 4.2.14 on 2024-07-23 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UtilityBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('calculation_date', models.DateTimeField(auto_now_add=True)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.apartment')),
            ],
        ),
    ]

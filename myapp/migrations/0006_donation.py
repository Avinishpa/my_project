# Generated by Django 4.1.7 on 2023-05-03 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('pay_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
                ('pay_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.blog')),
            ],
        ),
    ]
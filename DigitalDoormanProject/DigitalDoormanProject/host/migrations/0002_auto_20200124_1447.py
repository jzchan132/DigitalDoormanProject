# Generated by Django 3.0.2 on 2020-01-24 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_slug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qrID', models.IntegerField()),
                ('tokens', models.IntegerField()),
                ('inEvent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.Event', verbose_name='Events')),
            ],
        ),
    ]

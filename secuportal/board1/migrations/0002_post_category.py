# Generated by Django 5.0.6 on 2024-07-03 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('general', 'General'), ('temp1', '임시1'), ('temp2', '임시2'), ('temp3', '임시3'), ('temp4', '임시4')], default='general', max_length=50),
        ),
    ]

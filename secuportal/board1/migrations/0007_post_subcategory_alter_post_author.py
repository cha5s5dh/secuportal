# Generated by Django 5.0.6 on 2024-07-10 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board1', '0006_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subcategory',
            field=models.CharField(default='일반', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='임시 작성자', max_length=50),
        ),
    ]

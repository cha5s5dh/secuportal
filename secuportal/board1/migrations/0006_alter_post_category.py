# Generated by Django 5.0.6 on 2024-07-10 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board1', '0005_alter_post_author_alter_post_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]

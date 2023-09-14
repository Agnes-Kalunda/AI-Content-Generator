# Generated by Django 3.2.21 on 2023-09-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentGeneratorApp', '0002_blog_blogsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='audience',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='topic',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='keywords',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='wordCount',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]

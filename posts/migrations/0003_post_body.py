# Generated by Django 2.2.3 on 2019-07-06 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190706_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

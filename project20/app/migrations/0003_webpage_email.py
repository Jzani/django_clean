# Generated by Django 5.1.3 on 2025-02-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_accessrecord_topic_webpage_delete_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='hai@gmail.com', max_length=254),
        ),
    ]

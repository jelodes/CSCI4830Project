# Generated by Django 2.0.6 on 2018-07-18 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolpass', '0004_auto_20180718_0100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pass',
            name='student_ptr',
        ),
        migrations.RemoveField(
            model_name='pass',
            name='teacher_ptr',
        ),
        migrations.AddField(
            model_name='pass',
            name='id_pass',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]

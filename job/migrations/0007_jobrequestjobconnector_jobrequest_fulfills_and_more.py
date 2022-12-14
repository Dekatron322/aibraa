# Generated by Django 4.1 on 2022-08-19 18:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_remove_jobrequest_answer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobRequestJobConnector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
        ),
        migrations.AddField(
            model_name='jobrequest',
            name='fulfills',
            field=models.ManyToManyField(through='job.JobRequestJobConnector', to='job.job'),
        ),
        migrations.AddField(
            model_name='jobrequestjobconnector',
            name='job_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.jobrequest'),
        ),
    ]

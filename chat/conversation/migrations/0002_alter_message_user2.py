# Generated by Django 3.2.4 on 2021-06-28 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user2', to='conversation.profile'),
        ),
    ]
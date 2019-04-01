# Generated by Django 2.1.7 on 2019-04-01 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=200)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Party')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('name', 'admin_id')},
        ),
    ]

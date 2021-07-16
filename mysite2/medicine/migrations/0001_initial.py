# Generated by Django 3.1.2 on 2021-05-29 09:35

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='医薬品名')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日')),
                ('effect', models.TextField(blank=True, verbose_name='作用と効果')),
                ('caution', models.TextField(blank=True, verbose_name='使用上の注意')),
                ('dosage', models.TextField(blank=True, verbose_name='用法・用量')),
                ('side_effect', models.TextField(blank=True, verbose_name='副作用')),
            ],
            options={
                'db_table': 'medicine',
            },
        ),
    ]

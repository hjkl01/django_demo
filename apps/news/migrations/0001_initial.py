# Generated by Django 3.2.4 on 2022-08-29 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(db_index=True, unique=True)),
                ('website', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('title', models.TextField()),
                ('hot_score', models.IntegerField(default=0)),
                ('img_url', models.URLField(blank=True, null=True)),
                ('click_count', models.IntegerField(default=0)),
                ('if_sended', models.IntegerField(default=0, verbose_name='if sended')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now_add=True, verbose_name='date update')),
            ],
            options={
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
                'db_table': 'spider_news',
                'ordering': ['-created_time'],
            },
        ),
    ]

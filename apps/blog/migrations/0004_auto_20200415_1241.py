# Generated by Django 2.2.8 on 2020-04-15 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200414_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='icon',
            field=models.CharField(choices=[('fa fa-pencil', '笔标签'), ('fa fa-bell', '铃铛标签'), ('fa fa-diamond', '砖石标签'), ('fa fa-commenting-o', '评论标签'), ('fa fa-gavel', '工具标签'), ('fa fa-database', '数据库标签'), ('fa fa-music', '音乐标签'), ('fa fa-film', '音乐标签')], default='fa fa-pencil', max_length=50, verbose_name='图标'),
        ),
    ]

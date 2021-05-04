# Generated by Django 2.2 on 2021-05-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questionnaire02_app', '0001_initial'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Question',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('title', models.CharField(max_length=255, verbose_name='问卷标题')),
        #         ('choice_one', models.CharField(max_length=255, verbose_name='默认选择1（A）')),
        #         ('choice_two', models.CharField(max_length=255, verbose_name='默认选择2（B）')),
        #         ('choice_three', models.CharField(max_length=255, verbose_name='默认选择3（C）')),
        #         ('choice_four', models.CharField(max_length=255, verbose_name='默认选择4（D）')),
        #         ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
        #     ],
        #     options={
        #         'verbose_name': '调查问卷-题目设置（目前只单选）',
        #         'verbose_name_plural': '调查问卷-题目设置（目前只单选）',
        #     },
        # ),
        migrations.CreateModel(
            name='QuestionTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='问卷顶部大标题')),
                ('introduction', models.TextField(max_length=1024, verbose_name='问卷背景介绍')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '调查问卷-问卷背景介绍',
                'verbose_name_plural': '调查问卷-问卷背景介绍',
            },
        ),
    ]

# Generated by Django 2.2.16 on 2022-01-11 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodgram_app', '0016_auto_20220111_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodgram_app.Recipe')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodgram_app.Tag')),
            ],
        ),
    ]

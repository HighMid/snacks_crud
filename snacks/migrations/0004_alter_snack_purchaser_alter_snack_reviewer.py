# Generated by Django 5.0.2 on 2024-02-15 00:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0003_rename_title_snack_name_snack_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='purchaser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchased_snacks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='snack',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_snacks', to=settings.AUTH_USER_MODEL),
        ),
    ]

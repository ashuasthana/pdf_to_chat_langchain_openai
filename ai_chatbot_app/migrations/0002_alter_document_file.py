# Generated by Django 5.0.2 on 2024-02-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ai_chatbot_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="file",
            field=models.FileField(blank=True, upload_to="pdf_doc"),
        ),
    ]

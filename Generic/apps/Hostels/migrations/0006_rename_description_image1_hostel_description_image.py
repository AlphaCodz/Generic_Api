# Generated by Django 4.1.1 on 2023-02-16 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Hostels", "0005_hostel_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="hostel",
            old_name="description_image1",
            new_name="description_image",
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-20 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumbiniapp', '0003_alter_faq_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faqcategories',
            old_name='is_activate',
            new_name='is_active',
        ),
    ]

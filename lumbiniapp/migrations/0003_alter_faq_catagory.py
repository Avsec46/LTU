# Generated by Django 4.1.3 on 2022-12-20 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lumbiniapp', '0002_faqcategories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='catagory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lumbiniapp.faqcategories'),
        ),
    ]

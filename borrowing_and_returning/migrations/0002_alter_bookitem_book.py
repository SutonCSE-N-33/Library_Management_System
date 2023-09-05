# Generated by Django 4.2.4 on 2023-09-04 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_details_alter_book_isbn_and_more'),
        ('borrowing_and_returning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
    ]
# Generated by Django 4.1 on 2022-11-18 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_author_alter_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.borrower')),
            ],
        ),
        migrations.AddField(
            model_name='borrower',
            name='borrowed_books',
            field=models.ManyToManyField(through='library.Loan', to='library.book'),
        ),
    ]

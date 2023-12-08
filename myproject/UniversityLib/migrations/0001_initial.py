# Generated by Django 5.0 on 2023-12-08 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("inventory_number", models.CharField(max_length=100, unique=True)),
                ("author", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("Technical", "Technical"),
                            ("Art", "Art"),
                            ("Economic", "Economic"),
                        ],
                        max_length=50,
                    ),
                ),
                ("year", models.PositiveIntegerField()),
                ("pages", models.PositiveIntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "book_type",
                    models.CharField(
                        choices=[
                            ("Manual", "Manual"),
                            ("Book", "Book"),
                            ("Periodical", "Periodical"),
                        ],
                        max_length=50,
                    ),
                ),
                ("copies", models.PositiveIntegerField()),
                ("max_days", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Reader",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("card_number", models.CharField(max_length=100, unique=True)),
                ("last_name", models.CharField(max_length=100)),
                ("first_name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
                ("address", models.CharField(max_length=200)),
                (
                    "course",
                    models.IntegerField(
                        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4")]
                    ),
                ),
                ("group", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="BookIssue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("issue_code", models.CharField(max_length=100, unique=True)),
                ("issue_date", models.DateField()),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UniversityLib.book",
                    ),
                ),
                (
                    "reader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UniversityLib.reader",
                    ),
                ),
            ],
        ),
    ]
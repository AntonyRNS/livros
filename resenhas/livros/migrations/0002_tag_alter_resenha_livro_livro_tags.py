# Generated by Django 5.2.1 on 2025-05-21 23:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("livros", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("nome", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name="resenha",
            name="livro",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="resenhas",
                to="livros.livro",
            ),
        ),
        migrations.AddField(
            model_name="livro",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="livros", to="livros.tag"
            ),
        ),
    ]

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PageView",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("path", models.CharField(db_index=True, max_length=255)),
                ("timestamp", models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ("referrer", models.CharField(blank=True, max_length=500)),
                ("device", models.CharField(
                    choices=[("desktop", "Desktop"), ("mobile", "Mobile"), ("tablet", "Tablet")],
                    default="desktop",
                    max_length=10,
                )),
                ("ip_hash", models.CharField(blank=True, max_length=64)),
            ],
            options={
                "verbose_name": "page view",
                "verbose_name_plural": "page views",
                "ordering": ["-timestamp"],
            },
        ),
    ]

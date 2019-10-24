from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fuelest', '0003_auto_20190301_1856'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuoteHistory',
            new_name='Quote',
        ),
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

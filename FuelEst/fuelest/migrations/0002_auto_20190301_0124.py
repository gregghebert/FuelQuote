from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuelest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='quotehistory',
            name='gallons',
            field=models.IntegerField(),
        ),
    ]

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.IntegerField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gallons', models.IntegerField(max_length=10)),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('address', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='fuelest.Address')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='fuelest.Address')),
                ('username', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

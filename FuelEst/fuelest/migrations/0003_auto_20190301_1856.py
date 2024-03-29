from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fuelest', '0002_auto_20190301_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotehistory',
            name='user',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'),
                                            ('AR', 'Arkansas'), ('CA', 'California'), ('CO',
                                                                                       'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'),
                                            ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID',
                                                                                                     'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'),
                                            ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA',
                                                                                                   'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
                                            ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN',
                                                                                          'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'),
                                            ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH',
                                                                                                      'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'),
                                            ('NY', 'New York'), ('NC', 'North Carolina'), ('ND',
                                                                                           'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'),
                                            ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), (
                'SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'),
                ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.PositiveIntegerField(),
        ),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='nullable',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
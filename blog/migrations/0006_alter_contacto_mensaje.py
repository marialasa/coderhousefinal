from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_configcontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='mensaje',
            field=models.TextField(max_length=2000),
        ),
    ]

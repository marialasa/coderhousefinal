from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contacto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacto',
            new_name='Contact',
        ),
    ]

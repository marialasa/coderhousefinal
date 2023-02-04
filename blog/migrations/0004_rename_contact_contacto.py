from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_contacto_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Contacto',
        ),
    ]

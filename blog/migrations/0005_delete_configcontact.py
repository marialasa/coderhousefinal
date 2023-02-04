from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_contact_contacto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConfigContact',
        ),
    ]

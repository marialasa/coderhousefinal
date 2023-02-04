from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comentario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConfigAbout',
        ),
        migrations.DeleteModel(
            name='ConfigIndex',
        ),
    ]

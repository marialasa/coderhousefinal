from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_remove_comentario_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]

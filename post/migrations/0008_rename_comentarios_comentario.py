from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_remove_comentarios_activo_alter_comentarios_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comentarios',
            new_name='Comentario',
        ),
    ]

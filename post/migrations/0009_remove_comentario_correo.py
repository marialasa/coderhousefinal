from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_rename_comentarios_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='correo',
        ),
    ]

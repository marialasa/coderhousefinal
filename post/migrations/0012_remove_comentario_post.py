from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_remove_comentario_activo_alter_comentario_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='post',
        ),
    ]

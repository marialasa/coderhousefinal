from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_remove_comentario_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='activo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='post.post'),
        ),
    ]

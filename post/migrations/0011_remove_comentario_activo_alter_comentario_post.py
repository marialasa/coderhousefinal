from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_comentario_activo_alter_comentario_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='activo',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]

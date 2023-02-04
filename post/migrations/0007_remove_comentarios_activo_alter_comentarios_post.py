from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_comentarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='activo',
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]

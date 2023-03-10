from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=50)),
                ('mensaje', models.TextField(max_length=2000)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='post.post')),
            ],
        ),
    ]

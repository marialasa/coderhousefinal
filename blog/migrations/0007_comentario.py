from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_contacto_mensaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('mensaje', models.TextField(max_length=2000)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

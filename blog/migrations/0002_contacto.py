from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=50)),
                ('numero_telefono', models.CharField(max_length=20)),
                ('mensaje', models.TextField(default='sin descripcion', max_length=2000)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

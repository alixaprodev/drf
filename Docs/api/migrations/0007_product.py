# Generated by Django 4.2.7 on 2023-11-03 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_delete_mycategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('desciption', models.TextField(blank=True, max_length=200, null=True)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.category')),
            ],
        ),
    ]

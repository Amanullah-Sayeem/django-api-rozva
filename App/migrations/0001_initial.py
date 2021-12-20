# Generated by Django 3.2.7 on 2021-11-23 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('level', models.CharField(choices=[('top', 'Top'), ('medium', 'Medium'), ('normal', 'Normal')], max_length=200, null=True)),
                ('details', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('details', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=232)),
                ('brand', models.CharField(max_length=232)),
                ('size', models.CharField(max_length=232)),
            ],
        ),
        migrations.CreateModel(
            name='UsedFor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('details', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=244)),
                ('size', models.CharField(choices=[('XL', 'Extra Large'), ('L', 'Large'), ('M', 'Medium'), ('SM', 'Small'), ('XSM', 'Extra Small')], max_length=50)),
                ('quantity', models.CharField(max_length=244)),
                ('weight', models.CharField(max_length=244)),
                ('discount', models.IntegerField(help_text=' Entered value will be in %')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App.product', verbose_name='product_ID')),
            ],
        ),
        migrations.CreateModel(
            name='ImageLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/Images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.product')),
            ],
        ),
    ]

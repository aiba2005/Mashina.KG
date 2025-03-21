# Generated by Django 5.1.7 on 2025-03-11 07:11

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(65)])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make_name', models.CharField(max_length=34, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64, unique=True)),
                ('category_name_en', models.CharField(max_length=64, null=True, unique=True)),
                ('category_name_ru', models.CharField(max_length=64, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=34)),
                ('color_name_en', models.CharField(max_length=34, null=True)),
                ('color_name_ru', models.CharField(max_length=34, null=True)),
                ('color_image', models.FileField(upload_to='color_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('client_image', models.ImageField(upload_to='client_images/')),
                ('role', models.CharField(choices=[('client', 'client'), ('company', 'company')], default='client', max_length=32)),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
            },
            bases=('mashina.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=64)),
                ('company_name_en', models.CharField(max_length=64, null=True)),
                ('company_name_ru', models.CharField(max_length=64, null=True)),
                ('company_image', models.ImageField(upload_to='company_images/')),
                ('role', models.CharField(choices=[('client', 'client'), ('company', 'company')], default='compony', max_length=32)),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companies',
            },
            bases=('mashina.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=34, unique=True)),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_car', to='mashina.carmake')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('year', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='год')),
                ('carcass', models.CharField(choices=[('хэтчбек', 'хэтчбек'), ('внедорожник', 'внедорожник'), ('универсал', 'универсал'), ('минивэн', 'минивэн'), ('пикап', 'пикап')], max_length=64, verbose_name='кузов')),
                ('gear_box', models.CharField(choices=[('механика', 'механика'), ('автомат', 'автомат'), ('вариатор', 'вариатор'), ('робот', 'робот')], max_length=64, verbose_name='коробка')),
                ('drive', models.CharField(choices=[('передний', 'передний'), ('задний', 'задний'), ('полный', 'полный')], max_length=64, verbose_name='привод')),
                ('steering_wheel', models.CharField(choices=[('слева', 'слева'), ('справа', 'справа')], max_length=34, verbose_name='руль')),
                ('fuel', models.CharField(choices=[('бензин', 'бензин'), ('дизель', 'дизель'), ('бензин/газ', 'бензин/газ'), ('гибрид', 'гибрид'), ('электро', 'электро'), ('газ', 'газ')], max_length=34, verbose_name='топливо')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='mashina.carmake')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mashina.carmodel')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_car', to='mashina.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mashina.color')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mashina.client')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mashina.company')),
            ],
        ),
        migrations.CreateModel(
            name='CarPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_car', to='mashina.car')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mashina.cart')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mashina.car')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mashina.car')),
                ('favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mashina.favorite')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_name', models.CharField(max_length=32)),
                ('network_name_en', models.CharField(max_length=32, null=True)),
                ('network_name_ru', models.CharField(max_length=32, null=True)),
                ('network_Link', models.URLField()),
                ('title', models.CharField(blank=True, max_length=32, null=True)),
                ('title_en', models.CharField(blank=True, max_length=32, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=32, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_network', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

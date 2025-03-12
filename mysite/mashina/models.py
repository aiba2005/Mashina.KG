
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.exceptions import ValidationError

ROLE_CHOICES = (
    ('client', 'client'),
    ('company', 'company')

)

class User(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(65)], null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Network(models.Model):
    network_name = models.CharField(max_length=32)
    network_Link = models.URLField()
    title = models.CharField(max_length=32, null= True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_network')

    def __str__(self):
        return f'{self.user}, {self.network_name}'


class Client(User):
    client_image = models.ImageField(upload_to='client_images/')
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return f'{self.first_name}, {self.role}'

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'


class Company(User):
    company_name = models.CharField(max_length=64)
    company_image = models.ImageField(upload_to='company_images/')
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='compony')

    def __str__(self):
        return f'{self.company_name}, {self.role}'

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return f'{self.category_name}'


class Color(models.Model):
    color_name = models.CharField(max_length=34)
    color_image = models.FileField(upload_to='color_images/')


class CarMake(models.Model):
    make_name = models.CharField(max_length=34,unique=True)


class CarModel(models.Model):
    model_name = models.CharField(max_length=34, unique=True)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='model_car')


class Car(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name= 'car')
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_car')
    year = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='год')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    CARCASS_CHOICES = (
        ('хэтчбек', 'хэтчбек'),
        ('внедорожник', 'внедорожник'),
        ('универсал', 'универсал'),
        ('минивэн', 'минивэн'),
        ('пикап', 'пикап')

    )
    carcass = models.CharField(max_length=64, choices=CARCASS_CHOICES, verbose_name='кузов')
    GEAR_BOX_CHOICES = (
        ('механика', 'механика'),
        ('автомат', 'автомат'),
        ('вариатор', 'вариатор'),
        ('робот', 'робот'),
    )
    gear_box = models.CharField(max_length=64, choices=GEAR_BOX_CHOICES, verbose_name='коробка')
    DRIVE_CHOICES = (
        ('передний', 'передний'),
        ('задний', 'задний'),
        ('полный', 'полный'),
    )
    drive = models.CharField(max_length=64, choices=DRIVE_CHOICES, verbose_name='привод')
    STEERING_WHEEL_CHOICES = (
        ('слева', 'слева'),
        ('справа', 'справа'),
    )
    steering_wheel = models.CharField(max_length=34, choices=STEERING_WHEEL_CHOICES,verbose_name='руль')
    FUEL_CHOICES = (
        ('бензин', 'бензин'),
        ('дизель', 'дизель'),
        ('бензин/газ', 'бензин/газ'),
        ('гибрид', 'гибрид'),
        ('электро', 'электро'),
        ('газ', 'газ'),

    )
    fuel = models.CharField(max_length=34, choices=FUEL_CHOICES, verbose_name='топливо')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def clean(self):
        super().clean()
        if not self.client and not self.company :
            raise ValidationError('Choose minimum one of (client, company)!')


    def get_avg_review(self):
        total = self.reviews.all()
        if total.exists():
            return round(sum([i.stars for i in total]) / total.count(),1)
        return 0


    def get_count_people(self):
        people = self.reviews.all()
        if people.exists():
            return people.count()
        return 0




class CarPhoto(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name= 'image_car')
    image = models.ImageField(upload_to='car_images/')


class Rating(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    car_ratting = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 10)])
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)


    def clean(self):
        super().clean()
        if not self.client and not self.company :
            raise ValidationError('Choose minimum one of (client, company)!')



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_item')

    def __str__(self):
        return f'{self.cart}, {self.car}'

class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class FavoriteItem(models.Model):
    favorite= models.ForeignKey(Favorite, on_delete=models.CASCADE)
    course = models.ForeignKey(Car, on_delete=models.CASCADE)





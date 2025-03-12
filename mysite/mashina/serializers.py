from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'client_image', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Client.objects.create_user(**validated_data)
        return user


class ComponyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'company_name', 'company_image', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Company.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class NetworkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['network_name', 'network_Link', 'title']

class UserSerializer(serializers.ModelSerializer):
    user_network = NetworkUserSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['username']



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields =['username']


class CompanySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CarMakeCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = ['make_name',]


class CarModelCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['model_name']


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = ['image']


class CarSimpleSerializer(serializers.ModelSerializer):
    image_car = CarPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Car
        fields = ['id', 'image_car', 'price', 'year', 'gear_box', 'carcass', 'fuel', 'steering_wheel']




class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class CarListSerializer(serializers.ModelSerializer):
    car_make = CarMakeCarSerializer()
    car_model = CarModelCarSerializer()
    image_car = CarPhotoSerializer(many=True, read_only=True)
    get_avg_review = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = ['id', 'image_car', 'car_make', 'car_model', 'price', 'year', 'gear_box',
                  'carcass', 'fuel', 'steering_wheel', 'get_avg_review', 'get_count_people']

    def get_avg_review(self, obj):
        return obj.get_avg_review()

    def get_count_people(self, obj):
        return obj.get_count_people()



class CarMakeListSerializer(serializers.ModelSerializer):
    model_car= CarModelCarSerializer(many=True, read_only=True)
    car = CarSimpleSerializer(many=True, read_only=True)
    class Meta:
        model = CarMake
        fields = ['id', 'make_name', 'model_car', 'car']


class ColorCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name', 'color_image']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'



class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_car = CarListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'category_car']



class RatingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'



class RatingSerializer(serializers.ModelSerializer):
    created_date = serializers.DateField(format('%d-%m-%Y'))
    client = ClientSimpleSerializer()
    company = CompanySimpleSerializer()
    class Meta:
        model = Rating
        fields = ['client', 'company', 'stars', 'text', 'created_date']


class CarDetailSerializer(serializers.ModelSerializer):
    car_make = CarMakeCarSerializer()
    car_model = CarModelCarSerializer()
    color = ColorCarSerializer()
    reviews = RatingSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Car
        fields = ['client', 'company', 'car_make', 'car_model', 'price', 'year', 'gear_box', 'carcass', 'fuel',
                  'steering_wheel', 'color', 'description', 'reviews', 'created_at']


class CarDetailSimpleSerializer(serializers.ModelSerializer):
    color = ColorCarSerializer()

    class Meta:
        model = Car
        fields = ['client', 'company', 'price',  'year', 'gear_box', 'carcass', 'fuel',
                  'steering_wheel', 'color', 'description', 'created_at']


class CarMakeDetailSerializer(serializers.ModelSerializer):
    model_car= CarModelCarSerializer(many=True, read_only=True)
    car = CarDetailSimpleSerializer(many=True, read_only=True)
    class Meta:
        model = CarMake
        fields = ['make_name', 'model_car', 'car']



class CartItemSerializers(serializers.ModelSerializer):
    car_item = CarListSerializer(read_only=True)
    car_id = serializers.PrimaryKeyRelatedField(queryset = Car.objects.all(), write_only=True, source='car')

    class Meta:
        model = CartItem
        fields = ['id', 'car_item', 'car_id']


class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializers(many=True, read_only=True)
    get_total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields =['id', 'user', 'items', 'get_total_price']

        def get_total_price(self, obj):
            return obj.get_total_price()


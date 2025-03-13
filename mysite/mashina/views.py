from .serializers import *
from .models import *
from rest_framework import viewsets, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import CarFilter
from rest_framework_simplejwt.views import TokenObtainPairView
from  rest_framework.response import Response




class ClientRegisterView(generics.CreateAPIView):
    serializer_class = ClientUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class CompanyRegisterView(generics.CreateAPIView):
    serializer_class = ComponyUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserProfileView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CarMakeListAPIView(generics.ListAPIView):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['make_name']


class CarMakeDetailAPIView(generics.RetrieveAPIView):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeDetailSerializer


class CarOwnerAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer



class CarEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer


class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filters_class = [CarFilter]
    ordering_fields = ['price', 'year']


class CarCreateAPIView(generics.CreateAPIView):
    serializer_class = CarCreateSerializer


class CarDetailAPIView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartItemView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class FavoriteView(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class FavoriteItemView(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer



class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingCreateSerializer





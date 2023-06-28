
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Event, Registration, Venue, Category,User
from .serializers import UserSerializer, EventSerializer, RegistrationSerializer, VenueSerializer, CategorySerializer

 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Event.objects.all()
 
     
    def perform_create(self, serializer):
        user = self.request.user
        if isinstance(user, User):
            serializer.save(creator=user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.username==self.request.user:
            return Event.objects.filter(creator=user)
        else:
            return Event.objects.none()

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return  Registration.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
           return Registration.objects.filter( creator=user)
        else:
           return Registration.objects.none()


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

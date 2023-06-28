# from rest_framework import serializers
# from eventmodals.models import Event, Category

# # class CategorySerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Category
# #         fields = '__all__'

# class EventSerializer(serializers.ModelSerializer):
#       # Specify the serializer for the related field

#     class Meta:
#         model = Event
#         fields = '__all__'

from rest_framework import serializers
from .models import User, Event, Registration, Venue, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')  # Include additional fields as needed
    


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    # Field definitions and Meta class definition

    class Meta:
        model = Event
        fields = '__all__'

      
    # def perform_create(self, serializer):
    #     categories_data = self.request.data.get('categories', [])  # Retrieve categories data from the request
    #     event = serializer.save(creator=self.request.user)  # Assign the creator field with the authenticated user

    #     # Assign the categories to the event using the set() method
    #     event.categories.set(categories_data)

         
     
class RegistrationSerializer(serializers.ModelSerializer):
     
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    event = EventSerializer()

    class Meta:
        model = Registration
        fields = '__all__'



class RegistrationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
 

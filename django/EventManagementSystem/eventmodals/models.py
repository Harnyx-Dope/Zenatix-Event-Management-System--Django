# from django.db import models

# class Category(models.Model):
#     category_name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.category_name
# Category.objects.create(category_name='Comedy')
# Category.objects.create(category_name='Action')
# Category.objects.create(category_name='Romance')
# class Event(models.Model):
#     event_created_on = models.DateTimeField(auto_now=True)
#     event_title = models.CharField(max_length=50)
#     event_description = models.CharField(max_length=200)
#     event_date = models.DateField()
#     event_time = models.TimeField()
#     event_location = models.CharField(max_length=100)
#     event_capacity = models.PositiveIntegerField()
#     event_categories = models.CharField(max_length=100)

#     def __str__(self):
#         return self.event_title



#Participanst Models














#extra code
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class User(AbstractUser):
    # Add any additional fields or customizations to the User model if needed
    pass

    def __str__(self):
        return str(self.id)


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    categories = models.ManyToManyField('Category', related_name='events')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
     
    def __str__(self):
        return str(self.id)


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Venue(models.Model):
    # Add any additional fields specific to the Venue model
    capacity = models.PositiveIntegerField()
    amenities = models.TextField()
    availability = models.TextField()

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


User._meta.get_field('groups').remote_field.related_name = 'eventmodals_user_groups'
User._meta.get_field('groups').remote_field.related_query_name = 'eventmodals_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'eventmodals_user_permissions'
User._meta.get_field('user_permissions').remote_field.related_query_name = 'eventmodals_user_permissions'

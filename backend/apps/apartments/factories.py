import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model
from .models import Apartment


User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Sequence(lambda n: f"user{n}@example.com")
    is_verified = True
    auth_provider = "email"
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')



class ApartmentFactory(DjangoModelFactory):
    class Meta:
        model = Apartment

    name = factory.Sequence(lambda n: f"Apartment {n}")
    description = factory.Faker("paragraph", nb_sentences=3)
    price = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    number_of_rooms = factory.Faker("random_int", min=1, max=5)
    square = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)
    availability = factory.Faker("boolean")
    owner = factory.SubFactory(UserFactory)

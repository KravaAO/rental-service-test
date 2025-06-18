import random
from django.core.management.base import BaseCommand
from apps.apartments.factories import UserFactory, ApartmentFactory


class Command(BaseCommand):
    help = 'Seed test users and apartments'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=5, help='Кількість користувачів')
        parser.add_argument('--apartments', type=int, default=20, help='Кількість квартир')

    def handle(self, *args, **kwargs):
        users_count = kwargs['users']
        apartments_count = kwargs['apartments']

        self.stdout.write(f'Creating {users_count} users...')
        users = UserFactory.create_batch(users_count)

        self.stdout.write(f'Creating {apartments_count} apartments...')
        for _ in range(apartments_count):
            ApartmentFactory(owner=random.choice(users))

        self.stdout.write(self.style.SUCCESS(
            f'✅ Створено {users_count} користувачів та {apartments_count} квартир'
        ))

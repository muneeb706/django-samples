from django.core.management.base import BaseCommand
from test_dsh.models import TestA, TestB, TestC

class Command(BaseCommand):
    help = 'Creates 10 TestB instances using bulk_create_with_history and prints the number of queries executed'

    def handle(self, *args, **options):
        test_a = TestA.objects.create(name='TestA')  # Create a TestA instance to use as a foreign key

        # Create a TestB instance
        test_b = TestB.objects.create(name='TestB', test_a=test_a)

        # Create a TestC instance
        test_c = TestC.objects.create(id='dsfSERGserfseRFSREEDFEWdfawer34', test_b=test_b)
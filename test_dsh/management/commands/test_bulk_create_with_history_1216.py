from django.core.management.base import BaseCommand
from django.db import connection
from simple_history.utils import bulk_create_with_history

from test_dsh.models import TestA, TestB

class Command(BaseCommand):
    help = 'Creates 10 TestB instances using bulk_create_with_history and prints the number of queries executed'

    def handle(self, *args, **options):
        test_a = TestA.objects.create(name='TestA')  # Create a TestA instance to use as a foreign key

        new_instances = [TestB(name='name{}'.format(i), test_a=test_a) for i in range(10)]

        with connection.cursor() as cursor:
            # Reset the query count
            cursor.execute('SELECT 1')  # This query is needed to establish a connection and reset the query count
            initial_query_count = len(connection.queries)

            # Create the TestB instances and their historical records
            bulk_create_with_history(new_instances, TestB)

            final_query_count = len(connection.queries)
            print('Number of queries executed:', final_query_count - initial_query_count)

            # Print the SQL queries that were executed
            for query in connection.queries[initial_query_count:final_query_count]:
                print('Query:', query['sql'])
        
        # Delete all TestB instances and their historical records
        # TestB.objects.all().delete()
        # TestB.history.all().delete()
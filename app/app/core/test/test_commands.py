#

from unittest.mock import patch

from psycopg2 import OperationalError as Psycorpg2OpError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    
    def test_wait_for_db_ready(self,patched_check):
        #test database is ready
        patched_check.return_value = True
        
        call_command('wait_for_db')
        
        patched_check.assert_called_once_with(databases=['default'])
        
        
    @patch('time.sleep')
    def test_wait_for_db_delay(self,patched_sleep,patched_check):
        #test delay between attempts to connect to the db
        patched_check.side_effect = [Psycorpg2OpError] * 2 \
            [OperationalError] * 3  + [True]
        self.assertEqual(patched_check.call_count,6)
        patched_check.assert_called_with(database=['default'])

# import os
# import logging
# from django.test import TestCase
#
# class LoggingTestCase(TestCase):
#     def test_log_files_creation(self):
#         http_logs_path = os.path.join('logs', 'http_logs.log')
#         db_logs_path = os.path.join('logs', 'db_logs.log')
#         self.assertTrue(os.path.exists(http_logs_path))
#         self.assertTrue(os.path.exists(db_logs_path))
#
#     def test_logs_writing(self):
#         logger_http = logging.getLogger('django.request')
#         logger_db = logging.getLogger('django.db.backends')
#
#         logger_http.debug('Test HTTP log message')
#         logger_db.debug('Test DB log message')
#
#         with open(os.path.join('logs', 'http_logs.log'), 'r') as f:
#             http_logs_content = f.read()
#             self.assertIn('Test HTTP log message', http_logs_content)
#
#         with open(os.path.join('logs', 'db_logs.log'), 'r') as f:
#             db_logs_content = f.read()
#             self.assertIn


import os
import logging
from django.conf import settings
from django.test import TestCase

class LoggingTestCase(TestCase):
    def test_log_files_creation(self):
        http_logs_path = settings.LOGS_DIR / 'http_logs.log'
        db_logs_path = settings.LOGS_DIR / 'db_logs.log'

        self.assertTrue(os.path.exists(http_logs_path))
        self.assertTrue(os.path.exists(db_logs_path))

    def test_logs_writing(self):
        logger_http = logging.getLogger('django.request')
        logger_db = logging.getLogger('django.db.backends')

        logger_http.debug('Test HTTP log message')
        logger_db.debug('Test DB log message')

        with open(settings.LOGS_DIR / 'http_logs.log', 'r') as f:
            http_logs_content = f.read()
            self.assertIn('Test HTTP log message', http_logs_content)

        with open(settings.LOGS_DIR / 'db_logs.log', 'r') as f:
            db_logs_content = f.read()
            self.assertIn('Test DB log message', db_logs_content)



import unittest
from unittest.mock import patch, call
import subprocess
import re

from run import ping, traceroute, validate_domain

class TestNetworkTools(unittest.TestCase):

    def test_ping_success(self):
        with patch('subprocess.check_output') as mock_check_output:
            # Set up the mock to return a successful output
            mock_check_output.return_value = b'Ping successful'

            # Call the ping function
            ping('example.com')

            # Assert that subprocess.check_output was called with the correct arguments
            mock_check_output.assert_called_once_with(['ping', '-c', '4', 'example.com'])

    def test_ping_failure(self):
        with patch('subprocess.check_output') as mock_check_output:
            # Set up the mock to raise a CalledProcessError
            mock_check_output.side_effect = subprocess.CalledProcessError(1, 'ping')

            # Call the ping function
            with self.assertRaises(Exception) as cm:
                ping('example.com')

            # Assert the exception message
            self.assertEqual(str(cm.exception), "Ping to example.com failed: Command 'ping' returned non-zero exit status 1.")

    def test_traceroute_success(self):
        with patch('subprocess.check_output') as mock_check_output:
            # Set up the mock to return a successful output
            mock_check_output.return_value = b'Traceroute successful'

            # Call the traceroute function
            traceroute('example.com')

            # Assert that subprocess.check_output was called with the correct arguments
            mock_check_output.assert_called_once_with(['traceroute', 'example.com'])

    def test_traceroute_failure(self):
        with patch('subprocess.check_output') as mock_check_output:
            # Set up the mock to raise a CalledProcessError
            mock_check_output.side_effect = subprocess.CalledProcessError(1, 'traceroute')

            # Call the traceroute function
            with self.assertRaises(Exception) as cm:
                traceroute('example.com')

            # Assert the exception message
            self.assertEqual(str(cm.exception), "Traceroute to example.com failed: Command 'traceroute' returned non-zero exit status 1.")

    def test_validate_domain(self):
        # Test a valid domain
        self.assertTrue(validate_domain('example.com'))

        # Test an invalid domain
        self.assertFalse(validate_domain('invalid domain'))

if __name__ == '__main__':
    unittest.main()


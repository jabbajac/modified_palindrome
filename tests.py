import unittest
from click.testing import CliRunner
from modified_palindrome import isPalindrome


class TestModifiedPalindrom(unittest.TestCase):

    def test_simple_palindrome(self):
        """
        Setup the runner
        """
        runner = CliRunner()

        """
        Test a simple palindrome
        """
        result = runner.invoke(isPalindrome, ['-w', 'hooh'])
        self.assertEqual(result.output, "Is a palindrome\n")

    def test_simple_modified_palindrome(self):
        """
        Setup the runner
        """
        runner = CliRunner()

        """
        Test a modified palindrome
        """
        result = runner.invoke(isPalindrome, ['-w', 'h!o#oh'])
        self.assertEqual(result.output, "Is a palindrome\n")

    def test_billion_character_palindrome(self):
        """
        Setup the runner
        """
        runner = CliRunner()

        """
        Test a modified palindrome
        """
        string_to_test = 'a'*499999999 + 'b' + 'a'*499999999
        result = runner.invoke(isPalindrome, ['-w', string_to_test])
        self.assertEqual(result.output, "Is a palindrome\n")

    def test_simple_non_palindrome(self):
        """
        Setup the runner
        """
        runner = CliRunner()

        """
        Test a simple palindrome
        """
        result = runner.invoke(isPalindrome, ['-w', 'hoah'])
        self.assertEqual(result.output, "Not a palindrome\n")

    def test_simple_modified_non_palindrome(self):
        """
        Setup the runner
        """
        runner = CliRunner()

        """
        Test a modified palindrome
        """
        result = runner.invoke(isPalindrome, ['-w', 'a!o#oh'])
        self.assertEqual(result.output, "Not a palindrome\n")

    def test_billion_character_non_palindrome(self):
        """
        Setup the runner
        """
        runner = CliRunner()

        """
        Test a modified palindrome
        """
        string_to_test = 'a'*499999999 + 'b' + 'a'*499999999 + 'b'
        result = runner.invoke(isPalindrome, ['-w', string_to_test])
        self.assertEqual(result.output, "Not a palindrome\n")


if __name__ == '__main__':
    unittest.main()

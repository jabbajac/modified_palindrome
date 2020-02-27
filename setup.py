from setuptools import setup

setup(
    name='modified_palindrome',
    version='0.1',
    py_modules=['modified_palindrome'],
    scripts=['modified_palindrome.py'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        modified_palindrome = modified_palindrome:isPalindrome
    '''
)
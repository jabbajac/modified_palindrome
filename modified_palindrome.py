import click


@click.command()
@click.option('--word', '-w',
              help='Word you would like to check if it is a palindrome.')
def isPalindrome(word):
    reversed_word = [l for l in list(word.lower()) if l.isalnum()]
    word = ''.join(reversed_word)
    reversed_word.reverse()
    reversed_word = ''.join(reversed_word)
    if word == reversed_word:
        click.echo("Is a palindrome")
    else:
        click.echo("Not a palindrome")


if __name__ == '__main__':
    isPalindrome()

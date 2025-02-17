from sys import exit
from num2words import num2words
import decimal


def main() -> None:
    print('Welcome to The Number-to-Names Converter!')
    exit_message: str = 'Exiting program...'
    while True:
        try:
            user_input: str = input('Enter a number: ')

            if user_input == 'exit':
                print(exit_message)
                exit()

            print(num2words(user_input))

        except decimal.InvalidOperation:
            print('Please enter some valid input...')
            continue

        except KeyboardInterrupt:
            print(exit_message)
            exit()


if __name__ == '__main__':
    main()

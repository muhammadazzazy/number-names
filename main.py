from sys import exit
from num2words import num2words


def main() -> None:
    while True:
        try:
            user_input = input('Ente a number: ')

            if user_input == 'exit':
                print('Thanks for trying my program!')
                exit()
            print(num2words(user_input))

        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()

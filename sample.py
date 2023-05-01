#!/usr/bin/python
import os


def clear():
    """Clear the terminal screen (x-platform: Linux, Mac, Windows)."""
    os.system('clear') if os.name == 'posix' else os.system('cls')
# end of clear() definition.


def main():
    clear()
    print("Hello, Cruel World!")
# end of main() definition.


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nprocessing aborted by user. exiting...')
    finally:
        exit(0)

from app import pre_start, initial_data
import sys

def main() -> None:
    if sys.argv[1] == 'pre':
        pre_start.main()
    elif sys.argv[1] == 'init_db':
        initial_data.main()

if __name__ == "__main__":
    main()
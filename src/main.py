import argparse
import sys

def create_parser():
    """Создает и настраивает парсер аргументов командной строки."""
    parser = argparse.ArgumentParser(
        description="Инструмент визуализации графа зависимостей пакетов.")
    
    parser.add_argument(
        "--package",
        required=True,
        help="Имя анализируемого пакета."
    )
    
    parser.add_argument(
        "--repo",
        required=True,
        help="URL-адрес репозитория или путь к файлу тестового репозитория."
    )
    
    parser.add_argument(
        "--mode",
        required=True,
        help="Режим работы с тестовым репозиторием"
    )
    
    parser.add_argument(
        "--ascii",
        help="Режим вывода зависимостей в формате ASCII-дерева."
    )
    return parser

def validate_args(args):
    "Проверка корректности ввода аргуемнтов"
    if not args.package.strip():
        print("Имя пакета не может быть пустым.")
        sys.exit(1)

    if not args.repo.strip():
        print("Путь или URL репозитория не может быть пустым.")
        sys.exit(1)

def main():
    parser = create_parser()
    args = parser.parse_args()
    validate_args(args)

if __name__ == "__main__":
    main()
from config import habr_parser


if __name__ == '__main__':
    # Ключевые слова вписывать в нижнем регистре, чтобы избежать потери информации, вся информация по которой идет поиск
    # в статье приведена в нижний регистр
    keywords = ['дизайн', 'фото', 'web', 'python', 'php', 'it', 'машинное обучение']
    habr_parser(keywords)
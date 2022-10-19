import sys
from pathlib import Path

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")


images_suffix = ('JPEG', 'PNG', 'JPG', 'SVG')
documents_suffix = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
audio_suffix = ('MP3', 'OGG', 'WAV', 'AMR')
video_suffix = ('AVI', 'MP4', 'MOV', 'MKV')
archives_suffix = ('ZIP', 'GZ', 'TAR')


# p.name возвращает только имя(строкой) папки или файла, на который указывает p
# p.suffix возвращает строкой расширение файла, на который указывает p, начиная с точки
# p.exists() возвращает True или False, в зависимости от того, существует ли такой файл или папка
# p.is_dir() возвращает True, если p указывает на папку, и False, если на файл, или такой путь не существует
# p.is_file() возвращает True, если p указывает на файл, и False, если на папку, или такой путь не существует
# p.iterdir() возвращает итератор по всем файлам и папкам внутри папки p


def normalize(file_name):

    trans = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        trans[ord(c)] = l
        trans[ord(c.upper())] = l.upper()

    return file_name.translate(trans)


"""функция:
принимает на вход строку и возвращает строку;
проводит транслитерацию кириллических символов на латиницу;
заменяет все символы, кроме букв латинского алфавита и цифр, на символ '_';
транслитерация может не соответствовать стандарту, но быть читабельной;
большие буквы остаются большими, а меленькие — маленькими после транслитерации.
"""


def main():
    if len(sys.argv) < 2:
        return None
    else:
        dir_name = sys.argv[1]
        path = Path(dir_name)
        if path.exists() and path.is_dir():
            sort_dir(path)


def sort_dir(path):

    for p in path.iterdir():
        if p.is_dir():
            sort_dir(p)
        else:
            # обход всіх єлементів
            new_file_name = normalize(p.name)


if __name__ == '__main__':
    main()

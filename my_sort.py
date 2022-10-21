import sys
import re
from pathlib import Path
import shutil

IMAGES_SUFFIX = ('JPEG', 'PNG', 'JPG', 'SVG')
DOCUMENTS_SUFFIX = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
AUDIO_SUFFIX = ('MP3', 'OGG', 'WAV', 'AMR')
VIDEO_SUFFIX = ('AVI', 'MP4', 'MOV', 'MKV')
ARCHIVES_SUFFIX = ('ZIP', 'GZ', 'TAR')


def main():

    temp = 'C:/MyPyton/python-course/test1'
    # if len(sys.argv) < 2:
    if len(temp) < 2:
        print("Не вказано теку для обробки")
    else:
        # path = Path(sys.argv[1])
        path = Path(temp)
        if path.exists() and path.is_dir():
            print(f"Початок роботи {path.resolve()}")
            result = sort_dir(path)
            # TODO return {'result_list': result_list, 'to_do_suffix': to_do_suffix, 'unknown_suffix': unknown_suffix}
        else:
            print("Не вірна тека для обробки")


def normalize(in_string: str) -> str:
    """Replace cirilan symbils on latitians and change other to _ (except digit)

    Args:
        in_string (string):  need re module and use string translate
    """
    lation = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
              "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    trans = {}
    for c, l in zip("абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ", lation):
        trans[ord(c)] = l
        trans[ord(c.upper())] = l.upper()

    return re.sub(r'[^0-9a-zA-Z]', '_', in_string.translate(trans))


def sort_archives(file_path):
    print('0')
    # move file TODO


def move_file(file_path: Path, destany: str):
    Path(str(file_path.resolve().parent) + '\\' + destany.upper()
         ).mkdir(exist_ok=True, parents=True)

    shutil.move(str(file_path.resolve()), str(file_path.resolve().parent) + '\\' +
                destany.upper() + '\\' + normalize(file_path.stem) + file_path.suffix)


def sort_dir(path: Path):

    result_list = []
    to_do_suffix = []
    unknown_suffix = []

    for p in path.iterdir():
        if p.is_dir():
            new_dir_name = normalize(p.name)
            sort_dir(p)
            # rename p TODO
        else:
            if p.suffix.removeprefix('.').upper() in IMAGES_SUFFIX:
                move_file(p, 'images')
            elif p.suffix.removeprefix('.').upper() in DOCUMENTS_SUFFIX:
                move_file(p, 'documents')
            elif p.suffix.removeprefix('.').upper() in AUDIO_SUFFIX:
                move_file(p, 'audio')
            elif p.suffix.removeprefix('.').upper() in VIDEO_SUFFIX:
                move_file(p, 'video')
            elif p.suffix.removeprefix('.').upper() in ARCHIVES_SUFFIX:
                sort_archives(p)
            else:
                if not p.suffix in unknown_suffix:
                    unknown_suffix.append(p.suffix)

                # rename p TODO

    return {'result_list': result_list, 'to_do_suffix': to_do_suffix,
            'unknown_suffix': unknown_suffix}


if __name__ == '__main__':
    main()

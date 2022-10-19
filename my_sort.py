import sys
import re
from pathlib import Path
import shutil


images_suffix = ('JPEG', 'PNG', 'JPG', 'SVG')
documents_suffix = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
audio_suffix = ('MP3', 'OGG', 'WAV', 'AMR')
video_suffix = ('AVI', 'MP4', 'MOV', 'MKV')
archives_suffix = ('ZIP', 'GZ', 'TAR')


def main():

    if len(sys.argv) < 2:
        return None
    else:
        dir_name = sys.argv[1]
        path = Path(dir_name)
        if path.exists() and path.is_dir():
            sort_dir(path)


def normalize(in_string):
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
    # move file TODO


def sort_video(file_path):
    # move file TODO


def sort_audio(file_path):
    # move file TODO


def sort_images(file_path):
    # move file TODO


def sort_documents(file_path):
    # move file TODO


def sort_dir(path):
    for p in path.iterdir():
        if p.is_dir():
            new_dir_name = normalize(p.name)
            sort_dir(p)
            # rename p TODO
        else:
            new_file_name = normalize(p.name.removesuffix(p.suffix)) + p.suffix
            if p.suffix.removeprefix('.') in images_suffix:
                sort_images(p, new_file_name)
            elif p.suffix.removeprefix('.') in documents_suffix:
                sort_documents(p, new_file_name)
            elif p.suffix.removeprefix('.') in audio_suffix:
                sort_audio(p, new_file_name)
            elif p.suffix.removeprefix('.') in video_suffix:
                sort_video(p, new_file_name)
            elif p.suffix.removeprefix('.') in archives_suffix:
                sort_archives(p, new_file_name)
            else:
                # rename p TODO


if __name__ == '__main__':
    main()

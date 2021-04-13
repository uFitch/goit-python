import sys
import pathlib
images = []
audio = []
video = []
documents = []
other = []
archives = []
unknown = set()
extensions = set()
registered_extensions = {
    'JPEG': images,
    'PNG': images,
    'JPG': images,
    'SVG': images,
    'AVI': video,
    'MP4': video,
    'MOV': video,
    'MKV': video,
    'DOC': documents,
    'DOCX': documents,
    'TXT': documents,
    'XLSX': documents,
    'PPTX': documents,
    'PDF': documents,
    'MP3': audio,
    'OGG': audio,
    'WAV': audio,
    'AMR': audio,
    'ZIP': archives,
    'GZ': archives,
    'TAR': archives,
}
def get_extension(file_name: str) -> str:
    ext_start = 0
    for idx, char in enumerate(file_name):
        if char == ".":
            ext_start = idx
    return file_name[ext_start+1:].upper()
def scan(folder: pathlib.Path):
    for item in folder.iterdir():
        if item.is_dir():
            scan(item)
            continue
        extension = get_extension(file_name=item.name)
        if not extension:
            other.append(item.name)
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(item.name)
            except KeyError:
                unknown.add(extension)
                other.append(item.name)
if __name__ == "__main__":
    # Первый аргумент - считаем, что это валидный адрес в файловой сиситеме
    path = sys.argv[1]
    print(f"Start in {path}")
    # Список имен файлов и папок в path.
    arg = pathlib.Path(path)
    scan(arg)
    print(f"Images: {images}")
    print(f"Video files: {video}")
    print(f"Documents: {documents}")
    print(f"Audio files: {audio}")
    print(f"Unknown files: {other}")
    print(f"There are files of types: {extensions}")
    print(f"Unknown file types: {unknown}")

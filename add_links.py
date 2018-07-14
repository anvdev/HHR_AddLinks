import os


def add_links(directory):
    # Todo: сбор дополнительных файлов в архив
    for root, folders, files in os.walk(directory):
        for file in files:
            if file.endswith('txt'):
                asset_name = file.replace('.txt', '.otl')
                if os.path.exists(os.path.join(root, asset_name)):
                    with open(os.path.join(root, file), 'a', encoding='utf8') as f:
                        f.write(f'\n\n[Скачать пример|{asset_name}]')
                    continue
                asset_name = file.replace('.txt', '.hda')
                if os.path.exists(os.path.join(root, asset_name)):
                    with open(os.path.join(root, file), 'a', encoding='utf8') as f:
                        f.write(f'\n\n[Скачать пример|{asset_name}]')


if __name__ == '__main__':
    examples = r'S:\Houdini 16.5.525\houdini\help\examples'
    add_links(examples)

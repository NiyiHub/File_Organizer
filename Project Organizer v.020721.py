import os
import shutil


my_file = str(input('Enter file directory'))

for f in os.listdir(my_file):
    filename, file_ext = os.path.splitext(f)

    try:
        if not file_ext:
            pass

        elif file_ext in ('.dif', '.doc', '.docx', '.eps', '.exe', '.py', '.csv', '.ppt', '.pptx', '.pdf' , '.txt', '.wpd', '.wps', '.xls', '.xlsx'):
            shutil.move(
                os.path.join(my_file, f'{filename}{file_ext}'),
                os.path.join(my_file, 'Document Files', f'{filename}{file_ext}'))

        elif file_ext in ('.gif', '.jpeg', '.jpg', '.png', '.CR2', '.wepb'):
            shutil.move(
                os.path.join(my_file, f'{filename}{file_ext}'),
                os.path.join(my_file, 'Image Files', f'{filename}{file_ext}'))

        elif file_ext in ('.webm', '.mpg', '.mpeg', '.mpv', '.ogg', '.mkv', '.MP4', '.avi', '.mwv', '.mov', '.flv', '.avchd'):
            shutil.move(
                os.path.join(my_file, f'{filename}{file_ext}'),
                os.path.join(my_file, 'Movie Files', f'{filename}{file_ext}'))

        elif file_ext in ('.m4a', '.flac', '.mp3', '.wav', '.wma', '.aac'):
            shutil.move(
                os.path.join(my_file, f'{filename}{file_ext}'),
                os.path.join(my_file, 'Music Files', f'{filename}{file_ext}'))

        else:
            shutil.move(
                os.path.join(my_file, f'{filename}{file_ext}'),
                os.path.join(my_file, 'Others', f'{filename}{file_ext}'))
    except (FileNotFoundError, PermissionError):
        pass

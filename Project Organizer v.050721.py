import os
import shutil


my_file = os.getcwd()
other_file = str(input('Enter path'))

folder1 = 'Document Files'
path1 = os.path.join(my_file, folder1)
os.mkdir(path1)
path11 = os.path.join(other_file, folder1)
os.mkdir(path11)

folder2 = 'Image Files'
path2 = os.path.join(my_file, folder2)
os.mkdir(path2)
path22 = os.path.join(other_file, folder2)
os.mkdir(path22)

folder3 = 'Movie Files'
path3 = os.path.join(my_file, folder3)
os.mkdir(path3)
path33 = os.path.join(other_file, folder3)
os.mkdir(path33)

folder4 = 'Music Files'
path4 = os.path.join(my_file, folder4)
os.mkdir(path4)
path44 = os.path.join(other_file, folder4)
os.mkdir(path44)

folder5 = 'Others'
path5 = os.path.join(my_file, folder5)
os.mkdir(path5)
path55 = os.path.join(other_file, folder5)
os.mkdir(path55)


for f in os.listdir(my_file):
    filename, file_ext = os.path.splitext(f)

    try:
        if not file_ext:
            pass

        elif file_ext in ('.dif', '.doc', '.docx', '.eps', '.exe', '.py', '.csv', '.ppt', '.pptx', '.pdf' , '.txt', '.wpd', '.wps', '.xls', '.xlsx'):
            shutil.move(
                os.path.join(my_file, f'{filename}{file_ext}'),
                os.path.join(my_file, path1, f'{filename}{file_ext}'))

        elif file_ext in ('.gif', '.jpeg', '.jpg', '.png', '.CR2', '.wepb'):
            shutil.move(
                os.path.join(my_file, f'{filename}{file_ext}'),
                os.path.join(my_file, path2, f'{filename}{file_ext}'))

        elif file_ext in ('.webm', '.mpg', '.mpeg', '.mpv', '.ogg', '.mkv', '.MP4', '.avi', '.mwv', '.mov', '.flv', '.avchd'):
            shutil.move(
                os.path.join(my_file, f'{filename}{file_ext}'),
                os.path.join(my_file, path3, f'{filename}{file_ext}'))

        elif file_ext in ('.m4a', '.flac', '.mp3', '.wav', '.wma', '.aac'):
            shutil.move(
                os.path.join(my_file, f'{filename}{file_ext}'),
                os.path.join(my_file, path4, f'{filename}{file_ext}'))

        else:
            shutil.move(
                os.path.join(my_file, f'{filename}{file_ext}'),
                os.path.join(my_file, path5, f'{filename}{file_ext}'))

    except (FileNotFoundError, PermissionError, FileExistsError):
        pass


for f in os.listdir(other_file):
    filename, file_ext = os.path.splitext(f)

    try:
        if not file_ext:
            pass

        elif file_ext in ('.dif', '.doc', '.docx', '.eps', '.exe', '.py', '.csv', '.ppt', '.pptx', '.pdf', '.txt', '.wpd', '.wps', '.xls','.xlsx'):
            shutil.move(
                 os.path.join(other_file, f'{filename}{file_ext}'),
                 os.path.join(other_file, path11, f'{filename}{file_ext}'))

        elif file_ext in ('.gif', '.jpeg', '.jpg', '.png', '.CR2', '.wepb'):
            shutil.move(
                 os.path.join(other_file, f'{filename}{file_ext}'),
                 os.path.join(other_file, path22, f'{filename}{file_ext}'))

        elif file_ext in ('.webm', '.mpg', '.mpeg', '.mpv', '.ogg', '.mkv', '.MP4', '.avi', '.mwv', '.mov', '.flv', '.avchd'):
            shutil.move(
                os.path.join(other_file, f'{filename}{file_ext}'),
                os.path.join(other_file, path33, f'{filename}{file_ext}'))

        elif file_ext in ('.m4a', '.flac', '.mp3', '.wav', '.wma', '.aac'):
            shutil.move(
                os.path.join(other_file, f'{filename}{file_ext}'),
                os.path.join(other_file, path44, f'{filename}{file_ext}'))

        else:
            shutil.move(
                os.path.join(other_file, f'{filename}{file_ext}'),
                os.path.join(other_file, path55, f'{filename}{file_ext}'))

    except (FileNotFoundError, PermissionError, FileExistsError):
        pass

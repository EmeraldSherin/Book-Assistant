import os

def save_audio_file(file, folder="uploads"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    save_path = os.path.join(folder, file.filename)
    file.save(save_path)
    return save_path

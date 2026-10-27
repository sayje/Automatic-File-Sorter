import os, shutil

path = r"C:/Users/jyssa/Downloads/"

# Map each folder to the extensions that belong in it
categories = {
    "image files": (".png", ".jpg", ".jpeg", ".mp4"),
    "documents": (".pdf"),
    "application": (".exe"),
}

# Create the folders if they don't exist
for folder in categories:
    os.makedirs(os.path.join(path, folder), exist_ok=True)

# Move the files
for file in os.listdir(path):
    source = os.path.join(path, file)

    # Skip folders
    if not os.path.isfile(source):
        continue

    for folder, extensions in categories.items():
        if file.lower().endswith(extensions):
            destination = os.path.join(path, folder, file)
            if not os.path.exists(destination):
                shutil.move(source, destination)
            break


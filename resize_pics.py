import cv2
import os



folder = "pics"


for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    # Skip non-image files
    if not (filename.lower().endswith((".png", ".jpg", ".jpeg"))):
        continue

    img = cv2.imread(filepath)
    if img is None:
        continue  # Skip unreadable files

    resized = cv2.resize(img, (130, 130))
    cv2.imwrite(filepath, resized)

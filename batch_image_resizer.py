import cv2
import os
import glob

# Enter full path of where the images are stored
path = ""
# Enter the name of the folder you would like to contain the resized images - this will be created within the source folder
target_dir = "resized-images"

# Access location of images
os.chdir(path)

# Create directory for new images
try:
    os.mkdir(target_dir)
except OSError as e:
    pass


img_counter = 0

# TODO: Handle multiple file types
for original_img_name in glob.glob('*.jpg'): # Change the file type as appropriate
    img = cv2.imread("{}{}".format(path, original_img_name), 0)
    resized_img = cv2.resize(img, (100, 100)) # Enter settings for the manipulation
    os.chdir("{}{}/".format(path, target_dir))
    cv2.imwrite('[RESIZED]_{}'.format(original_img_name), resized_img)
    os.chdir(path)
    img_counter += 1

print("{} images processed".format(img_counter))

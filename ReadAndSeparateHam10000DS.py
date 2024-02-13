import pandas as pd
import os
import shutil

skin_df = pd.read_csv('metadata.csv')

# Define data and destination directories
data_dir = os.path.join(os.getcwd(), "ISIC-images")
dest_dir = os.path.join(os.getcwd(), "final_data")

# Get image labels
labels = skin_df['diagnosis'].unique().tolist()

# Create a list to store copied images
copied_images = []

# Iterate through labels
for label in labels:
    os.makedirs(os.path.join(dest_dir, label), exist_ok=True)  # Create subfolder if needed

    # Filter images for current label
    label_images = skin_df[skin_df['diagnosis'] == label]['isic_id'].tolist()

    # Iterate through images and copy them
    for image_id in label_images:
        source_file = os.path.join(data_dir, image_id + ".jpg")
        dest_file = os.path.join(dest_dir, label, image_id + ".jpg")

        try:
            shutil.copyfile(source_file, dest_file)
            copied_images.append(image_id)  # Track copied images for later use
        except FileNotFoundError:
            print(f"Error: Image file '{source_file}' not found.")

    print(f"Copied {len(copied_images)} images for label '{label}'.")

    # Clear list for next iteration
    copied_images = []

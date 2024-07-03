from PIL import Image
import os


def collect_images_to_tiff(folder_names, output_tif, base_path="Для тестового"):
    """Collect images from a directory and save them as a tif file.
    :param output_tif:
    :param folder_names:
    :param base_path:
    """

    #  List for save all images
    all_images = []

    for folder_path in folder_names:
        folder_path = os.path.join(base_path, folder_path)
        if not os.path.isdir(folder_path):
            print(f'{folder_path} does not exist, skipping.')
            continue

        image_files = [f for f in os.listdir(folder_path)
                       if f.endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff', '.bmp'))]

        images = [Image.open(os.path.join(folder_path, f)) for f in image_files]
        all_images.extend(images)

    #  Save images to tiff
    if all_images:
        all_images[0].save(output_tif, save_all=True, append_images=all_images[1:])
        folder_names_str = ', '.join(folder_names)
        print(f'Images from folders {folder_names_str} have been saved to {output_tif}')
    else:
        print(f'No images found to save.')

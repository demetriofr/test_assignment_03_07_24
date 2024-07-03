from utils import collect_images_to_tiff


def main():
    """Start the application."""

    #  Path to the images
    folder_names = ['1369_12_Наклейки 3-D_3',
                    '1388_2_Наклейки 3-D_1',
                    '1388_6_Наклейки 3-D_2',
                    '1388_12_Наклейки 3-D_3']

    #  Output file
    output_tif = 'Result.tif'

    collect_images_to_tiff(folder_names=folder_names, output_tif=output_tif)


if __name__ == '__main__':
    main()

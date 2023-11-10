import argparse


def get_input_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('--dir', default='pet_images',
                        help="path to image directory")
    parser.add_argument('--arch', default='vgg', help="CNN Model Architecture")
    parser.add_argument('--dogfile', default='dognames.txt',
                        help="Text file with dog names")

    return parser.parse_args()

# Uncomment the lines below for testing
# args = get_input_args()
# print(args.dir)
# print(args.arch)
# print(args.dogfile)

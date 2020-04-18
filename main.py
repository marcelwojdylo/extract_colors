import sys, argparse
from extract_colors import extract_colors


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=str, help='Set relative path for input image')
    parser.add_argument('--n', type=int, help='Set number of colors to be returned')
    args = parser.parse_args()
    image_path = args.f
    number_of_colors = args.n
    colors = extract_colors(image_path, number_of_colors)
    print(colors)
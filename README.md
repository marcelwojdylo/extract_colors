# extract_colors
A simple module for extracting dominant colors from an image. Color clusters are determined using k-means clustering through KMeans from the `scikit-learn` package.

```
usage: main.py [-h] [--f F] [--n N]

optional arguments:
  -h, --help  show this help message and exit
  --f F       Set relative path for input image
  --n N       Set number of colors to be returned
  ```
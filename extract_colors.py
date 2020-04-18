from sklearn.cluster import KMeans
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
import sys
import matplotlib.pyplot as plt


def rgb_to_hex(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_percentages(occurrences: []):
    total = sum(occurrences)
    percentages = []
    for value in occurrences:
        percentages.append(value/total*100)
    return percentages

def extract_colors(image_path: str, number_of_colors: int):
    # Load image with OpenCV
    image = cv2.imread(image_path)
    # Convert image array to RGB from OpenCV's default BGR
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Reshape 3-dimensional image array to 2 dimensions expected by KMeans
    image = image.reshape(image.shape[0]*image.shape[1], image.shape[2])
    # Set up KMeans for given number of clusters
    kmeans = KMeans(n_clusters = number_of_colors)
    # Run KMeans to get cluster labels for image
    labels = kmeans.fit_predict(image)
    # Use Counter to count occurrences of labels
    label_counts = Counter(labels)
    # Get center colors for each cluster
    center_colors = kmeans.cluster_centers_
    # Order colors by number of occurrences
    ordered_colors = [center_colors[i] for i in label_counts.keys()]
    # Convert colors to hexadecimal values, ordered by number of occurrences
    hex_colors = [rgb_to_hex(center_colors[i]) for i in label_counts.keys()]
    # Get sorted list of numbers of occurrences for colors
    sorted_occurrences = sorted(list(label_counts.values()), reverse=True)
    sorted_percentages = get_percentages(sorted_occurrences)

    # Uncomment to display pie chart of colors
    # plt.figure(figsize=(8, 6))
    # plt.pie(sorted_occurrences, labels=hex_colors, colors=hex_colors)
    # plt.show()

    color_summary = {}
    for i in range(number_of_colors):
        color_summary[hex_colors[i]] = {'percentage': sorted_percentages[i], 'occurrences':sorted_occurrences[i]}

    # print(f"Color summary:\n{color_summary}")
    return color_summary

# -*- coding: utf-8 -*-
"""ImageAnalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a6PsjtVk6DoUMPBV0GfRj6Y_5S8gR1C6
"""

import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from ipywidgets import widgets
from IPython.display import display, clear_output

def upload_image():
    upload_widget = widgets.FileUpload(accept='image/*', multiple=False)
    display(upload_widget)

    def on_upload_change(change):
        clear_output(wait=True)
        for filename, fileinfo in upload_widget.value.items():
            image_data = np.frombuffer(fileinfo['content'], np.uint8)
            image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            display_image(image_rgb)
            analyze_image(image_rgb)

    upload_widget.observe(on_upload_change, names='value')

def display_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(image)
    plt.axis('off')
    plt.title("Uploaded Image")
    plt.show()

def analyze_image(image):
    print(f"📏 **Image Dimensions:** {image.shape[0]}x{image.shape[1]} (Height x Width)")
    print(f"📊 **Number of Color Channels:** {image.shape[2]}")
    print(f"🖼️ **Total Pixels:** {image.size}")

    colors = ('Red', 'Green', 'Blue')
    plt.figure(figsize=(10, 5))
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color.lower(), label=f"{color} Channel")
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    avg_intensity = np.mean(gray_image)
    print(f"🔅 **Average Intensity (Grayscale):** {avg_intensity:.2f}")

    edges = cv2.Canny(gray_image, 100, 200)
    plt.figure(figsize=(6, 6))
    plt.imshow(edges, cmap='gray')
    plt.axis('off')
    plt.title("Edge Detection (Canny)")
    plt.show()

display(widgets.HTML("<h2>📂 Upload an Image for Analysis</h2>"))
upload_image()



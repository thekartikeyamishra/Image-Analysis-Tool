# **Image Analysis Tool**

## **Project Overview**

This **Image Analysis Tool** is an interactive Python-based application designed to analyze uploaded images. It provides insights such as image dimensions, color channel distribution, pixel intensity, and edge detection. The tool also includes visualizations like histograms and edge maps, making it an excellent choice for educational and prototyping purposes. The project runs seamlessly in **Google Colab**.

---

## **Features**

### 🖼️ **Image Upload**
- Interactive widget for uploading images directly in Google Colab.
- Accepts common image formats such as PNG, JPG, and JPEG.

### 📏 **Basic Image Analysis**
- Dimensions: Displays the height and width of the image.
- Number of Color Channels: Identifies the channels (e.g., RGB has 3 channels).
- Total Pixels: Calculates the total number of pixels in the image.

### 📊 **Color Histogram**
- Plots the pixel intensity distribution for Red, Green, and Blue channels.

### 🔅 **Grayscale Analysis**
- Converts the image to grayscale and calculates the average pixel intensity.

### 🖍️ **Edge Detection**
- Uses the **Canny Edge Detection** algorithm to highlight edges in the image.
- Visualizes edges with a grayscale edge map.

---

## **Installation Instructions**

### 1. Install Required Libraries
Run the following command to install the required Python libraries:
```bash
!pip install opencv-python-headless matplotlib pillow
```

### 2. Copy the Code
Copy the script into a **Google Colab** notebook.

---

## **How to Use**

1. **Run the Code**:
   - Paste the code into a Google Colab notebook and run it.

2. **Upload an Image**:
   - Use the interactive widget to upload an image file.

3. **Analyze the Image**:
   - The tool will automatically display the uploaded image, analyze its properties, and generate visualizations.

4. **View Results**:
   - Results are displayed in the notebook, including image properties, histograms, and edge detection output.

---

## **Code Walkthrough**

### 1. **Image Upload**
The `upload_image` function uses an interactive widget to allow users to upload images:
```python
upload_widget = widgets.FileUpload(accept='image/*', multiple=False)
```

### 2. **Image Display**
The `display_image` function renders the uploaded image:
```python
plt.imshow(image)
plt.axis('off')
plt.title("Uploaded Image")
```

### 3. **Basic Analysis**
The `analyze_image` function calculates and prints:
- Dimensions (`image.shape[0]` for height, `image.shape[1]` for width).
- Number of color channels (`image.shape[2]`).
- Total pixels (`image.size`).

### 4. **Color Histogram**
A histogram is plotted for each color channel (Red, Green, Blue):
```python
hist = cv2.calcHist([image], [i], None, [256], [0, 256])
plt.plot(hist, color=color.lower(), label=f"{color} Channel")
```

### 5. **Grayscale Intensity**
The image is converted to grayscale, and the average intensity is calculated:
```python
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
avg_intensity = np.mean(gray_image)
```

### 6. **Edge Detection**
The **Canny Edge Detection** algorithm highlights edges in the image:
```python
edges = cv2.Canny(gray_image, 100, 200)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection (Canny)")
```

---

## **Example Output**

### Input:
An uploaded image (e.g., `example.jpg`).

### Output:
1. **Image Properties**:
   ```
   📏 Image Dimensions: 512x512 (Height x Width)
   📊 Number of Color Channels: 3
   🖼️ Total Pixels: 786,432
   ```

2. **Color Histogram**:
   - A chart showing the pixel intensity distribution for Red, Green, and Blue channels.

3. **Grayscale Analysis**:
   ```
   🔅 Average Intensity (Grayscale): 120.45
   ```

4. **Edge Detection**:
   - A grayscale edge map highlighting the edges in the image.

---

## **Applications**

### 1. **Educational Tool**
- Demonstrates key image processing techniques such as histograms and edge detection.

### 2. **Prototyping**
- Serves as a quick prototype for image analysis workflows.

### 3. **Exploration**
- Helps users understand the properties and structure of digital images.

---

## **Potential Enhancements**

1. **Advanced Filters**:
   - Add options for image blurring, sharpening, and thresholding.

2. **ROI Analysis**:
   - Allow users to select and analyze specific regions of the image.

3. **Batch Analysis**:
   - Support the analysis of multiple images at once.

4. **Feature Detection**:
   - Add functionality for detecting shapes, objects, or faces.

5. **Image Comparison**:
   - Enable comparison of two images side-by-side for differences or similarities.

---

## **Contribute**

Contributions are welcome! Here's how you can contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature: feature-name"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## **Support**

If you find this project helpful:
- ⭐ Star the repository on GitHub.
- 🗣️ Share it with others.

---

Let me know if you'd like further refinements or additional sections! 🚀

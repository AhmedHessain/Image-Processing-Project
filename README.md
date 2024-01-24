# PyQt5 Image Processing Project

This is a Python application built using PyQt5 for image processing tasks. The application provides a graphical user interface (GUI) to perform various image operations, including histogram equalization, segmentation, and filtering.

## Features

### 1. Image Display and Selection
- Load and display images from a specified folder.
- Select images from a dropdown ComboBox.
- Display both original and processed images.

### 2. Histogram Operations
- Calculate and display histograms for RGB and grayscale images.
- Apply histogram equalization to enhance image contrast.
- Display original and processed histograms in a bar chart.

### 3. Segmentation
- Perform manual segmentation with a user-defined threshold.
- Implement automatic segmentation using Otsu's method.

### 4. Filters
- Apply a box filter with a user-selectable kernel size.
- Apply minimum filter (erosion) for noise reduction.
- Implement edge detection using Sobel and Canny filters.
- Apply Laplacian filter for detecting edges.

### 5. Transmission Time Calculation
- Estimate transmission time based on user-defined baud rate and channel type.
- Dynamically update the estimated time based on user inputs.

### 6. Progress Bar
- Show a progress bar during time-consuming operations.
- Utilize a separate thread to prevent GUI freezing.

## Getting Started

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**
    ```bash
    python your_application_file.py
    ```

## Usage

- Launch the application and use the GUI to perform various image processing tasks.
- Select an image from the dropdown menu and apply different operations using the provided buttons.
- View histograms, segmentation results, and filtered images in real-time.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import *
import math
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import convolve2d
from PIL import Image
from progress_thread import ProgressThread
from scipy import ndimage
import cv2
from skimage import feature



# Subclass QMainWindow to customize your application's main window
class UI(QMainWindow):
    chosen_image = None
    active_image = None
    original_hist_image_chart = ''
    result_hist_image_chart = ''
    original_hist = [[], [], []]
    applied_hist = [[], [], []]
    ui_path = os.path.dirname(os.path.abspath(__file__))

    # defite the constructor

    def __init__(self):
        super(UI, self).__init__()
        mainLayout = QVBoxLayout()
        full_path = os.path.join(self.ui_path, "image_processing.ui")
        uic.loadUi(f"{full_path}", self)

        ##Define Elements
        ##Histogram
        self.image_selection_combobox = self.findChild(QComboBox, "image_selection_combobox")
        self.unprocessed_image = self.findChild(QLabel, "Image")
        self.select_image_button = self.findChild(QPushButton, "select_image_button")
        self.histogram_image_chart = self.findChild(QLabel, "histogram_image_chart")
        self.original_histogram_image_button = self.findChild(QPushButton, "original_histogram_image_button")
        self.result_histogram_image_button = self.findChild(QPushButton, "result_histogram_image_button")
        self.result_image = self.findChild(QLabel, "result_image")
        self.apply_histogram_button = self.findChild(QPushButton, "apply_histogram_button")
        self.display_both_histogram_results_button = self.findChild(QPushButton,
                                                                    "display_both_histogram_results_button")

        ##Segmantation
        self.apply_manual_segmentation_button = self.findChild(QPushButton, "apply_manual_segmentation_button")
        self.apply_automatic_segmentation_button = self.findChild(QPushButton, "apply_automatic_segmentation_button")
        self.manual_segmentation_spinbox = self.findChild(QSpinBox, "manual_segmentation_spinbox")
        self.auto_segmentation_line_edit = self.findChild(QLineEdit, "auto_segmentation_line_edit")
        self.progress = self.findChild(QProgressBar, "progress_bar")

        self.checkBox = self.findChild(QCheckBox, "checkBox")

        self.edge_detection_combobox=self.findChild(QComboBox,"comboBox_4")
        self.Kernel_combobox=self.findChild(QComboBox,"comboBox")

        ##time transmission
        self.baudrate_spinbox = self.findChild(QSpinBox, "baudrate_spinbox")
        self.time_line_edit = self.findChild(QLineEdit, "time_line_edit")
        self.channels_combobox = self.findChild(QComboBox, "channels_combobox")

        ##Connect Elements with Events
        self.image_selection_combobox.activated.connect(self.image_selection_combobox_item_selected)
        self.select_image_button.clicked.connect(self.select_image_button_clicked)
        self.original_histogram_image_button.clicked.connect(self.original_histogram_image_button_clicked)
        self.result_histogram_image_button.clicked.connect(self.result_histogram_image_button_clicked)
        self.apply_histogram_button.clicked.connect(self.apply_histogram_button_clicked)
        self.display_both_histogram_results_button.clicked.connect(self.display_both_histogram_results_button_clicked)

        ##segementation
        self.apply_manual_segmentation_button.clicked.connect(
            lambda: self.startProgress(self.apply_manual_segmentation_button_clicked))
        self.apply_automatic_segmentation_button.clicked.connect(
            lambda: self.startProgress(self.apply_automatic_segmentation))

        ##min filter
        self.non_linear_filter_button = self.findChild(QPushButton, "non_linear_apply")
        self.non_linear_filter_button.clicked.connect(self.apply_min_filter)


        ##box filter
        self.non_linear_Bfilter_button = self.findChild(QPushButton, "pushButton_12")
        self.non_linear_Bfilter_button.clicked.connect(self.apply_box_filter)

        #edge detection
        self.edge_detect_filter_button = self.findChild(QPushButton, "edge_detec_apply")
        self.edge_detect_filter_button.clicked.connect(self.apply_edge_detection)

        #Laplacian
        self.Laplace = self.findChild(QPushButton, "pushButton_11")
        self.Laplace.clicked.connect(self.apply_Laplacina)

        ##time transmission
        self.baudrate_spinbox.valueChanged.connect(self.calc_transmission_time)
        self.channels_combobox.activated.connect(lambda: self.calc_transmission_time(self.baudrate_spinbox.value()))
        self.channels_combobox.addItem("RGB")
        self.progress.hide()
        self.Load_Images_To_Combobox()
        self.setLayout(mainLayout)
        self.showMaximized()

    ##define Events
    def image_selection_combobox_item_selected(self):
        self.chosen_image = self.image_selection_combobox.currentText()

    def select_image_button_clicked(self):
        if self.chosen_image != None:
            self.Display_Image(self.chosen_image)
            self.active_image = self.chosen_image
            self.result_histogram_image_button.setEnabled(False)
            self.display_both_histogram_results_button.setEnabled(False)
            self.original_hist_image_chart = ''
            self.result_hist_image_chart = ''
            self.result_image.clear()
            self.histogram_image_chart.clear()
            self.original_hist = [[], [], []]
            self.applied_hist = [[], [], []]
            self.calc_histogram()
            self.display_hist_chart()

    ##test
    def box_filter_rgb(self, image, kernel_size):

        height, width, channels = image.shape
        padding = kernel_size // 2
        kernel = np.ones((kernel_size, kernel_size, channels), dtype=np.float32) / (kernel_size ** 2)
        output = np.zeros((height, width, channels), dtype=np.uint8)

        # Add padding to the image
        padded_image = np.pad(image, ((padding, padding), (padding, padding), (0, 0)), mode='edge')

        # Apply the filter to each pixel
        for y in range(padding, height + padding):
            for x in range(padding, width + padding):
                window = padded_image[y - padding:y + padding + 1, x - padding:x + padding + 1]
                output[y - padding, x - padding] = np.sum(window * kernel, axis=(0, 1))

        return output

    def apply_box_filter(self, kernel_size=3):
        if self.Kernel_combobox.currentIndex() == 0:
            kernel_size = 3
        else:
            kernel_size = 5
        full_path = os.path.join(self.ui_path, f"Images/{self.active_image}")
        img = plt.imread(full_path)

        filtered_image = self.box_filter_rgb(img, kernel_size)

        qimage = QImage(filtered_image, filtered_image.shape[1], filtered_image.shape[0],
                        QImage.Format_RGB888)

        pixmap = QPixmap(qimage)
        self.result_image.setPixmap(pixmap)


    ##edge detection Event 
    def apply_edge_detection(self):
        if(self.edge_detection_combobox.currentIndex() == 0):
            self.apply_sobel_filter()
        elif(self.edge_detection_combobox.currentIndex() == 1):
            self.apply_Canny()

    ##Start Segmentation
    def apply_manual_segmentation_button_clicked(self):
        threshold = int(self.manual_segmentation_spinbox.text())

        full_path = os.path.join(self.ui_path, f"Images/{self.active_image}")
        img = plt.imread(full_path)

        img = self.RGB_to_Gray(img)
        height, width = img.shape

        segmented_img = np.zeros_like(img)

        for row in range(height):
            for col in range(width):
                pixel = img[row, col]
                if pixel > threshold:
                    segmented_img[row, col] = 255
                else:
                    segmented_img[row, col] = 0

        gray_img = segmented_img
        qimage = QImage(gray_img, gray_img.shape[1], gray_img.shape[0], gray_img.shape[1] * 1, QImage.Format_Grayscale8)

        pixmap = QPixmap(qimage)
        self.result_image.setPixmap(pixmap)

        self.result_histogram_image_button.setEnabled(False)
        self.display_both_histogram_results_button.setEnabled(False)

    def apply_automatic_segmentation(self):
        full_path = os.path.join(self.ui_path, f"Images/{self.active_image}")
        img = plt.imread(full_path)

        img = self.RGB_to_Gray(img)
        height, width = img.shape

        threshold = self.automatic_thresholding(img)

        self.progress_bar_end_behavior = lambda: self.output_threshold(threshold)

        segmented_img = np.zeros_like(img)

        for row in range(height):
            for col in range(width):
                pixel = img[row, col]
                if pixel > threshold:
                    segmented_img[row, col] = 255
                else:
                    segmented_img[row, col] = 0

        qimage = QImage(segmented_img, segmented_img.shape[1], segmented_img.shape[0], segmented_img.shape[1] * 1,
                        QImage.Format_Grayscale8)

        pixmap = QPixmap(qimage)
        self.result_image.setPixmap(pixmap)

        self.result_histogram_image_button.setEnabled(False)
        self.display_both_histogram_results_button.setEnabled(False)

    def output_threshold(self, threshold):
        self.auto_segmentation_line_edit.setText(str(threshold))

    ##End Segmentation

    def original_histogram_image_button_clicked(self):
        self.histogram_image_chart.setPixmap(self.original_histogram_image_chart)

    def result_histogram_image_button_clicked(self):
        self.histogram_image_chart.setPixmap(self.result_hist_image_chart)

    def apply_histogram_button_clicked(self):
        full_path = os.path.join(self.ui_path, f"Images/{self.active_image}")
        img = plt.imread(full_path)

        height, width, channels = img.shape

        hist_red = self.original_hist[0]
        hist_green = self.original_hist[1]
        hist_blue = self.original_hist[2]

        cdf_red = np.cumsum(hist_red)
        cdf_green = np.cumsum(hist_green)
        cdf_blue = np.cumsum(hist_blue)

        cdf_norm_red = (cdf_red - np.min(cdf_red)) / (height * width - np.min(cdf_red))
        cdf_norm_green = (cdf_green - np.min(cdf_green)) / (height * width - np.min(cdf_green))
        cdf_norm_blue = (cdf_blue - np.min(cdf_blue)) / (height * width - np.min(cdf_blue))

        lookup_table_red = np.round(255 * cdf_norm_red).astype('uint8')
        lookup_table_green = np.round(255 * cdf_norm_green).astype('uint8')
        lookup_table_blue = np.round(255 * cdf_norm_blue).astype('uint8')

        img_eq = np.zeros_like(img)

        for row in range(height):
            for col in range(width):
                red, green, blue = img[row, col]

                output_red = lookup_table_red[int(red)]
                output_green = lookup_table_green[int(green)]
                output_blue = lookup_table_blue[int(blue)]

                img_eq[row, col, 0] = output_red
                img_eq[row, col, 1] = output_green
                img_eq[row, col, 2] = output_blue
        plt.close()
        qimage = QImage(img_eq, img_eq.shape[1], img_eq.shape[0], width * channels, QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        self.result_image.setPixmap(pixmap)
        self.calc_histogram(img_eq)
        self.display_hist_chart(False)
        self.result_histogram_image_button.setEnabled(True)
        self.display_both_histogram_results_button.setEnabled(True)

    def display_both_histogram_results_button_clicked(self):
        hist1 = (self.original_hist[0] + self.original_hist[1] + self.original_hist[2]) / 3
        hist2 = (self.applied_hist[0] + self.applied_hist[1] + self.applied_hist[2]) / 3
        fig, ax = plt.subplots(2)
        ax[0].bar(range(256), hist1)
        ax[1].bar(range(256), hist2)
        fig.tight_layout(pad=0)
        ax[0].margins(0)
        ax[1].margins(0)
        fig.canvas.draw()
        image_from_plot = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        image_from_plot = image_from_plot.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        qimage = QImage(image_from_plot, image_from_plot.shape[1], image_from_plot.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        self.histogram_image_chart.setPixmap(pixmap)
        plt.close()

    ##Start Progress Bar Methods
    def startProgress(self, process):
        self.progress.show()
        self.thread = ProgressThread(process)
        self.thread.progress_update.connect(self.updateProgressBar)
        self.thread.start()

    def updateProgressBar(self, val):
        if val >= 100:
            if self.progress_bar_end_behavior is not None:
                self.progress_bar_end_behavior()
                self.progress_bar_end_behavior = None
            self.progress.hide()
        self.progress.setValue(val)

    ##End Progress Bar Methods

    ##define other Methods
    def Display_Image(self, image):
        full_path = os.path.join(self.ui_path, f"Images/{image}")
        pixmap = QPixmap(full_path)
        self.unprocessed_image.setPixmap(pixmap)

    def Load_Images_To_Combobox(self):
        full_path = os.path.join(self.ui_path, "Images")
        ext = ('.jpg', '.png', 'jpeg')
        for files in os.listdir(full_path):
            if files.endswith(ext):
                self.image_selection_combobox.addItem(files)
            else:
                continue
        self.chosen_image = self.image_selection_combobox.itemText(0)
        self.select_image_button_clicked()

    def laplacian_filter(self ,image):
        #"""Applies a Laplacian filter to an RGB image."""
        kernel = np.array([
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0]
        ])
        height,width,  channels = image.shape
        padding = kernel.shape[0] // 2
        output = np.zeros((height, width, channels), dtype=np.uint8)

        # Add padding to the image
        padded_image = np.pad(image, ((padding, padding), (padding, padding), (0, 0)), mode='edge')

        # Apply the filter to each pixel in each channel
        for y in range(padding, height + padding):
            for x in range(padding, width + padding):
                window = padded_image[y - padding:y + padding + 1, x - padding:x + padding + 1, :]
                output[y - padding, x - padding, :] = np.sum(window * kernel.reshape(3, 3, 1), axis=(0, 1))

        return output

    def minimum_filter(self, image, kernel_size):
        # Convert the image to a NumPy array
        image_array = np.array(image)

        # Pad the image with zeros to handle the edges of the image
        padding = kernel_size // 2
        padded_image_array = np.pad(image_array, ((padding, padding), (padding, padding), (0, 0)), mode='constant')

        # Create an empty output array
        output_array = np.zeros_like(image_array)

        # Apply the min filter to each pixel in the image
        for i in range(image_array.shape[0]):
            for j in range(image_array.shape[1]):
                for k in range(image_array.shape[2]):
                    output_array[i, j, k] = np.min(padded_image_array[i:i + kernel_size, j:j + kernel_size, k])

        return output_array

    def apply_Laplacina(self ,image):
        if self.checkBox.isChecked():
            # Load the input image
            full_path = os.path.join(self.ui_path, f"Images/{self.active_image}")
            img = plt.imread(full_path)

            # Apply the Laplacian filter to the image
            filtered_image = self.laplacian_filter(img)

            # Convert the filtered image to a QImage
            qimage = QImage(filtered_image, filtered_image.shape[1], filtered_image.shape[0], QImage.Format_RGB888)

            # Create a QPixmap from the QImage and display it in the GUI
            pixmap = QPixmap(qimage)
            self.result_image.setPixmap(pixmap)

    def apply_min_filter(self):
        if self.Kernel_combobox.currentIndex() == 0:
            kernel_size = 3
        else:
            kernel_size = 5

        full_path = os.path.join(self.ui_path, f"Images/{self.active_image}")
        img = plt.imread(full_path)

        filtered_image = self.minimum_filter(img, kernel_size)

        qimage = QImage(filtered_image, filtered_image.shape[1], filtered_image.shape[0],
                        QImage.Format_RGB888)

        pixmap = QPixmap(qimage)
        self.result_image.setPixmap(pixmap)

    def sobel_filter(self, img):
        # Convert the image to grayscale
        gray = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

        # Apply the Sobel filter in the x direction
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        filtered_x = convolve2d(gray, sobel_x, mode="same")

        # Apply the Sobel filter in the y direction
        sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        filtered_y = convolve2d(gray, sobel_y, mode="same")

        # Combine the x and y filtered images to get the final result
        filtered_image = np.sqrt(filtered_x ** 2 + filtered_y ** 2)

        # Normalize the filtered image to values between 0 and 1
        filtered_image = filtered_image / np.max(filtered_image)

        # Convert the filtered image back to the original data type
        filtered_image = (filtered_image * 255).astype(np.uint8)

        # Convert the filtered image to RGB for display
        filtered_image = np.stack((filtered_image,) * 3, axis=-1)

        return filtered_image

    def canny_filter(self,img, sigma=1.0, low_threshold=0.1, high_threshold=0.2):
        # Convert to grayscale
        gray = np.dot(img[...,:3], [0.299, 0.587, 0.114])

        # Apply Gaussian smoothing
        sigma = 1.4
        size = 2 * math.ceil(3 * sigma) + 1
        x, y = np.meshgrid(np.linspace(-1, 1, size), np.linspace(-1, 1, size))
        gaussian_kernel = np.exp(-((x**2 + y**2)/(2 * sigma**2)))
        gaussian_kernel = gaussian_kernel / np.sum(gaussian_kernel)
        smoothed = np.zeros_like(gray, dtype=float)
        smoothed[:,:] = gray
        for i in range(size//2, gray.shape[0]-size//2):
            for j in range(size//2, gray.shape[1]-size//2):
                window = gray[i-size//2:i+size//2+1, j-size//2:j+size//2+1]
                smoothed[i, j] = np.sum(window * gaussian_kernel)

        # Calculate gradients
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        gx = np.zeros_like(smoothed)
        gy = np.zeros_like(smoothed)
        for i in range(1, smoothed.shape[0]-1):
            for j in range(1, smoothed.shape[1]-1):
                window = smoothed[i-1:i+2, j-1:j+2]
                gx[i,j] = np.sum(window * sobel_x)
                gy[i,j] = np.sum(window * sobel_y)
        gradient_magnitude = np.sqrt(gx**2 + gy**2)
        gradient_direction = np.arctan2(gy, gx)

        # Non-maximum suppression
        suppressed = np.zeros_like(gradient_magnitude)
        for i in range(1, gradient_magnitude.shape[0]-1):
            for j in range(1, gradient_magnitude.shape[1]-1):
                angle = gradient_direction[i, j] * 180 / np.pi
                if angle < 0:
                    angle += 180
                if (angle >= 0 and angle < 22.5) or (angle >= 157.5 and angle <= 180):
                    before_pixel = gradient_magnitude[i, j-1]
                    after_pixel = gradient_magnitude[i, j+1]
                elif (angle >= 22.5 and angle < 67.5):
                    before_pixel = gradient_magnitude[i-1, j-1]
                    after_pixel = gradient_magnitude[i+1, j+1]
                elif (angle >= 67.5 and angle < 112.5):
                    before_pixel = gradient_magnitude[i-1, j]
                    after_pixel = gradient_magnitude[i+1, j]
                else:
                    before_pixel = gradient_magnitude[i-1, j+1]
                    after_pixel = gradient_magnitude[i+1, j-1]
                if gradient_magnitude[i, j] >= before_pixel and gradient_magnitude[i, j] >= after_pixel:
                    suppressed[i, j] = gradient_magnitude[i, j]

        # Double thresholding
        threshold_low = 0.2
        threshold_high = 0.4
        strong_edges = (suppressed > threshold_high)
        weak_edges = (suppressed >= threshold_low) & (suppressed <= threshold_high)

        # Edge tracking by hysteresis
        edges = np.zeros_like(strong_edges, dtype=float)
        for i in range(1, edges.shape[0]-1):
            for j in range(1, edges.shape[1]-1):
                if strong_edges[i, j]:
                    edges[i, j] = 1.0
                elif weak_edges[i, j]:
                    neighborhood = edges[i-1:i+2, j-1:j+2]
                    if np.max(neighborhood) == 1:
                        edges[i, j] = 1.0

        # Convert to RGB
        canny_array = np.zeros_like(img)
        canny_array[:,:,0] = edges * img[:,:,0]
        canny_array[:,:,1] = edges * img[:,:,1]
        canny_array[:,:,2] = edges * img[:,:,2]
        return canny_array

    def apply_Canny(self):
        full_path = os.path.join(self.ui_path, f"Images/{self.active_image}")
        img = plt.imread(full_path)

        filtered_image = self.canny_filter(img)

        qimage = QImage(filtered_image, filtered_image.shape[1], filtered_image.shape[0],
                        QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        self.result_image.setPixmap(pixmap)

    def apply_sobel_filter(self):
        full_path = os.path.join(self.ui_path, f"Images/{self.active_image}")
        img = plt.imread(full_path)

        filtered_image = self.sobel_filter(img)

        qimage = QImage(filtered_image, filtered_image.shape[1], filtered_image.shape[0],
                        QImage.Format_RGB888)

        pixmap = QPixmap(qimage)
        self.result_image.setPixmap(pixmap)

    def calc_histogram(self, image=None):
        if image is None:
            full_path = os.path.join(self.ui_path, f"Images/{self.active_image}")
            img = plt.imread(full_path)
        else:
            img = image

        height, width, channels = img.shape

        hist_red = np.zeros((256,))
        hist_green = np.zeros((256,))
        hist_blue = np.zeros((256,))

        for row in range(height):
            for col in range(width):
                red, green, blue = img[row, col]
                hist_red[int(red)] += 1
                hist_green[int(green)] += 1
                hist_blue[int(blue)] += 1

        if image is None:
            self.original_hist[0] = hist_red
            self.original_hist[1] = hist_green
            self.original_hist[2] = hist_blue
        else:
            self.applied_hist[0] = hist_red
            self.applied_hist[1] = hist_green
            self.applied_hist[2] = hist_blue

    def display_hist_chart(self, is_original=True):
        if is_original:
            hist = (self.original_hist[0] + self.original_hist[1] + self.original_hist[2]) / 3
        else:
            hist = (self.applied_hist[0] + self.applied_hist[1] + self.applied_hist[2]) / 3
        fig, ax = plt.subplots()
        ax.bar(range(256), hist)
        fig.tight_layout(pad=0)
        ax.margins(0)
        fig.canvas.draw()
        image_from_plot = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        image_from_plot = image_from_plot.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        qimage = QImage(image_from_plot, image_from_plot.shape[1], image_from_plot.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        plt.close()
        if is_original:
            self.original_histogram_image_chart = pixmap
            self.original_histogram_image_button_clicked()
        else:
            self.result_hist_image_chart = pixmap
            self.result_histogram_image_button_clicked()

    ##Segmentation Preferal Methods
    def automatic_thresholding(self, image):
        """
        I'm using Otsu's Method here i know that my code might be enhanced a little bit
        in terms of performance but really it would be great if we are allowed to use opencv's built-in thresholding"""
        height, width = image.shape
        totalPixels = width * height
        hist = self.calc_histogram_grayscale(image)
        list_of_thresholds = list()
        for i in range(256):
            n = hist[i]
            # background variables
            b_bars_height_count = 0
            b_bars_height_by_pixel_count = 0
            w_b = 0
            m_b = 0

            # Foreground Variables
            f_bars_height_count = 0
            f_bars_height_by_pixel_count = 0
            w_f = 0
            m_f = 0

            # Background
            for j in range(i):
                b_bars_height_count += hist[j]
                b_bars_height_by_pixel_count += hist[j] * j

            if (i != 0):
                w_b = (b_bars_height_count / totalPixels)
                m_b = (b_bars_height_by_pixel_count / b_bars_height_count)

            # Foreground
            for j in range(i, 256):
                f_bars_height_count += hist[j]
                f_bars_height_by_pixel_count += hist[j] * j

            if (i != 255):
                w_f = (f_bars_height_count / totalPixels)
                m_f = (f_bars_height_by_pixel_count / f_bars_height_count)

            threshold = (w_b * w_f * ((m_b - m_f) ** 2))
            list_of_thresholds.append(threshold)

        max = 0
        for k in range(256):
            if (list_of_thresholds[k] > list_of_thresholds[max]):
                max = k

        threshold_value = int(max)
        return threshold_value

    def calc_histogram_grayscale(self, image):
        """
        Calculates the histogram of a grayscale image
        Parameters ==> image: grayscale image as a numpy array
        """
        height, width = image.shape
        hist = np.zeros((256,), dtype=np.int32)
        for row in range(height):
            for col in range(width):
                hist[int(image[row, col])] += 1
        return hist

    def RGB_to_Gray(self, img):
        height, width, channels = img.shape
        result_img = np.zeros((height, width), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                red, green, blue = img[i, j]
                gray = 0.299 * int(red) + 0.587 * int(green) + 0.114 * int(blue)
                result_img[i, j] = gray
        return result_img

    def calc_transmission_time(self, value):
        full_path = os.path.join(self.ui_path, f"Images/{self.active_image}")
        img = plt.imread(full_path)
        time = 0
        height, width, channels = img.shape
        if (value != 0):
            if (self.channels_combobox.currentIndex() == 0):
                time = (width * height * 10) / (value * 1000)
            else:
                time = (width * height * 30) / (value * 1000)
        self.time_line_edit.setText(str(time))


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_processing.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(2452, 857)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 1))
        Form.setStyleSheet(u"background-color:#333333;\n"
"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1931, 851))
        self.widget.setAutoFillBackground(False)
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 35))
        self.label_23.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"color:white;\n"
"border:none;\n"
"background-color:transparent;\n"
"")
        self.label_23.setTextFormat(Qt.PlainText)
        self.label_23.setIndent(-1)

        self.verticalLayout_7.addWidget(self.label_23)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setKerning(True)
        self.frame.setFont(font1)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color:#393939;\n"
"border-radius:10px;\n"
"border:1px solid grey;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_12)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setMaximumSize(QSize(120, 16777215))
        font2 = QFont()
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color:white;\n"
"border:none")
        self.label.setTextFormat(Qt.PlainText)

        self.horizontalLayout.addWidget(self.label)

        self.manual_segmentation_spinbox = QSpinBox(self.frame)
        self.manual_segmentation_spinbox.setObjectName(u"manual_segmentation_spinbox")
        self.manual_segmentation_spinbox.setMinimumSize(QSize(600, 0))
        self.manual_segmentation_spinbox.setMaximumSize(QSize(600, 16777215))
        self.manual_segmentation_spinbox.setStyleSheet(u"#manual_segmentation_spinbox{\n"
"border:transparent;\n"
"color:white;\n"
"font-size:26px;\n"
"background-color:#292929;\n"
"}\n"
"#manual_segmentation_spinbox:hover{\n"
"border:1px solid pink;\n"
"}")
        self.manual_segmentation_spinbox.setAlignment(Qt.AlignCenter)
        self.manual_segmentation_spinbox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.manual_segmentation_spinbox.setMaximum(255)

        self.horizontalLayout.addWidget(self.manual_segmentation_spinbox)

        self.apply_manual_segmentation_button = QPushButton(self.frame)
        self.apply_manual_segmentation_button.setObjectName(u"apply_manual_segmentation_button")
        self.apply_manual_segmentation_button.setMinimumSize(QSize(111, 0))
        self.apply_manual_segmentation_button.setMaximumSize(QSize(111, 16777215))
        self.apply_manual_segmentation_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.apply_manual_segmentation_button.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"background-color:#6B6B6B;\n"
"border-radius:8px")

        self.horizontalLayout.addWidget(self.apply_manual_segmentation_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setMaximumSize(QSize(120, 16777215))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_2.setTextFormat(Qt.PlainText)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.auto_segmentation_line_edit = QLineEdit(self.frame)
        self.auto_segmentation_line_edit.setObjectName(u"auto_segmentation_line_edit")
        self.auto_segmentation_line_edit.setMinimumSize(QSize(600, 0))
        self.auto_segmentation_line_edit.setMaximumSize(QSize(600, 16777215))
        font3 = QFont()
        font3.setPointSize(11)
        self.auto_segmentation_line_edit.setFont(font3)
        self.auto_segmentation_line_edit.setStyleSheet(u"#auto_segmentation_line_edit{\n"
"background-color:#292929;\n"
"border:transparent;\n"
"color:white;}\n"
"#auto_segmentation_line_edit:hover{\n"
"border:1px solid pink;\n"
"}")
        self.auto_segmentation_line_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.auto_segmentation_line_edit)

        self.apply_automatic_segmentation_button = QPushButton(self.frame)
        self.apply_automatic_segmentation_button.setObjectName(u"apply_automatic_segmentation_button")
        self.apply_automatic_segmentation_button.setMinimumSize(QSize(111, 0))
        self.apply_automatic_segmentation_button.setMaximumSize(QSize(111, 16777215))
        self.apply_automatic_segmentation_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.apply_automatic_segmentation_button.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"background-color:#6B6B6B;\n"
"border-radius:8px")

        self.horizontalLayout_2.addWidget(self.apply_automatic_segmentation_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addWidget(self.frame)

        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 35))
        self.label_24.setMaximumSize(QSize(16777215, 35))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"color:white;\n"
"border:none;\n"
"background-color:transparent")
        self.label_24.setTextFormat(Qt.PlainText)

        self.verticalLayout_7.addWidget(self.label_24)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QSize(0, 65))
        self.frame_2.setMaximumSize(QSize(16777215, 65))
        self.frame_2.setFont(font1)
        self.frame_2.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"background-color:#393939;\n"
"border-radius:10px;\n"
"border:1px solid grey;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer = QSpacerItem(430, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(250, 0))
        self.label_9.setMaximumSize(QSize(251, 16777215))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_9.setTextFormat(Qt.PlainText)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.apply_histogram_button = QPushButton(self.frame_2)
        self.apply_histogram_button.setObjectName(u"apply_histogram_button")
        self.apply_histogram_button.setMinimumSize(QSize(111, 0))
        self.apply_histogram_button.setMaximumSize(QSize(111, 16777215))
        self.apply_histogram_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.apply_histogram_button.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"background-color:#6B6B6B;\n"
"border-radius:8px")

        self.horizontalLayout_4.addWidget(self.apply_histogram_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 35))
        self.label_25.setMaximumSize(QSize(16777215, 35))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"color:white;\n"
"border:none;\n"
"background-color:transparent;")
        self.label_25.setTextFormat(Qt.PlainText)

        self.verticalLayout_7.addWidget(self.label_25)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFont(font1)
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet(u"background-color:#393939;\n"
"border-radius:10px;\n"
"border:1px solid grey;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(150, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(150, 0))
        self.label_11.setMaximumSize(QSize(150, 16777215))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_11.setTextFormat(Qt.PlainText)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(494, 0))
        self.comboBox.setMaximumSize(QSize(494, 16777215))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"background-color:#6A6A6A;\n"
"color:white;\n"
"padding-left:10px")
        self.comboBox.setEditable(False)
        self.comboBox.setIconSize(QSize(10, 10))
        self.comboBox.setDuplicatesEnabled(True)

        self.horizontalLayout_6.addWidget(self.comboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_4 = QSpacerItem(150, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 0))
        self.label_12.setMaximumSize(QSize(150, 16777215))
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_12.setTextFormat(Qt.PlainText)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.comboBox_2 = QComboBox(self.frame_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(381, 0))
        self.comboBox_2.setMaximumSize(QSize(381, 16777215))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet(u"background-color:#6A6A6A;\n"
"color:white;\n"
"padding-left:10px")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setIconSize(QSize(10, 10))
        self.comboBox_2.setDuplicatesEnabled(True)

        self.horizontalLayout_8.addWidget(self.comboBox_2)

        self.pushButton_12 = QPushButton(self.frame_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(111, 0))
        self.pushButton_12.setMaximumSize(QSize(111, 16777215))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"background-color:#6B6B6B;\n"
"border-radius:8px")

        self.horizontalLayout_8.addWidget(self.pushButton_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(150, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 0))
        self.label_13.setMaximumSize(QSize(150, 16777215))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_13.setTextFormat(Qt.PlainText)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.comboBox_3 = QComboBox(self.frame_3)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(381, 0))
        self.comboBox_3.setMaximumSize(QSize(381, 16777215))
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet(u"background-color:#6A6A6A;\n"
"color:white;\n"
"padding-left:10px")
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setIconSize(QSize(10, 10))
        self.comboBox_3.setDuplicatesEnabled(True)

        self.horizontalLayout_7.addWidget(self.comboBox_3)

        self.pushButton_13 = QPushButton(self.frame_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(111, 0))
        self.pushButton_13.setMaximumSize(QSize(111, 16777215))
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"background-color:#6B6B6B;\n"
"border-radius:8px")

        self.horizontalLayout_7.addWidget(self.pushButton_13)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 35))
        self.label_26.setMaximumSize(QSize(16777215, 35))
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"color:white;\n"
"border:none;\n"
"background-color:transparent")
        self.label_26.setTextFormat(Qt.PlainText)

        self.verticalLayout_7.addWidget(self.label_26)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(True)
        self.frame_4.setMinimumSize(QSize(0, 65))
        self.frame_4.setMaximumSize(QSize(16777215, 65))
        self.frame_4.setFont(font1)
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet(u"background-color:#393939;\n"
"border-radius:10px;\n"
"border:1px solid grey;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_6 = QSpacerItem(150, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(110, 0))
        self.label_14.setMaximumSize(QSize(110, 16777215))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_14.setTextFormat(Qt.PlainText)

        self.horizontalLayout_10.addWidget(self.label_14)

        self.checkBox = QCheckBox(self.frame_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)
        self.checkBox.setMinimumSize(QSize(229, 0))
        self.checkBox.setMaximumSize(QSize(229, 16777215))
        self.checkBox.setFont(font)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"\n"
"#checkBox{\n"
"border:none;\n"
"color:white;\n"
"}")
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)

        self.horizontalLayout_10.addWidget(self.checkBox)

        self.pushButton_11 = QPushButton(self.frame_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(111, 0))
        self.pushButton_11.setMaximumSize(QSize(111, 16777215))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"background-color:#6B6B6B;\n"
"border-radius:8px")

        self.horizontalLayout_10.addWidget(self.pushButton_11)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 35))
        self.label_27.setMaximumSize(QSize(16777215, 35))
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"color:white;\n"
"border:none;\n"
"background-color:transparent")
        self.label_27.setTextFormat(Qt.PlainText)

        self.verticalLayout_7.addWidget(self.label_27)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setEnabled(True)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFont(font1)
        self.frame_5.setAutoFillBackground(False)
        self.frame_5.setStyleSheet(u"background-color:#393939;\n"
"border-radius:10px;\n"
"border:1px solid grey;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_7 = QSpacerItem(150, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(108, 0))
        self.label_16.setMaximumSize(QSize(108, 16777215))
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_16.setTextFormat(Qt.PlainText)

        self.horizontalLayout_11.addWidget(self.label_16)

        self.comboBox_4 = QComboBox(self.frame_5)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(501, 0))
        self.comboBox_4.setMaximumSize(QSize(501, 16777215))
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet(u"background-color:#6A6A6A;\n"
"color:white;\n"
"padding-left:10px")
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setIconSize(QSize(10, 10))
        self.comboBox_4.setDuplicatesEnabled(True)

        self.horizontalLayout_11.addWidget(self.comboBox_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_8 = QSpacerItem(150, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(100, 0))
        self.label_17.setMaximumSize(QSize(100, 16777215))
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_17.setTextFormat(Qt.PlainText)

        self.horizontalLayout_12.addWidget(self.label_17)

        self.comboBox_5 = QComboBox(self.frame_5)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(387, 0))
        self.comboBox_5.setMaximumSize(QSize(387, 16777215))
        self.comboBox_5.setFont(font)
        self.comboBox_5.setStyleSheet(u"background-color:#6A6A6A;\n"
"color:white;\n"
"padding-left:10px")
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setIconSize(QSize(10, 10))
        self.comboBox_5.setDuplicatesEnabled(True)

        self.horizontalLayout_12.addWidget(self.comboBox_5)

        self.pushButton_15 = QPushButton(self.frame_5)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(111, 0))
        self.pushButton_15.setMaximumSize(QSize(111, 16777215))
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"background-color:#6B6B6B;\n"
"border-radius:8px")

        self.horizontalLayout_12.addWidget(self.pushButton_15)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 35))
        self.label_28.setMaximumSize(QSize(16777215, 35))
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"color:white;\n"
"border:none;\n"
"background-color:transparent")
        self.label_28.setTextFormat(Qt.PlainText)

        self.verticalLayout_7.addWidget(self.label_28)

        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setEnabled(True)
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFont(font1)
        self.frame_6.setAutoFillBackground(False)
        self.frame_6.setStyleSheet(u"background-color:#393939;\n"
"border-radius:10px;\n"
"border:1px solid grey;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(120, 0))
        self.label_18.setMaximumSize(QSize(120, 16777215))
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_18.setTextFormat(Qt.PlainText)

        self.horizontalLayout_13.addWidget(self.label_18)

        self.baudrate_spinbox = QSpinBox(self.frame_6)
        self.baudrate_spinbox.setObjectName(u"baudrate_spinbox")
        self.baudrate_spinbox.setMinimumSize(QSize(600, 0))
        self.baudrate_spinbox.setMaximumSize(QSize(600, 16777215))
        self.baudrate_spinbox.setStyleSheet(u"#baudrate_spinbox{\n"
"border:transparent;\n"
"color:white;\n"
"font-size:26px;\n"
"background-color:#292929;\n"
"}\n"
"#baudrate_spinbox:hover{\n"
"border:1px solid pink;\n"
"}")
        self.baudrate_spinbox.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.baudrate_spinbox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.baudrate_spinbox.setMaximum(1000)

        self.horizontalLayout_13.addWidget(self.baudrate_spinbox)

        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(110, 0))
        self.label_21.setMaximumSize(QSize(110, 16777215))
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_21.setTextFormat(Qt.PlainText)

        self.horizontalLayout_13.addWidget(self.label_21)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(120, 0))
        self.label_19.setMaximumSize(QSize(120, 16777215))
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_19.setTextFormat(Qt.PlainText)

        self.horizontalLayout_14.addWidget(self.label_19)

        self.channels_combobox = QComboBox(self.frame_6)
        self.channels_combobox.addItem("")
        self.channels_combobox.setObjectName(u"channels_combobox")
        self.channels_combobox.setMinimumSize(QSize(800, 0))
        self.channels_combobox.setMaximumSize(QSize(800, 16777215))
        self.channels_combobox.setFont(font)
        self.channels_combobox.setStyleSheet(u"background-color:#6A6A6A;\n"
"color:white;\n"
"padding-left:10px")
        self.channels_combobox.setEditable(False)
        self.channels_combobox.setIconSize(QSize(10, 10))
        self.channels_combobox.setDuplicatesEnabled(True)

        self.horizontalLayout_14.addWidget(self.channels_combobox)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(119, 0))
        self.label_20.setMaximumSize(QSize(119, 16777215))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_20.setTextFormat(Qt.PlainText)

        self.horizontalLayout_15.addWidget(self.label_20)

        self.time_line_edit = QLineEdit(self.frame_6)
        self.time_line_edit.setObjectName(u"time_line_edit")
        self.time_line_edit.setMinimumSize(QSize(300, 0))
        self.time_line_edit.setMaximumSize(QSize(300, 16777215))
        self.time_line_edit.setFont(font3)
        self.time_line_edit.setStyleSheet(u"#time_line_edit{\n"
"background-color:#292929;\n"
"border:transparent;\n"
"color:white;}\n"
"#time_line_edit:hover{\n"
"border:1px solid pink;\n"
"}")
        self.time_line_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.time_line_edit)

        self.label_22 = QLabel(self.frame_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(100, 0))
        self.label_22.setMaximumSize(QSize(100, 16777215))
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_22.setTextFormat(Qt.PlainText)

        self.horizontalLayout_15.addWidget(self.label_22)

        self.horizontalSpacer_9 = QSpacerItem(150, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)


        self.verticalLayout_7.addWidget(self.frame_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_29 = QLabel(self.widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(200, 35))
        self.label_29.setMaximumSize(QSize(16777215, 35))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"color:white;\n"
"border:none;\n"
"background-color:transparent")
        self.label_29.setTextFormat(Qt.PlainText)

        self.horizontalLayout_9.addWidget(self.label_29)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)

        self.progress_bar = QProgressBar(self.widget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMinimumSize(QSize(400, 0))
        self.progress_bar.setStyleSheet(u" QProgressBar {\n"
"		color:white;\n"
"		font-size:20px;\n"
"        border: 2px solid grey;\n"
"        border-radius: 5px;\n"
"        text-align: center;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: #19d46d;\n"
"        width: 10px;\n"
"        margin: 0.5px;\n"
"    }")
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)

        self.horizontalLayout_9.addWidget(self.progress_bar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setFont(font1)
        self.frame_7.setAutoFillBackground(False)
        self.frame_7.setStyleSheet(u"background-color:#393939;\n"
"border-radius:10px;\n"
"border:1px solid grey;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(100, 16777215))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"color:white;\n"
"border:none")
        self.label_15.setTextFormat(Qt.PlainText)

        self.horizontalLayout_16.addWidget(self.label_15)

        self.image_selection_combobox = QComboBox(self.frame_7)
        self.image_selection_combobox.setObjectName(u"image_selection_combobox")
        self.image_selection_combobox.setMaximumSize(QSize(471, 16777215))
        self.image_selection_combobox.setFont(font)
        self.image_selection_combobox.setStyleSheet(u"background-color:#6A6A6A;\n"
"color:white;\n"
"padding-left:10px")
        self.image_selection_combobox.setEditable(False)
        self.image_selection_combobox.setIconSize(QSize(10, 10))
        self.image_selection_combobox.setDuplicatesEnabled(True)

        self.horizontalLayout_16.addWidget(self.image_selection_combobox)

        self.select_image_button = QPushButton(self.frame_7)
        self.select_image_button.setObjectName(u"select_image_button")
        self.select_image_button.setMaximumSize(QSize(111, 16777215))
        self.select_image_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_image_button.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"background-color:#6B6B6B;\n"
"border-radius:8px")

        self.horizontalLayout_16.addWidget(self.select_image_button)


        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(70)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(25, -1, 25, -1)
        self.Image = QLabel(self.frame_7)
        self.Image.setObjectName(u"Image")
        self.Image.setMinimumSize(QSize(367, 364))
        self.Image.setMaximumSize(QSize(367, 364))
        self.Image.setScaledContents(True)
        self.Image.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Image.setWordWrap(False)

        self.horizontalLayout_17.addWidget(self.Image)

        self.result_image = QLabel(self.frame_7)
        self.result_image.setObjectName(u"result_image")
        self.result_image.setMinimumSize(QSize(367, 364))
        self.result_image.setMaximumSize(QSize(367, 364))
        self.result_image.setPixmap(QPixmap(u"../../Desktop/Senua.webp"))
        self.result_image.setScaledContents(True)
        self.result_image.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.result_image.setWordWrap(False)

        self.horizontalLayout_17.addWidget(self.result_image)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 4)

        self.verticalLayout_10.addWidget(self.frame_7)

        self.label_30 = QLabel(self.widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 35))
        self.label_30.setMaximumSize(QSize(16777215, 35))
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"color:white;\n"
"border:none;\n"
"background-color:transparent")
        self.label_30.setTextFormat(Qt.PlainText)

        self.verticalLayout_10.addWidget(self.label_30)

        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFont(font1)
        self.frame_8.setAutoFillBackground(False)
        self.frame_8.setStyleSheet(u"background-color:#393939;\n"
"border-radius:10px;\n"
"border:1px solid grey;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(40, 30, 40, 30)
        self.histogram_image_chart = QLabel(self.frame_8)
        self.histogram_image_chart.setObjectName(u"histogram_image_chart")
        self.histogram_image_chart.setPixmap(QPixmap(u"../../Desktop/Senua.webp"))
        self.histogram_image_chart.setScaledContents(True)
        self.histogram_image_chart.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.histogram_image_chart.setWordWrap(False)

        self.verticalLayout_9.addWidget(self.histogram_image_chart)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.original_histogram_image_button = QPushButton(self.frame_8)
        self.original_histogram_image_button.setObjectName(u"original_histogram_image_button")
        self.original_histogram_image_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.original_histogram_image_button.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"background-color:#6B6B6B;\n"
"border-radius:8px")

        self.horizontalLayout_18.addWidget(self.original_histogram_image_button)

        self.result_histogram_image_button = QPushButton(self.frame_8)
        self.result_histogram_image_button.setObjectName(u"result_histogram_image_button")
        self.result_histogram_image_button.setEnabled(False)
        self.result_histogram_image_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.result_histogram_image_button.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"background-color:#6B6B6B;\n"
"border-radius:8px")

        self.horizontalLayout_18.addWidget(self.result_histogram_image_button)

        self.display_both_histogram_results_button = QPushButton(self.frame_8)
        self.display_both_histogram_results_button.setObjectName(u"display_both_histogram_results_button")
        self.display_both_histogram_results_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.display_both_histogram_results_button.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"background-color:#6B6B6B;\n"
"border-radius:8px")

        self.horizontalLayout_18.addWidget(self.display_both_histogram_results_button)


        self.verticalLayout_9.addLayout(self.horizontalLayout_18)

        self.verticalLayout_9.setStretch(0, 6)
        self.verticalLayout_9.setStretch(1, 1)

        self.verticalLayout_10.addWidget(self.frame_8)

        self.verticalLayout_10.setStretch(1, 2)
        self.verticalLayout_10.setStretch(2, 1)
        self.verticalLayout_10.setStretch(3, 2)

        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Image Processing", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Sengmentation", None))
        self.label.setText(QCoreApplication.translate("Form", u"Manual:", None))
        self.manual_segmentation_spinbox.setSuffix("")
        self.apply_manual_segmentation_button.setText(QCoreApplication.translate("Form", u"Apply", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Automatic:", None))
        self.auto_segmentation_line_edit.setText("")
        self.auto_segmentation_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Empty", None))
        self.apply_automatic_segmentation_button.setText(QCoreApplication.translate("Form", u"Apply", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Contrast Stretching", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Histogram Equalization", None))
        self.apply_histogram_button.setText(QCoreApplication.translate("Form", u"Apply", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Smoothing Filters", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Kernel Size:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"3 x 3", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"5 x 5", None))

        self.label_12.setText(QCoreApplication.translate("Form", u"Linear:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Box Filter", None))

        self.pushButton_12.setText(QCoreApplication.translate("Form", u"Apply", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Non-Linear:", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"Min Filter", None))

        self.pushButton_13.setText(QCoreApplication.translate("Form", u"Apply", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Sharpening Filters", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Laplacian:", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Enhanced", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"Apply", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Edge Detection", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Filter:", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Form", u"Sobel Filter", None))

        self.label_17.setText(QCoreApplication.translate("Form", u"Type:", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Form", u"Vertical", None))

        self.pushButton_15.setText(QCoreApplication.translate("Form", u"Apply", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Transimision Time", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Baudrate:", None))
        self.baudrate_spinbox.setSuffix("")
        self.label_21.setText(QCoreApplication.translate("Form", u"K (x1000)", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Channels:", None))
        self.channels_combobox.setItemText(0, QCoreApplication.translate("Form", u"grayscale", None))

        self.channels_combobox.setCurrentText(QCoreApplication.translate("Form", u"grayscale", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Time:", None))
        self.time_line_edit.setText("")
        self.time_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Empty", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Seconds", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Image", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Image:", None))
        self.select_image_button.setText(QCoreApplication.translate("Form", u"Apply", None))
        self.Image.setText("")
        self.result_image.setText("")
        self.label_30.setText(QCoreApplication.translate("Form", u"Histogram", None))
        self.histogram_image_chart.setText("")
        self.original_histogram_image_button.setText(QCoreApplication.translate("Form", u"Original", None))
        self.result_histogram_image_button.setText(QCoreApplication.translate("Form", u"Output", None))
        self.display_both_histogram_results_button.setText(QCoreApplication.translate("Form", u"Both", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(849, 657)
        icon = QIcon()
        icon.addFile(u":/newPrefix/res/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.XNull = QDoubleSpinBox(self.centralwidget)
        self.XNull.setObjectName(u"XNull")
        self.XNull.setFont(font)
        self.XNull.setMinimum(-100.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.XNull)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.Step = QDoubleSpinBox(self.centralwidget)
        self.Step.setObjectName(u"Step")
        self.Step.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Step)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.Epsilon = QDoubleSpinBox(self.centralwidget)
        self.Epsilon.setObjectName(u"Epsilon")
        self.Epsilon.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Epsilon)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.SpanningRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.SpanningRole, self.verticalSpacer_2)

        self.sectionBtn = QPushButton(self.centralwidget)
        self.sectionBtn.setObjectName(u"sectionBtn")
        font2 = QFont()
        font2.setPointSize(9)
        self.sectionBtn.setFont(font2)
        self.sectionBtn.setCheckable(False)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.sectionBtn)


        self.horizontalLayout_6.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(124, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Example1 = QRadioButton(self.groupBox)
        self.Example1.setObjectName(u"Example1")
        self.Example1.setFont(font)

        self.verticalLayout.addWidget(self.Example1)

        self.Example2 = QRadioButton(self.groupBox)
        self.Example2.setObjectName(u"Example2")
        self.Example2.setFont(font)

        self.verticalLayout.addWidget(self.Example2)

        self.Example3 = QRadioButton(self.groupBox)
        self.Example3.setObjectName(u"Example3")
        self.Example3.setFont(font)

        self.verticalLayout.addWidget(self.Example3)

        self.Example4 = QRadioButton(self.groupBox)
        self.Example4.setObjectName(u"Example4")
        self.Example4.setFont(font)

        self.verticalLayout.addWidget(self.Example4)

        self.Example5 = QRadioButton(self.groupBox)
        self.Example5.setObjectName(u"Example5")
        self.Example5.setFont(font)

        self.verticalLayout.addWidget(self.Example5)

        self.Example6 = QRadioButton(self.groupBox)
        self.Example6.setObjectName(u"Example6")
        self.Example6.setFont(font)

        self.verticalLayout.addWidget(self.Example6)


        self.horizontalLayout.addWidget(self.groupBox)

        self.ExamplePicture = QLabel(self.centralwidget)
        self.ExamplePicture.setObjectName(u"ExamplePicture")
        self.ExamplePicture.setMinimumSize(QSize(357, 193))
        self.ExamplePicture.setFont(font)

        self.horizontalLayout.addWidget(self.ExamplePicture)


        self.horizontalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setTabletTracking(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.sectionLine = QLineEdit(self.centralwidget)
        self.sectionLine.setObjectName(u"sectionLine")
        self.sectionLine.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.sectionLine)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.Nvalue = QSpinBox(self.groupBox_2)
        self.Nvalue.setObjectName(u"Nvalue")
        self.Nvalue.setFont(font)
        self.Nvalue.setMinimum(2)

        self.horizontalLayout_3.addWidget(self.Nvalue)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.solvePassiveSearch = QPushButton(self.groupBox_2)
        self.solvePassiveSearch.setObjectName(u"solvePassiveSearch")
        self.solvePassiveSearch.setCheckable(False)

        self.verticalLayout_3.addWidget(self.solvePassiveSearch)

        self.xPassive = QLineEdit(self.groupBox_2)
        self.xPassive.setObjectName(u"xPassive")
        self.xPassive.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.xPassive)


        self.horizontalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.epsValue = QDoubleSpinBox(self.groupBox_3)
        self.epsValue.setObjectName(u"epsValue")
        self.epsValue.setFont(font)
        self.epsValue.setDecimals(6)
        self.epsValue.setMinimum(0.000001000000000)

        self.horizontalLayout_4.addWidget(self.epsValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.solveGolden = QPushButton(self.groupBox_3)
        self.solveGolden.setObjectName(u"solveGolden")
        self.solveGolden.setCheckable(False)

        self.verticalLayout_2.addWidget(self.solveGolden)

        self.xGolden = QLineEdit(self.groupBox_3)
        self.xGolden.setObjectName(u"xGolden")
        self.xGolden.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.xGolden)


        self.horizontalLayout_5.addWidget(self.groupBox_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WindowTitle", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"h", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u03b5", None))
        self.sectionBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u043e\u0442\u0440\u0435\u0437\u043e\u043a", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u043f\u0440\u0438\u043c\u0435\u0440", None))
        self.Example1.setText(QCoreApplication.translate("MainWindow", u"1 \u041f\u0440\u0438\u043c\u0435\u0440", None))
        self.Example2.setText(QCoreApplication.translate("MainWindow", u"2 \u041f\u0440\u0438\u043c\u0435\u0440", None))
        self.Example3.setText(QCoreApplication.translate("MainWindow", u"3 \u041f\u0440\u0438\u043c\u0435\u0440", None))
        self.Example4.setText(QCoreApplication.translate("MainWindow", u"4 \u041f\u0440\u0438\u043c\u0435\u0440", None))
        self.Example5.setText(QCoreApplication.translate("MainWindow", u"5 \u041f\u0440\u0438\u043c\u0435\u0440", None))
        self.Example6.setText(QCoreApplication.translate("MainWindow", u"6 \u041f\u0440\u0438\u043c\u0435\u0440", None))
        self.ExamplePicture.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u043c\u043e\u0433\u043b\u0430 \u0431\u044b \u0431\u044b\u0442\u044c \u0432\u0430\u0448 \u0440\u0435\u043a\u043b\u0430\u043c\u0430 :)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0435\u0437\u043e\u043a \u043b\u043e\u043a\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u043f\u0430\u0441\u0441\u0438\u0432\u043d\u043e\u0433\u043e \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.solvePassiveSearch.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 X", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0437\u043e\u043b\u043e\u0442\u043e\u0433\u043e \u0441\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u03b5", None))
        self.solveGolden.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 X", None))
    # retranslateUi


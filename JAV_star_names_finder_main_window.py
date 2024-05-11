# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'JAV_star_names_finderrdxlgt.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(881, 611)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(0, 60))
        self.textEdit.setMaximumSize(QSize(16777215, 110))
        self.textEdit.setBaseSize(QSize(0, 0))
        self.textEdit.setAcceptDrops(False)
        self.textEdit.setFrameShape(QFrame.Shape.Box)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setFlat(False)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton)

        self.label_work_path = QLabel(self.groupBox)
        self.label_work_path.setObjectName(u"label_work_path")
        self.label_work_path.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.label_work_path)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.groupBox_2.setStyleSheet(u"")
        self.groupBox_2.setFlat(False)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox_sep_prev = QComboBox(self.groupBox_2)
        self.comboBox_sep_prev.addItem("")
        self.comboBox_sep_prev.addItem("")
        self.comboBox_sep_prev.addItem("")
        self.comboBox_sep_prev.addItem("")
        self.comboBox_sep_prev.setObjectName(u"comboBox_sep_prev")
        sizePolicy4.setHeightForWidth(self.comboBox_sep_prev.sizePolicy().hasHeightForWidth())
        self.comboBox_sep_prev.setSizePolicy(sizePolicy4)
        self.comboBox_sep_prev.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.comboBox_sep_prev, 0, 11, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.comboBox_sep_new = QComboBox(self.groupBox_2)
        self.comboBox_sep_new.addItem("")
        self.comboBox_sep_new.addItem("")
        self.comboBox_sep_new.addItem("")
        self.comboBox_sep_new.addItem("")
        self.comboBox_sep_new.setObjectName(u"comboBox_sep_new")
        sizePolicy4.setHeightForWidth(self.comboBox_sep_new.sizePolicy().hasHeightForWidth())
        self.comboBox_sep_new.setSizePolicy(sizePolicy4)
        self.comboBox_sep_new.setMinimumSize(QSize(40, 0))

        self.gridLayout.addWidget(self.comboBox_sep_new, 1, 11, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)

        self.comboBox_position_new = QComboBox(self.groupBox_2)
        self.comboBox_position_new.addItem("")
        self.comboBox_position_new.addItem("")
        self.comboBox_position_new.setObjectName(u"comboBox_position_new")
        sizePolicy4.setHeightForWidth(self.comboBox_position_new.sizePolicy().hasHeightForWidth())
        self.comboBox_position_new.setSizePolicy(sizePolicy4)
        self.comboBox_position_new.setMinimumSize(QSize(90, 0))

        self.gridLayout.addWidget(self.comboBox_position_new, 1, 1, 1, 2)

        self.label_example_prev = QLabel(self.groupBox_2)
        self.label_example_prev.setObjectName(u"label_example_prev")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_example_prev.sizePolicy().hasHeightForWidth())
        self.label_example_prev.setSizePolicy(sizePolicy5)
        self.label_example_prev.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.label_example_prev, 0, 12, 1, 1)

        self.comboBox_position_prev = QComboBox(self.groupBox_2)
        self.comboBox_position_prev.addItem("")
        self.comboBox_position_prev.addItem("")
        self.comboBox_position_prev.setObjectName(u"comboBox_position_prev")
        sizePolicy4.setHeightForWidth(self.comboBox_position_prev.sizePolicy().hasHeightForWidth())
        self.comboBox_position_prev.setSizePolicy(sizePolicy4)
        self.comboBox_position_prev.setMinimumSize(QSize(90, 0))
        self.comboBox_position_prev.setEditable(False)

        self.gridLayout.addWidget(self.comboBox_position_prev, 0, 1, 1, 2)

        self.label_example_new = QLabel(self.groupBox_2)
        self.label_example_new.setObjectName(u"label_example_new")
        sizePolicy5.setHeightForWidth(self.label_example_new.sizePolicy().hasHeightForWidth())
        self.label_example_new.setSizePolicy(sizePolicy5)
        self.label_example_new.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.label_example_new, 1, 12, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_4 = QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.label_status = QLabel(Form)
        self.label_status.setObjectName(u"label_status")

        self.verticalLayout.addWidget(self.label_status)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"JAV Star Names Finder V2.0", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">JAV Star Names Finder V2.0, Written by SangDo_Kim, a user in AVDBS.com.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\">\uc774 \ud30c\uc774\uc36c \ud504\ub85c\uadf8\ub7a8\uc740 JAV(\uc77c\ubcf8 \uc57c\ub3d9) \ud30c\uc77c\uc774 \ud3ec\ud568\ub41c \ud3f4\ub354\uc640 \uadf8 \ud558\uc704 \ud3f4\ub354\ub4e4\uc758 \ud30c\uc77c \uc774\ub984\ub4e4\uc744 \uc77d\uc740 \ud6c4, \ucd9c\uc5f0\uc790(\uc5ec\ubc30\uc6b0) \uc774\ub984\uc744 \ud55c\uae00\ub85c \uac01 \ud30c\uc77c\uc5d0 \ubd99\uc785\ub2c8\ub2e4.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">JAV \ud30c\uc77c \uc774\ub984\uc740 \ud488\ubc88(\uc608: JEL-223)\uc744 \ud3ec\ud568\ud574\uc57c \ud569\ub2c8\ub2e4.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\ucd9c\uc5f0\uc790 \uc815\ubcf4\ub294 \uad6c\uae00 \uc601\uad6d\uc5d0 \uc800\uc7a5\ub41c AVDBS.com\uc758 \ud398\uc774\uc9c0 \uc81c\ubaa9\uc5d0\uc11c \uc77d\uc5b4 \uc635\ub2c8\ub2e4.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc774 \ud504\ub85c\uadf8\ub7a8\uc740 \ucd9c\uc5f0\uc790\ub97c \ud30c\uc77c \uc774\ub984 \uc55e\uc5d0 \ubd99\uc774\uac70\ub098 \ub4a4\uc5d0 \ubd99\uc77c \uc218\ub3c4 \uc788\uc73c\uba70, \ucd9c\uc5f0\uc790 \uad6c\ubd84\uc790\ub97c \uc120\ud0dd\ud560 \uc218\ub3c4 \uc788\uc2b5\ub2c8\ub2e4. \uc608: #, ^, ', \ucd9c)</p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\uc791\uc5c5 \uacbd\ub85c", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\uacbd\ub85c \uc120\ud0dd", None))
        self.label_work_path.setText(QCoreApplication.translate("Form", u"*\uc544\uc9c1 \uc120\ud0dd\ub418\uc9c0 \uc54a\uc74c*", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\ucd9c\uc5f0\uc790 \uc704\uce58 \ubc0f \uad6c\ubd84\uc790", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\uad6c\ubd84\uc790:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\uae30\uc874 \uc704\uce58:", None))
        self.comboBox_sep_prev.setItemText(0, QCoreApplication.translate("Form", u"#", None))
        self.comboBox_sep_prev.setItemText(1, QCoreApplication.translate("Form", u"^", None))
        self.comboBox_sep_prev.setItemText(2, QCoreApplication.translate("Form", u"`", None))
        self.comboBox_sep_prev.setItemText(3, QCoreApplication.translate("Form", u"\ucd9c)", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\uc2e0\uaddc \uc704\uce58:", None))
        self.comboBox_sep_new.setItemText(0, QCoreApplication.translate("Form", u"#", None))
        self.comboBox_sep_new.setItemText(1, QCoreApplication.translate("Form", u"^", None))
        self.comboBox_sep_new.setItemText(2, QCoreApplication.translate("Form", u"`", None))
        self.comboBox_sep_new.setItemText(3, QCoreApplication.translate("Form", u"\ucd9c)", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"\uad6c\ubd84\uc790:", None))
        self.comboBox_position_new.setItemText(0, QCoreApplication.translate("Form", u"\ud30c\uc77c \ub4b7\ubd80\ubd84", None))
        self.comboBox_position_new.setItemText(1, QCoreApplication.translate("Form", u"\ud30c\uc77c \uc55e\ubd80\ubd84", None))

        self.label_example_prev.setText(QCoreApplication.translate("Form", u"\uc608: URE-066 \uc720) \uc0c1\uc810\uac00\uc758 \uad6c\uba4d \ubd80\uc778\ub4e4 #\ubbf8\uc988\ub178 \uc544\uc0ac\ud788", None))
        self.comboBox_position_prev.setItemText(0, QCoreApplication.translate("Form", u"\ud30c\uc77c \ub4b7\ubd80\ubd84", None))
        self.comboBox_position_prev.setItemText(1, QCoreApplication.translate("Form", u"\ud30c\uc77c \uc55e\ubd80\ubd84", None))

        self.label_example_new.setText(QCoreApplication.translate("Form", u"\uc608: URE-066 \uc720) \uc0c1\uc810\uac00\uc758 \uad6c\uba4d \ubd80\uc778\ub4e4 #\ubbf8\uc988\ub178 \uc544\uc0ac\ud788", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\uc791\uc5c5 \uc2e4\ud589", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\uc885\ub8cc", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\ubaa8\ub4e0 \ud30c\uc77c\uc5d0 \ub300\ud574 \uae30\uc874 \uc704\uce58 \ubc0f \uad6c\ubd84\uc790\ub97c \uc2e0\uaddc \uc124\uc815\uc73c\ub85c \uc774\ub984 \ubcc0\uacbd", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\ucd9c\uc5f0\uc790\ub97c \uad6c\uae00 \uac80\uc0c9\ud558\uc5ec \ud30c\uc77c \uc774\ub984 \ubcc0\uacbd", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\uc791\uc5c5 \ub0b4\uc6a9\uc744 \ud074\ub9bd\ubcf4\ub4dc\ub85c \ubcf5\uc0ac", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\uc791\uc5c5", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\uc791\uc5c5 \uc0c1\uc138", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\uae30\uc874 \ud30c\uc77c \uc774\ub984", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\uc2e0\uaddc \ud30c\uc77c \uc774\ub984", None));
        self.label_status.setText(QCoreApplication.translate("Form", u"\uc0c1\ud0dc \ud45c\uc2dc\uc904", None))
    # retranslateUi


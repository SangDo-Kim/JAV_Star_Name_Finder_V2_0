# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_ok_cancelEbHvGp.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.WindowModal)
        Dialog.resize(496, 191)
        Dialog.setModal(False)
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 10, 481, 121))
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(190, 150, 291, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\ud655\uc778, \ucde8\uc18c", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc120\ud0dd\ud55c \uc791\uc5c5 \uacbd\ub85c \ubc0f \uadf8 \ud558\uc704 \ud3f4\ub354\uc5d0 \uc788\ub294 \ubaa8\ub4e0 \ud30c\uc77c\uc5d0 \ub300\ud574 \uae30\uc874 \ucd9c\uc5f0\uc790 \uc704\uce58 \ubc0f \uad6c\ubd84\uc790\ub97c \uc2e0\uaddc \uc124\uc815\uc73c\ub85c \ubcc0\uacbd\ud569\ub2c8\ub2e4. \uc774 \uc791\uc5c5\uc744 \uc9c4\ud589\ud558\uae30 \uc804\uc5d0 Everything \ub4f1\uc758 \ud504"
                        "\ub85c\uadf8\ub7a8\uc744 \uc0ac\uc6a9\ud558\uc5ec \ud639\uc2dc \uae30\uc874 \uad6c\ubd84\uc790\uac00 \uc798\ubabb \ub4e4\uc5b4\uac00 \uc788\ub294 \ud30c\uc77c\uc774 \uc788\ub294\uc9c0 \ud655\uc778\ud574 \ubcf4\uae30\ub97c \uad8c\uc7a5\ud569\ub2c8\ub2e4. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc791\uc5c5\uc744 \uc9c4\ud589\ud558\ub824\uba74 [\ud655\uc778]\uc744, \ucde8\uc18c\ud558\ub824\uba74 [\ucde8\uc18c]\ub97c \uc120\ud0dd\ud558\uc2ed\uc2dc\uc624.</p></body></html>", None))
    # retranslateUi


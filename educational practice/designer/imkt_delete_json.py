from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 300)
        Form.setStyleSheet(u"background-color: #3380BA;")
        self.logo = QWidget(Form)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 0, 461, 61))
        self.logo.setStyleSheet(u"#logo{\n"
"border-bottom: 1.5px solid #ffffff;\n"
"}")
        self.text_logo = QLabel(self.logo)
        self.text_logo.setObjectName(u"text_logo")
        self.text_logo.setGeometry(QRect(0, 10, 461, 30))
        font = QFont()
        font.setPointSize(24)
        self.text_logo.setFont(font)
        self.text_logo.setStyleSheet(u"color: #ffffff")
        self.text_logo.setAlignment(Qt.AlignCenter)
        self.line = QLabel(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 100, 451, 20))
        font1 = QFont()
        font1.setPointSize(17)
        self.line.setFont(font1)
        self.line.setStyleSheet(u"color: #ffffff;")
        self.line.setAlignment(Qt.AlignCenter)
        self.line_2 = QLabel(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 140, 451, 20))
        font2 = QFont()
        font2.setPointSize(15)
        self.line_2.setFont(font2)
        self.line_2.setStyleSheet(u"color: #ffffff;")
        self.line_2.setAlignment(Qt.AlignCenter)
        self.btn_delete = QPushButton(Form)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(60, 210, 113, 32))
        self.btn_delete.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	background-color: #76BAFA;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}\n"
"\n"
"")
        self.btn_back = QPushButton(Form)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(280, 210, 113, 32))
        self.btn_back.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	background-color: #76BAFA;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}\n"
"\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.text_logo.setText(QCoreApplication.translate("Form", u"FEFU IMKT Enrolle Scan", None))
        self.line.setText("")
        self.line_2.setText("")
        self.btn_delete.setText(QCoreApplication.translate("Form", u"\u0414\u0430", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"\u041d\u0435\u0442", None))
    # retranslateUi


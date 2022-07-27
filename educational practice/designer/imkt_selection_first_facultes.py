from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
import designer.imkt

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(460, 605)
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
        self.text_choice = QLabel(Form)
        self.text_choice.setObjectName(u"text_choice")
        self.text_choice.setGeometry(QRect(0, 90, 461, 20))
        font1 = QFont()
        font1.setFamilies([u"Open Sans"])
        font1.setPointSize(10)
        self.text_choice.setFont(font1)
        self.text_choice.setStyleSheet(u"color: #ffffff;")
        self.text_choice.setAlignment(Qt.AlignCenter)
        self.btn_next = QPushButton(Form)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setGeometry(QRect(70, 260, 82, 28))
        font2 = QFont()
        font2.setPointSize(14)
        self.btn_next.setFont(font2)
        self.btn_next.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	background-color: #76BAFA;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}\n"
"\n"
"")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 300, 301, 291))
        self.label_2.setPixmap(QPixmap(u":/resurce/imkt-logo (1).png"))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.btn_faculty_3 = QPushButton(Form)
        self.btn_faculty_3.setObjectName(u"btn_faculty_3")
        self.btn_faculty_3.setGeometry(QRect(20, 214, 412, 26))
        font3 = QFont()
        font3.setPointSize(12)
        self.btn_faculty_3.setFont(font3)
        self.btn_faculty_3.setStyleSheet(u"QPushButton{\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}")
        self.btn_faculty_2 = QPushButton(Form)
        self.btn_faculty_2.setObjectName(u"btn_faculty_2")
        self.btn_faculty_2.setGeometry(QRect(20, 177, 412, 26))
        self.btn_faculty_2.setFont(font3)
        self.btn_faculty_2.setStyleSheet(u"QPushButton{\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}")
        self.btn_faculty_1 = QPushButton(Form)
        self.btn_faculty_1.setObjectName(u"btn_faculty_1")
        self.btn_faculty_1.setGeometry(QRect(20, 140, 412, 26))
        self.btn_faculty_1.setFont(font3)
        self.btn_faculty_1.setStyleSheet(u"QPushButton{\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}")
        self.btn_remove = QPushButton(Form)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setGeometry(QRect(310, 260, 82, 28))
        self.btn_remove.setFont(font2)
        self.btn_remove.setStyleSheet(u"QPushButton{\n"
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
        self.text_choice.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 1 \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u043c \u0445\u043e\u0442\u0438\u0442\u0435 \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0441\u0432\u043e\u0451 \u043c\u0435\u0441\u0442\u043e", None))
        self.btn_next.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.label_2.setText("")
        self.btn_faculty_3.setText(QCoreApplication.translate("Form", u"09.03.02 \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b \u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438", None))
        self.btn_faculty_2.setText(QCoreApplication.translate("Form", u"02.03.01 \u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u044b\u0435 \u043d\u0430\u0443\u043a\u0438", None))
        self.btn_faculty_1.setText(QCoreApplication.translate("Form", u"09.03.03 \u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430", None))
        self.btn_remove.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi


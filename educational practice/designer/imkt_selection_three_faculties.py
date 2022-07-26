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
        Form.resize(450, 605)
        font = QFont()
        font.setPointSize(14)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: #3380BA;")
        self.logo = QWidget(Form)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 20, 461, 61))
        self.logo.setStyleSheet(u"#logo{\n"
"border-bottom: 1.5px solid #ffffff;\n"
"}")
        self.text_logo = QLabel(self.logo)
        self.text_logo.setObjectName(u"text_logo")
        self.text_logo.setGeometry(QRect(0, 10, 461, 30))
        font1 = QFont()
        font1.setPointSize(24)
        self.text_logo.setFont(font1)
        self.text_logo.setStyleSheet(u"color: #ffffff")
        self.text_logo.setAlignment(Qt.AlignCenter)
        self.text_choice = QLabel(Form)
        self.text_choice.setObjectName(u"text_choice")
        self.text_choice.setGeometry(QRect(0, 110, 461, 20))
        font2 = QFont()
        font2.setFamilies([u"Open Sans"])
        font2.setPointSize(10)
        self.text_choice.setFont(font2)
        self.text_choice.setStyleSheet(u"color: #ffffff;")
        self.text_choice.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 460, 82, 28))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	background-color: #76BAFA;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}\n"
"")
        self.btn_faculty_moais = QPushButton(Form)
        self.btn_faculty_moais.setObjectName(u"btn_faculty_moais")
        self.btn_faculty_moais.setGeometry(QRect(20, 193, 412, 26))
        font3 = QFont()
        font3.setPointSize(12)
        self.btn_faculty_moais.setFont(font3)
        self.btn_faculty_moais.setStyleSheet(u"QPushButton{\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000;\n"
"}"
"QPushButton:pressed{\n"
"       border:1.5px solid #000000;\n"
"}")
        self.btn_faculty_mkn = QPushButton(Form)
        self.btn_faculty_mkn.setObjectName(u"btn_faculty_mkn")
        self.btn_faculty_mkn.setGeometry(QRect(20, 230, 412, 26))
        self.btn_faculty_mkn.setFont(font3)
        self.btn_faculty_mkn.setStyleSheet(u"QPushButton{\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}")
        self.btn_faculty_prog_in = QPushButton(Form)
        self.btn_faculty_prog_in.setObjectName(u"btn_faculty_prog_in")
        self.btn_faculty_prog_in.setGeometry(QRect(20, 266, 412, 26))
        self.btn_faculty_prog_in.setFont(font3)
        self.btn_faculty_prog_in.setStyleSheet(u"QPushButton{\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}")
        self.btn_faculty_pi = QPushButton(Form)
        self.btn_faculty_pi.setObjectName(u"btn_faculty_pi")
        self.btn_faculty_pi.setGeometry(QRect(20, 157, 412, 26))
        self.btn_faculty_pi.setFont(font3)
        self.btn_faculty_pi.setStyleSheet(u"QPushButton{\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}")
        self.btn_faculty_pmi = QPushButton(Form)
        self.btn_faculty_pmi.setObjectName(u"btn_faculty_pmi")
        self.btn_faculty_pmi.setGeometry(QRect(20, 303, 412, 26))
        self.btn_faculty_pmi.setFont(font3)
        self.btn_faculty_pmi.setStyleSheet(u"QPushButton{\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}")
        self.btn_faculty_ist = QPushButton(Form)
        self.btn_faculty_ist.setObjectName(u"btn_faculty_ist")
        self.btn_faculty_ist.setGeometry(QRect(20, 339, 412, 26))
        self.btn_faculty_ist.setFont(font3)
        self.btn_faculty_ist.setStyleSheet(u"QPushButton{\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}")
        self.btn_faculty_ib = QPushButton(Form)
        self.btn_faculty_ib.setObjectName(u"btn_faculty_ib")
        self.btn_faculty_ib.setGeometry(QRect(20, 375, 412, 26))
        self.btn_faculty_ib.setFont(font3)
        self.btn_faculty_ib.setStyleSheet(u"QPushButton{\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}")
        self.btn_faculty_kb = QPushButton(Form)
        self.btn_faculty_kb.setObjectName(u"btn_faculty_kb")
        self.btn_faculty_kb.setGeometry(QRect(20, 412, 412, 26))
        self.btn_faculty_kb.setFont(font3)
        self.btn_faculty_kb.setStyleSheet(u"QPushButton{\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:1.5px solid #000000\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.text_logo.setText(QCoreApplication.translate("Form", u"FEFU IMKT Enrolle Scan", None))
        self.text_choice.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 3 \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0432\u044b \u043f\u043e\u0434\u0430\u043b\u0438 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.btn_faculty_moais.setText(QCoreApplication.translate("Form", u"02.03.03 \u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u0447 \u043e\u0431\u0435\u0441\u043f\u0435\u0447 \u0438 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440...", None))
        self.btn_faculty_mkn.setText(QCoreApplication.translate("Form", u"02.03.01 \u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u044b\u0435 \u043d\u0430\u0443\u043a\u0438", None))
        self.btn_faculty_prog_in.setText(QCoreApplication.translate("Form", u"09.03.04 \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u0430\u044f \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0438\u044f", None))
        self.btn_faculty_pi.setText(QCoreApplication.translate("Form", u"09.03.03 \u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430", None))
        self.btn_faculty_pmi.setText(QCoreApplication.translate("Form", u"01.03.02 \u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430", None))
        self.btn_faculty_ist.setText(QCoreApplication.translate("Form", u"09.03.02 \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b \u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438", None))
        self.btn_faculty_ib.setText(QCoreApplication.translate("Form", u"10.03.01 \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c", None))
        self.btn_faculty_kb.setText(QCoreApplication.translate("Form", u"10.05.01 \u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u0430\u044f \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c", None))


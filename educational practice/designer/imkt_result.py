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
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(19, 130, 421, 115))
        self.widget.setStyleSheet(u"background-color: #ffffff;\n"
"color: #000000;\n"
"border-radius: 25px")
        self.lb_faculte = QLabel(self.widget)
        self.lb_faculte.setObjectName(u"lb_faculte")
        self.lb_faculte.setGeometry(QRect(20, 5, 391, 16))
        font2 = QFont()
        font2.setPointSize(10)
        self.lb_faculte.setFont(font2)
        self.lb_faculte.setAlignment(Qt.AlignCenter)
        self.line_scores = QLabel(self.widget)
        self.line_scores.setObjectName(u"line_scores")
        self.line_scores.setGeometry(QRect(40, 30, 111, 16))
        self.line_scores.setFont(font2)
        self.line_place = QLabel(self.widget)
        self.line_place.setObjectName(u"line_place")
        self.line_place.setGeometry(QRect(40, 50, 111, 16))
        self.line_place.setFont(font2)
        self.line_statements = QLabel(self.widget)
        self.line_statements.setObjectName(u"line_statements")
        self.line_statements.setGeometry(QRect(40, 70, 201, 16))
        self.line_statements.setFont(font2)
        self.line_sum = QLabel(self.widget)
        self.line_sum.setObjectName(u"line_sum")
        self.line_sum.setGeometry(QRect(40, 90, 301, 16))
        self.line_sum.setFont(font2)
        self.btn_back = QPushButton(Form)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(190, 260, 82, 28))
        font3 = QFont()
        font3.setPointSize(14)
        self.btn_back.setFont(font3)
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
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 300, 301, 291))
        self.label_6.setPixmap(QPixmap(u":/resurce/imkt-logo (1).png"))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.text_logo.setText(QCoreApplication.translate("Form", u"FEFU IMKT Enrolle Scan", None))
        self.text_choice.setText(QCoreApplication.translate("Form", u"\u041f\u043e \u0432\u0430\u0448\u0435\u043c\u0443 \u0437\u0430\u043f\u0440\u043e\u0441\u0443:", None))
        self.lb_faculte.setText(QCoreApplication.translate("Form", u"\u041d\u0430 \u0444\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442\u0435 02.03.01 \u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u044b\u0435 \u043d\u0430\u0443\u043a\u0438", None))
        self.line_scores.setText(QCoreApplication.translate("Form", u"- \u0432\u0430\u0448\u0438 \u0431\u0430\u043b\u043b\u044b 215", None))
        self.line_place.setText(QCoreApplication.translate("Form", u"- \u043d\u0430 80/213 \u043c\u0435\u0441\u0442\u0435", None))
        self.line_statements.setText(QCoreApplication.translate("Form", u"- \u043d\u0430 10/55 \u043f\u0440\u0438 \u043f\u043e\u0434\u0430\u0447\u0435 \u0437\u0430\u044f\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.line_sum.setText(QCoreApplication.translate("Form", u"- 243 \u0431\u0430\u043b\u043b\u0430 \u0434\u043b\u044f \u0442\u043e\u0447\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u043d\u0430 \u0431\u044e\u0434\u0436\u0435\u0442", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_6.setText("")
    # retranslateUi


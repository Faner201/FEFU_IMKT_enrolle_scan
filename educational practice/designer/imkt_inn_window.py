from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import designer.imkt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(458, 605)
        MainWindow.setStyleSheet(u"background-color: #3380BA;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo = QWidget(self.centralwidget)
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
        self.texn_inn = QLabel(self.centralwidget)
        self.texn_inn.setObjectName(u"texn_inn")
        self.texn_inn.setGeometry(QRect(6, 140, 451, 20))
        font1 = QFont()
        font1.setPointSize(16)
        self.texn_inn.setFont(font1)
        self.texn_inn.setStyleSheet(u"color: #ffffff;")
        self.texn_inn.setAlignment(Qt.AlignCenter)
        self.texn_inn.setWordWrap(True)
        self.btn = QPushButton(self.centralwidget)
        self.btn.setObjectName(u"btn")
        self.btn.setGeometry(QRect(190, 240, 82, 28))
        font2 = QFont()
        font2.setPointSize(14)
        self.btn.setFont(font2)
        self.btn.setStyleSheet(u"QPushButton{\n"
"	color: #ffffff;\n"
"	border-radius: 12px;\n"
"	background-color: #76BAFA;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1.5px solid #000000;\n"
"}\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 280, 271, 251))
        self.label_2.setPixmap(QPixmap(u":/resurce/imkt-logo (1).png"))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.input_inn = QLineEdit(self.centralwidget)
        self.input_inn.setObjectName(u"input_inn")
        self.input_inn.setGeometry(QRect(90, 200, 269, 25))
        font3 = QFont()
        font3.setPointSize(12)
        self.input_inn.setFont(font3)
        self.input_inn.setStyleSheet(u"QLineEdit{\n"
"background-color: #ffffff;\n"
"border-radius: 12px;\n"
"color: #000000;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 1.5px solid #000000;\n"
"}\n"
"")
        self.input_inn.setFrame(False)
        self.input_inn.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 458, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text_logo.setText(QCoreApplication.translate("MainWindow", u"FEFU IMKT Enrolle Scan", None))
        self.texn_inn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u0418\u041d\u041d", None))
        self.btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.label_2.setText("")
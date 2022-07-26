import sys
from PySide6.QtWidgets import QApplication
from window import InnInputWindow, SelectionFirstFaculties
import os.path

def main():
    app = QApplication(sys.argv)
    if os.path.isfile("json_inf.json"):
        programm = SelectionFirstFaculties()
    else:
        programm = InnInputWindow()
    programm.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

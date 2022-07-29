import os
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtGui import QFontDatabase
import requests

from designer.imkt_snils_window import Ui_MainWindow
from designer.imkt_selection_three_faculties import Ui_Form as Ui_Form_Three
from designer.imkt_selection_first_facultes import Ui_Form as Ui_Form_First
from designer.imkt_result import Ui_Form as Ui_Form_Result
from designer.imkt_error import Ui_Form as Ui_Error
from designer.imkt_delete_json import Ui_Form as Ui_Delete

from data import *

import json
from style import *
import re


class SnilsInputWindow(QMainWindow):
    def __init__(self):
        super(SnilsInputWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.match = False
        self.ui.texn_inn.setText("Введите ваш СНИЛС")

        QFontDatabase.addApplicationFont(
            "designer/Open_Sans (1)/static/OpenSans/OpenSans-Medium.ttf"
        )

        self.ui.btn.clicked.connect(self.request_date)

    def request_date(self) -> None:
        if self.ui.input_inn.text() != "":
            self.match = re.fullmatch(
                r"\d{3}\D\d{3}\D\d{3}\s\d{2}", self.ui.input_inn.text()
            )
            if self.match:
                inn = {"information": [{"snls": self.ui.input_inn.text()}]}
                with open("json_inf.json", "w") as file:
                    json.dump(inn, file)
                self.output = SelectionThreeFaculties()
                self.close()
                self.output.show()
            else:
                self.output = WindowError(True)
                self.close()
                self.output.show()


class WindowError(QWidget):
    def __init__(self, flag):
        self.number = flag
        super(WindowError, self).__init__()
        self.ui = Ui_Error()
        self.ui.setupUi(self)
        if self.number:
            self.ui.line.setText("Введённые данные не являются снилсом")
            self.ui.line_2.setText("Пожалуйста измените данные")
            self.ui.btn_back.clicked.connect(self.back_input)
        else:
            self.ui.line.setText("Даный снилс не валидный на данном факультете")
            self.ui.line_2.setText("Пожалуйста выберите другой факультет")
            self.ui.btn_back.clicked.connect(self.back_selection)

    def back_input(self):
        self.output = SnilsInputWindow()
        self.close()
        self.output.show()

    def back_selection(self):
        self.output = SelectionFirstFaculties()
        self.close()
        self.output.show()


class SelectionThreeFaculties(QWidget):
    def __init__(self):
        super(SelectionThreeFaculties, self).__init__()
        self.ui = Ui_Form_Three()
        self.ui.setupUi(self)
        self.name_faculties = []
        self.mismatches = 0
        self.btn_name = [
            "btn_faculty_pi",
            "btn_faculty_moais",
            "btn_faculty_mkn",
            "btn_faculty_prog_in",
            "btn_faculty_pmi",
            "btn_faculty_ist",
            "btn_faculty_ib",
            "btn_faculty_kb",
        ]

        QFontDatabase.addApplicationFont(
            "designer/Open_Sans (1)/static/OpenSans/OpenSans-Medium.ttf"
        )

        self.ui.btn_faculty_pi.clicked.connect(self.selection_faculties)
        self.ui.btn_faculty_moais.clicked.connect(self.selection_faculties)
        self.ui.btn_faculty_mkn.clicked.connect(self.selection_faculties)
        self.ui.btn_faculty_prog_in.clicked.connect(self.selection_faculties)
        self.ui.btn_faculty_pmi.clicked.connect(self.selection_faculties)
        self.ui.btn_faculty_ist.clicked.connect(self.selection_faculties)
        self.ui.btn_faculty_ib.clicked.connect(self.selection_faculties)
        self.ui.btn_faculty_kb.clicked.connect(self.selection_faculties)
        self.ui.pushButton.clicked.connect(self.transition)

    def selection_faculties(self) -> None:
        btn = self.sender()

        if btn.objectName() in self.btn_name:
            if self.deleting_faculty(btn):
                if len(self.name_faculties) < 3:
                    self.name_faculties.append(btn.text())
                    getattr(self.ui, btn.objectName()).setStyleSheet(style_click)

    def deleting_faculty(self, btn) -> bool:
        for i in range(len(self.name_faculties)):
            if btn.text() == self.name_faculties[i]:
                self.name_faculties.remove(btn.text())
                getattr(self.ui, btn.objectName()).setStyleSheet(style)
                return False
        return True

    def transition(self) -> None:
        if len(self.name_faculties) == 3:
            selection = {"facultets": self.name_faculties}
            with open(
                "json_inf.json",
                encoding="utf8",
            ) as file:
                data = json.load(file)
                data["information"].append(selection)
                with open(
                    "json_inf.json",
                    "w",
                    encoding="utf8",
                ) as outfile:
                    json.dump(data, outfile, ensure_ascii=False)
            self.output = SelectionFirstFaculties()
            self.close()
            self.output.show()


class SelectionFirstFaculties(QWidget):
    def __init__(self):
        super(SelectionFirstFaculties, self).__init__()
        self.ui = Ui_Form_First()
        self.ui.setupUi(self)
        with open(
            "json_inf.json"
        ) as file:
            json_faculties = json.load(file)
        self.text_button_faculties(json_faculties)
        self.number_faculty = ""

        self.ui.btn_faculty_1.clicked.connect(self.faculty_selection)
        self.ui.btn_faculty_2.clicked.connect(self.faculty_selection)
        self.ui.btn_faculty_3.clicked.connect(self.faculty_selection)
        self.ui.btn_next.clicked.connect(self.moving_results)
        self.ui.btn_remove.clicked.connect(self.remove_json)

        QFontDatabase.addApplicationFont(
           "designer/Open_Sans (1)/static/OpenSans/OpenSans-Medium.ttf"
        )

    def text_button_faculties(self, json_faculties) -> None:
        self.ui.btn_faculty_1.setText(json_faculties["information"][1]["facultets"][0])
        self.ui.btn_faculty_2.setText(json_faculties["information"][1]["facultets"][1])
        self.ui.btn_faculty_3.setText(json_faculties["information"][1]["facultets"][2])

    def faculty_selection(self) -> None:
        btn = self.sender()

        btn_name = ["btn_faculty_1", "btn_faculty_2", "btn_faculty_3"]

        if btn.objectName() in btn_name:
            if btn.text()[:8] == self.number_faculty:
                self.number_faculty = ""
                getattr(self.ui, btn.objectName()).setStyleSheet(style)
            else:
                self.number_faculty = btn.text()[:8]
                getattr(self.ui, btn.objectName()).setStyleSheet(style_click)

    def moving_results(self) -> None:
        self.output = ResultWindow(self.number_faculty)
        self.close()
        self.output.show()

    def remove_json(self) -> None:
        self.output = WindowDelete()
        self.close()
        self.output.show()


class ResultWindow(QWidget):
    def __init__(self, number):
        self.number_faculty = number
        super(ResultWindow, self).__init__()
        self.ui = Ui_Form_Result()
        self.ui.setupUi(self)
        self.faculties = ""
        self.scores = ""
        self.place = ""
        self.total = ""
        self.when_confirming = 0
        self.total_points = ""
        self.total_score = 0

        with open(
            "json_inf.json"
        ) as file:
            json_inn = json.load(file)
        for number in faculties:
            if number[:8] == self.number_faculty:
                self.faculties = number
                break
        self.request_dvfu_true_consent()
        self.request_dvfu_false_consent(json_inn)

        self.ui.lb_faculte.setText("На факультете " + self.faculties)

        self.ui.line_scores.setText("Ваши баллы - " + self.scores)
        self.ui.line_place.setText(
            "- на " + str(self.place) + "/" + self.total + " месте"
        )
        self.ui.line_statements.setText(
            "- на "
            + str(self.when_confirming)
            + "/"
            + self.total
            + " при подаче заявления"
        )
        self.ui.line_sum.setText(
            str(self.total_points) 
            + " баллов для точного прохождения на бюджет"
        )

        self.ui.btn_back.clicked.connect(self.go_back_selection)

        QFontDatabase.addApplicationFont(
            "designer/Open_Sans (1)/static/OpenSans/OpenSans-Medium.ttf"
        )

    def request_dvfu_false_consent(self, json_inn) -> None:
        self.data = self.request_dvfu("false")
        for applicans in self.data:
            if (
                json_inn["information"][0]["snls"] == applicans.get("name")
                and applicans.get("category") == "На общих основаниях"
            ):
                self.place = int(float(applicans.get("GENERALORDER")))
                self.total = applicans.get("bm")
                self.scores = applicans.get("scoreSum")
                break

    def request_dvfu_true_consent(self) -> None:
        self.data = self.request_dvfu("true")
        for applicans in self.data:
            if (
                applicans.get("scoreSum") != "-"
                and applicans.get("category") == "На общих основаниях"
            ):
                self.total_score += int(applicans.get("scoreSum"))
            if applicans.get("category") == "На общих основаниях":
                self.when_confirming += 1
        self.when_confirming += 1
        self.total_points = int(self.total_score / len(self.data))

    def request_dvfu(self, consent):
        self.current_data = request_data
        self.current_data["trainingDirection"] = self.faculties
        self.current_data["consent"] = consent
        responce = requests.post(
            "https://www.dvfu.ru/bitrix/services/main/ajax.php",
            params=request_parametrs,
            headers=user_agent,
            data=self.current_data,
        ).json()
        return responce.get("data")

    def go_back_selection(self) -> None:
        self.output = SelectionFirstFaculties()
        self.close()
        self.output.show()


class WindowDelete(QWidget):
    def __init__(self):
        super(WindowDelete, self).__init__()
        self.ui = Ui_Delete()
        self.ui.setupUi(self)

        self.ui.line.setText("Вы точно хотите обнулить свои данные?")
        self.ui.line_2.setText("После нажатия на кнопку приложение перезапуститься")

        self.ui.btn_delete.clicked.connect(self.delete_json)
        self.ui.btn_back.clicked.connect(self.back_selection)

    def delete_json(self) -> None:
        os.remove(
            "json_inf.json"
        )
        self.output = SnilsInputWindow()
        self.close()
        self.output.show()

    def back_selection(self) -> None:
        self.output = SelectionFirstFaculties()
        self.close()
        self.output.show()

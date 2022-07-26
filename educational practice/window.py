from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtGui import QFontDatabase
import requests

from designer.imkt_inn_window import Ui_MainWindow
from designer.imkt_selection_three_faculties import Ui_Form as Ui_Form_Three
from designer.imkt_selection_first_facultes import Ui_Form as Ui_Form_First
from designer.imkt_result import Ui_Form as Ui_Form_Result

from data import *

import json

class InnInputWindow(QMainWindow):
    def __init__(self):
        super(InnInputWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont(r"/Users/fanfurick/Documents/code/educational practice/designer/Open_Sans (1)/static/OpenSans/OpenSans-Medium.ttf")

        self.ui.btn.clicked.connect(self.request_date)


    def request_date(self) -> None:
        if self.ui.input_inn.text() != "":
            inn = {"information" : [{ 
                "inn" : self.ui.input_inn.text()
                }]}
            with open('json_inf.json', 'w') as file:
                json.dump(inn, file)
            self.output = SelectionThreeFaculties()
            self.close()
            self.output.show()


class SelectionThreeFaculties(QWidget):
    def __init__(self):
        super(SelectionThreeFaculties, self).__init__()
        self.ui = Ui_Form_Three()
        self.ui.setupUi(self)
        self.name_faculties = []
        self.mismatches = 0

        QFontDatabase.addApplicationFont(r"/Users/fanfurick/Documents/code/educational practice/designer/Open_Sans (1)/static/OpenSans/OpenSans-Medium.ttf")

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

        btn_name = [
            'btn_faculty_pi', 'btn_faculty_moais', 'btn_faculty_mkn',
            'btn_faculty_prog_in', 'btn_faculty_pmi', 'btn_faculty_ist',
            'btn_faculty_ib', 'btn_faculty_kb'
        ]
        if btn.objectName() in btn_name:
            if(self.deleting_faculty(btn)):
                if len(self.name_faculties) < 3:
                    self.name_faculties.append(btn.text())
                    # self.color_selected_faculties()
                    print(self.name_faculties)


    def deleting_faculty(self, btn) -> bool:
        for i in range(len(self.name_faculties)):
            if(btn.text() == self.name_faculties[i]):
                self.name_faculties.remove(btn.text())
                return False
        return True

        
    # def color_selected_faculties(self) -> None:
    #     for i in range(len(self.name_faculties)):
    #         if self.ui.btn_faculty_ib.text() == self.name_faculties[i]:
    #             self.ui.btn_faculty_ib.setStyleSheet('background-color: #888;')
    #         elif self.ui.btn_faculty_ist.text() == self.name_faculties[i]:
    #             self.ui.btn_faculty_ib.setStyleSheet('background-color: #888;')
    #         elif self.ui.btn_faculty_kb.text() == self.name_faculties[i]:
    #             self.ui.btn_faculty_kb.setStyleSheet('background-color: #888;')
    #         elif self.ui.btn_faculty_mkn.text() == self.name_faculties[i]:
    #             self.ui.btn_faculty_mkn.setStyleSheet('background-color: #888;')
    #         elif self.ui.btn_faculty_moais.text() == self.name_faculties[i]:
    #             self.ui.btn_faculty_moais.setStyleSheet('background-color: #888;')
    #         elif self.ui.btn_faculty_pi.text() == self.name_faculties[i]:
    #             self.ui.btn_faculty_pi.setStyleSheet('background-color: #888;')
    #         elif self.ui.btn_faculty_pmi.text() == self.name_faculties[i]:
    #             self.ui.btn_faculty_pmi.setStyleSheet('background-color: #888;')
    #         else:
    #             self.ui.btn_faculty_prog_in.setStyleSheet('background-color: #888;')
        

    def transition(self) -> None:
        if len(self.name_faculties) == 3:
            selection = {
                "facultets" : self.name_faculties
            }
            with open('json_inf.json', encoding='utf8') as file:
                data = json.load(file)
                data["information"].append(selection)
                with open('json_inf.json', 'w', encoding='utf8') as outfile:
                    json.dump(data, outfile, ensure_ascii=False)
            self.output = SelectionFirstFaculties()
            self.close()
            self.output.show()



class SelectionFirstFaculties(QWidget):
    def __init__(self):
        super(SelectionFirstFaculties, self).__init__()
        self.ui = Ui_Form_First()
        self.ui.setupUi(self)
        with open(r'/Users/fanfurick/Documents/code/educational practice/json_inf.json') as file:
            json_faculties = json.load(file)
        self.text_button_faculties(json_faculties)
        self.number_faculty = ''

        self.ui.btn_faculty_1.clicked.connect(self.faculty_selection)
        self.ui.btn_faculty_2.clicked.connect(self.faculty_selection)
        self.ui.btn_facultyi_3.clicked.connect(self.faculty_selection)
        self.ui.pushButton.clicked.connect(self.moving_results)

        QFontDatabase.addApplicationFont(r"/Users/fanfurick/Documents/code/educational practice/designer/Open_Sans (1)/static/OpenSans/OpenSans-Medium.ttf")


    def text_button_faculties(self, json_faculties) -> None:
        self.ui.btn_faculty_1.setText(json_faculties['information'][1]['facultets'][0])
        self.ui.btn_faculty_2.setText(json_faculties['information'][1]['facultets'][1])
        self.ui.btn_facultyi_3.setText(json_faculties['information'][1]['facultets'][2])


    def faculty_selection(self) -> None:
        btn = self.sender()

        btn_name = ['btn_faculty_1', 'btn_faculty_2', 'btn_facultyi_3']

        if btn.objectName() in btn_name:
            if btn.text()[:8] == self.number_faculty:
                self.number_faculty = ''
            else:
                self.number_faculty = btn.text()[:8]

    
    def moving_results(self) -> None:
        self.output = ResultWindow(self.number_faculty)
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
        self.when_confirming = ""
        self.total_points = ""
        self.total_score = 0

        with open(r'/Users/fanfurick/Documents/code/educational practice/json_inf.json') as file:
            json_inn = json.load(file)
        for number in faculties:
            if number[:8] == self.number_faculty:
                self.faculties = number
                break
        self.request_dvfu_false_consent(json_inn)
        self.request_dvfu_true_consent()

        self.ui.label_2.setText("Ваши баллы - " + self.scores)
        self.ui.label_3.setText("- на " + str(self.place) + "/" + self.total + " месте")
        self.ui.label_4.setText("- на " + str(self.when_confirming) + "/" + self.total + " при подаче заявления")
        self.ui.label_5.setText(str(self.total_points) + " баллов для точного прохождения на бюджет")

        self.ui.pushButton.clicked.connect(self.go_back_selection)

        QFontDatabase.addApplicationFont(r"/Users/fanfurick/Documents/code/educational practice/designer/Open_Sans (1)/static/OpenSans/OpenSans-Medium.ttf")


    def request_dvfu_false_consent(self, json_inn) -> None:
        self.current_data = request_data
        self.current_data['trainingDirection'] = self.faculties
        self.current_data['consent'] = 'false'
        responce = requests.post('https://www.dvfu.ru/bitrix/services/main/ajax.php', params=request_parametrs, headers=user_agent, data=self.current_data).json()
        self.data = responce.get('data')
        for applicans in self.data:
            if json_inn['information'][0]['inn'] == applicans.get('name') and applicans.get('category') == "На общих основаниях":
                self.place = int(float(applicans.get('GENERALORDER')))
                self.total = applicans.get('bm')
                self.scores = applicans.get('scoreSum')


    def request_dvfu_true_consent(self) -> None:
        self.current_data = request_data
        self.current_data['trainingDirection'] = self.faculties
        self.current_data['consent'] = 'true'
        responce = requests.post('https://www.dvfu.ru/bitrix/services/main/ajax.php', params=request_parametrs, headers=user_agent, data=self.current_data).json()
        self.data = responce.get('data')
        for applicans in self.data:
            if applicans.get('scoreSum') != '-':
                self.total_score += int(applicans.get('scoreSum'))
        self.total_points = int(self.total_score / len(self.data))
        self.when_confirming = len(self.data) + 1


    def go_back_selection(self) -> None:
        self.output = SelectionFirstFaculties()
        self.close()
        self.output.show()


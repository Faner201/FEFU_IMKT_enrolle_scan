import imp
from sqlite3 import apilevel
from numpy import average
import requests, json
from data import faculties,user_agent, request_parametrs, request_data

result = {}
consent_order = []
general_order = []
original_order = []
name = []
score_sum = []
total_score = 0
average_score = 0

print("Выберети цифрой один из факультетов:ПИ, МОАИС, МКН, Прогинж, ПМИ, ИСТ, ИБ, КБ")
choice = int(input())
print("Выберите цифрой наличие согласия : \n1)Да \n2)Нет")
availability_consent = int(input())
consent = 'true' if availability_consent == 1 else 'false'

current_data = request_data
current_data['trainingDirection'] = faculties[choice - 1]
current_data['consent'] = consent

responce = requests.post('https://www.dvfu.ru/bitrix/services/main/ajax.php', params=request_parametrs, headers=user_agent, data=current_data).json()
data = responce.get('data')
for applicans in data:
    if applicans.get('category') == "На общих основаниях":
        name.append(applicans.get('name'))
        score_sum.append(applicans.get('scoreSum'))
        general_order.append(int(float(applicans.get('GENERALORDER'))))
        if consent == 'true':
            consent_order.append(int(float(applicans.get('CONSENTORDER'))))
            original_order.append(int(float(applicans.get('ORIGINALORDER'))))
            total_score += int(applicans.get('scoreSum'))

average_score = int(total_score / len(data))

for i in range(general_order[-1]):
    if consent == 'true':
        print(
            "consent =", consent_order[i], " ", 
            "general =", general_order[i], " ",
            "original =", original_order[i], " ",
            "name =", name[i], " ", 
            "score_sum =", score_sum[i], " ",
            "average_score =", average_score
        )
    else:
        print(
            "general =", general_order[i], " ",
            "name =", name[i], " ",
            "score_sum =", score_sum[i], " ",
        )



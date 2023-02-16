import json
import time
import datetime

import requests

sair = False
while not False:
    req = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = json.loads(req.text)

    print('Data e horário: ', datetime.datetime.now())
    print('COTAÇÃO DO DÓLAR')
    print(cotacao['USDBRL']['name'] + '- Valor maximo: ' + cotacao['USDBRL']['high'] + ' Valor minimo: ' + cotacao['USDBRL']['low'])
    print('COTAÇÃO DO EURO')
    print(cotacao['EURBRL']['name'] + '- Valor maximo: ' + cotacao['EURBRL']['high'] + ' Valor minimo: ' + cotacao['EURBRL']['low'])
    print('COTAÇÃO DO  BITCOIN')
    print(cotacao['BTCBRL']['name'] + '- Valor maximo: ' + cotacao['BTCBRL']['high'] + ' Valor minimo: ' + cotacao['BTCBRL']['low'])
    time.sleep(3)
def getcards(text:str):
    import re
    text = text.replace('\n', ' ').replace('\r', '')
    card = re.findall(r"[0-9]+", text)
    if not card or len(card) < 3:
        return
    if len(card) == 3:
        cc = card[0]
        if len(card[1]) == 3:
            mes = card[2][:2]
            ano = card[2][2:]
            cvv = card[1]
        else:
            mes = card[1][:2]
            ano = card[1][2:]
            cvv = card[2]
    else:
        cc = card[0]
        if len(card[1]) == 3:
            mes = card[2]
            ano = card[3]
            cvv = card[1]
        else:
            mes = card[1]
            ano = card[2]
            cvv = card[3]
        if  len(mes) == 2 and (mes > '12' or mes < '01'):
            ano1 = mes
            mes = ano
            ano = ano1
    if cc[0] == 3 and len(cc) != 15 or len(cc) != 16 or int(cc[0]) not in [3,4,5,6]:
        return
    if len(mes) not in [2 , 4] or len(mes) == 2 and mes > '12' or len(mes) == 2 and mes < '01':
        return
    if len(ano) not in [2,4] or len(ano) == 2 and ano < '21' or len(ano)  == 4 and ano < '2021' or len(ano) == 2 and ano > '39' or len(ano)  == 4 and ano > '2039':
        return
    if cc[0] == 3 and len(cvv) != 4 or len(cvv) != 3:
        return
    if (cc,mes,ano,cvv):
        return cc,mes,ano,cvv
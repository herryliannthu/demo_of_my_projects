import json
import random
import tkinter as tk
import tkinter.messagebox
from tempfile import TemporaryFile
from xlwt import Workbook
#德莫克拉希
data_1 = {"N":{"Value":100,"Money":10},"I":{"Value":100,"Money":10},"A":{"Value":100,"Money":10},"B":{"Value":100,"Money":10},"D":100}
#福利丹尼國
data_2 = {"N":{"Value":100,"Money":10},"I":{"Value":100,"Money":10},"A":{"Value":100,"Money":10},"B":{"Value":100,"Money":10},"D":100}
#禮畢爾提國
data_3 = {"N":{"Value":100,"Money":10},"I":{"Value":100,"Money":10},"A":{"Value":100,"Money":10},"B":{"Value":100,"Money":10},"D":100}
#迪泰特國
data_4 = {"N":{"Value":100,"Money":10},"I":{"Value":100,"Money":10},"A":{"Value":100,"Money":10},"B":{"Value":100,"Money":10},"D":100}
#山卓雷斯國
data_5 = {"N":{"Value":100,"Money":10},"I":{"Value":100,"Money":10},"A":{"Value":100,"Money":10},"B":{"Value":100,"Money":10},"D":100}
#因迪凡卓拉森國
data_6 = {"N":{"Value":100,"Money":10},"I":{"Value":100,"Money":10},"A":{"Value":100,"Money":10},"B":{"Value":100,"Money":10},"D":100}
Country_list = [data_1,data_2,data_3,data_4,data_5,data_6]
#山桌雷

def rank_country(Country):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    c_c = [data_1,data_2,data_3,data_4,data_5,data_6]
    l = []
    result = 0
    for i in c_c:
        l.append(i["D"])
    l.sort()
    l.reverse()
    print (l)
    for i in range(len(l)):
        if (Country["D"] == l[i]):
            result = i
    print (result)
    return result
def Select_1(Choice,Country):
    if (Choice == 1):
        Country["A"]["Value"]+=10
    elif (Choice == 2):
        Country["B"]["Value"]+=20
        for people in Country:
            if (people == "D"):
                pass
            else:
                Country[people]["Value"]-=10
    elif(Choice == 0):
        pass
    elif(Choice == -1):
        for people in Country:
            if (people == "D"):
                pass
            else:
                Country[people]["Value"]-=10
    else:
        print ("Error !! Your choice {} is not allowed".format(Choice))
        return None
def Select_2(Choice,Country):
    if (Choice == 1):
        Country["I"]["Value"]+=10
        Country["N"]["Value"]-=30
        for people in Country:
            if (people == "D"):
                pass
            else:
                Country[people]["Money"]-=1
    elif (Choice == 2):
        Country["N"]["Value"]+=20
        Country["I"]["Value"]-=30
        for people in Country:
            if (people == "D"):
                pass
            else:
                Country[people]["Money"]-=2
    elif(Choice == 0):
        pass
    elif(Choice == -1):
        for people in Country:
            if (people == "D"):
                pass
            else:
                Country[people]["Value"]-=10
    else:
        print ("Error !! Your choice {} is not allowed".format(Choice))
        return None
    return Country
def Select_3(Choice,Country):
    if (Choice == 1):
        Country["A"]["Value"]+=20
        Country["N"]["Value"]-=40
    elif (Choice == 2):
        Country["N"]["Value"]+=10
        Country["A"]["Value"]-=30
        Country["N"]["Value"]-=20
    elif(Choice == 0):
        pass
    elif(Choice == -1):
        for people in Country:
            if (people == "D"):
                pass
            else:
                Country[people]["Value"]-=10
    else:
        print ("Error !! Your choice {} is not allowed".format(Choice))
        return None
    return Country
def Select_4(Choice,Country):
    if (Choice == 1):
        Country["I"]["Value"]+=30
        Country["B"]["Value"]-=30
        Country["B"]["Value"]-=20
    elif (Choice == 2):
        Country["B"]["Value"]+=30
        Country["I"]["Value"]-=40
    elif(Choice == 0):
        pass
    elif(Choice == -1):
        for people in Country:
            if (people == "D"):
                pass
            else:
                Country[people]["Value"]-=10
    else:
        print ("Error !! Your choice {} is not allowed".format(Choice))
        return None
    return Country
def Select_5(Choice,Country):
    if (Choice == 1):
        Country["I"]["Value"]+=40
        Country["A"]["Value"]-=10
        Country["B"]["Value"]+=10
    elif (Choice == 2):
        Country["N"]["Value"]+=30
        for people in Country:
            if (people == "D"):
                pass
            else:
                if (Country[people]["Money"]>=10):
                    Country[people]["Money"]-=2
                elif(Country[people]["Money"]<10):
                    Country[people]["Money"]+=1
    elif(Choice == 0):
        pass
    elif(Choice == -1):
        for people in Country:
            if (people == "D"):
                pass
            else:
                Country[people]["Value"]-=10
    else:
        print ("Error !! Your choice {} is not allowed".format(Choice))
        return None
    return Country
def Select_6(Choice,Country):
    if (Choice == 1):
        Country["A"]["Value"]+=40
        Country["B"]["Value"]-=40
    elif (Choice == 2):
        Country["I"]["Value"]+=20
        Country["B"]["Value"]-=10
        Country["B"]["Value"]-=10
        Country["A"]["Value"]+=20
        #Country["I"]["Value"]+=20
    elif(Choice == 0):
        pass
    elif(Choice == -1):
        for people in Country:
            if (people == "D"):
                pass
            else:
                Country[people]["Value"]-=10
    else:
        print ("Error !! Your choice {} is not allowed".format(Choice))
        return None
    return Country
def Select_7(Choice,Country):
    if (Choice == 1):
        Country["I"]["Value"]+=20
        Country["A"]["Value"]-=40
        Country["N"]["Value"]+=20
        Country["B"]["Value"]+=20
        #Country["N"]["Value"]+=20
        #Country["B"]["Value"]+=20
    elif (Choice == 2):
        Country["A"]["Value"]+=30
        Country["I"]["Value"]-=30
    elif(Choice == 0):
        pass
    elif(Choice == -1):
        for people in Country:
            if (people == "D"):
                pass
            else:
                Country[people]["Value"]-=10
    else:
        print ("Error !! Your choice {} is not allowed".format(Choice))
        return None
    return Country
def Select_8(Choice,Country):
    if (Choice == 1):
        Country["B"]["Value"]+=10
        Country["N"]["Value"]-=30
    elif (Choice == 2):
        Country["N"]["Value"]+=40
        Country["B"]["Value"]-=30
    elif(Choice == 0):
        pass
    elif(Choice == -1):
        for people in Country:
            if (people == "D"):
                pass
            else:
                Country[people]["Value"]-=10
    else:
        print ("Error !! Your choice {} is not allowed".format(Choice))
        return None
    return Country
def N_select_1(Choice,Country):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    if (Country == data_1):
        if (Choice == 2): #迪泰特 C
            data_4["N"]["Value"]+=20
            data_1["N"]["Value"]-=20
        elif (Choice == 1): #福利丹尼 A
            data_2["D"]-=20
            data_1["D"]+=30
        else :
            print ("N_select_1:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_2):
        if (Choice == 1): #迪泰特 A
            data_4["D"]-=20
            data_2["D"]+=30
        elif (Choice == 2): #因迪凡 C
            data_6["N"]["Value"]+=20
            data_2["N"]["Value"]-=20
        else :
            print ("N_select_1:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_3):
        if (Choice == 2): #福利丹 C
            data_2["N"]["Value"]+=20
            data_3["N"]["Value"]-=20
        elif (Choice == 1): #德莫克 A
            data_1["D"]-=20
            data_3["D"]+=30
        else :
            print ("N_select_1:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_4):
        if (Choice == 1): # 因迪凡 A
            data_6["D"]-=20
            data_4["D"]+=30
        elif (Choice == 2): #山卓 C
            data_5["N"]["Value"]+=20
            data_4["N"]["Value"]-=20
        else :
            print ("N_select_1:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_5):
        if (Choice == 2): #德莫 C
            data_1["N"]["Value"]+=20
            data_5["N"]["Value"]-=20
        elif (Choice == 1): #禮畢 A
            data_3["D"]-=20
            data_5["D"]+=30
        else :
            print ("N_select_1:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_6):
        if (Choice == 1): #山卓 A
            data_5["D"]-=20
            data_6["D"]+=30
        elif (Choice == 2): #禮畢 C
            data_3["N"]["Value"]+=20
            data_6["N"]["Value"]-=20
        else :
            print ("N_select_1:Error !! Your choice {} is not allowed".format(Choice))
    else :
        print ("N_select_1:Error !! Your choice {} is not allowed".format(Country))
def N_select_2(Choice,Country):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    if (Country == data_1):
        if (Choice == 2): #禮畢 A
            data_1["D"]+=20
        elif (Choice == 1): #山卓 B
            data_5["D"]-=10
            data_5["B"]["Value"]+=30
            data_1["D"]-=10
            data_1["B"]["Value"]+=30
        else :
            print ("N_select_2:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_2):
        if (Choice == 1): #德莫 A
            data_1["D"]-=20
            data_2["D"]+=30
        elif (Choice == 2): #禮畢 B
            data_3["A"]["Value"]+=30
            data_2["A"]["Value"]-=10
            data_2["N"]["Value"]-=10
            data_2["D"]-=10
        else :
            print ("N_select_2:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_3):
        if (Choice == 2): #因迪 B
            data_6["A"]["Value"]+=30
            data_3["A"]["Value"]-=10
            data_3["N"]["Value"]-=10
            data_3["D"]-=10
        elif (Choice == 1): #山卓 A
            data_5["D"]-=20
            data_3["D"]+=30
        else :
            print ("N_select_2:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_4):
        if (Choice == 2): #福利 A
            data_4["D"]+=20
        elif (Choice == 1): #德莫 B
            data_1["D"]-=10
            data_1["B"]["Value"]+=30
            data_4["D"]-=10
            data_4["B"]["Value"]+=30
        else :
            print ("N_select_2:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_5):
        if (Choice == 1): #迪泰 B
            data_4["D"]-=10
            data_4["B"]["Value"]+=30
            data_5["D"]-=10
            data_5["B"]["Value"]+=30
        elif (Choice == 2): #因迪 A
            data_5["D"]+=20
        else :
            print ("N_select_2:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_6):
        if (Choice == 1): #迪泰 A
            data_6["D"]+=20
        elif (Choice == 2): #福利 B
            data_2["D"]-=10
            data_2["B"]["Value"]+=30
            data_6["D"]-=10
            data_6["B"]["Value"]+=30
        else :
            print ("N_select_2:Error !! Your choice {} is not allowed".format(Choice))
    else :
        print ("N_select_2:Error !! Your choice {} is not allowed".format(Country))
def N_select_3(Result,Choice,Country):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    if (Result == 2):
        if (Choice == 1):
            Country["D"]-=20
        elif (Choice == 2):
            for prople in Country:
                if (prople == "D"):
                    Country["D"]+=20
                else:
                    Country[prople]["Value"]-=10
    elif (Result == 3):
        if (Choice == 1):
            for prople in Country:
                if (prople == "D"):
                    Country["D"]-=20
                else:
                    Country[prople]["Value"]+=10
        elif (Choice == 2):
            Country["D"]+=20
    elif (Result == 1):
        if (rank_country(Country) == 0 or rank_country(Country) == 1):
            pass
        elif (rank_country(Country) == 2 or rank_country(Country) == 3 ):
            for prople in Country:
                if (prople == "D"):
                    pass
                else:
                    Country[prople]["Value"]-=10
        elif (rank_country(Country) == 4 or rank_country(Country) == 5 ):
            for prople in Country:
                if (prople == "D"):
                    pass
                else:
                    Country[prople]["Value"]-=20
    else:
        print ("N_select_3:Error !! Your choice {} is not allowed".format(Choice))
def N_select_4(Choice,Country):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    if (Country == data_1):
        if (Choice == 2): #禮畢 C
            data_3["A"]["Value"]+=20
            data_3["N"]["Value"]+=20
            data_3["I"]["Value"]+=20
            data_3["B"]["Value"]+=20
            data_1["A"]["Value"]-=10
            data_1["I"]["Value"]-=10
            data_1["B"]["Value"]-=10
        elif (Choice == 1): #福利 B
            data_2["D"]-=10
            data_1["D"]-=10
            data_2["I"]["Value"]+=20
            data_2["A"]["Value"]+=20
            data_1["I"]["Value"]+=20
            data_1["A"]["Value"]+=20
        else :
            print ("N_select_4:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_2):
        if (Choice == 1): #迪泰 B
            data_4["D"]-=10
            data_4["I"]["Value"]+=20
            data_4["A"]["Value"]+=20
            data_2["D"]-=10
            data_2["I"]["Value"]+=20
            data_2["A"]["Value"]+=20
        elif (Choice == 2): #德莫 C
            data_1["D"]-=10
            data_1["B"]["Value"]-=10
            data_1["A"]["Value"]-=10
            data_1["I"]["Value"]-=10
            data_1["N"]["Value"]-=10
        else :
            print ("N_select_4:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_3):
        if (Choice == 2): #山卓 C
            data_5["I"]["Value"]-=10
            data_5["A"]["Value"]-=10
            data_5["N"]["Value"]-=10
            data_5["B"]["Value"]-=10
        elif (Choice == 1): #德莫 B
            data_1["D"]-=10
            data_1["I"]["Value"]+=20
            data_1["A"]["Value"]+=20
            data_3["D"]-=10
            data_3["I"]["Value"]+=20
            data_3["A"]["Value"]+=20
        else :
            print ("N_select_4:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_4):
        if (Choice == 1): #因迪 B
            data_6["D"]-=10
            data_6["I"]["Value"]+=20
            data_6["A"]["Value"]+=20
            data_4["D"]-=10
            data_4["I"]["Value"]+=20
            data_4["A"]["Value"]+=20
        elif (Choice == 2): # 福利 C
            data_2["N"]["Value"]+=20
            data_2["B"]["Value"]+=20
            data_2["A"]["Value"]+=20
            data_2["I"]["Value"]+=20
            data_4["A"]["Value"]-=10
            data_4["I"]["Value"]-=10
            data_4["B"]["Value"]-=10
        else :
            print ("N_select_4:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_5):
        if (Choice == 1): #禮畢 B
            data_3["D"]-=10
            data_3["I"]["Value"]+=20
            data_3["A"]["Value"]+=20
            data_5["D"]-=10
            data_5["I"]["Value"]+=20
            data_5["A"]["Value"]+=20
        elif (Choice == 2): #因迪 C
            data_6["I"]["Value"]+=20
            data_6["B"]["Value"]+=20
            data_6["N"]["Value"]+=20
            data_6["A"]["Value"]+=20
            data_5["I"]["Value"]-=10
            data_5["A"]["Value"]-=10
            data_5["B"]["Value"]-=10
        else :
            print ("N_select_4:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_6):
        if (Choice == 1): #迪泰 C
            data_4["N"]["Value"]+=20
            data_4["I"]["Value"]+=20
            data_4["B"]["Value"]+=20
            data_4["A"]["Value"]+=20
            data_6["A"]["Value"]-=10
            data_6["B"]["Value"]-=10
            data_6["I"]["Value"]-=10
        elif (Choice == 2): #山卓 B
            data_5["D"]-=10
            data_5["I"]["Value"]+=20
            data_5["A"]["Value"]+=20
            data_6["D"]-=10
            data_6["I"]["Value"]+=20
            data_6["A"]["Value"]+=20
        else :
            print ("N_select_4:Error !! Your choice {} is not allowed".format(Choice))
    else :
        print ("N_select_4:Error !! Your choice {} is not allowed".format(Country))
def N_select_5(Choice,Country):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    if (Country == data_1):
        if (Choice == 2): #理畢爾 B
            data_1["A"]["Value"]-=10
            data_1["B"]["Value"]-=10
            data_1["I"]["Value"]-=10
            data_3["A"]["Value"]+=20
            data_3["B"]["Value"]+=20
            data_3["I"]["Value"]+=20
        elif (Choice == 1): # 山卓 C
            data_5["I"]["Value"]-=10
            data_5["A"]["Value"]-=10
            data_5["B"]["Value"]-=10
            data_5["N"]["Value"]-=10
        else :
            print ("N_select_5:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_2):
        if (Choice == 2): #因迪 B
            data_6["D"]+=40
            data_6["B"]["Value"]+=20
            data_2["D"]+=40
            data_2["B"]["Value"]+=20
        elif (Choice == 1): #禮畢 C
            data_3["A"]["Value"]+=20
            data_3["I"]["Value"]+=20
            data_3["N"]["Value"]+=20
            data_3["B"]["Value"]+=20
            data_2["A"]["Value"]+=20
            data_2["I"]["Value"]+=20
            data_2["B"]["Value"]+=20
        else :
            print ("N_select_5:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_3):
        if (Choice == 2): #福利 B
            data_2["D"]+=40
            data_2["B"]["Value"]+=20
            data_3["D"]+=40
            data_3["B"]["Value"]+=20
        elif (Choice == 1): # 因迪 C
            data_6["I"]["Value"]+=20
            data_6["B"]["Value"]+=20
            data_6["A"]["Value"]+=20
            data_6["N"]["Value"]+=20
            data_3["A"]["Value"]-=10
            data_3["I"]["Value"]-=10
            data_3["B"]["Value"]-=10

        else :
            print ("N_select_5:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_4):
        if (Choice == 2): #山卓 B
            data_5["D"]+=40
            data_5["B"]["Value"]+=20
            data_4["D"]+=40
            data_4["B"]["Value"]+=20
        elif (Choice == 1): # 德莫 C
            data_1["I"]["Value"]-=10
            data_1["A"]["Value"]-=10
            data_1["N"]["Value"]-=10
            data_1["B"]["Value"]-=10
        else :
            print ("N_select_5:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_5):
        if (Choice == 1): # 迪泰 C
            data_4["I"]["Value"]-=10
            data_4["A"]["Value"]-=10
            data_4["N"]["Value"]-=10
            data_4["B"]["Value"]-=10
        elif (Choice == 2): # 福利丹 C
            data_2["A"]["Value"]-=20
            data_2["I"]["Value"]-=20
            data_2["N"]["Value"]-=20
            data_2["B"]["Value"]-=20
            data_5["I"]["Value"]+=10
            data_5["A"]["Value"]+=10
            data_5["N"]["Value"]+=10
            data_5["B"]["Value"]+=10

        else :
            print ("N_select_5:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_6):
        if (Choice == 1): # 福利 C
            data_2["A"]["Value"]-=10
            data_2["I"]["Value"]-=10
            data_2["N"]["Value"]-=10
            data_2["B"]["Value"]-=10
        elif (Choice == 2): # 禮畢 B
            data_3["D"]+=40
            data_3["B"]["Value"]+=20
            data_6["D"]+=40
            data_6["B"]["Value"]+=20
        else :
            print ("N_select_5:Error !! Your choice {} is not allowed".format(Choice))
    else :
        print ("N_select_5:Error !! Your choice {} is not allowed".format(Country))
def N_select_6(List_Choice):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    c_c = [data_1,data_2,data_3,data_4,data_5,data_6]
    team_1 = 0
    team_2 = 0
    for i in List_Choice:
        if (i == 1):
            team_1 += 1
        elif (i == 2):
            team_2 += 1
    if (abs(team_1 - team_2) >= 4):
        for Country in c_c:
            if (rank_country(Country) == 0 or rank_country(Country) == 1):
                pass
            elif (rank_country(Country) == 2 or rank_country(Country) == 3 ):
                for prople in Country:
                    if (prople == "D"):
                        pass
                    else:
                        Country[prople]["Value"]-=10
            elif (rank_country(Country) == 4 or rank_country(Country) == 5 ):
                for prople in Country:
                    if (prople == "D"):
                        pass
                    else:
                        Country[prople]["Value"]-=20
    else:
        team_1_D = 0
        team_2_D = 0
        for i in range(6):
            if (List_Choice[i] == 1):
                team_1_D += c_c[i]["D"]
            elif (List_Choice[i] == 2):
                team_2_D += c_c[i]["D"]
        if (team_1_D/team_1 > team_2_D/team_2):
            for i in range(6):
                if (List_Choice[i] == 1):
                    c_c[i]["D"] -=10
                elif (List_Choice[i] == 2):
                    c_c[i]["D"] -= 20
        elif (team_1_D/team_1 < team_2_D/team_2):
            for i in range(6):
                if (List_Choice[i] == 1):
                    c_c[i]["D"] -=20
                elif (List_Choice[i] == 2):
                    c_c[i]["D"] -= 10
        elif (team_1_D/team_1 == team_2_D/team_2):
            pass
    print ('N_select_6 good')


def N_select_7(Choice,Country):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    if (Country == data_1):
        if (Choice == 2): # 因迪 C
            data_6["I"]["Value"]-=20
            data_6["A"]["Value"]-=20
            data_6["N"]["Value"]-=20
            data_6["B"]["Value"]-=20
            data_1["B"]["Value"]+=10
            data_1["A"]["Value"]+=10
            data_1["N"]["Value"]+=10
            data_1["I"]["Value"]+=10
        elif (Choice == 1): # 山卓 A
            data_5["D"]-=20
            data_1["D"]+=30
        else :
            print ("N_select_7:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_2):
        if (Choice == 1): # 山卓 C
            data_5["I"]["Value"]-=20
            data_5["B"]["Value"]-=20
            data_5["A"]["Value"]-=20
            data_5["N"]["Value"]-=20
            data_2["N"]["Value"]+=10
            data_2["A"]["Value"]+=10
            data_2["I"]["Value"]+=10
            data_2["B"]["Value"]+=10
        elif (Choice == 2): # 禮畢 A
            data_2["D"]+=20
        else :
            print ("N_select_7:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_3):
        if (Choice == 2): #因迪 A
            data_3["D"]+=20
        elif (Choice == 1): # 迪泰 C
            data_4["A"]["Value"]-=20
            data_4["I"]["Value"]-=20
            data_4["N"]["Value"]-=20
            data_4["B"]["Value"]-=20
            data_3["B"]["Value"]+=10
            data_3["I"]["Value"]+=10
            data_3["A"]["Value"]+=10
            data_3["N"]["Value"]+=10
        else :
            print ("N_select_7:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_4):
        if (Choice == 2): # 禮畢 C
            data_3["I"]["Value"]-=20
            data_3["A"]["Value"]-=20
            data_3["B"]["Value"]-=20
            data_3["N"]["Value"]-=20
            data_4["I"]["Value"]+=10
            data_4["N"]["Value"]+=10
            data_4["B"]["Value"]+=10
            data_4["A"]["Value"]+=10
        elif (Choice == 1): # 德莫 A
            data_1["D"]-=20
            data_4["D"]+=30
        else :
            print ("N_select_7:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_5):
        if (Choice == 2): #福利 C
            data_2["D"]+=30
            data_5["D"]+=30
        elif (Choice == 1): # 迪泰 A
            data_4["D"]-=40
            data_5["D"]+=30
        else :
            print ("N_select_7:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_6):
        if (Choice == 2): #福利 A
            data_2["D"]-=20
            data_6["D"]+=30
        elif (Choice == 1): # 德莫 C
            data_1["I"]["Value"]-=20
            data_1["N"]["Value"]-=20
            data_1["A"]["Value"]-=20
            data_1["B"]["Value"]-=20
            data_6["I"]["Value"]+=10
            data_6["A"]["Value"]+=10
            data_6["B"]["Value"]+=10
            data_6["N"]["Value"]+=10
        else :
            print ("N_select_7:Error !! Your choice {} is not allowed".format(Choice))
    else :
        print ("N_select_7:Error !! Your choice {} is not allowed".format(Country))
def N_select_8(Choice,Country):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    if (Country == data_1):
        if (Choice == 1): # 因迪 A
            data_6["D"]+=30
            data_1["D"]+=30
        elif (Choice == 2): # 禮畢 B
            data_3["A"]["Value"]+=30
            data_1["A"]["Value"]-=10
            data_1["N"]["Value"]-=10
            data_1["D"]-=10
        else :
            print ("N_select_8:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_2):
        if (Choice == 2): # 山卓 A
            data_5["D"]+=30
            data_2["D"]+=30
        elif (Choice == 1): # 德莫 B
            data_1["I"]["Value"]-=10
            data_1["A"]["Value"]-=10
            data_1["B"]["Value"]-=10
            data_1["N"]["Value"]-=10
        else :
            print ("N_select_8:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_3):
        if (Choice == 2): #迪泰 A
            data_4["D"]+=30
            data_3["D"]+=30
        elif (Choice == 1): # 山卓 B
            data_5["D"]-=10
            data_5["B"]["Value"]+=30
            data_3["D"]-=10
            data_3["B"]["Value"]+=30
        else :
            print ("N_select_8:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_4):
        if (Choice == 1): # 禮畢 A
            data_3["D"]+=30
            data_4["D"]+=30
        elif (Choice == 2): # 福利 B
            data_2["A"]["Value"]+=30
            data_4["A"]["Value"]-=10
            data_4["N"]["Value"]-=10
            data_4["D"]-=10
        else :
            print ("N_select_8:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_5):
        if (Choice == 2): # 德莫 A
            data_5["D"]+=40
            data_5["B"]["Value"]+=20
            data_1["D"]+=40
            data_1["B"]["Value"]+=20
        elif (Choice == 1): # 因迪 B
            data_6["A"]["Value"]+=30
            data_5["A"]["Value"]-=10
            data_5["N"]["Value"]-=10
            data_5["D"]-=10
        else :
            print ("N_select_8:Error !! Your choice {} is not allowed".format(Choice))
    elif (Country == data_6):
        if (Choice == 2): # 迪泰 B
            data_4["A"]["Value"]+=30
            data_6["A"]["Value"]-=10
            data_6["N"]["Value"]-=10
            data_6["D"]-=10
        elif (Choice == 1): # 德莫 A
            data_1["D"]+=30
            data_6["D"]+=30
        else :
            print ("N_select_8:Error !! Your choice {} is not allowed".format(Choice))
    else :
        print ("N_select_8:Error !! Your choice {} is not allowed".format(Country))
def r():
    return random.randint(1,2)
#德莫克拉希
#福利丹尼國
#禮畢爾提國
#迪泰特國
#山卓雷斯國
#因迪凡卓拉森國
def print_country(round):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    print ("---------這是第",round,"回合--------------\n")
    print ("德莫克拉希")
    print ("農業數值",data_1["A"]["Value"]," 工業數值",data_1["I"]["Value"]," 商業數值",data_1["B"]["Value"]," 天然業數值",data_1["N"]["Value"]," 國防",data_1["D"])
    print ("\n")
    print ("福利丹尼國")
    print ("農業數值",data_2["A"]["Value"]," 工業數值",data_2["I"]["Value"]," 商業數值",data_2["B"]["Value"]," 天然業數值",data_2["N"]["Value"]," 國防",data_2["D"])
    print ("\n")
    print ("禮畢爾提國")
    print ("農業數值",data_3["A"]["Value"]," 工業數值",data_3["I"]["Value"]," 商業數值",data_3["B"]["Value"]," 天然業數值",data_3["N"]["Value"]," 國防",data_3["D"])
    print ("\n")
    print ("迪泰特國")
    print ("農業數值",data_4["A"]["Value"]," 工業數值",data_4["I"]["Value"]," 商業數值",data_4["B"]["Value"]," 天然業數值",data_4["N"]["Value"]," 國防",data_4["D"])
    print ("\n")
    print ("山卓雷斯國")
    print ("農業數值",data_5["A"]["Value"]," 工業數值",data_5["I"]["Value"]," 商業數值",data_5["B"]["Value"]," 天然業數值",data_5["N"]["Value"]," 國防",data_5["D"])
    print ("\n")
    print ("因迪凡卓拉森國")
    print ("農業數值",data_6["A"]["Value"]," 工業數值",data_6["I"]["Value"]," 商業數值",data_6["B"]["Value"]," 天然業數值",data_6["N"]["Value"]," 國防",data_6["D"])
    print ("\n")
    print ("---------這是第",round,"回合--------------\n")

def result_32(a,b,c,d,f,g):
    l = [a,b,c,d,f,g]
    restrict = 0
    non_restrict = 0
    for i in l:
        if (i == 1):
            restrict += 1
        elif (i == 2):
            non_restrict += 1
    if (restrict > non_restrict):
        return 2
    elif (non_restrict > restrict):
        return 3
    elif (non_restrict == restrict):
        return 1



def print_country_tk(round):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    s = "---------這是第"+str(round)+"回合--------------"+"\n\n德莫克拉希\n農業數值"+str(data_1["A"]["Value"])+" 工業數值"+str(data_1["I"]["Value"])+" 商業數值"+str(data_1["B"]["Value"])+" 天然業數值"+str(data_1["N"]["Value"])+" 國防"+str(data_1["D"])
    s =s+"\n\n福利丹尼國\n"+"農業數值"+str(data_2["A"]["Value"])+" 工業數值"+str(data_2["I"]["Value"])+" 商業數值"+str(data_2["B"]["Value"])+" 天然業數值"+str(data_2["N"]["Value"])+" 國防"+str(data_2["D"])
    s = s+"\n\n禮畢爾提國\n"+"農業數值"+str(data_3["A"]["Value"])+" 工業數值"+str(data_3["I"]["Value"])+" 商業數值"+str(data_3["B"]["Value"])+" 天然業數值"+str(data_3["N"]["Value"])+" 國防"+str(data_3["D"])
    s = s+"\n\n迪泰特國\n"+"農業數值"+str(data_4["A"]["Value"])+" 工業數值"+str(data_4["I"]["Value"])+" 商業數值"+str(data_4["B"]["Value"])+" 天然業數值"+str(data_4["N"]["Value"])+" 國防"+str(data_4["D"])
    s = s+"\n\n山卓雷斯國\n"+"農業數值"+str(data_5["A"]["Value"])+" 工業數值"+str(data_5["I"]["Value"])+" 商業數值"+str(data_5["B"]["Value"])+" 天然業數值"+str(data_5["N"]["Value"])+" 國防"+str(data_5["D"])
    s = s+"\n\n因迪凡卓拉森國\n"+"農業數值"+str(data_6["A"]["Value"])+" 工業數值"+str(data_6["I"]["Value"])+" 商業數值"+str(data_6["B"]["Value"])+" 天然業數值"+str(data_6["N"]["Value"])+" 國防"+str(data_6["D"])
    s = s+ "\n\n---------這是第"+str(round)+"回合--------------\n"
    return s

def re_start():
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    data_1 = {"N":{"Value":100,"Money":10},"I":{"Value":100,"Money":10},"A":{"Value":100,"Money":10},"B":{"Value":100,"Money":10},"D":100}
    #福利丹尼國
    data_2 = {"N":{"Value":100,"Money":10},"I":{"Value":100,"Money":10},"A":{"Value":100,"Money":10},"B":{"Value":100,"Money":10},"D":100}
    #禮畢爾提國
    data_3 = {"N":{"Value":100,"Money":10},"I":{"Value":100,"Money":10},"A":{"Value":100,"Money":10},"B":{"Value":100,"Money":10},"D":100}
    #迪泰特國
    data_4 = {"N":{"Value":100,"Money":10},"I":{"Value":100,"Money":10},"A":{"Value":100,"Money":10},"B":{"Value":100,"Money":10},"D":100}
    #山卓雷斯國
    data_5 = {"N":{"Value":100,"Money":10},"I":{"Value":100,"Money":10},"A":{"Value":100,"Money":10},"B":{"Value":100,"Money":10},"D":100}
    #因迪凡卓拉森國
    data_6 = {"N":{"Value":100,"Money":10},"I":{"Value":100,"Money":10},"A":{"Value":100,"Money":10},"B":{"Value":100,"Money":10},"D":100}


country_l = [
'德莫克拉希'
,'福利丹尼國'
,'禮畢爾提國'
,'迪泰特國'
,'山卓雷斯國'
,'因迪凡卓拉森國']

window = tk.Tk()
window.title('My Window')
window.geometry('1700x500')

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas = tk.Canvas(window, borderwidth=0)
frame = tk.Frame(canvas)
vsb = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")


# 第一回合----------------------------------------------------------
l = tk.Label(frame, bg='yellow', text='第一回合').grid(row=0, column=0)
Demo_Dom_C_1 = tk.IntVar()
Demo_Nat_C_1 = tk.IntVar()
Free_Dom_C_1 = tk.IntVar()
Free_Nat_C_1 = tk.IntVar()
Lib_Dom_C_1 = tk.IntVar()
Dec_Dom_C_1 = tk.IntVar()
Cen_Dom_C_1 = tk.IntVar()
Ind_Dom_C_1 = tk.IntVar()
Lib_Nat_C_1 = tk.IntVar()
Dec_Nat_C_1 = tk.IntVar()
Cen_Nat_C_1 = tk.IntVar()
Ind_Nat_C_1 = tk.IntVar()
var_l_Dom_1 = [Demo_Dom_C_1 ,Free_Dom_C_1,Lib_Dom_C_1,Dec_Dom_C_1 ,Cen_Dom_C_1,Ind_Dom_C_1]
var_l_Nat_1 = [Demo_Nat_C_1 ,Free_Nat_C_1,Lib_Nat_C_1,Dec_Nat_C_1 ,Cen_Nat_C_1,Ind_Nat_C_1]

c=1
r=1
for item  in country_l:
    tk.Label(frame, text= item,width = 30 ).grid(row=r, column = c,columnspan=3)
    tk.Label(frame, text='國內政策').grid(row=r+1, column=c)
    tk.Label(frame, text='國外政策').grid(row=r+1, column=c+1)
    c = c + 3

c = 1
for var in var_l_Dom_1:
    tk.Radiobutton(frame, text='-1',variable=var, value = -1).grid(row=r+2, column=c)
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+3, column=c)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+4, column=c)
    c = c + 3
c = 1

for var in var_l_Nat_1:
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+2, column=c+1)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+3, column=c+1)
    c = c + 3

# 第一回合----------------------------------------------------------

# 第二回合----------------------------------------------------------
l = tk.Label(frame, bg='yellow', text='第二回合').grid(row=6, column=0)
Demo_Dom_C_2 = tk.IntVar()
Demo_Nat_C_2 = tk.IntVar()
Free_Dom_C_2 = tk.IntVar()
Free_Nat_C_2 = tk.IntVar()
Lib_Dom_C_2 = tk.IntVar()
Dec_Dom_C_2 = tk.IntVar()
Cen_Dom_C_2 = tk.IntVar()
Ind_Dom_C_2 = tk.IntVar()
Lib_Nat_C_2 = tk.IntVar()
Dec_Nat_C_2 = tk.IntVar()
Cen_Nat_C_2 = tk.IntVar()
Ind_Nat_C_2 = tk.IntVar()
var_l_Dom_2 = [Demo_Dom_C_2 ,Free_Dom_C_2,Lib_Dom_C_2,Dec_Dom_C_2 ,Cen_Dom_C_2,Ind_Dom_C_2]
var_l_Nat_2 = [Demo_Nat_C_2 ,Free_Nat_C_2,Lib_Nat_C_2,Dec_Nat_C_2 ,Cen_Nat_C_2,Ind_Nat_C_2]

c = 1
r = 7
for item  in country_l:
    tk.Label(frame, text= item,width = 30 ).grid(row=r, column = c,columnspan=3)
    tk.Label(frame, text='國內政策').grid(row=r+1 ,column=c)
    tk.Label(frame, text='國外政策').grid(row=r+1, column=c+1)
    c = c + 3

c = 1
for var in var_l_Dom_2:
    tk.Radiobutton(frame, text='-1',variable=var, value = -1).grid(row=r+2, column=c)
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+3, column=c)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+4, column=c)
    c = c + 3
c = 1

for var in var_l_Nat_2:
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+2, column=c+1)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+3, column=c+1)
    c = c + 3

# 第二回合----------------------------------------------------------

# 第三回合----------------------------------------------------------
c = 1
r = 12
l = tk.Label(frame, bg='yellow', text='第三回合').grid(row=r, column=0)
Demo_Dom_C_3 = tk.IntVar()
Demo_Nat_C_3 = tk.IntVar()
Free_Dom_C_3 = tk.IntVar()
Free_Nat_C_3 = tk.IntVar()
Lib_Dom_C_3 = tk.IntVar()
Dec_Dom_C_3 = tk.IntVar()
Cen_Dom_C_3 = tk.IntVar()
Ind_Dom_C_3 = tk.IntVar()
Lib_Nat_C_3 = tk.IntVar()
Dec_Nat_C_3 = tk.IntVar()
Cen_Nat_C_3 = tk.IntVar()
Ind_Nat_C_3 = tk.IntVar()
var_l_Dom_3 = [Demo_Dom_C_3 ,Free_Dom_C_3,Lib_Dom_C_3,Dec_Dom_C_3 ,Cen_Dom_C_3,Ind_Dom_C_3]
var_l_Nat_3 = [Demo_Nat_C_3 ,Free_Nat_C_3,Lib_Nat_C_3,Dec_Nat_C_3 ,Cen_Nat_C_3,Ind_Nat_C_3]
r  = r+1
for item  in country_l:
    tk.Label(frame, text= item,width = 30 ).grid(row=r, column = c,columnspan=3)
    tk.Label(frame, text='國內政策').grid(row=r+1 ,column=c)
    tk.Label(frame, text='國外政策').grid(row=r+1, column=c+1)
    c = c + 3

c = 1
for var in var_l_Dom_3:
    tk.Radiobutton(frame, text='-1',variable=var, value = -1).grid(row=r+2, column=c)
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+3, column=c)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+4, column=c)
    c = c + 3
c = 1

for var in var_l_Nat_3:
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+2, column=c+1)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+3, column=c+1)
    c = c + 3

# 第三回合----------------------------------------------------------

# 第四回合----------------------------------------------------------
c = 1
r = 18
l = tk.Label(frame, bg='yellow', text='第四回合').grid(row=r, column=0)
Demo_Dom_C_4 = tk.IntVar()
Demo_Nat_C_4 = tk.IntVar()
Free_Dom_C_4 = tk.IntVar()
Free_Nat_C_4 = tk.IntVar()
Lib_Dom_C_4 = tk.IntVar()
Dec_Dom_C_4 = tk.IntVar()
Cen_Dom_C_4 = tk.IntVar()
Ind_Dom_C_4 = tk.IntVar()
Lib_Nat_C_4 = tk.IntVar()
Dec_Nat_C_4 = tk.IntVar()
Cen_Nat_C_4 = tk.IntVar()
Ind_Nat_C_4 = tk.IntVar()
var_l_Dom_4 = [Demo_Dom_C_4 ,Free_Dom_C_4,Lib_Dom_C_4,Dec_Dom_C_4 ,Cen_Dom_C_4,Ind_Dom_C_4]
var_l_Nat_4 = [Demo_Nat_C_4 ,Free_Nat_C_4,Lib_Nat_C_4,Dec_Nat_C_4 ,Cen_Nat_C_4,Ind_Nat_C_4]
r  = r+1
for item  in country_l:
    tk.Label(frame, text= item,width = 30 ).grid(row=r, column = c,columnspan=3)
    tk.Label(frame, text='國內政策').grid(row=r+1 ,column=c)
    tk.Label(frame, text='國外政策').grid(row=r+1, column=c+1)
    c = c + 3

c = 1
for var in var_l_Dom_4:
    tk.Radiobutton(frame, text='-1',variable=var, value = -1).grid(row=r+2, column=c)
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+3, column=c)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+4, column=c)
    c = c + 3
c = 1

for var in var_l_Nat_4:
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+2, column=c+1)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+3, column=c+1)
    c = c + 3

# 第四回合----------------------------------------------------------

# 第五回合----------------------------------------------------------
c = 1
r = 24
l = tk.Label(frame, bg='yellow', text='第五回合').grid(row=r, column=0)
Demo_Dom_C_5 = tk.IntVar()
Demo_Nat_C_5 = tk.IntVar()
Free_Dom_C_5 = tk.IntVar()
Free_Nat_C_5 = tk.IntVar()
Lib_Dom_C_5 = tk.IntVar()
Dec_Dom_C_5 = tk.IntVar()
Cen_Dom_C_5 = tk.IntVar()
Ind_Dom_C_5 = tk.IntVar()
Lib_Nat_C_5 = tk.IntVar()
Dec_Nat_C_5 = tk.IntVar()
Cen_Nat_C_5 = tk.IntVar()
Ind_Nat_C_5 = tk.IntVar()
var_l_Dom_5 = [Demo_Dom_C_5 ,Free_Dom_C_5,Lib_Dom_C_5,Dec_Dom_C_5 ,Cen_Dom_C_5,Ind_Dom_C_5]
var_l_Nat_5 = [Demo_Nat_C_5 ,Free_Nat_C_5,Lib_Nat_C_5,Dec_Nat_C_5 ,Cen_Nat_C_5,Ind_Nat_C_5]
r  = r+1
for item  in country_l:
    tk.Label(frame, text= item,width = 30 ).grid(row=r, column = c,columnspan=3)
    tk.Label(frame, text='國內政策').grid(row=r+1 ,column=c)
    tk.Label(frame, text='國外政策').grid(row=r+1, column=c+1)
    c = c + 3

c = 1
for var in var_l_Dom_5:
    tk.Radiobutton(frame, text='-1',variable=var, value = -1).grid(row=r+2, column=c)
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+3, column=c)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+4, column=c)
    c = c + 3
c = 1

for var in var_l_Nat_5:
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+2, column=c+1)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+3, column=c+1)
    c = c + 3

# 第五回合----------------------------------------------------------


# 第六回合----------------------------------------------------------
c = 1
r = 30
l = tk.Label(frame, bg='yellow', text='第六回合').grid(row=r, column=0)
Demo_Dom_C_6 = tk.IntVar()
Demo_Nat_C_6 = tk.IntVar()
Free_Dom_C_6 = tk.IntVar()
Free_Nat_C_6 = tk.IntVar()
Lib_Dom_C_6 = tk.IntVar()
Dec_Dom_C_6 = tk.IntVar()
Cen_Dom_C_6 = tk.IntVar()
Ind_Dom_C_6 = tk.IntVar()
Lib_Nat_C_6 = tk.IntVar()
Dec_Nat_C_6 = tk.IntVar()
Cen_Nat_C_6 = tk.IntVar()
Ind_Nat_C_6 = tk.IntVar()
var_l_Dom_6 = [Demo_Dom_C_6 ,Free_Dom_C_6,Lib_Dom_C_6,Dec_Dom_C_6 ,Cen_Dom_C_6,Ind_Dom_C_6]
var_l_Nat_6 = [Demo_Nat_C_6 ,Free_Nat_C_6,Lib_Nat_C_6,Dec_Nat_C_6 ,Cen_Nat_C_6,Ind_Nat_C_6]
r  = r+1
for item  in country_l:
    tk.Label(frame, text= item,width = 30 ).grid(row=r, column = c,columnspan=3)
    tk.Label(frame, text='國內政策').grid(row=r+1 ,column=c)
    tk.Label(frame, text='國外政策').grid(row=r+1, column=c+1)
    c = c + 3

c = 1
for var in var_l_Dom_6:
    tk.Radiobutton(frame, text='-1',variable=var, value = -1).grid(row=r+2, column=c)
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+3, column=c)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+4, column=c)
    c = c + 3
c = 1

for var in var_l_Nat_6:
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+2, column=c+1)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+3, column=c+1)
    c = c + 3

# 第六回合----------------------------------------------------------


# 第七回合----------------------------------------------------------
c = 1
r = 36
l = tk.Label(frame, bg='yellow', text='第七回合').grid(row=r, column=0)
Demo_Dom_C_7 = tk.IntVar()
Demo_Nat_C_7 = tk.IntVar()
Free_Dom_C_7 = tk.IntVar()
Free_Nat_C_7 = tk.IntVar()
Lib_Dom_C_7 = tk.IntVar()
Dec_Dom_C_7 = tk.IntVar()
Cen_Dom_C_7 = tk.IntVar()
Ind_Dom_C_7 = tk.IntVar()
Lib_Nat_C_7 = tk.IntVar()
Dec_Nat_C_7 = tk.IntVar()
Cen_Nat_C_7 = tk.IntVar()
Ind_Nat_C_7 = tk.IntVar()
var_l_Dom_7 = [Demo_Dom_C_7 ,Free_Dom_C_7,Lib_Dom_C_7,Dec_Dom_C_7 ,Cen_Dom_C_7,Ind_Dom_C_7]
var_l_Nat_7 = [Demo_Nat_C_7 ,Free_Nat_C_7,Lib_Nat_C_7,Dec_Nat_C_7 ,Cen_Nat_C_7,Ind_Nat_C_7]
r  = r+1
for item  in country_l:
    tk.Label(frame, text= item,width = 30 ).grid(row=r, column = c,columnspan=3)
    tk.Label(frame, text='國內政策').grid(row=r+1 ,column=c)
    tk.Label(frame, text='國外政策').grid(row=r+1, column=c+1)
    c = c + 3

c = 1
for var in var_l_Dom_7:
    tk.Radiobutton(frame, text='-1',variable=var, value = -1).grid(row=r+2, column=c)
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+3, column=c)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+4, column=c)
    c = c + 3
c = 1

for var in var_l_Nat_7:
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+2, column=c+1)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+3, column=c+1)
    c = c + 3

# 第七回合----------------------------------------------------------


# 第八回合----------------------------------------------------------
c = 1
r = 42
l = tk.Label(frame, bg='yellow', text='第八回合').grid(row=r, column=0)
Demo_Dom_C_8 = tk.IntVar()
Demo_Nat_C_8 = tk.IntVar()
Free_Dom_C_8 = tk.IntVar()
Free_Nat_C_8 = tk.IntVar()
Lib_Dom_C_8 = tk.IntVar()
Dec_Dom_C_8 = tk.IntVar()
Cen_Dom_C_8 = tk.IntVar()
Ind_Dom_C_8 = tk.IntVar()
Lib_Nat_C_8 = tk.IntVar()
Dec_Nat_C_8 = tk.IntVar()
Cen_Nat_C_8 = tk.IntVar()
Ind_Nat_C_8 = tk.IntVar()
var_l_Dom_8 = [Demo_Dom_C_8 ,Free_Dom_C_8,Lib_Dom_C_8,Dec_Dom_C_8 ,Cen_Dom_C_8,Ind_Dom_C_8]
var_l_Nat_8 = [Demo_Nat_C_8 ,Free_Nat_C_8,Lib_Nat_C_8,Dec_Nat_C_8 ,Cen_Nat_C_8,Ind_Nat_C_8]
r  = r+1
for item  in country_l:
    tk.Label(frame, text= item,width = 30 ).grid(row=r, column = c,columnspan=3)
    tk.Label(frame, text='國內政策').grid(row=r+1 ,column=c)
    tk.Label(frame, text='國外政策').grid(row=r+1, column=c+1)
    c = c + 3

c = 1
for var in var_l_Dom_8:
    tk.Radiobutton(frame, text='-1',variable=var, value = -1).grid(row=r+2, column=c)
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+3, column=c)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+4, column=c)
    c = c + 3
c = 1

for var in var_l_Nat_8:
    tk.Radiobutton(frame, text='1',variable=var, value = 1).grid(row=r+2, column=c+1)
    tk.Radiobutton(frame, text='2',variable=var, value = 2).grid(row=r+3, column=c+1)
    c = c + 3

# 第八回合----------------------------------------------------------
def print_country_6(round):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    d_1 = 0
    d_2 = 0
    d_3 = 0
    d_4 = 0
    d_5 = 0
    d_6 = 0
    for i in data_1:
        if (i == 'D'):
            pass
        else :
            d_1 += data_1[i]['Value']
    for i in data_2:
        if (i == 'D'):
            pass
        else :
            d_2 += data_2[i]['Value']
    for i in data_3:
        if (i == 'D'):
            pass
        else :
            d_3 += data_3[i]['Value']

    for i in data_4:
        if (i == 'D'):
            pass
        else :
            d_4 += data_4[i]['Value']
    for i in data_5:
        if (i == 'D'):
            pass
        else :
            d_5 += data_5[i]['Value']
    for i in data_6:
        if (i == 'D'):
            pass
        else :
            d_6 += data_6[i]['Value']
    s = "---------這是第"+str(round)+"回合--------------"
    s=s+"\n\n德莫克拉希\n"+str(d_1)
    s =s+"\n\n福利丹尼國\n"+str(d_2)
    s = s+"\n\n禮畢爾提國\n"+str(d_3)
    s = s+"\n\n迪泰特國\n"+str(d_4)
    s = s+"\n\n山卓雷斯國\n"+str(d_5)
    s = s+"\n\n因迪凡卓拉森國\n"+str(d_6)
    s = s+ "\n\n---------這是第"+str(round)+"回合--------------\n"
    return s


def print_country_6_result(List_Choice):
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    c_c = [data_1,data_2,data_3,data_4,data_5,data_6]
    team_1 = 0
    team_2 = 0
    for i in List_Choice:
        if (i == 1):
            team_1 += 1
        elif (i == 2):
            team_2 += 1
    if (abs(team_1 - team_2) >= 4):
        s = "No team win"
        return s
    else:
        team_1_D = 0
        team_2_D = 0
        for i in range(6):
            if (List_Choice[i] == 1):
                team_1_D += c_c[i]["D"]
            elif (List_Choice[i] == 2):
                team_2_D += c_c[i]["D"]
        print (team_1_D,team_1,team_2_D,team_2,team_1_D/team_1,team_2_D/team_2)
        if (team_1_D/team_1 > team_2_D/team_2):
            s = 'team1 win'
            return s
        elif (team_1_D/team_1 < team_2_D/team_2):
            s = 'team2 win'
            return s
        elif (team_1_D/team_1 == team_2_D/team_2):
            s = 'team1 and team2 have same score'
            return s


round = tk.IntVar()

def print_3_result(r):
    if (r == 2):
        return 'They decided restrict the nuclear weapon'
    elif (r == 3):
        return 'They decided not to restrict the nuclear weapon'
    elif (r== 1):
        return 'They did not make a decision'
def submit():
    if (round.get() == 1):
        print ("round 1 ")
        re_start()
        cal_1()
        tk.messagebox.showinfo(title='Hi', message=print_country_tk(1))
    if (round.get() == 2):
        print ("round 2 ")
        re_start()
        cal_1()
        cal_2()
        tk.messagebox.showinfo(title='Hi', message=print_country_tk(2))
    if (round.get() == 3):
        result_3 = 0
        result_3 = result_32(Demo_Nat_C_3.get(),Free_Nat_C_3.get(),Lib_Nat_C_3.get(),Dec_Nat_C_3.get(),Cen_Nat_C_3.get(),Ind_Nat_C_3.get())
        print ("round 3 ")
        re_start()
        cal_1()
        cal_2()
        cal_3(result_3)
        tk.messagebox.showinfo(title='Hi', message=print_country_tk(3))
        tk.messagebox.showinfo(title='Hi2', message=print_3_result(result_3))
    if (round.get() == 4):
        result_3 = 0
        result_3 = result_32(Demo_Nat_C_3.get(),Free_Nat_C_3.get(),Lib_Nat_C_3.get(),Dec_Nat_C_3.get(),Cen_Nat_C_3.get(),Ind_Nat_C_3.get())
        print ("round 4 ")
        re_start()
        cal_1()
        cal_2()
        cal_3(result_3)
        cal_4()
        tk.messagebox.showinfo(title='Hi', message=print_country_tk(4))
    if (round.get() == 5):
        result_3 = 0
        result_3 = result_32(Demo_Nat_C_3.get(),Free_Nat_C_3.get(),Lib_Nat_C_3.get(),Dec_Nat_C_3.get(),Cen_Nat_C_3.get(),Ind_Nat_C_3.get())
        print ("round 5 ")
        re_start()
        cal_1()
        cal_2()
        cal_3(result_3)
        cal_4()
        cal_5()
        tk.messagebox.showinfo(title='Hi', message=print_country_tk(5))
        tk.messagebox.showinfo(title='Hi2', message=print_country_6(5))
    if (round.get() == 6):
        result_3 = 0
        result_3 = result_32(Demo_Nat_C_3.get(),Free_Nat_C_3.get(),Lib_Nat_C_3.get(),Dec_Nat_C_3.get(),Cen_Nat_C_3.get(),Ind_Nat_C_3.get())
        lists = [Demo_Nat_C_6.get(),Free_Nat_C_6.get(),Lib_Nat_C_6.get(),Dec_Nat_C_6.get(),Cen_Nat_C_6.get(),Ind_Nat_C_6.get()]
        print ("round 6 ")
        re_start()
        cal_1()
        cal_2()
        cal_3(result_3)
        cal_4()
        cal_5()
        cal_6()
        tk.messagebox.showinfo(title='Hi', message=print_country_tk(6))
        tk.messagebox.showinfo(title='Hi2', message=print_country_6_result(lists))
    if (round.get() == 7):
        result_3 = 0
        result_3 = result_32(Demo_Nat_C_3.get(),Free_Nat_C_3.get(),Lib_Nat_C_3.get(),Dec_Nat_C_3.get(),Cen_Nat_C_3.get(),Ind_Nat_C_3.get())
        print ("round 7 ")
        re_start()
        cal_1()
        cal_2()
        cal_3(result_3)
        cal_4()
        cal_5()
        cal_6()
        cal_7()
        tk.messagebox.showinfo(title='Hi', message=print_country_tk(7))
    if (round.get() == 8):
        result_3 = 0
        result_3 = result_32(Demo_Nat_C_3.get(),Free_Nat_C_3.get(),Lib_Nat_C_3.get(),Dec_Nat_C_3.get(),Cen_Nat_C_3.get(),Ind_Nat_C_3.get())
        print ("round 8 ")
        re_start()
        cal_1()
        cal_2()
        cal_3(result_3)
        cal_4()
        cal_5()
        cal_6()
        cal_7()
        cal_8()
        tk.messagebox.showinfo(title='Hi', message=print_country_tk(8))
def cal_1():
    #德莫克拉希
    Select_1(Demo_Dom_C_1.get(),data_1)
    N_select_1(Demo_Nat_C_1.get(),data_1)

    #福利丹尼國

    Select_1(Free_Dom_C_1.get(),data_2)
    N_select_1(Free_Nat_C_1.get(),data_2)

    #禮畢爾提國

    Select_1(Lib_Dom_C_1.get(),data_3)
    N_select_1(Lib_Nat_C_1.get(),data_3)

    #迪泰特國

    Select_1(Dec_Dom_C_1.get(),data_4)
    N_select_1(Dec_Nat_C_1.get(),data_4)

    #山卓雷斯國

    Select_1(Cen_Dom_C_1.get(),data_5)
    N_select_1(Cen_Nat_C_1.get(),data_5)

    #因迪凡卓拉森國

    Select_1(Ind_Dom_C_1.get(),data_6)
    N_select_1(Ind_Nat_C_1.get(),data_6)
def cal_2():
    #德莫克拉希
    Select_2(Demo_Dom_C_2.get(),data_1)
    N_select_2(Demo_Nat_C_2.get(),data_1)

    #福利丹尼國

    Select_2(Free_Dom_C_2.get(),data_2)
    N_select_2(Free_Nat_C_2.get(),data_2)

    #禮畢爾提國

    Select_2(Lib_Dom_C_2.get(),data_3)
    N_select_2(Lib_Nat_C_2.get(),data_3)

    #迪泰特國

    Select_2(Dec_Dom_C_2.get(),data_4)
    N_select_2(Dec_Nat_C_2.get(),data_4)

    #山卓雷斯國

    Select_2(Cen_Dom_C_2.get(),data_5)
    N_select_2(Cen_Nat_C_2.get(),data_5)

    #因迪凡卓拉森國

    Select_2(Ind_Dom_C_2.get(),data_6)
    N_select_2(Ind_Nat_C_2.get(),data_6)
def cal_3(r):
    #1是支持    2是反對
    #德莫克拉希
    Select_3(Demo_Dom_C_3.get(),data_1)
    N_select_3(r,Demo_Nat_C_3.get(),data_1)

    #福利丹尼國

    Select_3(Free_Dom_C_3.get(),data_2)
    N_select_3(r,Free_Nat_C_3.get(),data_2)

    #禮畢爾提國

    Select_3(Lib_Dom_C_3.get(),data_3)
    N_select_3(r,Lib_Nat_C_3.get(),data_3)

    #迪泰特國

    Select_3(Dec_Dom_C_3.get(),data_4)
    N_select_3(r,Dec_Nat_C_3.get(),data_4)

    #山卓雷斯國

    Select_3(Cen_Dom_C_3.get(),data_5)
    N_select_3(r,Cen_Nat_C_3.get(),data_5)

    #因迪凡卓拉森國

    Select_3(Ind_Dom_C_3.get(),data_6)
    N_select_3(r,Ind_Nat_C_3.get(),data_6)
def cal_4():
    #德莫克拉希
    Select_4(Demo_Dom_C_4.get(),data_1)
    N_select_4(Demo_Nat_C_4.get(),data_1)

    #福利丹尼國

    Select_4(Free_Dom_C_4.get(),data_2)
    N_select_4(Free_Nat_C_4.get(),data_2)

    #禮畢爾提國

    Select_4(Lib_Dom_C_4.get(),data_3)
    N_select_4(Lib_Nat_C_4.get(),data_3)

    #迪泰特國

    Select_4(Dec_Dom_C_4.get(),data_4)
    N_select_4(Dec_Nat_C_4.get(),data_4)

    #山卓雷斯國

    Select_4(Cen_Dom_C_4.get(),data_5)
    N_select_4(Cen_Nat_C_4.get(),data_5)

    #因迪凡卓拉森國

    Select_4(Ind_Dom_C_4.get(),data_6)
    N_select_4(Ind_Nat_C_4.get(),data_6)
def cal_5():
    #德莫克拉希
    Select_5(Demo_Dom_C_5.get(),data_1)
    N_select_5(Demo_Nat_C_5.get(),data_1)

    #福利丹尼國

    Select_5(Free_Dom_C_5.get(),data_2)
    N_select_5(Free_Nat_C_5.get(),data_2)

    #禮畢爾提國

    Select_5(Lib_Dom_C_5.get(),data_3)
    N_select_5(Lib_Nat_C_5.get(),data_3)

    #迪泰特國

    Select_5(Dec_Dom_C_5.get(),data_4)
    N_select_5(Dec_Nat_C_5.get(),data_4)

    #山卓雷斯國

    Select_5(Cen_Dom_C_5.get(),data_5)
    N_select_5(Cen_Nat_C_5.get(),data_5)

    #因迪凡卓拉森國

    Select_5(Ind_Dom_C_5.get(),data_6)
    N_select_5(Ind_Nat_C_5.get(),data_6)
def cal_6():
    #德莫克拉希
    lists = [Demo_Nat_C_6.get(),Free_Nat_C_6.get(),Lib_Nat_C_6.get(),Dec_Nat_C_6.get(),Cen_Nat_C_6.get(),Ind_Nat_C_6.get()]
    Select_6(Demo_Dom_C_6.get(),data_1)
    N_select_6(lists)

    #福利丹尼國

    Select_6(Free_Dom_C_6.get(),data_2)


    #禮畢爾提國

    Select_6(Lib_Dom_C_6.get(),data_3)


    #迪泰特國

    Select_6(Dec_Dom_C_6.get(),data_4)


    #山卓雷斯國

    Select_6(Cen_Dom_C_6.get(),data_5)


    #因迪凡卓拉森國

    Select_6(Ind_Dom_C_6.get(),data_6)
def cal_7():
    #德莫克拉希
    Select_7(Demo_Dom_C_7.get(),data_1)
    N_select_7(Demo_Nat_C_7.get(),data_1)

    #福利丹尼國

    Select_7(Free_Dom_C_7.get(),data_2)
    N_select_7(Free_Nat_C_7.get(),data_2)

    #禮畢爾提國

    Select_7(Lib_Dom_C_7.get(),data_3)
    N_select_7(Lib_Nat_C_7.get(),data_3)

    #迪泰特國

    Select_7(Dec_Dom_C_7.get(),data_4)
    N_select_7(Dec_Nat_C_7.get(),data_4)

    #山卓雷斯國

    Select_7(Cen_Dom_C_7.get(),data_5)
    N_select_7(Cen_Nat_C_7.get(),data_5)

    #因迪凡卓拉森國

    Select_7(Ind_Dom_C_7.get(),data_6)
    N_select_7(Ind_Nat_C_7.get(),data_6)
def cal_8():
    #德莫克拉希
    Select_8(Demo_Dom_C_8.get(),data_1)
    N_select_8(Demo_Nat_C_8.get(),data_1)

    #福利丹尼國

    Select_8(Free_Dom_C_8.get(),data_2)
    N_select_8(Free_Nat_C_8.get(),data_2)

    #禮畢爾提國

    Select_8(Lib_Dom_C_8.get(),data_3)
    N_select_8(Lib_Nat_C_8.get(),data_3)

    #迪泰特國

    Select_8(Dec_Dom_C_8.get(),data_4)
    N_select_8(Dec_Nat_C_8.get(),data_4)

    #山卓雷斯國

    Select_8(Cen_Dom_C_8.get(),data_5)
    N_select_8(Cen_Nat_C_8.get(),data_5)

    #因迪凡卓拉森國

    Select_8(Ind_Dom_C_8.get(),data_6)
    N_select_8(Ind_Nat_C_8.get(),data_6)
def print_excel():
    global num
    global data_1
    global data_2
    global data_3
    global data_4
    global data_5
    global data_6
    c_c = [data_1,data_2,data_3,data_4,data_5,data_6]
    chinese_name=["德莫克拉希","福利丹尼國","禮畢爾提國","迪泰特國","山卓雷斯國","因迪凡卓拉森國"]
    people = ["A","N","I","B"]
    book = Workbook()
    sheet1 = book.add_sheet('Sheet 1')
    col0 = sheet1.row(0)
    col0.write(0,"A")
    col0.write(1,"N")
    col0.write(2,"I")
    col0.write(3,"B")
    col0.write(4,"D")
    c=1
    c1=0
    p=0
    for i in c_c:
        row=sheet1.row(c)
        for d in people:
            row.write(c1,i[d]["Value"])
            c1+=1
        row.write(c1,i["D"])
        c1+=1
        row.write(c1,chinese_name[p])
        p+=1
        c1=0
        c+=1
    book.save('C:\\games\\result_{}.xls'.format(num))
    book.save(TemporaryFile())
    num += 1
    tk.messagebox.showinfo(title='Hi', message="Estliblish Excel Successfully")


r = 49
b = tk.Button(frame, text='submit', font=('Arial', 12), width=10, height=1,command = submit).grid(row=48, column=10)
b1 = tk.Button(frame, text='excel', font=('Arial', 12), width=10, height=1,command = print_excel).grid(row=49, column=10)
tk.Label(frame, text='Round_Selection').grid(row=r-1, column=11)
for i in range(1,9):
    tk.Radiobutton(frame, text=str(i),variable=round, value = i).grid(row=r, column=11)
    r = r+1

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
num = 1
window.mainloop()

#%%

#%%

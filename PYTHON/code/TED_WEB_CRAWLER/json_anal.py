import json
import matplotlib.pyplot as plt
import random
from selenium import webdriver
def get_data():
    data = list()
    for i in range(1,79):
        with open("D:\python\code\工工_程設\程設資料\progam{}.json".format(i),"r",encoding='utf-8') as f:
            data.append(json.load(f))
    return data

def get_related_tags(data):
    count = {}
    try:
        for i in range(78):
            for n in range(len(data[i])):
                for h in range(len(data[i][n]["Related tags"])):
                    if (not(data[i][n]["Related tags"][h]) in count.keys()):
                        count[data[i][n]["Related tags"][h]] = 1
                    else:
                        count[data[i][n]["Related tags"][h]] += 1
    except Exception as e:
        pass
    return count

def get_speaker_videos(data):
    time = {}
    try:
        for i in range(78):
            for n in range(len(data[i])):
                if (not(data[i][n]["speaker"]) in time.keys()):
                    time[data[i][n]["speaker"]] = int(data[i][n]["views"].replace(",",""))
                else:
                    if ("views" in data[i][n].keys()):
                        time[data[i][n]["speaker"]] += int(data[i][n]["views"].replace(",",""))
    except KeyError as e:
        print (e)
    return time
def get_time_views(data):
    time = {}
    try:
        for i in range(78):
            for n in range(len(data[i])):
                if (not(data[i][n]["posted"]) in time.keys()):
                    time[data[i][n]["posted"]] = 0
                else:
                    if ("views" in data[i][n].keys()):
                        time[data[i][n]["posted"]] += int(data[i][n]["views"].replace(",",""))/1000000
    except KeyError as e:
        print (e)
    return time

def find_max(c):
    count_keys = list(c)
    max = int()
    for i in range(len(count_keys)):
        if (c[count_keys[i]]>max):
            max = c[count_keys[i]]
            max_key = count_keys[i]
    for i in range(len(count_keys)):
        if (c[count_keys[i]] == max):
            max_list = [[max,max_key]]
            max_list.append([c[count_keys[i]],count_keys[i]])
    return max_list
def find_top5(c):
    count_keys = list(c)
    top5 = list(c.items())
    top5_values = list()
    temp = list()
    for i in range(len(top5)):
        for t in range(1,len(top5)): # 這個要好好研究一下><
            if (top5[len(top5)-i-1][1]<top5[len(top5)-t][1]): #研究為啥 len(top5)-t-1 時 society會被放在最後面
                temp = top5[len(top5)-i-1]
                top5[len(top5)-i-1] = top5[len(top5)-t]
                top5[len(top5)-t] = temp
    return (top5)
def plt_pie(arry):
    top5_labels = list()
    top5_values = list()
    for i in range(len(arry)):
        top5_labels.append(arry[i][0])
        top5_values.append(arry[i][1])
    labels = top5_labels
    sizes = top5_values
    colors = ["red","green","blue","yellow","purple"]
    plt.pie(sizes,labels = labels,colors = colors,autopct = "%3.1f%%",startangle = 90,shadow = True)
    plt.axis("equal")
    plt.legend()
    plt.savefig("pie.jpg")
    plt.show()
def plt_plot(arry):
    time = []
    views = []
    for i in range(len(arry)):
        time.append(i)
        views.append(arry[i][1])
    listx = time
    listy = views
    plt.plot(listx,listy,label="views")
    plt.legend()
    plt.xlim(0,180)
    plt.ylim(0.150)
    plt.title("Time_Views")
    plt.xlabel("Time")
    plt.ylabel("Views")
    plt.savefig("plot.jpg")
    plt.show()
def random_video(data,tags = []):
    s1 = set(tags)
    i = random.randint(0,77)
    n = random.randint(0,len(data[i])-1)
    s2 = set(data[i][n]["Related tags"])
    if (s1 == set()):
        driver = webdriver.Chrome("D:\python\web_driver\chromedriver_win32\chromedriver.exe")
        driver.get(data[i][n]["href"])
    else:
        check = s2.intersection(s1)
        if(check.symmetric_difference(s1) == set()):
            driver = webdriver.Chrome("D:\python\web_driver\chromedriver_win32\chromedriver.exe")
            driver.get(data[i][n]["href"])
        else:
            random_video(data,tags)

    #print (data[i][n]["href"])
data = get_data()


views_num = get_time_views(data)
video_num = get_related_tags(data)
top5 = find_top5(video_num)[0:5]
speaker = get_speaker_videos(data)
spk_top5 = find_top5(speaker)
print (spk_top5[0:5])


#choices = ["society"]
#plt_pie(top5)
#plt_plot(list(views_num.items()))
#random_video(data,choices)
#print (data[0][0]["href"])




#%%
a = {"a":2,"b":6,"c":4,"d":6}
key = list(a)
max = 0
for i in range(len(key)):
    if (a[key[i]]>max):
        max = a[key[i]]
        max_key = key[i]
for i in range(len(key)):
    if (a[key[i]] == max):
        max_list = [[max,max_key]]
        max_list.append([a[key[i]],key[i]])

print (max_list)
a = "3,,,2,4"
if ("," in a):
    print (int(a.replace(",","")))
#%%
a = ["aa","bb","a","b","c"]
b = ["a","b"]
c = []
print (set(c))
s1 = set(a)
s2 = set(b)
d = s1.intersection(s2)
print (d.symmetric_difference(s2) == set())
#%%
def clickme():
    global count
    count += 1
    labeltext.set("click 你按我 " + str(count) + " times 次了！")
    if(btntext.get() == "click 按我！"):
        btntext.set("go back 回復原來文字！")
    else:
        btntext.set("click 按我！")

import tkinter as tk

win = tk.Tk()
labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label1 = tk.Label(win, fg="red", textvariable=labeltext)
labeltext.set("welcome 歡迎光臨Tkinter！")
label1.pack()
button1 = tk.Button(win, textvariable=btntext, command=clickme)
btntext.set("click 按我！")
button1.pack()
win.mainloop()

#!@Author: NathanPG
import urllib
import requests
from bs4 import BeautifulSoup
import time 
class Course(object):
    def __init__(self, data):
        self.CRN = data[0]
        self.SubjCrse = data[1]
        self.Title = data[2]
        self.Type = data[3]
        self.Cred = data[4]
        self.GrTp = data[5]
        self.Days = data[6]
        self.StartTime = data[7]
        self.EndTime = data[8]
        self.Instructor = data[9]
        self.Location = data[10]
        self.Cap = int(data[11])
        self.Act = int(data[12])
        self.Rem = int(data[13])

    def UpdateLastAct(self,NewAct):
        self.LastAct = NewAct

    def UpdateAct(self,NewAct):
        self.Act = NewAct

    def getLastActual(self):
        return self.LastAct

    def getKey(self):
        return self.SubjCrse + "/" + self.Instructor[0]

    def getActual(self):
        return self.Act

    def __str__(self):
        return "actual:{}".format(self.Act)

    def __repr__(self):
        return "{}".format(self.Act)

    def crawler():
        data = []
        courses = dict()
        count = 0
        currentDepartment = ""
        oldDepartment = ""
        tempDepartment = ""
        print(datetime.now(), " Begin")
        f = open('/DATATEST.txt', 'a')
        f.write(str(datetime.now())+"\n")
        f.close()
            

        for element in soup.find_all("td"):
            text = element.get_text().strip()
            #New data
            if count == 0 and text != " " and text != "":
                temp = text.split(" ")
                data.append(temp[0])
                data.append(temp[1].split("-")[0] + temp[1].split("-")[1])
                oldDepartment = temp[1].split("-")[0]
                tempDepartment = oldDepartment
            #Not the first data
            else:
                data.append(text)
            count += 1

            #Note block, delete this data
            if count == 3 and "NOTE:" in data[1]:
                count = 0
                data.clear()
                continue

            if currentDepartment != oldDepartment and oldDepartment != "":
                f = open ('/LastData.txt','r+')
                print("Update last data")
                f.seek(0)
                f.truncate()
                for key in sorted(courses):
                    f.write("{}:{}".format(key, courses[key].getActual()))
                    f.write("\n")
                f.close()
                courses.clear()

                f = open('/DATATEST.txt', 'a')
                print("write file")
                for key in sorted(courses):
                    f.write("{}:{}".format(key, courses[key].getActual()))
                    f.write("\n")
                f.close()
                courses.clear()
            currentDepartment = tempDepartment

            if count == 14:
                if data[0] == "":
                    count = 0
                    data.clear()
                    continue
                course = Course(data)
                if course.getKey() in courses:
                    courses[course.getKey()] = courses[course.getKey()] + course
                else:
                    courses[course.getKey()] = course

                print(courses)
                data.clear()
                count = 0

        for key in sorted(courses):
            if courses[key].getLastActual() == null:
                courses[key].UpdateLastAct(courses[key].getActual())

            if courses[key].getActual() == null or courses[key].getActual() >= courses[key].getActual():
                courses[key].UpdateAct(courses[key].getLastActual())
                courses[key].UpdateLastAct(courses[key].getActual())

        f = open ('/LastData.txt','r+')
        print("Update last data")
        f.seek(0)
        f.truncate()
        for key in sorted(courses):
            f.write("{}:{}".format(key, courses[key].getActual()))
            f.write("\n")
        f.close()
        courses.clear()
        data.clear()
        count = 0

        f = open('/DATATEST.txt', 'a')
        print("write file")
        for key in sorted(courses):
            f.write("{}:{}".format(key, courses[key].getActual()))
            f.write("\n")
        f.close()
        courses.clear()
        data.clear()
        count = 0
        print(datetime.now(), " Finish")

def timer(n):
        #Infinite, Ctrl+C to stop
        while True:  
            print time.strftime('%Y-%m-%d %X',time.localtime())  
            crawler()
            time.sleep(n)

def getHTMLv1(url):
    page = urllib.urlopen(url)
    html_code = page.read()
    return html_code

def getHTMLv2(url):
    page = requests.get(url)
    html_code = page.read()
    return html_code

if __name__ == '__main__':
    html = getHTMLv1('https://sis.rpi.edu/reg/zs201809.htm')
    soup = BeautifulSoup(html, 'html.parser')
    #Infinite, Ctrl+C to stop
    timer(43200)
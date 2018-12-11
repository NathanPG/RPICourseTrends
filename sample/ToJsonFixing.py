import urllib
from urllib import request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from datetime import  datetime
import numpy as np

class Course(object):

    def __init__(self, data):


        self.CRN = data[0]
        self.SubjCrse = data[1]
        self.Subject = self.SubjCrse[0:4]
        self.Crse = self.SubjCrse[4:]
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
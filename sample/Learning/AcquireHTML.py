#!@Author: NathanPG
import urllib.request
 
def getHTML(url):
    html = urllib.request.urlopen(url).read()
    return html
 
def saveHTML(fname, htmlcontent):

    with open(fname.replace('/', '_') + ".html", "wb") as f:
       
        f.write(htmlcontent)
 
if __name__ == '__main__':
	url = "https://sis.rpi.edu/reg/zs201809.htm/"

	html = getHtml(url)

	saveHtml("SisCourses", html)

	print("Save Complete!")


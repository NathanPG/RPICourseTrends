import urllib.request
 
def getHTML(url):
    html = urllib.request.urlopen(url).read()
    return html
 
def saveHTML(fname, htmlcontent):

    with open(fname.replace('/', '_') + ".html", "wb") as f:
       
        f.write(htmlcontent)
 
if __name__ == '__main__':
	url = "https://robertsspaceindustries.com/"

	html = getHtml(url)

	saveHtml("StarCitizen", html)

	print("Save Complete!")


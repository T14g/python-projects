##
# Job scrapping script using requests and bs4
##
import bs4
from bs4 import BeautifulSoup
import requests
import json

def openJSON(file):
    with open('./'+ file, 'r') as f:
        return json.load(f)

def lastPage(last):
    if last:
        parts = last.get('href').split('=')
        return True
    else:
        return False

def getJobPages(url, arr):
    r = requests.post(url) 
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    last = soup.find("a", class_="paginationItemLast")

    if lastPage(last):
        print("there is a last page")
    else:
        pages = soup.find_all("span", class_="jobTitle")
        
        for page in pages:
            arr.append(page.find('a').get('href'))

def getData(base ,url):
    print("Fetching job data....")
    r = requests.post(base + url) 
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find("div", class_="jobDisplay")
    return str(content)

def loopJobs(baseUrl, pages):
    print("Started jobs LOOP")
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Job List</title>
        <link rel="stylesheet" href="css/styles.css">
    </head>
    <body>
    <div class="jobs-container">
    """

    for page in pages:
        html += getData(baseUrl, page)

    html += """
    </div>
    </body>
    </html>
    """
    return html

def saveJobs(fileName, content):
    print("Saving data to file")
    file = open(fileName,"w", encoding="utf-8")
    file.write(content)
    file.close()

def startMachine():

    data = openJSON('config.json')
    sites = data['sites']
    for site in sites:
        print(site['specificURL'])
        jobsURLS  = []
        getJobPages(site['specificURL'], jobsURLS)
        results = loopJobs(site['baseURL'], jobsURLS)
        saveJobs(site['fileOutput'], results)

#Start everything
startMachine()






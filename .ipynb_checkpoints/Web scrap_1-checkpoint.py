from bs4 import BeautifulSoup
import lxml
import requests
res = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=GIS+Developer&txtLocation=').text
soup = BeautifulSoup(res, 'lxml')
salary = soup.find_all('a', class_ = "blkclor")
print(salary)
company = soup.find('h3', class_ = "joblist-comp-name")
print(company)

print(f'''
Company Name is : {company}
Job is : {salary}
''')
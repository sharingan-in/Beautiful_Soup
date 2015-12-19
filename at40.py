''' the user should enter the year and month and the script will display the top 3 songs of that month '''


from bs4 import BeautifulSoup
import requests
month=['NAN','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
year = str(input("enter the year"))
mon = str(input("enter the month"))
mon=mon.upper()

mon=month.index(mon)
req = requests.get("http://www.at40.com/top-40/" + year +'/'+ str(mon))
content = req.text
code= BeautifulSoup(content)
store = code.find('td',"listtable1")
print("\n\n")

data=str(store.get_text())

data=' '.join(data.split())

print(data)



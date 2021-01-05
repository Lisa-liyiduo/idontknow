from bs4 import BeautifulSoup

f = open('D:\\BaiduYunDownload\\pysonar2-master\\pysonar2-master\\html\\site-packages\\augeas.py.html')
html = f.read()
f.close()

soup = BeautifulSoup(html,'html.parser')
result_1 = soup.find_all(name='span',attrs={'class':'lineno'})
t=0
for r in result_1:
	print(r.text)
	t=t+1
# print(result_1)
m=0
result_2 = soup.find_all(name='a')
for r in result_2:
	m = m + 1
	try:
		print(r.attrs['href'])

	except:
		pass
print(t)
print(m)
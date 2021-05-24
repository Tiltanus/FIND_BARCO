import requests
import array

planetarium = 0;
barco = []
while(planetarium < 3606):
     url = 'http://www.aplf-planetariums.org/en/index.php?onglet=planetariums&menu=sheet_planetarium&filtre=%d' %(planetarium)
     r = requests.get(url)
     with open('test.txt', 'w') as output_file:
        if (r.content.decode('cp1251').find('Barco : F35') > -1):
            barco.append(planetarium)
     print(planetarium)
     planetarium+=1

print(barco)


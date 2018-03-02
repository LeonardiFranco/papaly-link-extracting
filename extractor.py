from bs4 import BeautifulSoup

name = "Estudio"

with open(name+'.html', encoding = 'utf-8') as page:
    soup = BeautifulSoup(page, 'html5lib')

with open(name.lower() +'.md', 'w', errors='surrogateescape', encoding='utf-8') as fout:
    try:
        title = soup.div['board-name']
        fout.write('# ' + title +'\n\n')
        fout.write('Backup of the board made by Franco Leonardi.\n')
    except:
        pass
    for div in soup.find_all('div'):
        if 'parent-category' in div['class']:
            fout.write('\n## ' + div.find_all('h2')[0].find_all(string=True)[0]+'\n\n')
            for link in div.find_all('a'):
                for content in link.contents:
                    try:
                        if content['class'] == ['item-name']:
                            fout.write('* [{}]({})\n'.format(content.contents[0],link.get('href')))
                    except:
                        pass
    #print(link.get('href'))

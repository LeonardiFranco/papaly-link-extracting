from bs4 import BeautifulSoup
import re
import glob

name = "Programming"
personalText = 'Backup of the board made by Franco Leonardi.\n'

list_of_files = glob.glob('./*.html')
data=[]
with open('README.md', 'w', errors='surrogateescape', encoding='utf-8') as readme:
    readme.write("# Franco's Papaly bookmarks\n\nThese are the backup bookmarks from my Papaly account.\n\n")
    for i,f in enumerate(list_of_files):
        fname = f[:-5]
        with open(fname+'.html', "r", errors="surrogateescape",encoding="utf-8") as fin:
            lines_list = fin.readlines()

        with open(fname+'.html', encoding = 'utf-8') as page:
            soup = BeautifulSoup(page, 'html5lib')

        with open(fname.lower() +'.md', 'w', errors='surrogateescape', encoding='utf-8') as fout:
            titles = []
            try:
                title = soup.div['board-name']
                fout.write('# ' + title +'\n\n')
                fout.write(personalText)
            except:
                pass
            for div in soup.find_all('div'):
                if 'parent-category' in div['class']:
                    subtitle = div.find_all('h2')[0].find_all(string=True)[0]
                    reducedT = ''
                    for let in subtitle:
                        if let.isalpha():
                            reducedT += let.lower()
                        if let == ' ' or let == '-':
                            reducedT += '-'
                    titles.append([subtitle,reducedT])
                    fout.write('\n### ' + subtitle +'\n\n')
                    for link in div.find_all('a'):
                        for content in link.contents:
                            try:
                                if content['class'] == ['item-name']:
                                    fout.write('* [{}]({})\n'.format(content.contents[0],link.get('href')))
                            except:
                                pass

        with open(fname.lower() + '.md', 'r', errors='surrogateescape', encoding='utf-8') as fin:
            lines = list(fin)

        with open(fname.lower() + '.md', 'w', errors='surrogateescape', encoding='utf-8') as fout:
            for line in lines:
                fout.write(line)
                if line == personalText:
                    fout.write('\n--- \n\n## Tabla de contenidos\n')
                    for t in titles:
                        fout.write("* [{}](\#{})\n".format(t[0],t[1]))

        readme.write("* [{}](/{}.md)\n".format(title,fname.lower()[2:]))
import requests
from bs4 import BeautifulSoup

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"  
}

def remove_blank_from_beginning(s):
    for i in range(len(s)):
        if s[i] != ' ':
            return s[i:]
    return ''

def get_movies(url, headers):
    res = []
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    tars = soup.find_all(class_='info')
    for tar in tars:
        tmp = {}
        title = tar.find(class_='title').get_text()
        tmp['Title'] = title
        score = tar.find(class_='rating_num').get_text()
        tmp['Score'] = score
        info = remove_blank_from_beginning(tar.find('p').get_text().split('\n')[2])
        tmp['Info'] = info
        res.append(tmp)
    return res

def save_movies(l, direct):
    with open(direct, 'w', encoding='utf-8') as f:
        print('Name, info, score', file=f)
        for item in l:
            print(item['Title']+',', item['Info']+',', item['Score'], file=f)

if __name__ == '__main__':
    template = 'https://movie.douban.com/top250?start={}&filter='
    res = []
    for i in range(0, 250, 25):
        res += get_movies(template.format(i), headers)
    save_movies(res, 'result.csv')
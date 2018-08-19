import re
import os
def get_date(path):
    with open(path, 'r',encoding='UTF-8') as f:
        line = f.readline()
        date = re.findall('\d{8}', line)
        return int(date[0])

def generate_html():
    pass

def sort_by_dates(date_title_path):
    return sorted(date_title_path, key=lambda x: x[0], reverse=False)
    
def generate_index(date_title_path, destination='.'):
    head = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Note Index</title>
<script src="../js/switch.js"></script>
<link rel="stylesheet" type="text/css" href="css/iframe.css">
</head>

<body id="body">
<ol>'''
    tail = '''
</ol>
</body>
</html>'''
    content = ''
    for date, title, path in date_title_path:
        _date = str(date)
        content += '<li><b>{0}</b><br>\nURL: <i><a href=\"#\" onclick=\"note_goto(\'{1}\')\">{0}</a></i>\n<br>{2}年{3}月{4}日</li>'.format(title, path, int(_date[:4]), int(_date[4:6]), int(_date[6:8]))
    with open(os.path.join(destination, 'note_index.html'), mode='w', encoding='UTF-8') as f:
        f.write(head+content+tail)
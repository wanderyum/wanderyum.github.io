import re
import os
import markdown2
import codecs

def get_date_desc(path):
    with open(path, 'r',encoding='UTF-8') as f:
        line = f.readline()
        date = re.findall('\d{8}', line)[0]
        line = f.readline()
        desc = re.findall('\(.+\)', line)[0]
        return date, desc[1:-1]

def generate_html(path, destination='./source', additional_css='', style=3):
    css_style = ['code', 'fruity', 'manni', 'native', 'perldoc']
    css = css_style[style]
    
    with codecs.open(path, mode='r', encoding='utf-8') as mdfile:
        md_text = mdfile.read()

        extras = ['code-friendly', 'fenced-code-blocks', 'footnotes']
        html_text = markdown2.markdown(md_text, extras=extras)

        html_name = './source/{}.html'.format(path.split('/')[-1][:-3])
        with codecs.open(html_name, 'w', encoding='utf-8', errors='xmlcharrefreplace') as output_file:
            output_file.write(add_head_and_tail(html_text, html_name[:-5], css, additional_css))

def add_head_and_tail(content, title, css, additional_css):
    head = '<!DOCTYPE HTML>\n<html>\n<head>\n\t<meta charset=\"utf-8\">\n\t<title>%s</title>\n\t<link rel=\"stylesheet\" type=\"text/css\" href=\"css/%s.css\">\n\t%s</head>\n<body>\n' % (title, css, additional_css)
    tail = '\n</body>\n</html>'
    return head+content+tail


def sort_by_dates(date_title_desc_path):
    return sorted(date_title_desc_path, key=lambda x: x[0], reverse=False)
    
def generate_index(date_title_desc_path, destination='.'):
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
    for date, title, desc, path in date_title_desc_path:
        content += '<li><b><a href=\"#\" onclick=\"note_goto(\'{1}\')\">{0}</a></b><br>\n<i>{5}</i>\n<br>{2}年{3}月{4}日</li>'.format(title, path, int(date[:4]), int(date[4:6]), int(date[6:8]), desc)
    with open(os.path.join(destination, 'note_index.html'), mode='w', encoding='UTF-8') as f:
        f.write(head+content+tail)

import markdown2
import codecs
import sys

css_style = ['code', 'fruity', 'manni', 'native', 'perldoc']
css = css_style[3]

additional_css = ''

def main(argv):
    md_name = argv[0]

    with codecs.open(md_name, mode='r', encoding='utf-8') as mdfile:
        md_text = mdfile.read()

        extras = ['code-friendly', 'fenced-code-blocks', 'footnotes']
        html_text = markdown2.markdown(md_text, extras=extras)

        html_name = '../%s.html' % (md_name[:-3])
        with codecs.open(html_name, 'w', encoding='utf-8', errors='xmlcharrefreplace') as output_file:
            output_file.write(add_body_and_head(html_text, md_name[:-3]))

def add_body_and_head(content, title):
    head = '<!DOCTYPE HTML>\n<html>\n<head>\n\t<meta charset=\"utf-8\">\n\t<title>%s</title>\n\t<link rel=\"stylesheet\" type=\"text/css\" href=\"css/%s.css\">\n\t%s</head>\n<body>\n' % (title, css, additional_css)
    tail = '\n</body>\n</html>'
    return head + content + tail

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1:])
    else:
        print("Error:please specify markdown file path")

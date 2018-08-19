import re
def get_date(path):
    with open(path, 'r') as f:
        line = f.readline()
        date = re.findall('\d{8}', line)
        return int(date[0])

def generate_html():
    pass

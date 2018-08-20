import os
from func_share import get_date_desc, generate_html, sort_by_dates, generate_index

# 若html文件存在是否重复生成
generate_exist = True


md_root = './source/md'
html_root = './source'
md_paths = []
html_paths = []
for root, dirs, files in os.walk("./source", topdown=False):
    for name in files:
        if name[-3:] == '.md':
            md_paths.append(name)
        if name[-5:] == '.html':
            html_paths.append(name)

aim_paths = []
if generate_exist == True:
    aim_paths = md_paths
else:
    for item in md_paths:
        if item[:-3]+'.html' not in html_paths:
            aim_paths.append(item)
print('aim_paths:',aim_paths)
if len(aim_paths) == 0:
    print('No new markdown file to be converted...')
else:
    date_title_desc_path = []
    for item in aim_paths:          # aim_paths -> markdown file path
        md_path = os.path.join(md_root, item)
        date_desc = get_date_desc(md_path)     # date(int)
        generate_html(md_path)
        html_path = html_root + '/' + item[:-3]+'.html'
        date_title_desc_path.append((date_desc[0], item[:-3], date_desc[1], html_path))
    date_title_desc_path = sort_by_dates(date_title_desc_path)
    generate_index(date_title_desc_path, destination='.')





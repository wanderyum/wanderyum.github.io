import os
from func_share import get_date, generate_html, sort_by_dates

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
    paths_and_dates = []
    for item in aim_paths:
        path = os.path.join(md_root, item)
        date = get_date(path)   # date(int)
        generate_html()
        paths_and_dates.append((date, path))
        paths_and_dates = sort_by_dates(paths_and_dates)





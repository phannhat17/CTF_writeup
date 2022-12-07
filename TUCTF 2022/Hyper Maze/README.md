# Hyper Maze

## Challenge description:


## Solution description:
My script:
```python
import re
import requests
from bs4 import BeautifulSoup
 

para = ''
for i in range(101):
    url = f'https://hyper-maze.tuctf.com/pages/{para}'
    if i == 0:
        para = 'page_aesthetician100.html'
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for link in soup.find_all(href=re.compile("page_")):
            para = str(link.get('href'))
    else:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for link in soup.find_all(href=re.compile("page_")):
            para = str(link.get('href'))
        print(para)
```
Then we have the last page: `page_lagenaria1.html`  
Go to this page we have the path to flag: `3xtr4_s3cr3t_fl4g_429850252068.html`
The flag is:
```
TUCTF{y0u_50lv3d_my_hyp3r73x7_m4z3_38157}
```


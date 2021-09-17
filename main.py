# v2020.8.108011
from bs4 import BeautifulSoup
import requests
import os
import subprocess


username = str(input('Enter the github username: '))

HOMEDIR = os.path.expanduser('~')
path = HOMEDIR
tmp = input(f'Path where to save repos (Default: {HOMEDIR}):')
if tmp:
    path = tmp
path = os.path.join(path, f'{username}_repos')
if not os.path.exists(path):
    print(f'Çreating folder {path}.......')
    os.mkdir(path)


allRepoNames = []
url = f'https://github.com/{username}?tab=repositories'

print('Fetching the repo names.............')


while True:

    s = requests.get(url)
    soup = BeautifulSoup(s.text, 'html.parser')
    a = soup.findAll('h3', {'class': 'wb-break-all'})

    for i in a:
        tmp = i.find('a')
        tmp = tmp.text[9:]
        allRepoNames.append(tmp)

    try:
        pg = soup.find('div', {'class': 'paginate-container'})
        next = pg.find('a')
        url = next['href']
        if next.text == 'Previous':
            break
    except Exception as e:
        print('--------------------------------------------------\nSome error occured, If the problem persist, please create an issue on https://github.com/pvcodes/github-repo-cloner/issues, explain your issue and copy paste the below error lines...')
        print(f'{e}\n--------------------------------------------------')
        break


# print(allRepoNames)

# os.mkdir('repos')


for reponame in allRepoNames:

    # os.system()
    repo_path = os.path.join(path, f'{reponame}')
    if os.path.exists(repo_path):
        p = subprocess.Popen('git pull', cwd=repo_path)
    else:
        command = f'git clone https://github.com/{username}/{reponame}'
        print(command)
        p = subprocess.Popen(command, cwd=path)

    print(f'\nCloning {reponame} at {repo_path}....')
    p.wait()
    print('\n')

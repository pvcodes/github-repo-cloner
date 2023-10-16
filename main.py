import requests
import os
from git import Repo

from rich import print
from rich.console import Console

console = Console()
console._log_render.omit_repeated_times = False

from rich.prompt import Prompt
from rich.prompt import Confirm
# name = Prompt.ask("Enter your name", default="Paul Atreides")

# username = str(input("Enter the github username: "))
username = Prompt.ask("Enter the [bold green]Github Username[/]")

HOMEDIR = os.path.expanduser("~")
path = HOMEDIR
# tmp = input(f"Path where to save repos (Default: {HOMEDIR}):")
tmp = Prompt.ask(f"Path where to save repos",default=path)

if tmp:
    path = tmp
path = os.path.join(path, f"{username}_repos")
if not os.path.exists(path):
    console.log(f"Çreating folder {path}")
    os.mkdir(path)


url = f"https://api.github.com/users/{username}/repos"

# print("Fetching the repo names:")
with console.status("[Working on fetching repositories details]\n", spinner="aesthetic"):

    response = requests.get(url, headers={"Accept": "application/vnd.github.v3+json"})

# Getting the repo names
repos = []
if response.status_code == 200:
    res = response.json()
    console.log(f"Found [b color=cyan]{len(res)}[/    ] repositories.")
    for i in res:
        repos.append((i["name"], i["clone_url"]))

else:
    console.log(f":warning: Failed to fetch repositories. Status code: {response.status_code}")


if len(repos) == 0:
    console.log(":warning: No repositories found or invalid username")
    console.log(f":warning: Deleting the folder created {path}")
    os. rmdir(path)
    exit()


# Clone the repos to the specified path
os.chdir(path)
for repo_name, repo_url in repos:
    repo_path = os.path.join(path, f"{repo_name}")

    if os.path.exists(repo_path):
        console.log(f"[link={repo_url}]{repo_name}[/link] repository exists, pulling changes...")

        repo = Repo(repo_name)
        origin = repo.remote("origin")
        origin.pull()

    else:
        try:
            console.log(f"Cloning [link={repo_url}]{repo_name}[/link]")
            repo = Repo.clone_from(repo_url, repo_path)
            console.log(":100: [bold green]Cloned!![/]")
        except Exception as e:
            console.log(f":warning: Failed to clone [link={repo_url}]{repo_name}[/link] at {repo_path}")
            print(f":x: [bold red]{e}[/]")

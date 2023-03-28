import pandas as pd

df_repos = pd.read_csv('repo.csv', header=None, names=['repo_name'])
repo_names = df_repos['repo_name'].tolist()

print(len(repo_names))  # check the length of the repo_names list
for repo_name in repo_names:
    print(repo_name)
    # your code for extracting commit information goes here
    
extract api url
for repo_name in repo_names:
    url = f'https://api.github.com/repos/{repo_name}/commits'
    print(url)  # check the URL being used
    response = requests.get(url)
    # rest of your code for extracting commit information goes here

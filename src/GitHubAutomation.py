import requests
import random
import base64

# Replace 'YOUR_GITHUB_TOKEN' with your actual GitHub token
GITHUB_TOKEN = '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'
GITHUB_USERNAME = 'NorthernL1ghts'

adjectives = ["Brave", "Bright", "Clever", "Dynamic", "Elegant", "Fierce", "Gentle", "Innovative",
              "Majestic", "Noble", "Optimistic", "Radiant", "Sophisticated", "Vigorous"]
nouns = ["Panther", "Falcon", "Phoenix", "Dragon", "Lion", "Shark", "Eagle", "Tiger",
         "Hawk", "Dolphin", "Whale", "Wolf", "Bear", "Leopard"]

def GenerateRandomRepoName():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f'{adjective}{noun}'

def CreateGithubRepo():
    repo_name = GenerateRandomRepoName()
    url = f'https://api.github.com/user/repos'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'name': repo_name,
        'auto_init': True,
        'private': True,  # Set to True to make the repository private
        'description': f'This is a private repository named {repo_name}, created programmatically.',
        'gitignore_template': 'Python',  # Adds a .gitignore template
        'license_template': 'mit'  # Adds an MIT license
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f'Successfully created private repository: {repo_name}')
        CreateReadme(repo_name)
    else:
        print(f'Failed to create repository: {response.content}')

def GetFileSha(repo_name, file_path):
    url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/contents/{file_path}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['sha']
    else:
        return None

def CreateReadme(repo_name):
    url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/contents/README.md'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    sha = GetFileSha(repo_name, 'README.md')
    readme_content = f'# {repo_name}\n\nThis is a private repository named {repo_name}, created programmatically using a Python script. The repository includes a basic `.gitignore` file for Python projects and an MIT license.\n\n## Features\n\n- Automatically generated repository name\n- Initialized with a README, .gitignore, and MIT license\n- Private repository'
    data = {
        'message': 'Update README.md',
        'content': base64.b64encode(readme_content.encode('utf-8')).decode('utf-8'),
        'sha': sha  # Include the current sha of the file to update
    }

    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f'Successfully updated README.md for repository: {repo_name}')
    else:
        print(f'Failed to update README.md: {response.content}')

if __name__ == '__main__':
    CreateGithubRepo()

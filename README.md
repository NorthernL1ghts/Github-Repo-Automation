
# GitHub Repository Automation Script

This Python script automates the creation of new GitHub repositories with randomized names, a basic `README.md`, a `.gitignore` file for Python, and an MIT license. It is designed for developers who need to quickly set up new repositories with minimal manual effort.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Functionality](#code-functionality)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

The **GitHub Repository Automation Script** streamlines the process of creating new repositories on GitHub. It generates repositories with random, meaningful names, initializes them with essential files, and ensures they are private. This tool is ideal for developers and teams looking to save time by automating repetitive tasks involved in setting up new projects.

---

## Features

- **Randomized Repository Names**: Generates unique names using combinations of adjectives and nouns.
- **Initialization with Essential Files**: Automatically includes a `README.md`, `.gitignore` (Python template), and an MIT license.
- **Private Repositories**: Ensures all created repositories are private by default.
- **Error Handling**: Implements robust error handling for API responses and file updates.

---

## Prerequisites

- Python 3.x installed on your system.
- A GitHub account with a personal access token (generate one via GitHub settings).

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/github-repo-automation.git
   cd github-repo-automation
   ```

2. Install the required dependencies:

   ```bash
   pip install requests
   ```

---

## Usage

1. Replace `GITHUB_TOKEN` and `GITHUB_USERNAME` in the script with your actual GitHub token and username.

2. Run the script:

   ```bash
   python create_repo.py
   ```

---

## Code Functionality

### `GenerateRandomRepoName`
Generates random repository names using combinations of adjectives and nouns.

```python
def GenerateRandomRepoName():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f'{adjective}{noun}'
```

### `CreateGithubRepo`
Creates a new repository on GitHub using the API.

```python
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
        'private': True,
        'description': f'This is a private repository named {repo_name}, created programmatically.',
        'gitignore_template': 'Python',
        'license_template': 'mit'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f'Successfully created private repository: {repo_name}')
        CreateReadme(repo_name)
    else:
        print(f'Failed to create repository: {response.content}')
```

### `GetFileSha`
Retrieves the `sha` of a file to enable updates.

```python
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
```

### `CreateReadme`
Updates the `README.md` file in the repository.

```python
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
        'sha': sha
    }
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f'Successfully updated README.md for repository: {repo_name}')
    else:
        print(f'Failed to update README.md: {response.content}')
```

---

## Contributing

To contribute, fork the repository and submit a pull request with your changes. For major changes, open an issue first to discuss your proposed modifications.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

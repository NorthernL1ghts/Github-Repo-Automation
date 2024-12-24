import os
import requests
import subprocess

class GitHubRepositoryAutomation:
    def __init__(self, m_GitHubUsername, m_GitHubToken, m_RepositoryName, m_Description):
        self.m_GitHubUsername = m_GitHubUsername
        self.m_GitHubToken = m_GitHubToken
        self.m_RepositoryName = m_RepositoryName
        self.m_Description = m_Description

    def CreateGitHubRepository(self):
        url = f'https://api.github.com/user/repos'
        headers = {
            'Authorization': f'token {self.m_GitHubToken}',
            'Accept': 'application/vnd.github.v3+json'
        }
        data = {
            'name': self.m_RepositoryName,
            'description': self.m_Description,
            'private': False,
            'auto_init': False
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            print(f'Repository {self.m_RepositoryName} created successfully.')
        else:
            print(f'Failed to create repository: {response.json()["message"]}')
            return None

        return f'https://github.com/{self.m_GitHubUsername}/{self.m_RepositoryName}.git'

    def PushFilesToRepository(self, repo_url):
        relative_path = os.path.join('..', 'resources')
        os.chdir(relative_path)
        commands = [
            'git init',
            'git add .',
            'git commit -m "Initial commit"',
            f'git remote add origin {repo_url}',
            'git push -u origin master'
        ]

        for command in commands:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode != 0:
                print(f'Error: {stderr.decode().strip()}')
            else:
                print(stdout.decode().strip())

class EntryPoint:
    @staticmethod
    def Main():
        m_GitHubUsername = input('Enter your GitHub username: ')
        m_GitHubToken = input('Enter your GitHub token: ')
        m_RepositoryName = input('Enter the name of the repository: ')
        m_Description = input('Enter a description for the repository: ')

        automation = GitHubRepositoryAutomation(m_GitHubUsername, m_GitHubToken, m_RepositoryName, m_Description)
        repo_url = automation.CreateGitHubRepository()
        if repo_url:
            automation.PushFilesToRepository(repo_url)

if __name__ == "__main__":
    EntryPoint.Main()

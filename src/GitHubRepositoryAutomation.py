import requests
import json

class GitHubRepositoryAutomation:
    def __init__(self, token, username):
        self.m_token = token
        self.m_username = username

    def CreateRepository(self, repo_name, repo_description):
        url = 'https://api.github.com/user/repos'
        headers = {
            'Authorization': f'token {self.m_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        data = {
            'name': repo_name,
            'description': repo_description,
            'private': False  # Set to True if you want the repo to be private
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 201:
            print(f"Repository '{repo_name}' created successfully.")
        else:
            print(f"Failed to create repository. Status code: {response.status_code}")
            print(f"Response: {response.json()}")

class EntryPoint:
    @staticmethod
    def Main():
        GITHUB_TOKEN = 'your_github_token'  # Replace with your GitHub personal access token
        GITHUB_USERNAME = 'your_github_username'  # Replace with your GitHub username

        repo_name = input("Enter the repository name: ")
        repo_description = input("Enter the repository description: ")

        automation = GitHubRepositoryAutomation(GITHUB_TOKEN, GITHUB_USERNAME)
        automation.CreateRepository(repo_name, repo_description)

if __name__ == '__main__':
    EntryPoint.Main()

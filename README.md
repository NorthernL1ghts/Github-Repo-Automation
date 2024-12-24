
# GitHub-Repository-Automation

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/NorthernL1ghts/Github-Repo-Automation/blob/main/LICENSE)

## Overview
`GitHub-Repository-Automation` is a Python-based tool that simplifies the process of creating and managing GitHub repositories. With minimal input, it sets up a repository with:
- Pre-configured **VSCode settings** for C, C++, and Python development.
- Essential files like `.gitignore`, `LICENSE` (MIT), and a `README.md` file.
- Automatic file push to the newly created GitHub repository.

---

## Features
- **Automated Repository Creation:** Creates a GitHub repository using your GitHub username and personal access token.
- **Pre-Configured Development Environment:** Includes a `.vscode/` folder for:
  - Settings for Python, C, and C++ development.
  - Extension recommendations for developers.
- **Essential Project Files:** Adds:
  - `.gitignore` tailored for most projects.
  - MIT License.
  - A `README.md` file.
- **Streamlined Workflow:** Automatically initializes the repository locally, commits changes, and pushes them to GitHub.

---

## Prerequisites
1. **Python 3.x:** Ensure Python is installed on your system.
2. **Git:** Make sure Git is installed and accessible via the command line.
3. **GitHub Account:** A personal access token (PAT) with the necessary permissions to create repositories and push code.
4. **Libraries:** Install the required Python libraries:
   ```bash
   pip install requests
   ```

---

## Tech Stack
- **Programming Language:** Python
- **APIs:** GitHub REST API (v3)
- **Version Control:** Git

---

## Installation and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/NorthernL1ghts/Github-Repo-Automation.git
cd Github-Repo-Automation
```

### 2. Run the Script
Execute the script with Python:
```bash
python GitHubRepositoryAutomation.py
```

### 3. Provide User Inputs
The script will prompt you to enter:
- **GitHub Username:** Your GitHub account name.
- **Personal Access Token:** Your GitHub token (ensure it has repository permissions).
- **Repository Name:** The name for your new repository.
- **Repository Description:** A brief description of the repository.

### 4. Output
- A new repository is created on your GitHub account.
- Files (`.vscode/`, `.gitignore`, `LICENSE`, and `README.md`) are added to the repository.
- The changes are committed and pushed to GitHub.

---

## Example Workflow

1. **Input:**
   ```
   Enter your GitHub username: NorthernL1ghts
   Enter your GitHub token: <your-token>
   Enter the name of the repository: GitHub-Repository-Automation
   Enter a description for the repository: Automates GitHub repository setup with essential files.
   ```

2. **Output:**
   ```
   Repository GitHub-Repository-Automation created successfully.
   Initialized empty Git repository in <local-path>
   [master (root-commit) abc1234] Initial commit
   5 files changed, 100 insertions(+)
   create mode 100644 .vscode/settings.json
   create mode 100644 .gitignore
   create mode 100644 LICENSE
   create mode 100644 README.md
   ```

---

## License
This project is licensed under the [MIT License](https://github.com/NorthernL1ghts/Github-Repo-Automation/blob/main/LICENSE).

Feel free to fork, contribute, or submit issues!

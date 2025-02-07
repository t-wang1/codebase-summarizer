import os
import git 

def clone_repo(repo_url, repo_path):
    if os.path.exists(repo_path):
        print("repository exists. pulling changes")
        repo = git.Repo(repo_path)
        repo.remotes.origin.pull()
    else:
        print("cloning repository from {repo_url}")
        git.Repo.clone_from(repo_url, repo_path)
    
    return repo_path


import git
import os
import shutil

# Function to check for updates and pull if needed
def update_repo_if_needed(repo_url, local_dir):
    if os.path.exists(local_dir):
        # Open the existing repository
        repo = git.Repo(local_dir)
        
        # Fetch the latest changes from the remote repository
        print("Fetching latest changes from the remote repository...")
        repo.remotes.origin.fetch()
        
        # Check if the local branch is behind the remote branch
        local_commit = repo.head.commit
        remote_commit = repo.remotes.origin.refs[repo.active_branch.name].commit
        
        if local_commit != remote_commit:
            print("Local repository is outdated. Pulling the latest changes...")
            repo.remotes.origin.pull()
            print("Repository updated successfully.")
            return True  # Return True to indicate that the repo was updated
        else:
            print("The local repository is already up to date.")
            return False  # No updates, return False
    else:
        # If the directory does not exist, clone the repository
        print(f"Cloning repository {repo_url} into {local_dir}.")
        git.Repo.clone_from(repo_url, local_dir)
        return True  # Repo cloned for the first time

# Function to copy a file from the repo to a specific destination
def copy_file_from_repo(local_repo_path, file_to_copy, destination_path):
    # Ensure that the destination directory exists
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    # Full path of the file in the repo
    source_file = os.path.join(local_repo_path, file_to_copy)
    
    if os.path.exists(source_file):
        print(f"Copying {source_file} to {destination_path}.")
        shutil.copy(source_file, destination_path)
        print("File copied successfully.")
    else:
        print(f"File {file_to_copy} not found in the repo.")

# Main function to check for updates and copy file
def check_update_and_copy(repo_url, local_repo_dir, file_to_copy, destination_path):
    # Check if repo needs an update
    if update_repo_if_needed(repo_url, local_repo_dir):
        # If the repo was updated or cloned, copy the specific file
        copy_file_from_repo(local_repo_dir, file_to_copy, destination_path)
    else:
        print("No updates found, skipping file copy.")

# Usage example
repo_url = "https://github.com/ankitalodha05/newCICD.git"  # Replace with the actual repo URL
local_repo_dir = "/newproject/newCICD"  # Temporary directory to clone the repo
file_to_copy = "/newproject/newCICD/index.html"  # Path inside the repo
destination_path = "/usr/share/nginx/html/index.html"  # Path on the server where file should be copied

# Check for updates and copy the file if necessary
check_update_and_copy(repo_url, local_repo_dir, file_to_copy, destination_path)

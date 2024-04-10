import os
from pathlib import Path
import subprocess

#function to clone a directory when provided with url
def clone_a_directory_from_git(clone_url):
    try:
        subprocess.run(["git", "clone", clone_url], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("repo has been clonned")
    except subprocess.CalledProcessError as e:
        print("error:", e.stderr.decode().strip())

#function to create a new directory in github
def add_directory_to_git(directory_name, commit_message, remote_repo_url, branch_name="main"):
    try:
        path = os.path.join(os.getcwd(), directory_name)
        os.chdir(path)
        subprocess.run(["gh", "repo", "create", directory_name, "--public"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["git", "init"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["git", "add", "."], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["git", "commit", "-m", commit_message], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["git", "remote", "add", "origin", remote_repo_url], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["git", "branch", branch_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["git", "push", "--set-upstream", "origin", branch_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("repo has been created")
    except subprocess.CalledProcessError as e:
        print("error:", e.stderr.decode().strip())

#function to get the details for cloning or making a repo in github
def get_details(flag_repo):
    if flag_repo=="n":
        clone_url = input("Paste the url of the repo you want to clone: ")
        clone_a_directory_from_git(clone_url=clone_url)
    elif flag_repo=="y":
        branch_name = input("Enter the branch name: ")
        commit_message = input("Enter first commit messgage: ")
        remote_repo_url = "https://github.com/PManiAwasthi/" + NAMEOFPROJECT +".git"
        add_directory_to_git(NAMEOFPROJECT, commit_message, remote_repo_url, branch_name)
    else:
        print("wrong input exiting script.....")

#function to make the folder structure
def make_folders(list_of_files):
    for filepath in list_of_files:
        flag = 0
        if NAMEOFPROJECT in filepath or filepath == 'src':
            flag = 1
        
        filepath = os.path.join(src_path, filepath)
        if filepath != "" :
            os.makedirs(filepath, exist_ok = True)
            if flag == 1:
                with open(os.path.join(filepath, "__init__.py"), 'w') as f:
                    pass


flag_folder = input("Do you want to create a folder structure. (y/n): ")

if flag_folder=='y':
    NAMEOFPROJECT = input("Enter the name of the project: ")
    src_path = os.path.join(os.getcwd(), NAMEOFPROJECT)
    inside_main_project_path = os.path.join('src', NAMEOFPROJECT+"_Project")

    list_of_files = [
        "config",
        "src",
        "experiment",
        "data",
        inside_main_project_path,
        os.path.join(inside_main_project_path, "component"),
        os.path.join(inside_main_project_path, "constant"),
        os.path.join(inside_main_project_path, "entity"),
        os.path.join(inside_main_project_path, "exception"),
        os.path.join(inside_main_project_path, "logger"),
        os.path.join(inside_main_project_path, "pipeline"),
        os.path.join(inside_main_project_path, "utils"),
    ]
    make_folders(list_of_files)
    print("Folder have been created.")
    flag_repo = input("Do you want to create a repo. (y/n): ")
    get_details(flag_repo)
else:
    print("wrong input...")








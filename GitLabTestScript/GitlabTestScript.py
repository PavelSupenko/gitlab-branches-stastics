import gitlab
import v4.objects
from colorama import init, Fore, Back, Style

string_splitter = "\n------------------------------"

# init colorama
init()


class ProjectInformation:
    project_name = None
    project = None


def is_branch_named_correctly(branch_name):
    return \
        branch_name == "develop" or \
        branch_name == "master" or \
        "feature/" in branch_name or \
        "hotfix/" in branch_name or \
        "release/" in branch_name


def get_project_name(project):
    return str(project.web_url).split("/")[-1]

token = raw_input("Enter you GitLab token: ")


print string_splitter
print "Projects you have access to:"

gl = gitlab.Gitlab('https://gitlab.magestudio.io/', private_token=token)
gl.auth()

projects = gl.projects.list()
projectsDictionary = None
project_index = 0

for project in projects:
    projectName = get_project_name(project)

    project_info = ProjectInformation()
    project_info.project = project
    project_info.project_name = projectName

    projects[project_index]
    project_index = project_index+1

    print ("[" + str(project_index) + "] " + projectName)


print string_splitter
chosen_project_number = -1
while True:
    while chosen_project_number < 1 or chosen_project_number > project_index:
        chosen_project_number = int(raw_input("Choose project number: "))

    print get_project_name(projects[chosen_project_number-1])
    print string_splitter

    branches = projects[chosen_project_number-1].branches.list()

    correct_named_branches = 0
    wrong_named_branches = 0
    for branch in branches:
        branch_name = branch.name
        is_correct = is_branch_named_correctly(branch_name)

        if is_correct:
            correct_named_branches = correct_named_branches + 1
            print (Fore.GREEN + branch_name)
        else:
            wrong_named_branches = wrong_named_branches + 1
            print (Fore.RED + branch_name)

    print(Fore.RESET)
    print string_splitter
    print ("Wrong named branches:   " + str(wrong_named_branches))
    print ("Correct named branches: " + str(correct_named_branches))
    print string_splitter
    chosen_project_number = -1

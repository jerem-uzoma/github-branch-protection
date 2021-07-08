from github import Github

# Creating this to mass update all of our repos settings.

# First you need to create a personal token (this way the script will know what access you have to repos).
# https://github.com/settings/tokens
# reduce the scope of the access token only to the repo, then grant all repo access except delete repo.

# Uses https://github.com/PyGithub/PyGithub

g = Github("TOKEN_HERE")  # Your personal token


def change_protected_branch_settings():
    # Loops through all the repos and changes the /settings/branch_protection_rules/
    # CAREFUL with this!
    for repo in g.get_user().get_repos():
        branch = repo.get_branch("master")
        branch.edit_protection(
            required_approving_review_count=2, enforce_admins=True)
        print("Edited the branch protection rules for: " + repo.name)


def change_protected_branch_settings_test():
    repo = g.get_repo("org/repo_name")
    branch = g.get_repo("org/repo_name").get_branch("master")
    branch.edit_protection(
        required_approving_review_count=2, enforce_admins=True)

# Uncomment out one of these lines. change_protected_branch_settings() is for the whole org, Test tis for a single repo/branch.
# change_protected_branch_settings()
# change_protected_branch_settings_test()

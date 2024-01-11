from github import Github, GithubException

# Replace with your GitHub token
github_token = "YOUR_GITHUB_TOKEN"
repo_name = "YourRepoName"
organization_name = ""
branch_name = "master"

"""
Explanation:

This function, check_and_fix_branch_protection, takes a GitHub repository object as its argument.
It retrieves information about the specified branch (default is "master") in the given repository.
If the branch is not protected, it prints a message indicating that the branch is not protected and provides information about the repository and branch.
It includes lines of code to enable branch protection. These lines edit the branch protection settings with options like required status checks, enforcement for administrators, and restrictions.
After enabling branch protection, it prints a confirmation message.
If the branch is already protected, it prints a message indicating that the branch is already protected in the specified repository.
"""


def check_and_fix_branch_protection(repository):
    branch = repository.get_branch(branch_name)

    if not branch.protected:
        print(f"Branch '{branch_name}' in '{repository.full_name}' repository is not protected.")
        branch.edit_branch_protection(
            required_status_checks=None,
            enforce_admins=True,
            restrictions=None
        )
        print(f"Branch {branch_name} is now protected.")
    else:
        print(f"Branch '{branch_name}' in '{repository.full_name}' repository is already protected.")

#
# def check_and_fix_mfa(repository):
#     for user in repository.get_collaborators():
#         if not user.get_verified():
#             print(f"MFA is not enabled for user: {user.login}")
#             user.create_gpg_key(title="MFA Enabled Key", key="YOUR_GPG_KEY")
#             print(f"MFA has been enabled for user: {user.login}")


def main():
    try:
        g = Github(github_token)
        repo = g.get_repo(repo_name)

        check_and_fix_branch_protection(repo)
        # check_and_fix_mfa(repo)
    except GithubException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

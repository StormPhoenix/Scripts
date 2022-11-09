import subprocess
import git


def get_repo(path):
    return git.Repo(path)


def checkout_local(repo, branch_name):
    if branch_name in repo.branches:
        repo.git.checkout(branch_name)
    else:
        # create new branch
        repo.git.checkout('-b', branch_name)


def merge_local_branch(repo, merge_from, merge_to):
    if merge_to is None:
        merge_to = repo.active_branch
    raw_branch = repo.active_branch
    checkout_local(repo, merge_to)
    repo.git.merge(merge_from)
    checkout_local(repo, raw_branch)


def merge_remote_branch(repo, remote_name, merge_from, merge_to):
    if merge_to is None:
        merge_to = repo.active_branch

    raw_branch = repo.active_branch
    checkout_local(repo, merge_to)
    repo.git.merge('{}/{}'.format(remote_name, merge_from))
    checkout_local(repo, raw_branch)


def push_to_remote(repo, local_branch, remote_name='origin'):
    if local_branch is None:
        local_branch = repo.active_branch

    remote = repo.remote(name=remote_name)
    remote.push(local_branch)

def reset_to_remote(repo, local_branch, remote_name, remote_branch):
    raw_branch = repo.active_branch
    checkout_local(repo, local_branch)
    repo.git.reset('--hard', '{}/{}'.format(remote_name, remote_branch))
    checkout_local(repo, raw_branch)


def config_remote(repo, remote_name, remote_url):
    if remote_name is None or remote_url is None:
        return

    if remote_name in repo.remotes:
        repo.delete_remote(remote_name)
    return repo.create_remote(remote_name, url=remote_url)


def checkout_remote(repo, remote_name, remote_branch):
    local_branch = remote_branch

    checkout_local(repo, local_branch)
    repo.git.reset('--hard', '{}/{}'.format(remote_name, remote_branch))
    repo.git.branch('--set-upstream-to={}/{}'.format(remote_name, remote_branch), local_branch)


def get_remote_url(repo, remote_name):
    if remote_name is None:
        return None

    if remote_name not in repo.remotes:
        return None

    remote = repo.remote(remote_name)
    return remote.url


if __name__ == '__main__':
    cmd_path = r'C:\Users\StormPhoenix\Workspace\Scripts'

    git_repo = get_repo(cmd_path)
    checkout_local(git_repo, 'cb')
    push_to_remote(git_repo, local_branch='cb', remote_name='origin')

    url = get_remote_url(git_repo, 'origin')
    remote = config_remote(git_repo, 'test_origin', url)
    remote.fetch()

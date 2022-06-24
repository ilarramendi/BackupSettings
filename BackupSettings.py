from git import Repo

PATH_OF_GIT_REPO = ".git/"  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'Test commit from python script'

def git_push():
    repo = Repo(PATH_OF_GIT_REPO)
    repo.git.add(all=True)
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name='origin')
    origin.push()

git_push()
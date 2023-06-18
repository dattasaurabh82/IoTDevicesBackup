#!/usr/bin/env python3

import os
curr_dir = os.path.join(os.path.dirname(__file__))
# print(curr_dir)

from git import Repo

repo = Repo(curr_dir)

# check that the repository loaded correctly
if not repo.bare:
    print('Repo at {} successfully loaded.'.format(curr_dir))
    if repo.is_dirty(untracked_files=True):
        print('Changes detected.')
        # Provide a list of the files to stage
        repo.index.add(".")
        repo.index.commit("test commit")
        repo.remotes.origin.push()
    else:
        print('No new changes detecetd')
else:
    print('Could not load repository at {} :('.format(curr_dir))

# repo_path = 
# assert not repo.bare

# my_repo = git.Repo('some_repo')
# if my_repo.is_dirty(untracked_files=True):
#     print('Changes detected.')
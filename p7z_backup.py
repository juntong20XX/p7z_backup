"""

"""

from subprocess import run

path_base = "/mnt/HDD16T-1/nextcloud-docker/data/"
users = ["ray", "hmm", "work", "NextCloud-docker"]
path_end = ["/files"]

for user in users:
    path_ = path_base + user
    for end in path_end:
        name = user + end[1:] + ".7z"
        cmd = ["7z", "a", name, path_ + end + "/*"]
        print(cmd)
        run(cmd)

#!/usr/bin/env python
import os
from multiprocessing import Pool
import subprocess

def run(task):
    subprocess.call(["rsync", "-arq", src, dest])

src = "/data/prod/"
dest = "/data/prod_backup/"
tasks = os.walk(src)
p = Pool(len(tasks))
p.map(run, tasks)
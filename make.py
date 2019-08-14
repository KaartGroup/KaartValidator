#!/usr/bin/env python3
import json
import os
import glob
import shutil
import git # I use GitPython
import datetime

PROJECT_DIRECTORY = "projects"
MODULE_DIRECTORY = "modules"

def projectData(project):
    with open(project) as f:
        return json.load(f)

def getVersion(filename):
    git_object = git.Repo(os.path.dirname(filename)).git
    version = str(len(git_object.log(filename).split('\n')))
    date = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    return version + "_" + date


def writeHeader(filename, data):
    if "meta" in data:
        meta = data['meta']
        with open(filename, 'w') as f:
            f.write("meta\n")
            f.write("{\n")
            for key in meta:
                f.write("  " + str(key) + ": \"" + str(meta[key]) + "\";\n")
            f.write("  version: \"" + getVersion(filename) + "\";\n")
            f.write("}\n")
        return True
    return False

def writeTests(filename, module):
    with open(filename, 'a') as f, open(module, 'r') as m:
        for line in m:
            f.write(line)

def addTests(filename, data):
    if not "modules" in data:
        return False
    modules = data['modules']
    for module in modules:
        writeTests(filename, os.path.join(MODULE_DIRECTORY, module))
        if (modules.index(module) == len(modules) - 1):
            break
        with open (filename, 'a') as f:
            f.write("\n")
    return True

if __name__ == "__main__":
    projects = glob.glob(os.path.join(PROJECT_DIRECTORY, "*.json"))
    for project in projects:
        data = projectData(project)
        filename = 'kaart.' + os.path.splitext(os.path.basename(project))[0] + '.validator.mapcss'
        writeHeader(filename, data)
        addTests(filename, data)
    shutil.copyfile('kaart.clingstone.validator.mapcss', 'kaart.validator.mapcss')

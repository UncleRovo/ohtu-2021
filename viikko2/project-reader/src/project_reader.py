from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        dict_content = toml.loads(content)
        
        name = dict_content["tool"]["poetry"]["name"]
        desc = dict_content["tool"]["poetry"]["description"]
        deps = dict_content["tool"]["poetry"]["dependencies"]
        devdeps = dict_content["tool"]["poetry"]["dev-dependencies"]

        return Project(name, desc, deps, devdeps)

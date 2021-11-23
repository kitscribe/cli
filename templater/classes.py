import os


class Templater:
    def __init__(self, name, template_file):
        self.root = os.path.join(os.curdir, name)
        self.template_file = template_file
        os.mkdir(self.root)

        with open(template_file, 'r') as f_handler:
            for line in f_handler:
                # get the routes and make it a list of directories
                routes = list(filter(lambda x: x != '', line.strip().split("/")))
                dirs = routes[:-1]
                file = routes[-1]

                for directory in dirs:
                    d = os.path.join(self.root, directory)
                    if not os.path.exists(d):
                        os.mkdir(d)

                if file != "_":
                    with open(os.path.join(self.root, *dirs, file), "w"):
                        pass

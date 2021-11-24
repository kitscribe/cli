import os


class Templater:
    def __init__(self, name, template_file):
        self.root = os.path.join(os.curdir, name)
        self.templates_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')
        self.template_file = os.path.join(self.templates_dir, template_file + ".tmpl")

    def make(self):
        os.mkdir(self.root)

        if not os.path.exists(os.path.join(self.templates_dir, self.template_file)):
            raise ValueError("No template exists with the given name")

        with open(self.template_file, 'r') as f_handler:
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

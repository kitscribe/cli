# Templater
A CLI tool to make project templates directories and files with the given project name by the template file

## Usage
* Clone the repo
* Create `/opt/cli` directory and add it to the `PATH`
* Create a symlink for the `main.py` using `sudo ln -s /<absolute path to the main.py> /opt/cli/templater`
* Check if `main.py` is executable
* Open templates folder and create a text file with `*.tmpl` extension
* Describe there what directories and files do you want to create using this template 
* Run `templater -n <projectName> -t <templateName> (without .tmpl extension)`
* Example `templater -n testproject -t web`

### How to describe a template?
Template is a set of rows with the directories to the file or empty folders.
Here's a simple web template:

```
/index.html
/css/style.css
/scripts/script.js
/images/_
```

It would create an `index.html` file into the root, `style.css` file within the `css` folder
and a `script.js` - within the `scripts`. It also creates an empty folder named `images`

So then, to create the template all you need is to describe it's files and directories.
If you need an empty folder, you have to put `_` sign after the folder name.
For example, `/data/backups/_` or `/images/_`
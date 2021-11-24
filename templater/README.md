# Templater
A CLI tool to make project templates directories and files with the given project name by the template file

## Usage
* Clone the repo and add it's directory to the `PATH`
* Open templates folder and create a text file with `*.tmpl` extension
* Describe there what directories and files do you want to create
* Open the terminal and change the directory to your projects folder
* Then run `templater -n <projectName> -t <templateName>`
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
as a `script.js` within the `scripts`. It also creates blank folder named `images`.

So, to create the template all you need is to describe it's files and directories.
If you need a blank folder, you have to put `_` sign after the folder name.
For example, `/data/backups/_` or `/images/_`
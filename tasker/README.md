# Simple CLI Task Manager

## Usage
* Clone the repo
* Create `/opt/cli` directory and add it to the `PATH`
* Create symlink for the `main.py` using `sudo ln -s /<absolute path to main.py /opt/cli/tasker`
* Check if `main.py` file is executable
* Run the tasker with `tasker -a <task title>`
* To list your tasks use `tasker -l`
* To remove one - `tasker -rm <task id>`

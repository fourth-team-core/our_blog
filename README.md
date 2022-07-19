# Team 4 blog
### GB diploma project MVP


## Installation ##

### Easy way: ###

- Open pycharm
- Find "create new project" option
- Choose from CVS
- Paste link to project 
  - git@github.com:fourth-team-core/our_blog.git 
  - Try this one if you don't use SSH: https://github.com/fourth-team-core/our_blog.git
- Choose directory
- Press "Create"
- Follow the advices of Pycharm


### Manual installation:
- Make sure you have poetry installed
https://python-poetry.org/
- clone project from git
- go to project dir and run 
```
poetry init
``` 
- wait for project installation


### Run the project (basic run)
- copy `blog/.env.temlpate` file and rename to just `.env` 
- go to blog directory and run
```
python manage.py runserver
```

You are goint to see something like this in the terminal
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 18, 2022 - 18:33:48
Django version 4.0.6, using settings 'blog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
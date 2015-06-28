# logfind
The logfind tool is designed to find all the log files that have at least one instance of some text by just typing this:

$ logfind deonheyns

The results of this will be a list of all files that have one instance of the word ‘deonheyns’ in them, which I can then pass to another tool if I want.

### Features
- [X] Specify what files are important in a ~/.logfind file, using regular expressions.

- [X] Logfind takes any number of arguments as strings to find in those files, and assumes you mean and. So looking for "deon has blue eyes" means files that have "deon AND has AND blue AND eyes" in it.

- [X] You can pass in one argument, -o (dash oh) and the default is then or logic instead. In the example above -o would change it to mean "deon OR has OR blue OR eyes".

- [X] Ability to install logfind on my computer and run it like other projects.

- [X] You can specify regular expressions as things to find in files.

The logfind challenge is [project 1 of Projects the Hard Way](http://projectsthehardway.com/2015/06/16/project-1-logfind-2/) by [Zed Shaw](http://zedshaw.com/) 
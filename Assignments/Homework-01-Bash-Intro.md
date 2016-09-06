# Bash Homework 1
Due: Tuesday September 13th by Class time.


### Prep Work

1. Make sure there is a user: `griffin` on your server with the password `2D2016!!!` and sudo access (if there is not it will mean an automatic zero for this assignment).
2. Clone your github repository in the folder: `/opt/`. Make sure the permissions on this folder are `755`.
3. Make a folder called `assignments` in your github repo.
4. Make another folder called `homework-01` in the `assignments` folder.
5. All scripts for this assignment will be in the `homework-01` folder.
6. The contents of the `homework-01` folder should also be in a folder called `homework-01` the same level as your github repo in `/opt` (this will make the path consistent on everyone's server so I can find your programs faster).

### Work Flow

You can get your work done however you want as long as your scripts end up:

1. In your github repo in the correct folders.
2. On your server at the prescribed path. 

One method of work would be:

1. Create a folder called `homework-01` in gitbash (doesn't matter where).
2. Keep working locally in gitbash and forget about the server or github for now.
2. Write all your scripts (naming them correctly) in this folder.
3. You can use notepad++ or any editor to get this done since your local.
3. Once finished, copy the folder and its contents to your repository (assuming you cloned it already).
4. Then run:
    - `git add -A`
    - `git comit -m "adding homework 1"`
    - `git push origin master`

Another method would be:

1. Fire up notepad++ and turn on the `npp-ftp` plugin.
2. Add a connection to your server (Instructions can be found [here](http://www.addictivetips.com/windows-tips/nppftp-for-notepad-access-download-edit-code-files-on-ftp-server/))

| Notepad ++ Connect via SFTP|
|:----------------:|
| Click the "cog" wheel to open profile settings: |
| ![](https://d3vv6lp55qjaqc.cloudfront.net/items/183u17421b3s3u012p3Z/npp1.png?X-CloudApp-Visitor-Id=1094421) |
| Create a new profile: |
| ![](https://d3vv6lp55qjaqc.cloudfront.net/items/1a2s0w1s2i0M3a1d1T3h/npp2.png?X-CloudApp-Visitor-Id=1094421) |
| Choose that profile to log in: |
| ![](https://d3vv6lp55qjaqc.cloudfront.net/items/422h3Q0X093r1w473Z2c/npp3.png?X-CloudApp-Visitor-Id=1094421) |

### Script 1

- Create a script called `command_args.sh` which will read in all command line arguments and print them out.
- For example `$ ./command_args.sh arg1 "hello" 44` would print out:

```
command_args.sh
(contents of arg1)
hello
44
```



### Script 2


- Create a script which will print a random word. There is a file containing a list of words on your system (usually /usr/share/dict/words or /usr/dict/words). Hint: Piping will be useful here.
- Name this script: `myrandom.sh` and when run, should print out 1 random word to std out.


### Script 3 

- Create a script which will take a filename as its first argument and create a dated copy of the file. eg. if the file was named `file1.txt` it would create a copy such as `2016-01-28_file1.txt`. (To achieve this you will probably want to play with command substitution and the command date).
- Name this script `versiona.sh`.

### Script 4

- Using the script from `versiona.sh`, see if you can get it so that the date is after the name of the file (eg. file1_2016-01-28.txt (The command `basename` can be useful here.)
- Name this script `versionb.sh`. 

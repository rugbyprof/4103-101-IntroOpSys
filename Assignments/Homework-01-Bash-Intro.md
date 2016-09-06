# Bash Homework 1
Due: Tuesday September 13th by Class time.



## Warning

- Folder names, paths, filenames are all case sensitive. 
- Nearly every assignment I ask you to do the same things. 
- For example: 
    - create a folder called `homework_X` and put it in the `/xyz` folder and then write a script called `abc-1.sh` and put it the `homework_X` folder.
- Then I will log in to your server and try to execute 
    - `/xyz/homework_X/abc-1.sh`
- The path above is NOT the same path as:
    - `/xyz/homework_Y/abc-1.sh`
    - `/xyz/homework-X/abc-1.sh`
    - `/xyz/homework_X/abd-1.sh`
- One character wrong means I don't find it (and I don't grade it). 
- So read carefully and if I didn't specify a name for your files, you may want to ask. 

## Prep Work

1. Make sure there is a user: `griffin` on your server with the password `2D2016!!!` and sudo access (if there is not it will mean an automatic zero for this assignment).
2. Clone your github repository in the folder: `/opt/`. Make sure the permissions on this folder are `755`.
3. Make a folder called `assignments` in your github repo.
4. Make another folder called `homework-01` in the `assignments` folder.
5. All scripts for this assignment will be in the `homework-01` folder (that's in the `assignments` folder).
6. A copy of the `homework-01` folder should also be at the same level as your github repo in `/opt` (this will make the path consistent on everyone's server so I can find your programs faster).

![](https://d3vv6lp55qjaqc.cloudfront.net/items/1b2s3x3z2a290E2W0K3X/Image%202016-09-06%20at%2012.40.55%20PM.png?X-CloudApp-Visitor-Id=1094421)

### Work Flow (Still Prep)

You can get your work done however you want as long as your scripts end up:

1. In your github repo which also ends up on github.
2. On your server at the prescribed path. 
3. In the correctly named folders. 

One method of work would be (preferred):

- Create a folder called `homework-01` in gitbash (doesn't matter where).
- Keep working locally in gitbash (in your `homework-01` folder) and forget about the server or github for now.
- Write all your scripts (naming them correctly) in this folder.
- You can use notepad++ or any editor to get this done since your local and not connecting via SFTP.
- Once finished, copy the folder and its contents to your repository (assuming you cloned it already).
- Then run:
    - `git add -A`
    - `git comit -m "adding homework 1"`
    - `git push origin master`
- Login to your server and goto directory `/opt`
- Run `git pull git@github.com:yourusername/your4103repo.git`
- `cp -r your4103repo/assignments/homework-01 .` 

Another method would be:

- Connect via the `npp-ftp` plugin.

| Notepad ++ Connect via SFTP|
|:----------------:|
| Click the "cog" wheel to open profile settings: |
| ![](https://d3vv6lp55qjaqc.cloudfront.net/items/183u17421b3s3u012p3Z/npp1.png?X-CloudApp-Visitor-Id=1094421) |
| Create a new profile: |
| ![](https://d3vv6lp55qjaqc.cloudfront.net/items/1a2s0w1s2i0M3a1d1T3h/npp2.png?X-CloudApp-Visitor-Id=1094421) |
| Choose that profile to log in: |
| ![](https://d3vv6lp55qjaqc.cloudfront.net/items/422h3Q0X093r1w473Z2c/npp3.png?X-CloudApp-Visitor-Id=1094421) |

- Create a folder called `homework-01` in the `/opt` via notepad++ interface.
- Create all your scripts in your `homework-01` folder via notepad++.
- Now log in to your server via `gitbash` and go to the `\opt` folder.
- Clone your repo.
- If you didn't create your `assignments` folder in your repo, do it now.
- Assuming you changed into your repo folder:
    - run this: `cp -r ../homework-01 ./assignments`
- If your IN your assignments folder:
    - run this: `cp -r ../../homework-01 .`
- If your in `\opt` at the same level as your repo:
    - run this `cp -r homework-01 ./your4103repo/assignments`
- Essentally all three commands are the same thing but run from different directories.
- Now push your assignments to github:
- `cd your4130repo`
- Then run:
    - `git add -A`
    - `git comit -m "adding homework 1"`
    - `git push origin master`

## Write Scripts 

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

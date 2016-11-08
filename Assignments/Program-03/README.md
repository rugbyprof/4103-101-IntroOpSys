### Program 3: Disk Simulation

#### Overview

For the first part of our virtual memory simulation we are going to create a disk simulation. Loading processes into memory requires accessing disk to retrieve pages and load them into main memory (RAM), and whatever doesn't fit into main memory, we place in virtual memory. 
 
Before we implement our two level Page Table mapping virtual addresses into physical address, I would like us to create a "physical disk" simulation. This simulation will have `Disks` with varying page sizes,  and a variable number of processes (files) stored on each disk. Of course, the files will be stored in a manner that fits with the `page size` for that particular disk. To help us find or files on `disk`, we need a structure to point us in the right direction. For this, we will use the concept of a `file allocation table`.


#### File Allocation Table

A File Allocation Table or `FAT` is a simple structure that stores the name of a process (filename), it's starting address, and it's length. For our simulation, each `Disk` will have its own `FAT` associated with it. The naming convention for FAT's will simple be:
- Fat-0
- Fat-1
- ...
- Fat-N

The format of a `FAT` is as follows:
- file name (alpha numeric)
- starting address (integer)
- length of file / process (integer)

***Example Fat:*** (start of)

~~~txt
xyxyxy.txt 0 3235
zzzzzz.dat 4096 7869
ououou.txt 8192 234456
~~~

~~~python
class File(object):
    def __init__(self,name,start,length):
        self.Name = name
        self.StartAddress = start
        self.Length = length

    
class Fat(object):
    def __init__(self,fat_name):
        self.FileList = []
        # open name
        # read in # of files
        # dynamically size the FileArray
        # load the File Array with the information from the file
            
        # GetNumberOfFiles()           # return number of files on disk.
        # GetFileNames()               # returns array of filenames.
        # GetFileByName(filename)      # returns starting address, and length of file (or just a struct File with everything is ok).
        
~~~

#### Disk

A `disk` (in our simulation) is actually a file that holds `P` number of processes (or files). Each process `p` will be of varying size, but will be stored in a page aligned manner. So, if a particular disk has a `4K` page size, then the data for each process will start on a byte that is aligned with `4K`.

For example of a process `p` is 12,324 bytes, it will consume 3 pages. 

- Page 1 (0    -> 4095)
- Page 2 (4096 -> 8191)
- Page 3 (8192 -> 12288)

Assuming process `p` starts at address `0` it will consume entirely the first 2 pages, but it still consumes the first 36 bytes of page `3` (wasting the rest of that page). 

The file name of the `Disk` will store the page size of that particular disk, along with its disk number. For example:

- Disk-4096-0     means that it has a 4K page size, and it is disk number 0.
- Disk-512-4   means that it has a 512byte page size, and it is disk number 4.
- ...
- Disk-xxx-N

The number is important, because it needs to be associated with a `File Allocation Table` with the same number. We could embed the `FAT` on the actual disk (which is how it's actually done), but this would make address translation that much harder. We'll pretend that we have some `hardware` that is joining them both together, allowing us to access individual files (processes). YOU are the hardware:)

***Example Disk:*** (start of)

~~~cpp
    class Disk :  public Fat{
    private:
        Fat *F;             //Pointer to disks file allocation table
        int PageSize;       //Integer page size of disk (in bytes)
        int DiskNumber;
        ifstream DiskIn;
    public:
        Disk(string disk_name){
            //parse disk_name to get information
            //get disk number
            //get page size
            //load (read in) disks file allocation table
        }
        //OpenFile(file_name);                //Returns the instructions from start to start+length of file_name
        //
        
    };
~~~


#### What You Need to Accomplish

I will provide an `Driver` of sorts that will act like the operating system.  Really, it will be a file that tells you how many disks you have to gain access to, and then will requests the contents of specific files by name. So YOUR job is to create objects for each disk allowing some user (me or you), to read a file by its file name. 


***Example Driver File:***

~~~cpp
4
Disk-4096-0
Disk-1024-1
Disk-512-2
Disk-2048-3
5
a.txt
b.txt
c.txt
hello.dat
what.txt
~~~

So, you know there will be 4 disks to read and 5 files to find on 1 of these disks.

For each file that you read, output its contents (stored in hex) as ascii to some output file that will contain:

~~~cpp
a.txt 
Disk: 1
Start: 23454
Length: 2345
----------------------------------------------------------------------------------------------------------------
Contents of a.txt
blah
blah
blah

.
.
.

what.txt 
Disk: 3
Start: 55345
Length: 76354
----------------------------------------------------------------------------------------------------------------
Contents of what.txt
blah
blah
blah

~~~

As a help, you can go to [AsciiTable.com](http://www.asciitable.com/). Notice that each character ranges from  0x20 to 0x7E, so our traditional grouping of 8 hexidecimal characters would result in 4 ascii characters.

Why are we outputting in ascii? This is to test your disk reading code. I will create `disks` that are page aligned according to the specs, and if you read the proper address range on the proper disk, then by outputting it in ascii you will know if you did it correctly (because of the data I will store on the disk).

Check [HERE](http://cs.mwsu.edu/~terry/courses/5133/project2_files/) for your disks, and file allocation tables (stored as files of course). 

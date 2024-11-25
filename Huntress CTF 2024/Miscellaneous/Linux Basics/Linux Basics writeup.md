# Challenge Name: Linux Basics

**Category:** Miscellaneous  
**CTF Event:** Huntress CTF 2024    
**Points:** 50 Points

## Challenge Description
This challenge presents a series of Linux-related questions where you're required to use various command-line tools to answer them. Below are the questions, the steps taken to answer each, and the correct answers.

---


## Challenge Questions


    linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ answer 

 - Question 0: What's your home directory?
 - Question 1: Search the man pages. What command would you use to generate random permutations?
 - Question 2: On what day was /home/user/myfile.txt modified? Use the date format 2019-12-31
 - Question 3: How big is /home/user/myfile.txt, in kilobytes? Round to the nearest whole number.
 - Question 4: What user owns the file /home/user/myfile.txt
 - Question 5: What's the 3-digit octal permissions of the file /home/user/myfile.txt? (e.g 777)
 - Question 6: What is the user id of 'admin'?
 - Question 7: There is a user 'john' on the system. Can they write to /home/user/myfile.txt? (yes/no)
 - Question 8: Can the 'admin' user execute /home/user/myfile.txt? (yes/no)
 - Question 9: Which user on the system, except for you, root, admin and john, can execute /home/user/myfile.txt?
 - Question 10: /home/user/myfile.txt looks like a txt file, but it actually isn't. What kind of file is it?


&nbsp;
### Question 0: What's your home directory?
---

**Solution:**  
The home directory for the user can be found using the `pwd` command, which prints the current working directory. In this case, executing the command returns `/home/user`.

**Command:**
```bash
pwd
```

**Output:**
```
/home/user
```

**Output in the CTF Terminal:-**
```
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ pwd    
pwd
/home/user
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ answer 0
answer 0
Question: What's your home directory? /home/user
/home/user
Nice Job!
```


&nbsp;
### Question 1: Search the man pages. What command would you use to generate random permutations?
---

**Solution:**    
The shuf command is used to generate random permutations. It can be confirmed by searching through the manual pages using man -k random, which will list the relevant commands for generating random permutations.


**Output:**
```
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ shuf -i 1-10
shuf -i 1-10
10
4
1
9
7
2
6
5
8
3
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ answer 1
answer 1
Question: Search the man pages. What command would you use to generate random permutations? shuf
shuf
Nice Job!
```


&nbsp;
### Question 2: On what day was /home/user/myfile.txt modified? Use the date format 2019-12-31
---

**Solution:**   
The stat command shows detailed information about the file, including modification time. The Modify field provides the exact modification date in the correct format.


**Command:**
```
stat /home/user/myfile.txt
```

**Output:**
```
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ stat /home/user/myfile.txt
stat /home/user/myfile.txt
  File: /home/user/myfile.txt
  Size: 22200     	Blocks: 48         IO Block: 4096   regular file
Device: 1000f5h/1048821d	Inode: 537854      Links: 1
Access: (0754/-rwxr-xr--)  Uid: (    0/    root)   Gid: ( 1338/   admin)
Access: 1997-08-29 02:13:00.000000000 -0700
Modify: 1997-08-29 02:13:00.000000000 -0700
Change: 2024-10-18 02:45:07.385214290 -0700

linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ answer 2
answer 2
Question: On what day was /home/user/myfile.txt modified? Use the date format 2019-12-31 1997-08-29
1997-08-29
Nice Job!
```

&nbsp;
### Question 3: How big is /home/user/myfile.txt, in kilobytes? Round to the nearest whole number.
---

**Solution:**   
The du -k command displays the size of the file in kilobytes. Alternatively, we can use stat to get the file size in bytes, then convert it to kilobytes and round

**Commands:**
```
du -k /home/user/myfile.txt
# OR
stat -c%s /home/user/myfile.txt
echo $(( $(stat -c%s /home/user/myfile.txt) / 1024 ))
```

**Output:**
```
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ echo $(( $(stat -c%s /home/user/myfile.txt) / 1024 ))
<ho $(( $(stat -c%s /home/user/myfile.txt) / 1024 ))
21

linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ answer 3
answer 3
Question: How big is /home/user/myfile.txt, in kilobytes? Round to the nearest whole number. 22
22
Nice Job!
``` 

&nbsp;
### Question 4: What user owns the file /home/user/myfile.txt
---

**Solution:**   
The ls -l or stat command can be used to view the file's ownership details. The output shows the owner of the file is root

**Command:** 
```
ls -l /home/user/myfile.txt
```

**Output:**
```
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ ls -l /home/user/myfile.txt
ls -l /home/user/myfile.txt
-rwxr-xr--    1 root     admin        22200 Aug 29  1997 /home/user/myfile.txt

linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ answer 4 
answer 4 
Question: What user owns the file /home/user/myfile.txt root
root
Nice Job!
```

&nbsp;
### Question 5: What's the 3-digit octal permissions of the file /home/user/myfile.txt? (e.g 777)

**Solution:**   
The file permissions can be found using the stat command with the %a format specifier, which outputs the octal value of the file's permissions. The result shows 0754.

**Command:**
```
stat -c "%a" /home/user/myfile.txt
```

**Output:**
```
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ stat -c "%a" /home/user/myfile.txt
<8489cc4-n9nxn:~$ stat -c "%a" /home/user/myfile.txt
754

linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ answer 5
answer 5
Question: What's the 3-digit octal permissions of the file /home/user/myfile.txt? (e.g 777) 754
754
Nice Job!
```

&nbsp;
### Question 6: What is the user id of 'admin'?

**Solution:**   
The id command can be used to retrieve the user ID of any user. Running it with admin as the argument gives the user ID 1338.

**Command:**
```
id -u admin
```

**Output:**
```
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ id -u admin
id -u admin
1338

linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ answer 6 
answer 6 
Question: What is the user id of 'admin'? 1338
1338
Nice Job!
```



&nbsp;
### Question 7: There is a user 'john' on the system. Can they write to /home/user/myfile.txt? (yes/no)
---

**Solution:**   
The ls -l command shows the permissions for /home/user/myfile.txt. The permissions rwxr-xr-- indicate that only the owner (root) has write access, while the group (admin) and others have read/execute permissions but not write access. Since john is in the admin group, he cannot write to the file.

**Command:**
```
ls -l /home/user/myfile.txt
```

**Output:**
```
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ ls -l /home/user/myfile.txt 
<6c-6f48489cc4-n9nxn:~$ ls -l /home/user/myfile.txt 
-rwxr-xr--    1 root     admin        22200 Aug 29  1997 /home/user/myfile.txt

linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ answer 7    
answer 7 
Question: There is a user 'john' on the system. Can they write to /home/user/myfile.txt? (yes/no) no
no
Nice Job!
```


&nbsp;
### Question 8: Can the 'admin' user execute /home/user/myfile.txt? (yes/no)
---

**Solution:**   
The file permissions rwxr-xr-- show that the group (which includes admin) has the execute (x) permission. Therefore, admin can execute the file.

**Command:**
```
ls -l /home/user/myfile.txt
```

**Output:**
```
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ answer 8 
answer 8 
Question: Can the 'admin' user execute /home/user/myfile.txt? (yes/no) yes
yes
Nice Job!
```

&nbsp;
### Question 9: Which user on the system, except for you, root, admin and john, can execute /home/user/myfile.txt?

**Solution:**   
Using cat /etc/passwd, we can check all the users on the system. The file permissions (rwxr-xr--) indicate that others have read and execute access. From the list of users, we can see that the user rose belongs to a group that can execute the file.


**Command:**
```
cat /etc/passwd
```

**Output:**
```
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ cat /etc/passwd
cat /etc/passwd
root:x:0:0:root:/root:/bin/sh
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
admin:x:1338:1338:Linux User,,,:/:/bin/false
user:x:1337:1338:Linux User,,,:/home/user:/bin/bash
john:x:1001:1338:Linux User,,,:/:/bin/false
dave:x:1002:1002:Linux User,,,:/:/bin/false
rose:x:1003:1338:Linux User,,,:/:/bin/false
jade:x:1004:1000:Linux User,,,:/:/bin/false


linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ answer 9 
answer 9 
Question: Which user on the system, except for you, root, admin and john, can execute /home/user/myfile.txt? rose
rose
Nice Job!
```

&nbsp;
### Question 10: /home/user/myfile.txt looks like a txt file, but it actually isn't. What kind of file is it?

**Solution:**   
The file command can be used to identify the actual type of a file. Running the command reveals that the file is actually a JPEG image.

**Command** 
```
file /home/user/myfile.txt
```

**Output:**
```
linux-basics-8d6cba8bf8b0796c-6f48489cc4-n9nxn:~$ file myfile.txt 
file myfile.txt 
myfile.txt: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 807x114, components 3

answer 10 
answer 10 
Question: /home/user/myfile.txt looks like a txt file, but it actually isn't. What kind of file is it? jpeg image data 
jpeg image data
Nice Job!
```

### Once answering all the question it reveals the flag:- 

```
Here's the flag: 8873fe66f8e7a6019d7d71261864f6c5  -
```

Thus, the flag is: 

**flag{8873fe66f8e7a6019d7d71261864f6c5}**
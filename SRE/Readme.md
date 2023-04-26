SRE INTERVIEW PREPARATION
Programming
○ Python basics (skip videos if you already know the concepts)
■ https://www.youtube.com/watch?v=mHtjvDEdlas&list=PLhqPDa2HoaAZN9pG0c
UugTmgAddRtF3zK - working on

Video 1-Done
Video 2-Working
Video 3
Video 4
Video 5
Video 6
Video 7
Video 8
Video 9
Video 10



○ Solve basic questions in Python - hackerrank easy




○ Advanced Python tutorial
■ https://www.youtube.com/watch?v=QLTdOEn79Rc&list=PLqnslRFeH2UqLwzS0
AwKDKLrpYBKzLBy2


○ Solve more advance level questions


■ hacker rank advance easy

■ hacker rank advance medium

○ Classes in Python

■ https://youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

○ DSA with Python

■ https://youtube.com/playlist?list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l

○ Take 30 day coding challenge

■ https://www.hackerrank.com/domains/tutorials/30-days-of-code

○ Solve more basic DSA questions gain more confidence

■ Leetcode basic free questions

○ After solving problems in the links given, you should be good with the basics of Python

and DSA.

○ If you want to solve more DSA problems

■ https://workat.tech/problem-solving/practice/topics
■ Start with easy problems first in the topic you select

○ Python scripting

■ https://youtube.com/playlist?list=PLckUzKjgYDgaMCzGIvdcyOlcUTx1sBBtR

(Complete till 14th video)

■ This will require basic knowledge of operating systems and networking.

■ This is helpful if you are interested in DevOps/SRE areas.

Operating system basics

● Operating system basics -

https://www.youtube.com/watch?v=0UvZ2BPIPX0&list=PLhqPDa2HoaAZLws7PFYWl4

MnzCyHf8do- (These videos should be more than enough for interviews)

● Linux kernel development by Robert Love is one of the best books to read for diving into

the internals of Linux. (optional)
● The end goal here is to understand how the operating system works.


● After going through the above video, you should be able to explain:

○ What is OS? Difference between OS and kernel

○ Intro to Linux, Linux distributions

○ System calls

○ Interrupts and signals

○ Process management

■ Program vs Process

■ Process states and PCB

■ Process scheduling and context switch

■ Process creation - fork(), exec(), wait()

■ Zombie and orphan process

■ Process vs Threads

○ Race condition, deadlock, mutex, and semaphore

○ Memory management

■ Logical address vs physical address

■ Paging

■ Virtual memory

■ TLB

○ File system management

■ Files, directories, special files, links, sockets
■ File system layout

■ Proc file system

■ VFS

■ Common file operations - read, write, append, open, close

■ Inodes

■ Volumes and partition

■ RAID

● Detailed topics list -

https://docs.google.com/document/d/1Vy2EUAgIShloS6gcSWPdVCg5vhsYWZHl686h9x

AkYOA

Linux commands

● https://www.digitalocean.com/community/tutorials/linux-commands

● The above link should be enough to cover basic Linux commands.

● Try to practice all the commands on your system. If you do not have Linux on your
system, install it by dual boot or use a virtual machine. Install red hat Linux.

● After covering the above videos and blogs, you should be comfortable with the concepts
below.

● What happens when you run a command - https://youtu.be/sL7h1rOn0K0

● Reading manual pages - man command

● File system navigation

○ cd

○ pwd

○ ls

○ less

○ more

○ file

○ tail

○ head

○ cat

● Manipulating files

○ cp

○ mv

○ rm

○ mkdir

○ touch

○ echo

● Users and groups

○ useradd

○ passwd

○ usermod

○ userdel

● Sudo user

● File permissions

○ chmod

○ chown

○ chgrp

● I/O redirection and pipes

● sort, uniq, awk, sed, grep

● ssh, scp, smtp

● Package management

● Process management commands

○ /proc/PID/

○ top

○ ps

○ Background and foreground process - fg, bg, jobs

○ Kill

● Memory management commands

○ /proc/meminfo

○ free

○ Vmstat

● File system management

○ Searching files - find
○ Disk usage - df

○ Files usage - du

● Networking commands

○ Application layer - telnet, curl, wget, ssh, sftp, scp, dig, nslookup

○ Transport layer - nc, tcpdump, netstat(ss)

○ Network layer - ping, traceroute, route, ip addr, iptables, nmap

○ Data link layer - arp

● Managing system services - systemd

● Detailed list of topics -
https://docs.google.com/document/d/1BCJ3iRYAif4MGxEn9j5N6dyu8-0YGA5xgHq-ldnV

3po/

Computer networking

○ Computer networking basics -

https://www.youtube.com/playlist?list=PLhqPDa2HoaAYYXjiIdRsf5-tKmJUlZx4o

○ Computer networking animation videos -

https://www.youtube.com/playlist?list=PLhqPDa2HoaAYXaCph61kioSbJS7lwcwUt

○ Focus on understanding the following:
■ Layers in TCP/IP model

■ Functions of each layer

■ How these layers help in moving data from one machine to another

■ Application layer protocols like HTTP, DNS, SSH, HTTPS, TLS, etc

■ Transport layer protocols like TCP and UDP

● Difference between TCP and UDP

● TCP 3-way handshake

● TCP connection termination

■ Network layer - subnet, CIDR, and IP addresses

■ Other networking protocols like ICMP, DHCP, ARP, etc are important

■ After reading the above, you should be able to answer what happens when you
type www.google.com on your browser and hit enter? -

https://jvns.ca/networking-zine.pdf

■ Networking commands like telnet, curl, dig, ping, traceroute, netcat etc

● Detailed list of topics -

https://docs.google.com/document/d/1S84HYWNL52ZUdcoweOWiBBcJcWlxc7RTrzK03

SVKqVg

System design

● System design basics by Gaurav Sen(must watch) -

https://www.youtube.com/watch?v=xpDnVSmNFX0&list=PLMCXHnjXnTnvo6alSjVkgxVVH6EPyvoX

● System design primer(examples + concepts) -

https://github.com/donnemartin/system-design-primer

● Go through both the links above

● Designing a distributed system - https://youtu.be/ohtqI3AHR0k

● Focus on understanding the following:

○ How do big companies design their infrastructure?

○ Important concepts:

■ Load balancer

■ Vertical vs horizontal scaling

■ Reverse proxy

■ CDN

■ What is reliability?

■ CAP theorem

■ Caching

■ Database

● sql vs nosql databases

● ACID properties

● Database sharding

● Database replication

■ Full list -

https://github.com/donnemartin/system-design-primer#system-design-topi

cs-start-here

System troubleshooting

● Debugging performance issues on a single server

○ https://syedali.net/2013/08/20/linux-troubleshooting-tools/

○ https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-acc

c10403c55

● How to troubleshoot issues in production

○ https://sre.google/sre-book/effective-troubleshooting/ [must read]

● Read Julia Evans zines/blogs on debugging [must read]

○ https://jvns.ca/debugging-zine.pdf

○ https://jvns.ca/perf-zine-print.pdf

○ https://jvns.ca/tcpdump-zine.pdf

○ https://jvns.ca/debugging-zine.pdf

○ https://jvns.ca/strace-zine-v3-print.pdf

○ https://jvns.ca/blog/2014/04/20/debug-your-programs-like-theyre-closed-source/

○ https://jvns.ca/blog/2021/04/03/what-problems-do-people-solve-with-strace/

Tools

● DevOps interview preparation course from kodekloud(paid course) -

https://kodekloud.com/courses/devops-interview-prep-course/

● The above course covers:

○ Github

○ AWS

○ Docker
○ Terraform

○ Jenkins

○ Kubernetes

○ Monitoring

SRE interview questions and experiences

● https://github.com/mxssl/sre-interview-prep-guide

● https://github.com/michaelkkehoe/sre-interview

● https://amiralisobhgol.medium.com/i-received-sre-offers-from-facebook-and-google-with

out-a-university-degree-here-is-how-224f06b49e7d

● Go through all the blogs here -

https://github.com/mxssl/sre-interview-prep-guide#blogposts

● https://danrl.com/srm/#screen

● Hiring SRE at dropbox - https://youtu.be/ucCSRY-KOCI
● Hiring SRE at LinkedIn - https://youtu.be/ZemNg9GYvOA




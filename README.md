#To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

##The virtual machine

This project makes use of the Linux-based virtual machine (VM).
you'll use a virtual machine (VM) to run an SQL database server and a web app that uses it. The VM is a Linux server
system that runs on top of your own computer. You can share files easily between your computer and the VM; and you'll be
running a web service inside the VM which you'll be able to access from your regular browser.


###tools called Vagrant and VirtualBox to install and manage the VM. You'll need to install these


Install VirtualBox-----> https://www.virtualbox.org/wiki/Downloads

 Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need
 to launch VirtualBox after installing it; Vagrant will do that.



Install Vagrant-----> https://www.vagrantup.com/downloads.html
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's
filesystem.

if successfully installed you will be able to run vagrant --version



## Running the `newsdata.py`

1. download the logs-analysis-project.zip

2. open git terminal, if you don't have it install it.

3. Change to the logs-analysis-project directory in your terminal with cd. Inside, you will find another directory
called vagrant. Change directory to the vagrant directory:


##Start the virtual machine

1. From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the
Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet
connection is.

2.  When vagrant up is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log
in to your newly installed Linux VM!

3.  To access your shared files type: `cd /vagrant`

4.  `ls` to see list of files

5.  `cd` into newsdata dir

#### Load the data into the database:
1. Load the data using the following command: ``` psql -d news -f newsdata.sql ```

6.  to run the newsdata.py:

7.  type: /usr/bin/python newsdb.py or python newsdb.py

#####if your python file path is different run `whereis python` to get the path of python.

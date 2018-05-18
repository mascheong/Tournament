# Project Title

The Tournament Planner project contains an SQL file that sets up the tables for a tournament database and a Python file that contains administrative
functions for the database. There is also another Python test suite file
that was originally provided by Udacity. An optional Vagrantfile to ensure
users have the same environment as the developer.

## Getting Started

Download the zip file which contains all the Python files and SQL file.
Install Vagrant and VirtualBox.

Vagrant - https://www.vagrantup.com/
VirtualBox - https://www.virtualbox.org/wiki/Downloads

### Prerequisites

Have Python 2.7 installed.
Have Vagrant installed.
Have VirtualBox installed.

### Installing

Unzip files into the Vagrant directory.
Open a command window and navigate to your Vagrant folder.
Type in `vagrant up` in the window to initialize the virtual machine.
Type in `vagrant ssh` to SSH into the virtual machine.
Type in `psql`
Run the SQL file by typing in `\i tournament.sql`
In a separate command window, SSH into Vagrant again.
There you can run `python tournament_test.py` to confirm the functions
  are working as intended.

## Built With

Python 2.7
Atom
Git
Vagrant
VirtualBox

## Authors

* **Mason Cheong

## Acknowledgments

Thanks to Udacity for providing the test suite and the VagrantFile

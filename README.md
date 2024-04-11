# sync-tool-for-Remarkable-2

## Overview
A utility to sync your reMarkable 2 tablet's system time with your computer. Perfect for keeping accurate timestamps on notes and sketches.

## Installation
Clone and set up with:

```bash
git clone https://github.com/qingdd33/sync-tool-for-Remarkable-2.git
cd sync-tool-for-Remarkable-2
pip install paramiko
```
## Usage
Adjust the script with your reMarkable's IP and root password. Then, run it using:

```bash
python sync_time.py
```
##To adjust the script for someone with no prior knowledge, follow these simple steps:
1.Find the Script File: Locate the sync_time.py file you saved on your computer.
2.Open the File: Right-click the file and open it with a text editor (like Notepad or TextEdit).
3.Identify the Lines to Edit: Look for lines that say something like remarkable_ip = '...' and root_password = '...'.
4.Edit IP and Password: Replace the placeholder values within the quotes ('...') with your reMarkable's actual IP address and root password.
5.Save Changes: After editing, save the file and close the text editor.
6.Run the Script: Open a terminal or command prompt, navigate to the folder containing the script, and type python sync_time.py then press Enter.

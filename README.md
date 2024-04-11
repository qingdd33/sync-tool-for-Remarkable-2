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
## Adjusting the Script: A Step-by-Step Guide

For those new to working with scripts, follow these steps to adjust your `sync_time.py` for the reMarkable tablet:

1. **Find the Script File**
   - Locate `sync_time.py` on your computer.

2. **Open the File**
   - Right-click on `sync_time.py` and open it with a text editor like Notepad or TextEdit.

3. **Locate Lines to Edit**
   - Search for lines containing `remarkable_ip = '...'` and `root_password = '...'`.

4. **Enter Your Details**
   - Replace `'...'` with your reMarkable's IP address and root password. Keep the details within the quotes.

5. **Save Changes**
   - Save the file and close the text editor.

6. **Run the Script**
   - Open a command prompt or terminal, navigate to the script's folder, and type `python sync_time.py`, then press Enter.


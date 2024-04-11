import paramiko
from datetime import datetime

# Your reMarkable's IP and root password
remarkable_ip = '10.11.99.1'
root_password = 'your_root_password'

# Establish an SSH client and connect to reMarkable
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(remarkable_ip, username='root', password=root_password)

# Get current system time in the format required by `date` command
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Command to update reMarkable's date and time
command = f"date -s '{current_time}'"
stdin, stdout, stderr = ssh.exec_command(command)

# Check for errors
if stderr.read():
    print("Error in setting time")
else:
    print("Time synchronized successfully")

# Close the connection
ssh.close()

# Atria-CityPulse-Bhuvan

This repository documents basic Linux command-line tasks. Each task explains the commands and includes a screenshot of the output from my terminal.

## Contents

- [Task 1: Remove Directories](#task-1-remove-directories)
- [Task 2: Remove Files and Directories Recursively](#task-2-remove-files-and-directories-recursively)
- [Task 3: Rename Files and Check Disk Usage](#task-3-rename-files-and-check-disk-usage)
- [Task 4: Linux Permissions](#task-4-linux-permissions)
- [Task 5: List Running Processes](#task-5-list-running-processes)
- [Extra: Current User](#extra-current-user)
- [Extra: WSL Check](#extra-wsl-check)

---

## Task 1: Remove Directories

Use `mkdir` to create a directory and `rmdir` to remove an empty directory.

```bash
mkdir temp-dir
rmdir temp-dir
```

`rmdir` only works when the directory is empty. Use `rm -r` or `rm -rf` to remove directories that contain files or subdirectories.

**Output:**

![Creating and removing a directory](screenshots/task1-rmdir.png)

---

## Task 2: Remove Files and Directories Recursively

Use `rm` to remove a file and `rm -r` or `rm -rf` to remove a directory and everything inside it.

```bash
# Remove a file
rm filename.txt

# Remove a directory and its contents interactively
rm -r folder-name

# Remove a directory and its contents without prompting
rm -rf folder-name
```

> **Warning:** `rm -rf` permanently deletes data. Double-check the path before running it.

**Output:**

![Removing files and directories](screenshots/task2-rm.png)

---

## Task 3: Rename Files and Check Disk Usage

### Rename a File or Directory

The `mv` command renames a file or directory:

```bash
mv old-name.txt new-name.txt
mv old-folder-name new-folder-name
```

To move and rename a file at the same time:

```bash
mv filename.txt folder/filename.txt
```

**Output:**

![Renaming and moving files](screenshots/task3-mv.png)

### Check Disk Usage

Use `df -h` to see the disk space available on mounted filesystems:

```bash
df -h
```

**Output:**

![df -h output](screenshots/task3-df.png)

Use `du -h` to show the size of files and directories:

```bash
# Show the size of the current directory
du -h

# Show only the size summary of the current directory
du -sh

# Show the size of a specific folder
du -sh folder-name
```

**Output:**

![du -sh output](screenshots/task3-du.png)

---

## Task 4: Linux Permissions

Linux files and directories have three permission types:

| Permission | Symbol | Meaning |
| --- | --- | --- |
| Read | `r` | View file contents or list directory contents |
| Write | `w` | Modify a file or change directory contents |
| Execute | `x` | Run a file as a program or enter a directory |

Permissions are assigned to:

- The file owner
- The owner's group
- Other users

Use `chmod` to change permissions:

```bash
# Add execute permission for the owner
chmod u+x script.sh

# Give the owner read and write permissions
chmod u+rw file.txt

# Make a file readable and writable by everyone
chmod 666 file.txt

# Give the owner full permissions and others read/execute permissions
chmod 755 script.sh
```

View permissions with:

```bash
ls -l
```

Example permission modes:

- `644`: owner can read/write; group and others can read
- `755`: owner can read/write/execute; group and others can read/execute
- `777`: all users have read, write, and execute permissions

---

## Task 5: List Running Processes

Use `ps` to view processes for the current terminal:

```bash
ps
```

Use `ps aux` to list processes from the entire system:

```bash
ps aux
```

**Output:**

![ps aux output](screenshots/task5-ps-aux.png)

To search for a specific process:

```bash
ps aux | grep process-name
```

An alternative, interactive process viewer is:

```bash
top
```

Press `q` to exit `top`.

**Output:**

![ps aux with grep, then top](screenshots/task5-grep-top.png)

---

## Extra: Current User

Several ways to check which user you are logged in as:

```bash
whoami
id -un
echo $USER
```

**Output:**

![Checking the current user](screenshots/extra-whoami.png)

> `echo %USERNAME%` is Windows syntax and does not work in zsh/bash.

---

## Extra: WSL Check

```bash
wsl --list
```

WSL (Windows Subsystem for Linux) is Windows-only, so on macOS the command is not found.

**Output:**

![WSL command check](screenshots/wsl-check.png)

---

## Screenshot Summary

| Screenshot | Description |
| --- | --- |
| `screenshots/task1-rmdir.png` | Creating and removing a directory |
| `screenshots/task2-rm.png` | Removing files and directories with `rm` and `rm -r` |
| `screenshots/task3-mv.png` | Renaming and moving files with `mv` |
| `screenshots/task3-df.png` | Disk space with `df -h` |
| `screenshots/task3-du.png` | Folder size with `du -sh` |
| `screenshots/task5-ps-aux.png` | Listing all processes with `ps aux` |
| `screenshots/task5-grep-top.png` | Filtering with `grep`, then `top` |
| `screenshots/extra-whoami.png` | Checking the current user |
| `screenshots/wsl-check.png` | Checking whether WSL is available |

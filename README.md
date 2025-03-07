<p align="center">
  <a href="https://www.python.org/" target="blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="200" alt="Python Logo" />
  </a>
</p>

[ci-image]: https://img.shields.io/github/actions/workflow/status/python/cpython/ci.yml?branch=main
[ci-url]: https://github.com/python/cpython/actions

<p align="center">A powerful and versatile <a href="https://www.python.org/" target="_blank">Python</a> framework for building high-performance and reliable server-side applications.</p>

<p align="center">
  <a href="https://pypi.org/project/" target="_blank">
    <img src="https://img.shields.io/pypi/v/django.svg" alt="PyPI Version" />
  </a>
  <a href="https://docs.python.org/3/" target="_blank">
    <img src="https://img.shields.io/badge/docs-latest-blue.svg" alt="Documentation" />
  </a>
  <a href="https://github.com/python/cpython" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/python/cpython/ci.yml?branch=main" alt="CI Status" />
  </a>
  <!-- <a href="https://codecov.io/gh/python/cpython" target="_blank">
    <img src="https://codecov.io/gh/python/cpython/branch/main/graph/badge.svg" alt="Coverage" />
  </a> -->
  <a href="https://discord.gg/python" target="_blank">
    <img src="https://img.shields.io/discord/267624335836053506.svg" alt="Discord">
  </a>
  <a href="https://github.com/sponsors/python" target="_blank">
    <img src="https://img.shields.io/badge/Support%20us-GitHub%20Sponsors-41B883.svg" alt="Support us">
  </a>
  <a href="https://twitter.com/ThePSF" target="_blank">
    <img src="https://img.shields.io/twitter/follow/ThePSF.svg?style=social&label=Follow">
  </a>
</p>

# FileSyncProject

FileSyncNet is a program for **synchronizing and uploading files** between devices in a network in real-time. It enables users to **share, update, and copy files** to a designated destination automatically over the network. The program supports both **one-to-one file synchronization** and **distribution to multiple devices**, similar to uploading files to **Google Drive** or other **cloud storage services**.

## Google Docs

[FileSyncNet in Google Docs](https://docs.google.com/document/d/152E3qQqoM92rUX3k7c2qDRV0P4AzSXz-MSYV1LqXpHw/edit?tab=t.0)

## Google Docs

[FileSync in Google Docs](https://docs.google.com/document/d/152E3qQqoM92rUX3k7c2qDRV0P4AzSXz-MSYV1LqXpHw/edit?usp=sharing)

## Requirements
- [Python](https://www.python.org/downloads/) **(Optional: version 3.11)**
- [Python in Microsoft Store](https://apps.microsoft.com/detail/9NRWMJP3717K?hl=en-us&gl=KR&ocid=pdpshare)

## Download & Run

[FileSyncProject.zip](https://github.com/TonRattakan/FileSyncProject/archive/refs/heads/python.zip)

1. Extract `FileSyncProject.zip`.
2. Navigate to the `FileSyncProject folder` and double-click **run.bat**.

## Manual Download & Run
```bash
git clone https://github.com/TonRattakan/FileSyncProject.git
cd FileSyncProject
python client.py
python server.py
```

## Pre-buit Download
Navigate to the [Releases](https://github.com/TonRattakan/FileSyncProject/releases)
page and download the latest release for test FileSyncNet.<br>
Launch: `server`, `client`

(Optional)
[Gofile](https://gofile.io/d/hajAOQ)

## Output
The following message should appear:

**Client:** <br>
**[Client] -> Sending: SYNC_REQUEST test.txt 4** <br>
**[Client] <- Received: SYNC_ACK 200 OK** <br>
**Sent 4/4 bytes...** <br>
**[Client] <- Received: TRANSFER_COMPLETE 201 Created**<br>
**[Client] -> File 'test.txt' successfully synced with server**<br>
**[Client] -> File 'test.txt' successfully copied to destination_folder**<br>

**Server:** <br>
**Server started on 127.0.0.1:65432**<br>
**Connected by ('127.0.0.1', 52705)**<br>
**Received message from client: SYNC_REQUEST test.txt 4**<br>
**Preparing to receive file: test.txt (4 bytes)**<br>
**[Server] -> SYNC_ACK 200 OK**<br>
**Receiving test.txt... 4/4 bytes**<br>
**[Server] -> Debug: Expected 4, Received 4, Actual File Size 4**<br>
**[Server] -> TRANSFER_COMPLETE 201 Created**<br>
**File 'test.txt' received successfully! (4 bytes)**<br>
**Connection with ('127.0.0.1', 52705) closed**<br>

![filesync](filesync.png)

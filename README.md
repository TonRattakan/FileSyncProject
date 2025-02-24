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

Test FileSyncNet

## Requirements
- [Python](https://www.python.org/downloads/) **(version 3.11)**

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

## Output
The following message should appear:

**Connected by ('127.0.0.1', 61207)**  
**Received message from client: SYNC_REQUEST texttest.txt 4**  
**Preparing to receive file: texttest.txt (4 bytes)**  
**Receiving texttest.txt... 4/4 bytes**  
**File 'texttest.txt' (4 bytes) synced successfully!**  
**Connection with ('127.0.0.1', 61207) closed**  
**--------------------------------------------------------------------------------**  

![filesync](filesync.png)

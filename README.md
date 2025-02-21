<p align="center">
  <a href="https://www.rust-lang.org/" target="blank"><img src="https://www.rust-lang.org/static/images/rust-logo-blk.svg" width="200" alt="Rust Logo" /></a>
</p>

[ci-image]: https://img.shields.io/github/actions/workflow/status/rust-lang/rust/ci.yml?branch=master
[ci-url]: https://github.com/rust-lang/rust/actions

<p align="center">A robust and modern <a href="https://www.rust-lang.org/" target="_blank">Rust</a> framework for building high-performance and reliable server-side applications.</p>
<p align="center">
<a href="https://crates.io/crates" target="_blank"><img src="https://img.shields.io/crates/v/tokio.svg" alt="Crate Version" /></a>
<a href="https://doc.rust-lang.org/" target="_blank"><img src="https://img.shields.io/badge/docs-latest-blue.svg" alt="Documentation" /></a>
<a href="https://github.com/rust-lang/rust" target="_blank"><img src="https://img.shields.io/github/workflow/status/rust-lang/rust/ci/master.svg" alt="CI Status" /></a>
<!-- <a href="https://codecov.io/gh/rust-lang/rust" target="_blank"><img src="https://codecov.io/gh/rust-lang/rust/branch/master/graph/badge.svg" alt="Coverage" /></a> -->
<a href="https://discord.gg/rust-lang" target="_blank"><img src="https://img.shields.io/discord/442252698964721669.svg" alt="Discord"></a>
<a href="https://github.com/sponsors/rust-lang" target="_blank"><img src="https://img.shields.io/badge/Support%20us-GitHub%20Sponsors-41B883.svg" alt="Support us"></a>
<a href="https://twitter.com/rustlang" target="_blank"><img src="https://img.shields.io/twitter/follow/rustlang.svg?style=social&label=Follow"></a>
</p>

# FileSyncProject

Test FileSync

## Requirements
- [Rust](https://www.rust-lang.org/tools/install)
- [NodeJS](https://nodejs.org/en) **(Optional)**

## Download & Run

[FileSyncProject.zip](https://github.com/TonRattakan/FileSyncProject/archive/refs/heads/main.zip)

1. Extract `FileSyncProject.zip`.
2. Navigate to the `FileSyncProject folder` and double-click **run.bat**.

## Manual Download & Run
```bash
git clone https://github.com/TonRattakan/FileSyncProject.git
cd FileSyncProject
cargo run --bin filesync_server
cargo run --bin filesync_client
```
## Output
The following message should appear:

**"Received: Object {"command": String("UPLOAD_FILE"), "filename": String("test.txt"), "filesize": Number(762528)}**

**📄 Receiving file: test.txt (762528 bytes)"**

![filesync](filesync.png)

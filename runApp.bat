@REM @echo off

@REM start cmd /k cargo run --bin filesync_client

@REM start cmd /k cargo run --bin filesync_server

cd /d "%~dp0"

:: Start Server First
pushd "server"
start cmd /k "cargo run --bin filesync_server"
popd

:: Start Tauri Client
pushd "client/src-tauri"
start cmd /k "cargo tauri dev"
popd

exit /b 0

@echo off
REM PQC Quickstart Tutor Launcher
REM Usage: pqc-tutor          (interactive)
REM        pqc-tutor "query"   (one-shot question)
REM Place this directory in PATH or create a desktop shortcut.

cd /d D:\PQC_Agent\PQC_Agent

if "%~1"=="" (
    echo Starting PQC Quickstart Tutor...
    echo Type your PQC question, or /help for options.
    echo.
    claude
) else (
    claude -p "%~1"
)

# PQC Quickstart Tutor — Install Script

@echo off
setlocal enabledelayedexpansion

echo ============================================
echo   PQC Quickstart Tutor - Installer
echo   Post-Quantum Cryptography Teaching Agent
echo ============================================
echo.

set "AGENT_DIR=%~dp0"
set "AGENT_DIR=%AGENT_DIR:~0,-1%"

echo Agent location: %AGENT_DIR%
echo.

:: Step 1: Verify agent files exist
if not exist "%AGENT_DIR%\CLAUDE.md" (
    echo [FAIL] CLAUDE.md not found. Is this the right directory?
    pause
    exit /b 1
)
echo [OK] Agent core files found.

:: Step 2: Check Claude Code availability
where claude >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARN] Claude Code CLI not found in PATH.
    echo        The agent works with any AGENTS.md-compatible AI tool.
    echo        See PLATFORMS.md for supported platforms.
) else (
    echo [OK] Claude Code CLI found.
)

:: Step 3: Offer setup options
echo.
echo Choose setup option:
echo   1. Add launcher to PATH (recommended)
echo   2. Create Desktop shortcut
echo   3. Just show me how to use it
echo   4. Exit
echo.
set /p choice="Enter choice [1-4]: "

if "%choice%"=="1" goto :add_path
if "%choice%"=="2" goto :desktop_shortcut
if "%choice%"=="3" goto :show_usage
if "%choice%"=="4" goto :end
goto :end

:add_path
echo.
echo To add the agent to your PATH, run this in an ADMIN terminal:
echo   setx PATH "%%PATH%%;%AGENT_DIR%"
echo.
echo After that, type 'pqc-tutor' from anywhere to start.
goto :show_usage

:desktop_shortcut
echo.
echo Desktop shortcut can be created manually:
echo   1. Right-click Desktop ^> New ^> Shortcut
echo   2. Location: %AGENT_DIR%\pqc-tutor.bat
echo   3. Name: PQC Tutor
goto :show_usage

:show_usage
echo.
echo ============================================
echo   HOW TO USE PQC QUICKSTART TUTOR
echo ============================================
echo.
echo [Method 1] Open in Claude Code (best experience):
echo   cd "%AGENT_DIR%"
echo   claude
echo   Then just ask: "Explain ML-KEM"
echo.
echo [Method 2] Use the launcher from anywhere:
echo   "%AGENT_DIR%\pqc-tutor.bat"
echo.
echo [Method 3] One-shot question:
echo   "%AGENT_DIR%\pqc-tutor.bat" "Compare ML-KEM and HQC"
echo.
echo [Method 4] Use /pqc slash command (inside Claude Code):
echo   /pqc
echo.
echo [Method 5] Open in any AI tool:
echo   Cursor:      Open "%AGENT_DIR%" folder
echo   Windsurf:    Open "%AGENT_DIR%" folder
echo   Copilot:     Open "%AGENT_DIR%" in VS Code
echo   Codex:       codex "%AGENT_DIR%"
echo.
echo The agent auto-activates when you open this directory.
echo Just ask PQC questions naturally.
echo.
echo Full platform guide: PLATFORMS.md
echo ============================================

:end
echo.
echo Setup complete!
pause

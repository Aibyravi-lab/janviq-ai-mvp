# Issues Log

## Issue #001

Date: 2026-06-09

Problem:
pip.exe blocked by Device Guard policy

Root Cause:
Direct pip executable was blocked

Resolution:
Used python -m pip command instead of pip

Status:
Resolved

---

## Issue #002

Problem:
PowerShell activation blocked

Root Cause:
Execution policy restriction

Resolution:
Used activate.bat in CMD

Status:
Resolved

---

## Issue #003

Problem:
ModuleNotFoundError: openai

Root Cause:
Package was not available inside active environment

Resolution:
Installed openai package correctly

Status:
Resolved

---

## Issue #004

Problem:
Git command not recognized

Root Cause:
VS Code did not refresh PATH

Resolution:
Restarted VS Code

Status:
Resolved

---

## Issue #005

Problem:
Git push rejected

Root Cause:
Remote repository already had commits

Resolution:
Used git pull --allow-unrelated-histories

Status:
Resolved

---

## Issue #006

Problem:
.gitignore merge conflict

Root Cause:
Local and remote gitignore mismatch

Resolution:
Resolved conflict and committed changes

Status:
Resolved

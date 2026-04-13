---
id: TASK-5
title: Bouw inspectiescript voor project-auto-detectie
status: To Do
assignee: []
created_date: '2026-04-13 17:31'
labels:
  - code
  - fase3
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Script dat een projectdirectory scant en structured output levert: package manager, runtimes, env vars (uit code/README), scripts, git-state, directory tree, services. Taal: Python of Bash, geen exotische deps.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 scripts/inspect.py of .sh bestaat en draait op 3 testfixtures
- [ ] #2 Output is JSON of gestructureerde markdown
- [ ] #3 Respecteert .gitignore en secrets blocklist
- [ ] #4 Exit code nonzero bij onverwachte fouten
<!-- AC:END -->

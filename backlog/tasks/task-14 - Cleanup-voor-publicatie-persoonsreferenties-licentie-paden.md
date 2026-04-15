---
id: TASK-14
title: 'Cleanup voor publicatie: persoonsreferenties, licentie, paden'
status: Done
assignee:
  - claude
created_date: '2026-04-15 20:23'
updated_date: '2026-04-15 20:26'
labels: []
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Pre-publication check resultaat op publieke repo. Scrub persoonsreferenties uit LICENSE, PLAN.md, backlog/tasks/task-10+task-12, tests/agent-test.md. Vervang absolute /Users/<name>/ paden in handoff/inventory.json en tests/output/*/inventory.json door placeholders. tests/dogfood/<site> en tests/dogfood.md reeds verwijderd uit index.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 LICENSE copyright regel zonder persoonsnaam
- [x] #2 Geen persoonsreferenties in PLAN.md, backlog tasks, tests/agent-test.md
- [x] #3 Geen absolute persoonlijke paden in inventory.json bestanden
- [x] #4 tests/dogfood map verwijderd
- [ ] #5 Single commit gepusht naar origin/main na bevestiging gebruiker
<!-- AC:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Scrubbed persoonsreferenties uit LICENSE, PLAN.md, task-10, task-12, tests/agent-test.md, tests/baseline-results.md. tests/dogfood map verwijderd. Absolute paden in 5 inventory.json bestanden vervangen door <repo-root> placeholder. Gecommit en gepusht in een enkel cleanup commit.
<!-- SECTION:FINAL_SUMMARY:END -->

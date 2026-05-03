---
title: "Charmbracelet"
aliases: [Charm, charmbracelet]
tags: [org, golang, tui, cli, open-source]
sources: [Charm.md]
status: ingested
fidelity_score: 5
date_created: 2026-04-05
date_updated: 2026-04-05
---

# Charmbracelet

Charmbracelet is an open-source organization building terminal user interface tools and libraries in Go. The org maintains 54+ repositories focused on making CLI and TUI development elegant.

## Flagship Projects

| Project | Description | Stars | Category |
|---------|-------------|-------|----------|
| [[Bubble Tea]] | TUI framework | 41.2k | Framework |
| [[Glow]] | Markdown renderer for CLI | 24.2k | Tool |
| [[Gum]] | Shell script utilities | 23.2k | Tool |
| [[Crush]] | Agentic coding tool | 22.5k | Tool |
| [[VHS]] | CLI screen recorder | 19.3k | Tool |
| [[Lip Gloss]] | Terminal layout styling | 11k | Library |
| [[Bubbles]] | TUI components for Bubble Tea | 8.1k | Library |
| [[Soft Serve]] | Self-hosted Git server | 6.8k | Infrastructure |
| [[Wish]] | SSH app framework | 5.1k | Framework |
| [[Catwalk]] | LLM inference provider collection | 656 | AI |

## Ecosystem Architecture

The stack layers upward: [[Lip Gloss]] handles styling, [[Bubbles]] provides reusable components, and [[Bubble Tea]] orchestrates full TUI applications. [[Gum]] exposes these capabilities to shell scripts. [[Wish]] extends the model over SSH. [[Crush]] and [[Catwalk]] represent the org's expansion into AI tooling.

## Distribution

Packages are distributed via Homebrew (`homebrew-tap`), Scoop (`scoop-bucket`), WinGet (`winget-pkgs`), and Nix (`nur`).

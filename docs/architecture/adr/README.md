# Architecture Decision Records (ADRs)

## Purpose
Architecture Decision Records (ADRs) document significant architectural decisions made during the development of a project. Each ADR captures the context, decision, consequences, and rationale for important technical choices that shape the system's architecture.

## Structure
- Each ADR is a standalone markdown file in this directory.
- ADRs are numbered sequentially with 4 digits (adr-0001, adr-0002, etc.).
- Each ADR follows a consistent template format.
- ADRs are immutable once accepted - new decisions create new ADRs.

## Usage
- Use the ADR template to document new architectural decisions.
- Reference ADRs in code comments, documentation, and discussions.
- Review ADRs when considering architectural changes.
- Update ADRs only to add new decisions, never to modify existing ones.

## ADR Status
- **Proposed**: Under consideration
- **Accepted**: Decision made and implemented
- **Deprecated**: Superseded by newer decision
- **Superseded**: Replaced by another ADR

## Current ADRs

- [ADR-0001: Adopt AgenticOps Value Train™ Methodology](adr-0001-adopt-agenticops-value-train.md) - **Accepted**
- [ADR-0002: Implement Autonomous Agent Workflow Orchestration (Auto-Pilot)](adr-0002-implement-autonomous-agent-orchestration.md) - **Proposed**
- [ADR-0003: Implement Git Hooks for Quality Gate Enforcement](adr-0003-implement-git-hooks-quality-gates.md) - **Proposed**
- [ADR-0004: Adopt Session-Based Context Management with YAML Front-matter](adr-0004-adopt-session-based-context-management.md) - **Accepted**
- [ADR-0005: Standardize Build Automation with Makefile](adr-0005-standardize-build-automation-with-makefile.md) - **Proposed**
- [ADR-0006: Migrate from Centralized to Distributed Session Context Management](adr-0006-migrate-to-distributed-session-contexts.md) - **Proposed**
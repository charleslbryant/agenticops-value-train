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

### Foundation & Methodology
- [ADR-0001: Adopt AgenticOps Value Train™ Methodology](adr-0001-adopt-agenticops-value-train.md) - **Accepted**
- [ADR-0007: Migrate from Python to C# for Value Train Implementation](adr-0007-migrate-from-python-to-csharp.md) - **Proposed**
- [ADR-0008: Adopt Microsoft Semantic Kernel for Agent Orchestration](adr-0008-adopt-semantic-kernel-agent-orchestration.md) - **Proposed**

### Infrastructure & Automation
- [ADR-0002: Implement Autonomous Agent Workflow Orchestration (Auto-Pilot)](adr-0002-implement-autonomous-agent-orchestration.md) - **Proposed**
- [ADR-0003: Implement Git Hooks for Quality Gate Enforcement](adr-0003-implement-git-hooks-quality-gates.md) - **Proposed**
- [ADR-0005: Standardize Build Automation with Makefile](adr-0005-standardize-build-automation-with-makefile.md) - **Proposed**
- [ADR-0009: Observability and Monitoring Strategy](adr-0009-observability-and-monitoring-strategy.md) - **Proposed**

### Context & Communication
- [ADR-0004: Adopt Session-Based Context Management with YAML Front-matter](adr-0004-adopt-session-based-context-management.md) - **Accepted**
- [ADR-0006: Migrate from Centralized to Distributed Session Context Management](adr-0006-migrate-to-distributed-session-contexts.md) - **Proposed**
- [ADR-0011: Agent Communication Using Semantic Kernel Handoff Patterns](adr-0011-agent-communication-via-semantic-kernel.md) - **Proposed**
- [ADR-0012: Context and Memory Management Strategy](adr-0012-context-and-memory-management.md) - **Proposed**
- [ADR-0013: Reasoning and Planning Strategy for Agent Decision-Making](adr-0013-reasoning-and-planning-strategy.md) - **Proposed**

### Tool Integration
- [ADR-0010: Integrate Tools and Skills via Model Context Protocol (MCP)](adr-0010-integrate-tools-via-mcp.md) - **Proposed**
- [ADR-0014: File and Code Management Integration Strategy](adr-0014-file-and-code-management-integration.md) - **Proposed**
- [ADR-0015: Web Search Integration via MCP](adr-0015-web-search-integration.md) - **Proposed**
- [ADR-0016: Secure Command-Line Tool Integration](adr-0016-secure-command-line-tool.md) - **Proposed**
- [ADR-0017: Document Generation Capabilities](adr-0017-document-generation-capabilities.md) - **Proposed**
- [ADR-0018: API Integration Strategy](adr-0018-api-integration-strategy.md) - **Proposed**
- [ADR-0019: Error Handling and Retry Strategy for Agent Operations](adr-0019-error-handling-and-retry-strategy.md) - **Proposed**
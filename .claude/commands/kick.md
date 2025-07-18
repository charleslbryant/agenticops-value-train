---
description: Switch to Project Kickoff Mode for customizing CMDS templates
allowed-tools: Read, Write, MultiEdit, TodoWrite, Grep, Glob, LS
---

# Kick Mode

Always start your chats with `🤖 [Kick Mode]`

Your initial response is a status update where you run commands and summarize the results:

```
🤖 [Kick Mode]

## Template Status
**Product Templates:**
!`ls -la /docs/product/`

**Architecture Templates:**
!`ls -la /docs/architecture/`

**Template Files Needing Customization:**
!`grep -r "TEMPLATE FILE" /docs/product/ /docs/architecture/ | head -10`

## Git Repository Status
**Git Repository:**
!`# Git repository detection and analysis
if git rev-parse --git-dir >/dev/null 2>&1 && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    # Determine repository type
    if git rev-parse --is-bare-repository >/dev/null 2>&1 && [ "$(git rev-parse --is-bare-repository)" = "true" ]; then
        repo_type="Bare"
    else
        repo_type="Normal"
    fi
    
    # Check repository state (clean vs dirty)
    if git status --porcelain 2>/dev/null | grep -q .; then
        repo_state="Dirty"
    else
        repo_state="Clean"
    fi
    
    # Check repository health
    if git fsck --unreachable >/dev/null 2>&1; then
        repo_health="Healthy"
    else
        repo_health="Issues Detected"
    fi
    
    # Output status
    echo "- Status: Found"
    echo "- Type: $repo_type"
    echo "- State: $repo_state"
    echo "- Health: $repo_health"
else
    # No valid git repository found
    echo "- Status: Not Found"
    echo "- Type: N/A"
    echo "- State: N/A"
    echo "- Health: N/A"
fi`
```

## Workflow

You are now in **Project Kickoff Mode**. You are an expert at project setup and template customization. Focus on helping the operator customize CMDS templates for their specific project. Follow the checklist exactly and do not exit this mode until all required tasks are complete or the operator instructs you to change modes.

### Mode Context Files

Before starting the checklist, reread all mode context files. This ensures clean memory boundaries between modes.

**Rule Files:**

* `/docs/rules/session-workflow.md`
* `/docs/rules/documentation-rules.md`
* `/docs/rules/git-workflow.md`

**Template Files:**

* `/docs/product/`
* `/docs/architecture/`

### Checklist (TodoWrite)

You will create a TodoWrite checklist with the items below, share it with the operator, and complete all required items (*) before exiting this mode.

0. **Read Mode Context Files***: Read all rule and session context files
1. **Inventory Templates***: List all template files that need customization
2. **Review Product Vision Template***: Read and understand current product vision template
3. **Customize Product Vision***: Work with operator to create project-specific product vision
4. **Review Product Strategy Template***: Read and understand current product strategy template
5. **Customize Product Strategy***: Work with operator to create project-specific product strategy
6. **Review Architecture Template***: Read and understand current architecture template
7. **Customize Architecture***: Work with operator to create project-specific architecture documentation
8. **Review ADR Template***: Ensure ADR template matches project needs
9. **Create Initial ADRs***: If needed, create foundational architecture decisions
10. **Validate Customizations***: Review all customized templates with operator
11. **Update Session Context***: Update context files to reflect project setup
12. **Remove Template Warnings***: Remove "TEMPLATE FILE" warnings from customized files
13. **Ready for Development***: Verify project is ready for `/begin` mode

### Customization Approach

For each template file:

1. **Read Current Template**: Understand structure and placeholder content
2. **Gather Project Information**: Ask operator about their project specifics
3. **Create Customized Version**: Replace template content with project-specific information
4. **Review with Operator**: Ensure customization meets their needs
5. **Finalize and Save**: Write the customized version

### Questions to Ask Operator

**For Product Vision:**
- What problem does your project solve?
- Who is your target audience?
- What is your unique value proposition?
- What are your success metrics?

**For Product Strategy:**
- What is your go-to-market approach?
- What are your key milestones?
- What are your competitive advantages?
- What are your resource constraints?

**For Architecture:**
- What is your technology stack?
- What are your key components?
- What are your scalability requirements?
- What are your security requirements?
- What are your deployment constraints?

### Mode Rules

* **Collaborative Approach**: Work with operator, don't assume
* **Project-Specific**: All customizations must be specific to their project
* **Complete Templates**: Don't leave placeholder content
* **Validate Understanding**: Confirm details before writing
* **Document Decisions**: Capture rationale for customizations

### Template Customization Priority

1. **High Priority** (Required for development):
   - Product vision
   - Architecture overview
   - Key technology decisions

2. **Medium Priority** (Helpful for context):
   - Product strategy
   - Detailed architecture
   - Initial ADRs

3. **Low Priority** (Can be done later):
   - Detailed product requirements
   - Comprehensive ADR set

### Mode Exit Requirement

Before exiting this mode:

* All template warnings removed from customized files
* Operator approval on all customizations
* Write session state to `/docs/session-context/ACTIVE_SESSION.md` with customization summary
* Update `/CURRENT_STATE.md` with project setup completion
* Wait for operator to `/clear` context before switching modes

### Available Transitions

* `/begin` - Start development with customized project context
* `/plan` - Begin planning work with proper project context

---

*Project Kickoff Mode Active - Customize templates for your specific project*
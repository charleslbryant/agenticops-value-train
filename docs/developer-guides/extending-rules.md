# Extending the Rules System - Developer Guide

This guide explains how to extend and modify the Value Train rules system. It covers adding new rules, creating mode-specific logic, and integrating rules with CLI commands.

## Rules System Architecture

### Three-Layer Architecture

The rules system follows a three-layer approach for comprehensive enforcement:

```
┌─────────────────────────────────────────┐
│           Layer 1: Documentation       │
│         (Human Reference)               │
│  /docs/rules/*.md - Comprehensive      │
│  rule documentation with examples      │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│         Layer 2: Command Integration   │
│            (LLM Guidance)              │
│  Slash commands reference rules and    │
│  guide LLM behavior                    │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│         Layer 3: CLI Enforcement       │
│        (Deterministic Logic)           │
│  C# CLI commands implement critical    │
│  business logic with type safety       │
└─────────────────────────────────────────┘
```

### Rule Categories

#### Universal Rules
Rules that apply across all modes and contexts:
- **Location**: `/docs/rules/[rule-name].md`
- **Examples**: `session-workflow.md`, `task-management.md`, `git-workflow.md`
- **Scope**: Fundamental operations like session management, Git workflow

#### Mode-Specific Rules  
Rules that apply to specific Value Train modes:
- **Location**: `/docs/rules/checklists/[mode]-checklist.md`
- **Examples**: `intake-checklist.md`, `discover-checklist.md`
- **Scope**: Mode entry/exit criteria, required activities, deliverables

#### Context-Specific Rules
Rules that adapt based on work context (business, ML engineering, software engineering):
- **Location**: `/docs/rules/contexts/[context]-context.md` (future)
- **Examples**: Template selection, success criteria, tool restrictions
- **Scope**: Context-appropriate behaviors and requirements

## Adding New Rules

### 1. Create Rule Documentation

#### Universal Rules
```markdown
# [Rule Name] Rules

## Purpose
[Clear explanation of why this rule exists]

## Scope
[When and where this rule applies]

## Requirements
### Mandatory Requirements
- [Specific, testable requirement]
- [Specific, testable requirement]

### Optional Guidelines
- [Helpful guidance that improves outcomes]

## Validation
[How compliance with this rule can be verified]

## Examples
### Good Example
[Concrete example of following the rule correctly]

### Bad Example  
[Example of what NOT to do]

## Related Rules
- [Links to related rules]

## TodoWrite Integration
[TodoWrite checklist items for this rule]
- [ ] [Specific action item]
- [ ] [Specific action item]
```

#### Mode-Specific Rules (Checklists)
```markdown
# [Mode] Mode Checklist

## Mode Configuration
- **Mode**: [mode-name]
- **Description**: [Brief purpose statement]
- **Primary Agent**: [responsible-agent]
- **Allowed Tools**: [List of permitted tools]

## Entry Criteria
- [ ] [Prerequisite that must be met to enter this mode]

## Core Activities Checklist
### [Activity Category]
- [ ] [Specific, measurable activity]
- [ ] [Specific, measurable activity]

## Deliverables
- [ ] [Required output artifact]
- [ ] [Required output artifact]

## Exit Criteria
- [ ] [Requirement that must be met to leave this mode]

## Quality Gates
- [ ] [Quality standard that must be met]

## Transition Rules
- **[Next Mode]**: [Conditions for this transition]
- **[Alternative Mode]**: [Conditions for alternative path]

## Common Pitfalls
- [Things to avoid in this mode]

## Mode-Specific Tools
- [Tools and resources specific to this mode]
```

### 2. Integrate with Commands

#### Slash Command Integration
Update the relevant slash command to reference the new rule:

```markdown
### Mode Context Files

Before starting the checklist, reread all mode context files. This ensures clean memory boundaries between modes.

**Rule Files:**
* `/docs/rules/session-workflow.md`
* `/docs/rules/task-management.md`
* `/docs/rules/[your-new-rule].md`  # Add your rule here
```

#### CLI Command Integration
Create or update CLI command to enforce the rule:

```csharp
// ValueTrain.Application/Features/RuleValidation/ValidateNewRule/
public class ValidateNewRuleQuery : IRequest<ValidateNewRuleResponse>
{
    public string Context { get; set; }
    public string Mode { get; set; }
}

public class ValidateNewRuleQueryHandler : IRequestHandler<ValidateNewRuleQuery, ValidateNewRuleResponse>
{
    public async Task<ValidateNewRuleResponse> Handle(ValidateNewRuleQuery request, CancellationToken cancellationToken)
    {
        // Implement deterministic rule validation logic
        var violations = new List<string>();
        
        // Check rule compliance
        if (!IsRuleCompliant(request))
        {
            violations.Add("Specific violation description");
        }
        
        return new ValidateNewRuleResponse
        {
            IsValid = violations.Count == 0,
            Violations = violations
        };
    }
}
```

### 3. Add Validation Logic

#### Documentation Validation
Ensure rule documentation follows standards:

```bash
# Check rule documentation completeness
agenticops rules validate-docs --rule [rule-name]

# Validate rule file format
agenticops rules check-format --file /docs/rules/[rule-name].md
```

#### Runtime Validation
Implement runtime checks for rule compliance:

```csharp
public interface IRuleValidator
{
    Task<RuleValidationResult> ValidateAsync(string ruleName, object context);
}

public class RuleValidationResult
{
    public bool IsValid { get; set; }
    public List<string> Violations { get; set; }
    public List<string> Warnings { get; set; }
}
```

## Creating Mode-Specific Logic

### 1. Define Mode Requirements

#### Mode Configuration
```yaml
# Add to pipeline.yml or mode configuration
modes:
  - name: "new-mode"
    description: "Description of what this mode does"
    primary_agent: "responsible-agent"
    allowed_tools:
      - "Read"
      - "Write"
      - "TodoWrite"
    entry_criteria:
      - "Previous mode completed successfully"
    exit_criteria:
      - "All checklist items completed"
    next_modes:
      - "follow-up-mode"
```

#### Checklist Creation
Create comprehensive checklist following the template above, including:
- **Entry Criteria**: What must be true to start this mode
- **Core Activities**: Specific actions required in this mode
- **Deliverables**: Required outputs and artifacts
- **Exit Criteria**: What must be true to complete this mode
- **Quality Gates**: Standards that must be met

### 2. Implement Mode Command

#### Slash Command Structure
```markdown
---
description: Brief description of what this mode does
allowed-tools: Read, Write, TodoWrite, Bash(git:*), Bash(gh:*)
---

# [Mode] Mode - [Agent] Agent

Always start your chats with `🤖 [[Mode] Mode - [Agent] Agent]`

## Current Status
[Status update commands and context loading]

## Workflow
[Detailed explanation of mode purpose and workflow]

### Mode Context Files
[List of rule files that apply to this mode]

### [Mode] Checklist (TodoWrite)
[Comprehensive checklist with all required activities]

### Mode Rules
[Mode-specific rules and constraints]

### Mode Exit Requirement
[Clear criteria for completing this mode]

### Available Transitions
[Allowed next modes and conditions]
```

#### CLI Command Implementation
```csharp
// ValueTrain.Presentation.Cli/Commands/NewModeCommand.cs
[Description("Execute [new-mode] mode")]
public class NewModeCommand : AsyncCommand<NewModeCommand.Settings>
{
    public class Settings : CommandSettings
    {
        [Description("Specific mode parameter")]
        [CommandOption("--parameter")]
        public string Parameter { get; set; }
    }

    public override async Task<int> ExecuteAsync(CommandContext context, Settings settings)
    {
        // ASCII Art Display
        _console.Write(new FigletText("NEW MODE").Color(Color.Blue));
        
        // Execute mode logic via MediatR
        var command = new ExecuteNewModeCommand { Parameter = settings.Parameter };
        var result = await _mediator.Send(command);
        
        return result.IsSuccess ? 0 : 1;
    }
}
```

### 3. Context-Specific Adaptations

#### Context Detection Logic
```csharp
public class ContextDetectionService : IContextDetectionService
{
    public async Task<WorkContext> DetectContextAsync(int? issueId, string[] labels)
    {
        // Implement context detection logic
        if (labels.Contains("ml") || labels.Contains("data-science"))
            return WorkContext.MLEngineering;
            
        if (labels.Contains("business") || labels.Contains("strategy"))
            return WorkContext.Business;
            
        return WorkContext.SoftwareEngineering; // Default
    }
}
```

#### Context-Aware Rule Application
```csharp
public class ContextAwareRuleProcessor
{
    public async Task<List<string>> GetApplicableRulesAsync(string mode, WorkContext context)
    {
        var rules = new List<string>();
        
        // Universal rules (always apply)
        rules.AddRange(await GetUniversalRulesAsync());
        
        // Mode-specific rules
        rules.AddRange(await GetModeRulesAsync(mode));
        
        // Context-specific rules
        rules.AddRange(await GetContextRulesAsync(context));
        
        return rules;
    }
}
```

## CLI Integration Best Practices

### 1. Command Design Patterns

#### Command Structure
```csharp
// Follow established patterns for consistency
public class RuleCommand : AsyncCommand<RuleCommand.Settings>
{
    private readonly IMediator _mediator;
    private readonly IAnsiConsole _console;
    private readonly ILogger<RuleCommand> _logger;

    // Constructor with DI
    // Settings class with validation attributes
    // Execute method with error handling
    // ASCII art for visual feedback
}
```

#### Error Handling
```csharp
public override async Task<int> ExecuteAsync(CommandContext context, Settings settings)
{
    try
    {
        // Display command start
        _console.Write(new FigletText("RULE CMD").Color(Color.Green));
        
        // Execute with comprehensive logging
        _logger.LogInformation("Starting rule command with {Settings}", settings);
        
        var result = await _mediator.Send(command);
        
        if (result.IsSuccess)
        {
            _console.MarkupLine("[green]✅ Rule validation successful[/]");
            return 0;
        }
        else
        {
            _console.MarkupLine("[red]❌ Rule validation failed:[/]");
            foreach (var error in result.Errors)
            {
                _console.MarkupLine($"[red]  • {error}[/]");
            }
            return 1;
        }
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "Rule command failed");
        _console.MarkupLine($"[red]Error: {ex.Message}[/]");
        return 1;
    }
}
```

### 2. Validation Integration

#### Pre-Command Validation
```csharp
public class RuleValidationBehavior<TRequest, TResponse> : IPipelineBehavior<TRequest, TResponse>
{
    public async Task<TResponse> Handle(TRequest request, RequestHandlerDelegate<TResponse> next, CancellationToken cancellationToken)
    {
        // Validate applicable rules before command execution
        var violations = await ValidateRulesAsync(request);
        
        if (violations.Any())
        {
            throw new RuleViolationException(violations);
        }
        
        return await next();
    }
}
```

#### Post-Command Validation
```csharp
public class PostCommandRuleValidator
{
    public async Task ValidateAfterCommandAsync(string commandName, object result)
    {
        // Ensure command execution didn't violate any rules
        var applicableRules = await GetPostCommandRulesAsync(commandName);
        
        foreach (var rule in applicableRules)
        {
            await ValidateRuleAsync(rule, result);
        }
    }
}
```

## Testing Rules

### 1. Rule Documentation Tests

```csharp
[Test]
public async Task RuleDocumentation_ShouldHaveRequiredSections()
{
    var ruleFiles = Directory.GetFiles("docs/rules", "*.md");
    
    foreach (var file in ruleFiles)
    {
        var content = await File.ReadAllTextAsync(file);
        
        // Verify required sections exist
        Assert.That(content, Contains.Substring("## Purpose"));
        Assert.That(content, Contains.Substring("## Requirements"));
        Assert.That(content, Contains.Substring("## TodoWrite Integration"));
    }
}
```

### 2. Rule Validation Tests

```csharp
[Test]
public async Task RuleValidator_ShouldDetectViolations()
{
    var validator = new SessionWorkflowRuleValidator();
    var context = new InvalidSessionContext(); // Missing required fields
    
    var result = await validator.ValidateAsync(context);
    
    Assert.That(result.IsValid, Is.False);
    Assert.That(result.Violations, Is.Not.Empty);
}
```

### 3. Integration Tests

```csharp
[Test]
public async Task ModeCommand_ShouldEnforceRules()
{
    var command = new IntakeCommand();
    var settings = new IntakeCommand.Settings { /* invalid settings */ };
    
    var result = await command.ExecuteAsync(context, settings);
    
    Assert.That(result, Is.EqualTo(1)); // Should fail due to rule violation
}
```

## Common Patterns

### 1. Rule Composition
```csharp
public class CompositeRuleValidator : IRuleValidator
{
    private readonly List<IRuleValidator> _validators;
    
    public async Task<RuleValidationResult> ValidateAsync(object context)
    {
        var allViolations = new List<string>();
        
        foreach (var validator in _validators)
        {
            var result = await validator.ValidateAsync(context);
            allViolations.AddRange(result.Violations);
        }
        
        return new RuleValidationResult
        {
            IsValid = allViolations.Count == 0,
            Violations = allViolations
        };
    }
}
```

### 2. Rule Caching
```csharp
public class CachedRuleProvider : IRuleProvider
{
    private readonly IMemoryCache _cache;
    
    public async Task<List<Rule>> GetRulesAsync(string context)
    {
        return await _cache.GetOrCreateAsync($"rules:{context}", async entry =>
        {
            entry.SlidingExpiration = TimeSpan.FromMinutes(30);
            return await LoadRulesFromFileSystemAsync(context);
        });
    }
}
```

### 3. Rule Evolution
```csharp
public class RuleVersionManager
{
    public async Task<Rule> GetRuleVersionAsync(string ruleName, Version version)
    {
        // Support versioned rules for backward compatibility
        var ruleFile = $"docs/rules/versions/{version}/{ruleName}.md";
        return await LoadRuleFromFileAsync(ruleFile);
    }
}
```

## Troubleshooting

### Common Issues

1. **Rule Not Being Enforced**
   - Check if rule is referenced in relevant commands
   - Verify CLI command implements validation logic
   - Ensure rule file follows correct format

2. **Rule Validation Too Strict**
   - Review rule requirements for necessary flexibility
   - Consider context-specific adaptations
   - Add override mechanisms for special cases

3. **Performance Issues**
   - Implement rule caching for frequently accessed rules
   - Optimize validation logic for common cases
   - Consider async validation for expensive checks

### Debugging Tips

```csharp
// Enable detailed rule validation logging
builder.Services.Configure<RuleValidationOptions>(options =>
{
    options.EnableDetailedLogging = true;
    options.LogRuleEvaluations = true;
});

// Use validation commands for testing
agenticops rules validate --verbose --rule [rule-name]
agenticops rules debug --context [context] --mode [mode]
```

## Contributing to Rules

### 1. Rule Proposal Process
1. **Identify Need** - Document why new rule is needed
2. **Draft Rule** - Create comprehensive rule documentation
3. **Review Process** - Get feedback from team members
4. **Implementation** - Add CLI validation and command integration
5. **Testing** - Comprehensive testing of rule enforcement
6. **Documentation** - Update guides and examples

### 2. Rule Evolution
- Rules can be updated based on lessons learned
- Backward compatibility should be maintained when possible
- Breaking changes require team consensus and migration plan

### 3. Best Practices
- Keep rules simple and testable
- Provide clear examples and rationale
- Consider edge cases and exceptions
- Document rule interactions and dependencies

The rules system is designed to grow and evolve with the Value Train. By following these patterns and practices, you can extend the system while maintaining consistency and quality across all operations.
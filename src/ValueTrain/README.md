# Value Train - C# Implementation

A simple, lightweight C# implementation of the Value Train workflow system.

## Build and Run

```bash
# Build
dotnet build

# Run
dotnet run

# Or build and run
dotnet run --project src/ValueTrain/ValueTrain.csproj
```

## Usage

1. Start the program and enter your task name
2. Use mode commands to progress through your workflow:
   - `plan` - Define business requirements
   - `research` - Investigate technical approach
   - `design` - Create UX, UI, technical specs, and go-to-market
   - `build` - Write code
   - `validate` - Test (unit, integration, e2e)
   - `review` - Code review, PR review, demos, and merge
   - `deliver` - Deploy to production
   - `operate` - Monitor and maintain
   - `evaluate` - Assess delivery meets requirements
   - `improve` - Optimize and enhance

3. Use `/status` to see your progress
4. Use `/todo` to manage your checklist
5. Use `/next` to advance to the next mode

## Example Session

```
🚂 Welcome to Value Train - Simple Software Development Workflow

What are you building? Add dark mode to app

[None] > /plan
🚂 Switched to Plan mode

📋 Plan Mode Checklist:
  ⬜ Define business requirements
  ⬜ Identify stakeholders  
  ⬜ Document success criteria
  ⬜ Create GitHub issues

[Plan] > /todo
Todo Management:
  1. Add todo
  2. Start todo
  3. Complete todo
  4. Show todos
Choice: 3
1. Define business requirements
2. Identify stakeholders
3. Document success criteria
4. Create GitHub issues
Select todo (1-4): 1
✅ Todo completed

[Plan] > /next
🚂 Switched to Research mode
```

## Features

- **Simple mode progression** - Linear workflow through 10 modes
- **Automatic checklists** - Each mode generates relevant todos
- **Progress tracking** - See completed modes and pending tasks
- **Lightweight** - No external dependencies, just .NET

## Extending

The `ValueTrainSession` class can be easily extended:

```csharp
// Add custom modes
public enum CustomMode 
{
    Research,
    Prototype,
    // etc
}

// Track additional metadata
public class ExtendedSession : ValueTrainSession
{
    public string GitBranch { get; set; }
    public List<string> CommitHashes { get; set; }
    // etc
}
```

## Philosophy

- **Structure prevents chaos** - Follow the modes
- **Small steps** - Complete one mode at a time
- **Document everything** - Track decisions in todos
- **Ship frequently** - Don't get stuck in any mode too long
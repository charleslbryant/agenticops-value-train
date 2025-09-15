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
   - `/intake` - Gather requirements
   - `/discover` - Research unknowns  
   - `/scope` - Estimate effort
   - `/design` - Plan architecture
   - `/build` - Write code
   - `/evaluate` - Test
   - `/deliver` - Deploy
   - `/operate` - Monitor
   - `/improve` - Optimize

3. Use `/status` to see your progress
4. Use `/todo` to manage your checklist
5. Use `/next` to advance to the next mode

## Example Session

```
🚂 Welcome to Value Train - Simple Software Development Workflow

What are you building? Add dark mode to app

[None] > /intake
🚂 Switched to Intake mode

📋 Intake Mode Checklist:
  ⬜ Define the problem to solve
  ⬜ Identify stakeholders  
  ⬜ Document success criteria
  ⬜ Capture constraints and assumptions

[Intake] > /todo
Todo Management:
  1. Add todo
  2. Start todo
  3. Complete todo
  4. Show todos
Choice: 3
1. Define the problem to solve
2. Identify stakeholders
3. Document success criteria
4. Capture constraints and assumptions
Select todo (1-4): 1
✅ Todo completed

[Intake] > /next
🚂 Switched to Discover mode
```

## Features

- **Simple mode progression** - Linear workflow through 9 modes
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
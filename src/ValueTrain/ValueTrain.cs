using System;
using System.Collections.Generic;
using System.Linq;

namespace ValueTrain
{
    public enum Mode
    {
        None,
        Intake,     // What needs to be built?
        Discover,   // What don't we know?
        Scope,      // What's in/out? Constraints?
        Design,     // Requirements & specifications
        Build,      // Write the code
        Evaluate,   // Does it work?
        Deliver,    // Ship it
        Operate,    // Keep it running
        Improve     // Make it better
    }

    public class Todo
    {
        public string Id { get; set; } = Guid.NewGuid().ToString();
        public string Content { get; set; } = "";
        public TodoStatus Status { get; set; } = TodoStatus.Pending;
        public DateTime CreatedAt { get; set; } = DateTime.Now;
        public DateTime? CompletedAt { get; set; }
    }

    public enum TodoStatus
    {
        Pending,
        InProgress,
        Completed
    }

    public class ValueTrainSession
    {
        public Mode CurrentMode { get; private set; } = Mode.None;
        public List<Todo> Todos { get; } = new List<Todo>();
        public Dictionary<Mode, DateTime> ModeHistory { get; } = new Dictionary<Mode, DateTime>();
        public string TaskName { get; set; } = "";
        
        public void SwitchMode(Mode newMode)
        {
            if (newMode == Mode.None)
                throw new ArgumentException("Cannot switch to None mode");
            
            CurrentMode = newMode;
            ModeHistory[newMode] = DateTime.Now;
            
            Console.WriteLine($"🚂 Switched to {newMode} mode");
            GenerateModeChecklist(newMode);
        }
        
        public void AddTodo(string content)
        {
            Todos.Add(new Todo { Content = content });
        }
        
        public void StartTodo(string todoId)
        {
            var todo = Todos.FirstOrDefault(t => t.Id == todoId);
            if (todo != null)
                todo.Status = TodoStatus.InProgress;
        }
        
        public void CompleteTodo(string todoId)
        {
            var todo = Todos.FirstOrDefault(t => t.Id == todoId);
            if (todo != null)
            {
                todo.Status = TodoStatus.Completed;
                todo.CompletedAt = DateTime.Now;
            }
        }
        
        public void ShowStatus()
        {
            Console.WriteLine($"\n📋 Task: {TaskName}");
            Console.WriteLine($"📍 Current Mode: {CurrentMode}");
            Console.WriteLine($"\n✅ Completed Modes:");
            foreach (var mode in ModeHistory.OrderBy(m => m.Value))
            {
                Console.WriteLine($"  - {mode.Key} ({mode.Value:g})");
            }
            
            Console.WriteLine($"\n📝 Todos:");
            foreach (var todo in Todos)
            {
                var icon = todo.Status switch
                {
                    TodoStatus.Completed => "✅",
                    TodoStatus.InProgress => "🚧",
                    _ => "⬜"
                };
                Console.WriteLine($"  {icon} {todo.Content}");
            }
        }
        
        private void GenerateModeChecklist(Mode mode)
        {
            var checklists = new Dictionary<Mode, string[]>
            {
                [Mode.Intake] = new[]
                {
                    "Define the problem to solve",
                    "Identify stakeholders",
                    "Document success criteria",
                    "Capture constraints and assumptions"
                },
                [Mode.Discover] = new[]
                {
                    "Research existing solutions",
                    "Identify technical unknowns",
                    "Spike on new technologies if needed",
                    "Document findings and options"
                },
                [Mode.Scope] = new[]
                {
                    "Define what's in scope",
                    "Define what's out of scope", 
                    "Identify constraints (time/budget/tech)",
                    "Decide what to defer"
                },
                [Mode.Design] = new[]
                {
                    "Document functional requirements",
                    "Define non-functional requirements",
                    "Create technical specifications",
                    "Define acceptance criteria"
                },
                [Mode.Build] = new[]
                {
                    "Write unit tests",
                    "Implement functionality",
                    "Write documentation",
                    "Commit code frequently"
                },
                [Mode.Evaluate] = new[]
                {
                    "Run unit tests",
                    "Perform integration testing",
                    "Code review",
                    "Verify requirements are met"
                },
                [Mode.Deliver] = new[]
                {
                    "Create pull request",
                    "Deploy to staging",
                    "Get approvals",
                    "Deploy to production"
                },
                [Mode.Operate] = new[]
                {
                    "Monitor application health",
                    "Check error logs",
                    "Review performance metrics",
                    "Respond to alerts"
                },
                [Mode.Improve] = new[]
                {
                    "Analyze usage patterns",
                    "Identify bottlenecks",
                    "Plan optimizations",
                    "Create improvement backlog"
                }
            };
            
            if (checklists.ContainsKey(mode))
            {
                Console.WriteLine($"\n📋 {mode} Mode Checklist:");
                foreach (var item in checklists[mode])
                {
                    AddTodo(item);
                    Console.WriteLine($"  ⬜ {item}");
                }
            }
        }
        
        public bool IsModeComplete(Mode mode)
        {
            // Check if all todos for this mode are completed
            // In a real implementation, you'd track which todos belong to which mode
            return Todos.Where(t => t.Status != TodoStatus.Completed).Count() == 0;
        }
        
        public Mode GetNextMode()
        {
            return CurrentMode switch
            {
                Mode.Intake => Mode.Discover,
                Mode.Discover => Mode.Scope,
                Mode.Scope => Mode.Design,
                Mode.Design => Mode.Build,
                Mode.Build => Mode.Evaluate,
                Mode.Evaluate => Mode.Deliver,
                Mode.Deliver => Mode.Operate,
                Mode.Operate => Mode.Improve,
                Mode.Improve => Mode.None,
                _ => Mode.Intake
            };
        }
    }
}
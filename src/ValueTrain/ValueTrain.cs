using System;
using System.Collections.Generic;
using System.Linq;

namespace ValueTrain
{
    public enum Mode
    {
        None,
        Plan,       // Define business requirements
        Research,   // Investigate technical approach
        Design,     // Create UX, UI, technical specs, and go-to-market
        Build,      // Write the code
        Validate,   // Test (unit, integration, e2e)
        Review,     // Code review, PR review, demos, and merge
        Deliver,    // Deploy to production
        Operate,    // Monitor and maintain
        Evaluate,   // Assess delivery meets requirements
        Improve     // Optimize and enhance
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
        public string IssueNumber { get; set; } = "";
        public string Branch { get; set; } = "";
        
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
            if (!string.IsNullOrEmpty(IssueNumber))
                Console.WriteLine($"🔗 Issue: #{IssueNumber}");
            if (!string.IsNullOrEmpty(Branch))
                Console.WriteLine($"🌿 Branch: {Branch}");
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
                [Mode.Plan] = new[]
                {
                    "Define business requirements",
                    "Identify stakeholders",
                    "Document success criteria",
                    "Create GitHub issues"
                },
                [Mode.Research] = new[]
                {
                    "Investigate technical approaches",
                    "Identify unknowns and risks",
                    "Research libraries and tools",
                    "Document findings in issue"
                },
                [Mode.Design] = new[]
                {
                    "Create UX wireframes and flows",
                    "Design UI components and mockups",
                    "Create technical specifications",
                    "Define go-to-market strategy"
                },
                [Mode.Build] = new[]
                {
                    "Implement functionality",
                    "Follow coding standards",
                    "Write documentation",
                    "Commit code frequently"
                },
                [Mode.Validate] = new[]
                {
                    "Write unit tests",
                    "Run integration tests",
                    "Execute end-to-end tests",
                    "Fix identified issues"
                },
                [Mode.Review] = new[]
                {
                    "Create pull request",
                    "Complete code review",
                    "Demo to stakeholders",
                    "Merge approved changes"
                },
                [Mode.Deliver] = new[]
                {
                    "Prepare deployment artifacts",
                    "Deploy to staging",
                    "Get final approvals",
                    "Deploy to production"
                },
                [Mode.Operate] = new[]
                {
                    "Monitor application health",
                    "Check error logs",
                    "Review performance metrics",
                    "Respond to alerts"
                },
                [Mode.Evaluate] = new[]
                {
                    "Compare outcomes to requirements",
                    "Measure success criteria",
                    "Gather user feedback",
                    "Document lessons learned"
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
                Mode.Plan => Mode.Research,
                Mode.Research => Mode.Design,
                Mode.Design => Mode.Build,
                Mode.Build => Mode.Validate,
                Mode.Validate => Mode.Review,
                Mode.Review => Mode.Deliver,
                Mode.Deliver => Mode.Operate,
                Mode.Operate => Mode.Evaluate,
                Mode.Evaluate => Mode.Improve,
                Mode.Improve => Mode.None,
                _ => Mode.Plan
            };
        }
    }
}
using System;
using System.Linq;

namespace ValueTrain
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("🚂 Welcome to Value Train - Simple Software Development Workflow\n");
            
            var session = new ValueTrainSession();
            
            Console.Write("What are you building? ");
            session.TaskName = Console.ReadLine() ?? "Unnamed Task";
            
            Console.WriteLine("\nCommands:");
            Console.WriteLine("  /intake    - Start gathering requirements");
            Console.WriteLine("  /discover  - Research and learn");
            Console.WriteLine("  /scope     - Define priorities");
            Console.WriteLine("  /design    - Plan architecture");
            Console.WriteLine("  /build     - Write code");
            Console.WriteLine("  /evaluate  - Test it");
            Console.WriteLine("  /deliver   - Ship it");
            Console.WriteLine("  /operate   - Monitor it");
            Console.WriteLine("  /improve   - Make it better");
            Console.WriteLine("  /status    - Show current status");
            Console.WriteLine("  /todo      - Manage todos");
            Console.WriteLine("  /next      - Move to next mode");
            Console.WriteLine("  /exit      - Exit\n");
            
            while (true)
            {
                Console.Write($"[{session.CurrentMode}] > ");
                var input = Console.ReadLine()?.Trim().ToLower() ?? "";
                
                if (input == "/exit" || input == "exit")
                    break;
                
                switch (input)
                {
                    case "/intake":
                        session.SwitchMode(Mode.Intake);
                        break;
                    case "/discover":
                        session.SwitchMode(Mode.Discover);
                        break;
                    case "/scope":
                        session.SwitchMode(Mode.Scope);
                        break;
                    case "/design":
                        session.SwitchMode(Mode.Design);
                        break;
                    case "/build":
                        session.SwitchMode(Mode.Build);
                        break;
                    case "/evaluate":
                        session.SwitchMode(Mode.Evaluate);
                        break;
                    case "/deliver":
                        session.SwitchMode(Mode.Deliver);
                        break;
                    case "/operate":
                        session.SwitchMode(Mode.Operate);
                        break;
                    case "/improve":
                        session.SwitchMode(Mode.Improve);
                        break;
                    case "/status":
                        session.ShowStatus();
                        break;
                    case "/next":
                        var nextMode = session.GetNextMode();
                        if (nextMode != Mode.None)
                        {
                            session.SwitchMode(nextMode);
                        }
                        else
                        {
                            Console.WriteLine("✅ All modes complete!");
                        }
                        break;
                    case "/todo":
                        ManageTodos(session);
                        break;
                    default:
                        if (!string.IsNullOrEmpty(input))
                            Console.WriteLine("Unknown command. Type a mode command or /status");
                        break;
                }
            }
            
            Console.WriteLine("\n👋 Goodbye! Keep shipping great software!");
        }
        
        static void ManageTodos(ValueTrainSession session)
        {
            Console.WriteLine("\nTodo Management:");
            Console.WriteLine("  1. Add todo");
            Console.WriteLine("  2. Start todo");
            Console.WriteLine("  3. Complete todo");
            Console.WriteLine("  4. Show todos");
            Console.Write("Choice: ");
            
            var choice = Console.ReadLine();
            
            switch (choice)
            {
                case "1":
                    Console.Write("Todo content: ");
                    var content = Console.ReadLine();
                    if (!string.IsNullOrWhiteSpace(content))
                    {
                        session.AddTodo(content);
                        Console.WriteLine("✅ Todo added");
                    }
                    break;
                    
                case "2":
                case "3":
                    var todos = session.Todos.Where(t => t.Status != TodoStatus.Completed).ToList();
                    if (todos.Count == 0)
                    {
                        Console.WriteLine("No pending todos");
                        break;
                    }
                    
                    for (int i = 0; i < todos.Count; i++)
                    {
                        Console.WriteLine($"{i + 1}. {todos[i].Content}");
                    }
                    
                    Console.Write($"Select todo (1-{todos.Count}): ");
                    if (int.TryParse(Console.ReadLine(), out int index) && index > 0 && index <= todos.Count)
                    {
                        if (choice == "2")
                        {
                            session.StartTodo(todos[index - 1].Id);
                            Console.WriteLine("🚧 Todo started");
                        }
                        else
                        {
                            session.CompleteTodo(todos[index - 1].Id);
                            Console.WriteLine("✅ Todo completed");
                        }
                    }
                    break;
                    
                case "4":
                    foreach (var todo in session.Todos)
                    {
                        var icon = todo.Status switch
                        {
                            TodoStatus.Completed => "✅",
                            TodoStatus.InProgress => "🚧",
                            _ => "⬜"
                        };
                        Console.WriteLine($"{icon} {todo.Content}");
                    }
                    break;
            }
        }
    }
}
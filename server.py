from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ToDo")

items = []


@mcp.resource("todo://list")
def list_todo():
    """
    List all TODO items.
    """
    return items


@mcp.resource("todo://view/{item_idx}")
def view_todo(item_idx: int):
    """
    View a TODO item.
    """

    if item_idx < 0 or item_idx >= len(items):
        return "Item not found"
    return items[item_idx]

@mcp.prompt("create_task")
def create_task(task_name: str, priority: str = "medium", due_date: str = ""):
    """
    Create a structured todo task with metadata.
    
    Args:
        task_name: The name/description of the task
        priority: Task priority (low, medium, high)
        due_date: When the task is due (optional)
    """
    formatted_task = f"[{priority.upper()}]"
    
    if due_date:
        formatted_task += f" Due: {due_date} - "
    else:
        formatted_task += " - "
        
    formatted_task += task_name
    
    return {
        "content": f"I'd like to add a new todo item with the following details:\n\nTask: {task_name}\nPriority: {priority}\nDue date: {due_date or 'None'}\n\nFormatted as: {formatted_task}",
        "task_string": formatted_task
    }

@mcp.tool()
def add_todo(value: str):
    """
    Add a TODO item.
    """

    items.append(value)
    return f"Added TODO item: '{value}' at index '{len(items) - 1}'"


@mcp.tool()
def remove_todo(item_idx: int):
    """
    Remove a TODO item.
    """

    if item_idx < 0 or item_idx >= len(items):
        return "Item not found"
    removed_item = items.pop(item_idx)

    return f"Removed TODO item: '{removed_item}' from index '{item_idx}'"


@mcp.tool()
def clear_todo():
    """
    Clear all TODO items.
    """

    items.clear()
    return "Cleared all TODO items"


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
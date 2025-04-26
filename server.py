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

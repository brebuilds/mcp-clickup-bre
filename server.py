#!/usr/bin/env python3
"""
ClickUp MCP Server - Comprehensive implementation of all ClickUp API capabilities
"""

import os
import json
from typing import Any, Optional, List, Dict
from datetime import datetime

import httpx
from mcp.server import Server
from mcp.types import Tool, TextContent
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ClickUp API Configuration
CLICKUP_API_TOKEN = os.getenv("CLICKUP_API_TOKEN")
CLICKUP_API_BASE = "https://api.clickup.com/api/v2"

if not CLICKUP_API_TOKEN:
    raise ValueError("CLICKUP_API_TOKEN environment variable is required")

# Initialize MCP Server
app = Server("clickup-mcp")

# HTTP Client with authentication
client = httpx.AsyncClient(
    base_url=CLICKUP_API_BASE,
    headers={
        "Authorization": CLICKUP_API_TOKEN,
        "Content-Type": "application/json"
    },
    timeout=30.0
)


# ============================================================================
# WORKSPACE & ORGANIZATION TOOLS
# ============================================================================

@app.list_tools()
async def list_tools() -> List[Tool]:
    """List all available tools"""
    return [
        # Workspace & Organization
        Tool(
            name="get_authorized_user",
            description="Get the authenticated user's information",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_teams",
            description="Get all teams the authenticated user is part of",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_workspaces",
            description="Get all workspaces",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_workspace",
            description="Get a specific workspace by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "The workspace ID"
                    }
                },
                "required": ["workspace_id"]
            }
        ),
        Tool(
            name="get_spaces",
            description="Get all spaces in a workspace",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "The workspace ID"
                    },
                    "archived": {
                        "type": "boolean",
                        "description": "Include archived spaces"
                    }
                },
                "required": ["workspace_id"]
            }
        ),
        Tool(
            name="get_space",
            description="Get a specific space by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "space_id": {
                        "type": "string",
                        "description": "The space ID"
                    }
                },
                "required": ["space_id"]
            }
        ),
        Tool(
            name="create_space",
            description="Create a new space",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "The workspace ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "Space name"
                    },
                    "multiple_assignees": {
                        "type": "boolean",
                        "description": "Allow multiple assignees"
                    },
                    "features": {
                        "type": "object",
                        "description": "Space features configuration"
                    }
                },
                "required": ["workspace_id", "name"]
            }
        ),
        Tool(
            name="update_space",
            description="Update a space",
            inputSchema={
                "type": "object",
                "properties": {
                    "space_id": {
                        "type": "string",
                        "description": "The space ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "New space name"
                    },
                    "multiple_assignees": {
                        "type": "boolean",
                        "description": "Allow multiple assignees"
                    },
                    "features": {
                        "type": "object",
                        "description": "Space features configuration"
                    }
                },
                "required": ["space_id"]
            }
        ),
        Tool(
            name="get_folders",
            description="Get all folders in a space",
            inputSchema={
                "type": "object",
                "properties": {
                    "space_id": {
                        "type": "string",
                        "description": "The space ID"
                    },
                    "archived": {
                        "type": "boolean",
                        "description": "Include archived folders"
                    }
                },
                "required": ["space_id"]
            }
        ),
        Tool(
            name="get_folder",
            description="Get a specific folder by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "folder_id": {
                        "type": "string",
                        "description": "The folder ID"
                    }
                },
                "required": ["folder_id"]
            }
        ),
        Tool(
            name="create_folder",
            description="Create a new folder",
            inputSchema={
                "type": "object",
                "properties": {
                    "space_id": {
                        "type": "string",
                        "description": "The space ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "Folder name"
                    }
                },
                "required": ["space_id", "name"]
            }
        ),
        Tool(
            name="update_folder",
            description="Update a folder",
            inputSchema={
                "type": "object",
                "properties": {
                    "folder_id": {
                        "type": "string",
                        "description": "The folder ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "New folder name"
                    }
                },
                "required": ["folder_id"]
            }
        ),
        Tool(
            name="get_lists",
            description="Get all lists in a folder or space",
            inputSchema={
                "type": "object",
                "properties": {
                    "folder_id": {
                        "type": "string",
                        "description": "The folder ID (optional if space_id provided)"
                    },
                    "space_id": {
                        "type": "string",
                        "description": "The space ID (optional if folder_id provided)"
                    },
                    "archived": {
                        "type": "boolean",
                        "description": "Include archived lists"
                    }
                }
            }
        ),
        Tool(
            name="get_list",
            description="Get a specific list by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "The list ID"
                    }
                },
                "required": ["list_id"]
            }
        ),
        Tool(
            name="create_list",
            description="Create a new list",
            inputSchema={
                "type": "object",
                "properties": {
                    "folder_id": {
                        "type": "string",
                        "description": "The folder ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "List name"
                    },
                    "content": {
                        "type": "string",
                        "description": "List content/description"
                    },
                    "due_date": {
                        "type": "integer",
                        "description": "Due date timestamp"
                    },
                    "due_date_time": {
                        "type": "boolean",
                        "description": "Include time in due date"
                    },
                    "priority": {
                        "type": "integer",
                        "description": "Priority (1=urgent, 2=high, 3=normal, 4=low)"
                    },
                    "assignee": {
                        "type": "string",
                        "description": "Assignee user ID"
                    },
                    "status": {
                        "type": "string",
                        "description": "Status name"
                    }
                },
                "required": ["folder_id", "name"]
            }
        ),
        Tool(
            name="update_list",
            description="Update a list",
            inputSchema={
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "The list ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "New list name"
                    },
                    "content": {
                        "type": "string",
                        "description": "New list content/description"
                    },
                    "due_date": {
                        "type": "integer",
                        "description": "Due date timestamp"
                    },
                    "due_date_time": {
                        "type": "boolean",
                        "description": "Include time in due date"
                    },
                    "priority": {
                        "type": "integer",
                        "description": "Priority (1=urgent, 2=high, 3=normal, 4=low)"
                    },
                    "assignee": {
                        "type": "string",
                        "description": "Assignee user ID"
                    },
                    "status": {
                        "type": "string",
                        "description": "Status name"
                    }
                },
                "required": ["list_id"]
            }
        ),
        Tool(
            name="get_list_members",
            description="Get members of a list",
            inputSchema={
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "The list ID"
                    }
                },
                "required": ["list_id"]
            }
        ),
        Tool(
            name="get_list_views",
            description="Get views for a list",
            inputSchema={
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "The list ID"
                    }
                },
                "required": ["list_id"]
            }
        ),
        # Task Management
        Tool(
            name="get_tasks",
            description="Get tasks from a list, folder, or space with filters",
            inputSchema={
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "List ID (optional)"
                    },
                    "folder_id": {
                        "type": "string",
                        "description": "Folder ID (optional)"
                    },
                    "space_id": {
                        "type": "string",
                        "description": "Space ID (optional)"
                    },
                    "archived": {
                        "type": "boolean",
                        "description": "Include archived tasks"
                    },
                    "page": {
                        "type": "integer",
                        "description": "Page number"
                    },
                    "order_by": {
                        "type": "string",
                        "description": "Order by field (id, created, updated, due_date)"
                    },
                    "reverse": {
                        "type": "boolean",
                        "description": "Reverse order"
                    },
                    "subtasks": {
                        "type": "boolean",
                        "description": "Include subtasks"
                    },
                    "statuses": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Filter by statuses"
                    },
                    "include_closed": {
                        "type": "boolean",
                        "description": "Include closed tasks"
                    },
                    "assignees": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Filter by assignee IDs"
                    },
                    "tags": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Filter by tags"
                    },
                    "due_date_gt": {
                        "type": "integer",
                        "description": "Due date greater than (timestamp)"
                    },
                    "due_date_lt": {
                        "type": "integer",
                        "description": "Due date less than (timestamp)"
                    },
                    "date_created_gt": {
                        "type": "integer",
                        "description": "Date created greater than (timestamp)"
                    },
                    "date_created_lt": {
                        "type": "integer",
                        "description": "Date created less than (timestamp)"
                    },
                    "date_updated_gt": {
                        "type": "integer",
                        "description": "Date updated greater than (timestamp)"
                    },
                    "date_updated_lt": {
                        "type": "integer",
                        "description": "Date updated less than (timestamp)"
                    }
                }
            }
        ),
        Tool(
            name="get_task",
            description="Get a specific task by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "The task ID"
                    },
                    "custom_task_ids": {
                        "type": "boolean",
                        "description": "Use custom task IDs"
                    },
                    "team_id": {
                        "type": "string",
                        "description": "Team ID (required for custom task IDs)"
                    },
                    "include_subtasks": {
                        "type": "boolean",
                        "description": "Include subtasks"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="create_task",
            description="Create a new task",
            inputSchema={
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "The list ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "Task name"
                    },
                    "description": {
                        "type": "string",
                        "description": "Task description"
                    },
                    "assignees": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Assignee user IDs"
                    },
                    "tags": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Tag names"
                    },
                    "status": {
                        "type": "string",
                        "description": "Status name"
                    },
                    "priority": {
                        "type": "integer",
                        "description": "Priority (1=urgent, 2=high, 3=normal, 4=low)"
                    },
                    "due_date": {
                        "type": "integer",
                        "description": "Due date timestamp"
                    },
                    "due_date_time": {
                        "type": "boolean",
                        "description": "Include time in due date"
                    },
                    "start_date": {
                        "type": "integer",
                        "description": "Start date timestamp"
                    },
                    "start_date_time": {
                        "type": "boolean",
                        "description": "Include time in start date"
                    },
                    "notify_all": {
                        "type": "boolean",
                        "description": "Notify all assignees"
                    },
                    "parent": {
                        "type": "string",
                        "description": "Parent task ID"
                    },
                    "links_to": {
                        "type": "string",
                        "description": "Task ID to link to"
                    },
                    "check_required_custom_fields": {
                        "type": "boolean",
                        "description": "Check required custom fields"
                    },
                    "custom_fields": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "Custom field values"
                    }
                },
                "required": ["list_id", "name"]
            }
        ),
        Tool(
            name="update_task",
            description="Update an existing task",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "The task ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "New task name"
                    },
                    "description": {
                        "type": "string",
                        "description": "New task description"
                    },
                    "status": {
                        "type": "string",
                        "description": "New status name"
                    },
                    "priority": {
                        "type": "integer",
                        "description": "Priority (1=urgent, 2=high, 3=normal, 4=low)"
                    },
                    "due_date": {
                        "type": "integer",
                        "description": "Due date timestamp"
                    },
                    "due_date_time": {
                        "type": "boolean",
                        "description": "Include time in due date"
                    },
                    "start_date": {
                        "type": "integer",
                        "description": "Start date timestamp"
                    },
                    "start_date_time": {
                        "type": "boolean",
                        "description": "Include time in start date"
                    },
                    "assignees": {
                        "type": "object",
                        "description": "Assignee configuration (add/rem arrays)"
                    },
                    "archived": {
                        "type": "boolean",
                        "description": "Archive status"
                    },
                    "parent": {
                        "type": "string",
                        "description": "Parent task ID"
                    },
                    "time_estimate": {
                        "type": "integer",
                        "description": "Time estimate in milliseconds"
                    },
                    "time_spent": {
                        "type": "integer",
                        "description": "Time spent in milliseconds"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="search_tasks",
            description="Search for tasks across workspace",
            inputSchema={
                "type": "object",
                "properties": {
                    "team_id": {
                        "type": "string",
                        "description": "Team ID"
                    },
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    },
                    "page": {
                        "type": "integer",
                        "description": "Page number"
                    }
                },
                "required": ["team_id"]
            }
        ),
        Tool(
            name="get_task_comments",
            description="Get comments for a task",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "The task ID"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="create_task_comment",
            description="Add a comment to a task",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "The task ID"
                    },
                    "comment_text": {
                        "type": "string",
                        "description": "Comment text"
                    },
                    "assignee": {
                        "type": "string",
                        "description": "Assignee user ID to notify"
                    },
                    "notify_all": {
                        "type": "boolean",
                        "description": "Notify all assignees"
                    }
                },
                "required": ["task_id", "comment_text"]
            }
        ),
        Tool(
            name="update_task_comment",
            description="Update a task comment",
            inputSchema={
                "type": "object",
                "properties": {
                    "comment_id": {
                        "type": "string",
                        "description": "The comment ID"
                    },
                    "comment_text": {
                        "type": "string",
                        "description": "New comment text"
                    },
                    "assignee": {
                        "type": "string",
                        "description": "Assignee user ID to notify"
                    }
                },
                "required": ["comment_id", "comment_text"]
            }
        ),
        Tool(
            name="get_task_dependencies",
            description="Get task dependencies",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "The task ID"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="create_task_dependency",
            description="Create a task dependency",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "The task ID"
                    },
                    "depends_on": {
                        "type": "string",
                        "description": "Task ID this task depends on"
                    },
                    "dependency_of": {
                        "type": "string",
                        "description": "Task ID that depends on this task"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="get_task_time_entries",
            description="Get time entries for a task",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "The task ID"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="create_task_time_entry",
            description="Create a time entry for a task",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "The task ID"
                    },
                    "start": {
                        "type": "integer",
                        "description": "Start time timestamp"
                    },
                    "billable": {
                        "type": "boolean",
                        "description": "Is billable"
                    },
                    "duration": {
                        "type": "integer",
                        "description": "Duration in milliseconds"
                    },
                    "description": {
                        "type": "string",
                        "description": "Time entry description"
                    },
                    "tags": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "Time entry tags"
                    }
                },
                "required": ["task_id", "start", "duration"]
            }
        ),
        Tool(
            name="get_task_attachments",
            description="Get attachments for a task",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "The task ID"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="get_task_watchers",
            description="Get watchers for a task",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "The task ID"
                    }
                },
                "required": ["task_id"]
            }
        ),
        # Time Tracking
        Tool(
            name="get_time_entries",
            description="Get time entries with filters",
            inputSchema={
                "type": "object",
                "properties": {
                    "team_id": {
                        "type": "string",
                        "description": "Team ID"
                    },
                    "start_date": {
                        "type": "integer",
                        "description": "Start date timestamp"
                    },
                    "end_date": {
                        "type": "integer",
                        "description": "End date timestamp"
                    },
                    "assignee": {
                        "type": "string",
                        "description": "Assignee user ID"
                    },
                    "include_task_tags": {
                        "type": "boolean",
                        "description": "Include task tags"
                    },
                    "include_location_names": {
                        "type": "boolean",
                        "description": "Include location names"
                    },
                    "space_id": {
                        "type": "string",
                        "description": "Space ID filter"
                    },
                    "folder_id": {
                        "type": "string",
                        "description": "Folder ID filter"
                    },
                    "list_id": {
                        "type": "string",
                        "description": "List ID filter"
                    },
                    "task_id": {
                        "type": "string",
                        "description": "Task ID filter"
                    }
                },
                "required": ["team_id"]
            }
        ),
        Tool(
            name="get_time_entry",
            description="Get a specific time entry",
            inputSchema={
                "type": "object",
                "properties": {
                    "team_id": {
                        "type": "string",
                        "description": "Team ID"
                    },
                    "timer_id": {
                        "type": "string",
                        "description": "Timer ID"
                    }
                },
                "required": ["team_id", "timer_id"]
            }
        ),
        Tool(
            name="start_time_entry",
            description="Start a timer for a task",
            inputSchema={
                "type": "object",
                "properties": {
                    "team_id": {
                        "type": "string",
                        "description": "Team ID"
                    },
                    "task_id": {
                        "type": "string",
                        "description": "Task ID"
                    },
                    "billable": {
                        "type": "boolean",
                        "description": "Is billable"
                    },
                    "description": {
                        "type": "string",
                        "description": "Timer description"
                    },
                    "tags": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "Timer tags"
                    },
                    "tid": {
                        "type": "string",
                        "description": "Time tracking ID"
                    }
                },
                "required": ["team_id", "task_id"]
            }
        ),
        Tool(
            name="stop_time_entry",
            description="Stop a running timer",
            inputSchema={
                "type": "object",
                "properties": {
                    "team_id": {
                        "type": "string",
                        "description": "Team ID"
                    },
                    "timer_id": {
                        "type": "string",
                        "description": "Timer ID"
                    }
                },
                "required": ["team_id", "timer_id"]
            }
        ),
        Tool(
            name="update_time_entry",
            description="Update a time entry",
            inputSchema={
                "type": "object",
                "properties": {
                    "team_id": {
                        "type": "string",
                        "description": "Team ID"
                    },
                    "timer_id": {
                        "type": "string",
                        "description": "Timer ID"
                    },
                    "description": {
                        "type": "string",
                        "description": "New description"
                    },
                    "tags": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "New tags"
                    },
                    "billable": {
                        "type": "boolean",
                        "description": "Is billable"
                    },
                    "start": {
                        "type": "integer",
                        "description": "Start time timestamp"
                    },
                    "duration": {
                        "type": "integer",
                        "description": "Duration in milliseconds"
                    }
                },
                "required": ["team_id", "timer_id"]
            }
        ),
        # Goals
        Tool(
            name="get_goals",
            description="Get goals for a workspace",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "Workspace ID"
                    },
                    "include_completed": {
                        "type": "boolean",
                        "description": "Include completed goals"
                    }
                },
                "required": ["workspace_id"]
            }
        ),
        Tool(
            name="get_goal",
            description="Get a specific goal",
            inputSchema={
                "type": "object",
                "properties": {
                    "goal_id": {
                        "type": "string",
                        "description": "Goal ID"
                    }
                },
                "required": ["goal_id"]
            }
        ),
        Tool(
            name="create_goal",
            description="Create a new goal",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "Workspace ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "Goal name"
                    },
                    "due_date": {
                        "type": "integer",
                        "description": "Due date timestamp"
                    },
                    "description": {
                        "type": "string",
                        "description": "Goal description"
                    },
                    "rem_owners": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Owner user IDs"
                    },
                    "color": {
                        "type": "string",
                        "description": "Goal color"
                    }
                },
                "required": ["workspace_id", "name"]
            }
        ),
        Tool(
            name="update_goal",
            description="Update a goal",
            inputSchema={
                "type": "object",
                "properties": {
                    "goal_id": {
                        "type": "string",
                        "description": "Goal ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "New goal name"
                    },
                    "due_date": {
                        "type": "integer",
                        "description": "Due date timestamp"
                    },
                    "description": {
                        "type": "string",
                        "description": "New goal description"
                    },
                    "rem_owners": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Owner user IDs"
                    },
                    "color": {
                        "type": "string",
                        "description": "Goal color"
                    },
                    "add_to_user_favorites": {
                        "type": "boolean",
                        "description": "Add to user favorites"
                    }
                },
                "required": ["goal_id"]
            }
        ),
        Tool(
            name="get_goal_key_results",
            description="Get key results for a goal",
            inputSchema={
                "type": "object",
                "properties": {
                    "goal_id": {
                        "type": "string",
                        "description": "Goal ID"
                    }
                },
                "required": ["goal_id"]
            }
        ),
        Tool(
            name="create_goal_key_result",
            description="Create a key result for a goal",
            inputSchema={
                "type": "object",
                "properties": {
                    "goal_id": {
                        "type": "string",
                        "description": "Goal ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "Key result name"
                    },
                    "type": {
                        "type": "string",
                        "description": "Key result type (number, currency, percentage, automatic, manual)"
                    },
                    "unit": {
                        "type": "string",
                        "description": "Unit (for number type)"
                    },
                    "steps_start": {
                        "type": "integer",
                        "description": "Starting value"
                    },
                    "steps_end": {
                        "type": "integer",
                        "description": "Target value"
                    },
                    "steps_current": {
                        "type": "integer",
                        "description": "Current value"
                    },
                    "task_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Task IDs to link"
                    },
                    "list_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List IDs to link"
                    }
                },
                "required": ["goal_id", "name", "type"]
            }
        ),
        Tool(
            name="update_goal_key_result",
            description="Update a goal key result",
            inputSchema={
                "type": "object",
                "properties": {
                    "goal_id": {
                        "type": "string",
                        "description": "Goal ID"
                    },
                    "key_result_id": {
                        "type": "string",
                        "description": "Key result ID"
                    },
                    "steps_current": {
                        "type": "integer",
                        "description": "Current value"
                    }
                },
                "required": ["goal_id", "key_result_id"]
            }
        ),
        # Custom Fields
        Tool(
            name="get_custom_fields",
            description="Get custom fields for a list",
            inputSchema={
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "List ID"
                    }
                },
                "required": ["list_id"]
            }
        ),
        Tool(
            name="get_custom_field",
            description="Get a specific custom field",
            inputSchema={
                "type": "object",
                "properties": {
                    "field_id": {
                        "type": "string",
                        "description": "Custom field ID"
                    }
                },
                "required": ["field_id"]
            }
        ),
        Tool(
            name="update_custom_field_value",
            description="Update a custom field value for a task",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "Task ID"
                    },
                    "field_id": {
                        "type": "string",
                        "description": "Custom field ID"
                    },
                    "value": {
                        "type": "any",
                        "description": "Field value (type depends on field type)"
                    }
                },
                "required": ["task_id", "field_id", "value"]
            }
        ),
        # Views
        Tool(
            name="get_views",
            description="Get views for a workspace or space",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "Workspace ID (optional if space_id provided)"
                    },
                    "space_id": {
                        "type": "string",
                        "description": "Space ID (optional if workspace_id provided)"
                    }
                }
            }
        ),
        Tool(
            name="get_view",
            description="Get a specific view",
            inputSchema={
                "type": "object",
                "properties": {
                    "view_id": {
                        "type": "string",
                        "description": "View ID"
                    }
                },
                "required": ["view_id"]
            }
        ),
        Tool(
            name="get_view_tasks",
            description="Get tasks from a view",
            inputSchema={
                "type": "object",
                "properties": {
                    "view_id": {
                        "type": "string",
                        "description": "View ID"
                    },
                    "page": {
                        "type": "integer",
                        "description": "Page number"
                    }
                },
                "required": ["view_id"]
            }
        ),
        # Tags
        Tool(
            name="get_tags",
            description="Get tags for a workspace",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "Workspace ID"
                    }
                },
                "required": ["workspace_id"]
            }
        ),
        Tool(
            name="create_tag",
            description="Create a tag",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "Workspace ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "Tag name"
                    },
                    "tag_fg": {
                        "type": "string",
                        "description": "Tag foreground color"
                    },
                    "tag_bg": {
                        "type": "string",
                        "description": "Tag background color"
                    }
                },
                "required": ["workspace_id", "name"]
            }
        ),
        Tool(
            name="update_tag",
            description="Update a tag",
            inputSchema={
                "type": "object",
                "properties": {
                    "tag_name": {
                        "type": "string",
                        "description": "Tag name"
                    },
                    "workspace_id": {
                        "type": "string",
                        "description": "Workspace ID"
                    },
                    "tag_fg": {
                        "type": "string",
                        "description": "Tag foreground color"
                    },
                    "tag_bg": {
                        "type": "string",
                        "description": "Tag background color"
                    }
                },
                "required": ["tag_name", "workspace_id"]
            }
        ),
        # Statuses
        Tool(
            name="get_list_statuses",
            description="Get statuses for a list",
            inputSchema={
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "List ID"
                    }
                },
                "required": ["list_id"]
            }
        ),
        Tool(
            name="create_list_status",
            description="Create a status for a list",
            inputSchema={
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "List ID"
                    },
                    "status": {
                        "type": "string",
                        "description": "Status name"
                    },
                    "type": {
                        "type": "string",
                        "description": "Status type (open, custom, closed)"
                    },
                    "orderindex": {
                        "type": "integer",
                        "description": "Order index"
                    }
                },
                "required": ["list_id", "status", "type"]
            }
        ),
        Tool(
            name="update_list_status",
            description="Update a list status",
            inputSchema={
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "List ID"
                    },
                    "status_id": {
                        "type": "string",
                        "description": "Status ID"
                    },
                    "status": {
                        "type": "string",
                        "description": "New status name"
                    },
                    "orderindex": {
                        "type": "integer",
                        "description": "Order index"
                    }
                },
                "required": ["list_id", "status_id"]
            }
        ),
        # Webhooks
        Tool(
            name="get_webhooks",
            description="Get webhooks for a workspace",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "Workspace ID"
                    }
                },
                "required": ["workspace_id"]
            }
        ),
        Tool(
            name="create_webhook",
            description="Create a webhook",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "Workspace ID"
                    },
                    "endpoint": {
                        "type": "string",
                        "description": "Webhook endpoint URL"
                    },
                    "client_id": {
                        "type": "string",
                        "description": "Client ID"
                    },
                    "events": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Events to subscribe to"
                    },
                    "task_id": {
                        "type": "string",
                        "description": "Task ID filter (optional)"
                    },
                    "list_id": {
                        "type": "string",
                        "description": "List ID filter (optional)"
                    },
                    "folder_id": {
                        "type": "string",
                        "description": "Folder ID filter (optional)"
                    },
                    "space_id": {
                        "type": "string",
                        "description": "Space ID filter (optional)"
                    },
                    "health": {
                        "type": "object",
                        "description": "Health check configuration"
                    }
                },
                "required": ["workspace_id", "endpoint", "client_id", "events"]
            }
        ),
        Tool(
            name="update_webhook",
            description="Update a webhook",
            inputSchema={
                "type": "object",
                "properties": {
                    "webhook_id": {
                        "type": "string",
                        "description": "Webhook ID"
                    },
                    "endpoint": {
                        "type": "string",
                        "description": "New webhook endpoint URL"
                    },
                    "events": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Events to subscribe to"
                    },
                    "status": {
                        "type": "string",
                        "description": "Webhook status (active, inactive)"
                    }
                },
                "required": ["webhook_id"]
            }
        ),
        # Documents
        Tool(
            name="search_documents",
            description="Search documents in a workspace",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "Workspace ID"
                    },
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    }
                },
                "required": ["workspace_id"]
            }
        ),
        Tool(
            name="get_document",
            description="Get a specific document",
            inputSchema={
                "type": "object",
                "properties": {
                    "document_id": {
                        "type": "string",
                        "description": "Document ID"
                    }
                },
                "required": ["document_id"]
            }
        ),
        # Checklists
        Tool(
            name="get_task_checklists",
            description="Get checklists for a task",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "Task ID"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="create_task_checklist",
            description="Create a checklist for a task",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "Task ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "Checklist name"
                    }
                },
                "required": ["task_id", "name"]
            }
        ),
        Tool(
            name="create_checklist_item",
            description="Create a checklist item",
            inputSchema={
                "type": "object",
                "properties": {
                    "checklist_id": {
                        "type": "string",
                        "description": "Checklist ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "Item name"
                    },
                    "assignee": {
                        "type": "string",
                        "description": "Assignee user ID"
                    }
                },
                "required": ["checklist_id", "name"]
            }
        ),
        Tool(
            name="update_checklist_item",
            description="Update a checklist item",
            inputSchema={
                "type": "object",
                "properties": {
                    "checklist_id": {
                        "type": "string",
                        "description": "Checklist ID"
                    },
                    "checklist_item_id": {
                        "type": "string",
                        "description": "Checklist item ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "New item name"
                    },
                    "assignee": {
                        "type": "string",
                        "description": "Assignee user ID"
                    },
                    "resolved": {
                        "type": "boolean",
                        "description": "Is resolved"
                    }
                },
                "required": ["checklist_id", "checklist_item_id"]
            }
        ),
        # Task Templates
        Tool(
            name="get_task_templates",
            description="Get task templates for a workspace",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "Workspace ID"
                    },
                    "page": {
                        "type": "integer",
                        "description": "Page number"
                    }
                },
                "required": ["workspace_id"]
            }
        ),
        Tool(
            name="get_task_template",
            description="Get a specific task template",
            inputSchema={
                "type": "object",
                "properties": {
                    "template_id": {
                        "type": "string",
                        "description": "Template ID"
                    }
                },
                "required": ["template_id"]
            }
        ),
        Tool(
            name="create_task_from_template",
            description="Create a task from a template",
            inputSchema={
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "List ID"
                    },
                    "template_id": {
                        "type": "string",
                        "description": "Template ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "Task name"
                    }
                },
                "required": ["list_id", "template_id", "name"]
            }
        ),
        # Members
        Tool(
            name="get_team_members",
            description="Get members of a team",
            inputSchema={
                "type": "object",
                "properties": {
                    "team_id": {
                        "type": "string",
                        "description": "Team ID"
                    }
                },
                "required": ["team_id"]
            }
        ),
        Tool(
            name="get_team_member",
            description="Get a specific team member",
            inputSchema={
                "type": "object",
                "properties": {
                    "team_id": {
                        "type": "string",
                        "description": "Team ID"
                    },
                    "user_id": {
                        "type": "string",
                        "description": "User ID"
                    }
                },
                "required": ["team_id", "user_id"]
            }
        ),
        # Shared Hierarchy
        Tool(
            name="get_shared_hierarchy",
            description="Get shared hierarchy for a workspace",
            inputSchema={
                "type": "object",
                "properties": {
                    "workspace_id": {
                        "type": "string",
                        "description": "Workspace ID"
                    }
                },
                "required": ["workspace_id"]
            }
        ),
    ]


# ============================================================================
# TOOL HANDLERS - Workspace & Organization
# ============================================================================

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> List[TextContent]:
    """Handle tool calls"""
    try:
        if name == "get_authorized_user":
            response = await client.get("/user")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_teams":
            response = await client.get("/team")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_workspaces":
            response = await client.get("/team")
            teams = response.json()
            workspaces = []
            for team in teams.get("teams", []):
                workspaces.extend(team.get("workspaces", []))
            return [TextContent(type="text", text=json.dumps(workspaces, indent=2))]

        elif name == "get_workspace":
            workspace_id = arguments["workspace_id"]
            response = await client.get(f"/team/{workspace_id}")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_spaces":
            workspace_id = arguments["workspace_id"]
            params = {}
            if "archived" in arguments:
                params["archived"] = arguments["archived"]
            response = await client.get(f"/team/{workspace_id}/space", params=params)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_space":
            space_id = arguments["space_id"]
            response = await client.get(f"/space/{space_id}")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_space":
            workspace_id = arguments["workspace_id"]
            data = {"name": arguments["name"]}
            if "multiple_assignees" in arguments:
                data["multiple_assignees"] = arguments["multiple_assignees"]
            if "features" in arguments:
                data["features"] = arguments["features"]
            response = await client.post(f"/team/{workspace_id}/space", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_space":
            space_id = arguments["space_id"]
            data = {}
            if "name" in arguments:
                data["name"] = arguments["name"]
            if "multiple_assignees" in arguments:
                data["multiple_assignees"] = arguments["multiple_assignees"]
            if "features" in arguments:
                data["features"] = arguments["features"]
            response = await client.put(f"/space/{space_id}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_folders":
            space_id = arguments["space_id"]
            params = {}
            if "archived" in arguments:
                params["archived"] = arguments["archived"]
            response = await client.get(f"/space/{space_id}/folder", params=params)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_folder":
            folder_id = arguments["folder_id"]
            response = await client.get(f"/folder/{folder_id}")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_folder":
            space_id = arguments["space_id"]
            data = {"name": arguments["name"]}
            response = await client.post(f"/space/{space_id}/folder", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_folder":
            folder_id = arguments["folder_id"]
            data = {}
            if "name" in arguments:
                data["name"] = arguments["name"]
            response = await client.put(f"/folder/{folder_id}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_lists":
            params = {}
            if "archived" in arguments:
                params["archived"] = arguments["archived"]
            
            if "folder_id" in arguments:
                response = await client.get(f"/folder/{arguments['folder_id']}/list", params=params)
            elif "space_id" in arguments:
                response = await client.get(f"/space/{arguments['space_id']}/list", params=params)
            else:
                return [TextContent(type="text", text='{"error": "Either folder_id or space_id is required"}')]
            
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_list":
            list_id = arguments["list_id"]
            response = await client.get(f"/list/{list_id}")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_list":
            folder_id = arguments["folder_id"]
            data = {"name": arguments["name"]}
            if "content" in arguments:
                data["content"] = arguments["content"]
            if "due_date" in arguments:
                data["due_date"] = arguments["due_date"]
            if "due_date_time" in arguments:
                data["due_date_time"] = arguments["due_date_time"]
            if "priority" in arguments:
                data["priority"] = arguments["priority"]
            if "assignee" in arguments:
                data["assignee"] = arguments["assignee"]
            if "status" in arguments:
                data["status"] = arguments["status"]
            response = await client.post(f"/folder/{folder_id}/list", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_list":
            list_id = arguments["list_id"]
            data = {}
            for key in ["name", "content", "due_date", "due_date_time", "priority", "assignee", "status"]:
                if key in arguments:
                    data[key] = arguments[key]
            response = await client.put(f"/list/{list_id}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_list_members":
            list_id = arguments["list_id"]
            response = await client.get(f"/list/{list_id}/member")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_list_views":
            list_id = arguments["list_id"]
            response = await client.get(f"/list/{list_id}/view")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Task Management
        elif name == "get_tasks":
            params = {}
            for key in ["archived", "page", "order_by", "reverse", "subtasks", "include_closed"]:
                if key in arguments:
                    params[key] = arguments[key]
            if "statuses" in arguments:
                params["statuses[]"] = arguments["statuses"]
            if "assignees" in arguments:
                params["assignees[]"] = arguments["assignees"]
            if "tags" in arguments:
                params["tags[]"] = arguments["tags"]
            for key in ["due_date_gt", "due_date_lt", "date_created_gt", "date_created_lt", "date_updated_gt", "date_updated_lt"]:
                if key in arguments:
                    params[key] = arguments[key]
            
            if "list_id" in arguments:
                response = await client.get(f"/list/{arguments['list_id']}/task", params=params)
            elif "folder_id" in arguments:
                response = await client.get(f"/folder/{arguments['folder_id']}/task", params=params)
            elif "space_id" in arguments:
                response = await client.get(f"/space/{arguments['space_id']}/task", params=params)
            else:
                return [TextContent(type="text", text='{"error": "list_id, folder_id, or space_id is required"}')]
            
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_task":
            task_id = arguments["task_id"]
            params = {}
            if "custom_task_ids" in arguments:
                params["custom_task_ids"] = arguments["custom_task_ids"]
            if "team_id" in arguments:
                params["team_id"] = arguments["team_id"]
            if "include_subtasks" in arguments:
                params["include_subtasks"] = arguments["include_subtasks"]
            response = await client.get(f"/task/{task_id}", params=params)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_task":
            list_id = arguments["list_id"]
            data = {"name": arguments["name"]}
            for key in ["description", "assignees", "tags", "status", "priority", "due_date", "due_date_time", 
                       "start_date", "start_date_time", "notify_all", "parent", "links_to", "check_required_custom_fields", "custom_fields"]:
                if key in arguments:
                    data[key] = arguments[key]
            response = await client.post(f"/list/{list_id}/task", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_task":
            task_id = arguments["task_id"]
            data = {}
            for key in ["name", "description", "status", "priority", "due_date", "due_date_time", 
                       "start_date", "start_date_time", "assignees", "archived", "parent", 
                       "time_estimate", "time_spent"]:
                if key in arguments:
                    data[key] = arguments[key]
            response = await client.put(f"/task/{task_id}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "search_tasks":
            team_id = arguments["team_id"]
            params = {"team_id": team_id}
            if "query" in arguments:
                params["query"] = arguments["query"]
            if "page" in arguments:
                params["page"] = arguments["page"]
            response = await client.get("/task", params=params)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_task_comments":
            task_id = arguments["task_id"]
            response = await client.get(f"/task/{task_id}/comment")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_task_comment":
            task_id = arguments["task_id"]
            data = {"comment_text": arguments["comment_text"]}
            if "assignee" in arguments:
                data["assignee"] = arguments["assignee"]
            if "notify_all" in arguments:
                data["notify_all"] = arguments["notify_all"]
            response = await client.post(f"/task/{task_id}/comment", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_task_comment":
            comment_id = arguments["comment_id"]
            data = {"comment_text": arguments["comment_text"]}
            if "assignee" in arguments:
                data["assignee"] = arguments["assignee"]
            response = await client.put(f"/comment/{comment_id}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_task_dependencies":
            task_id = arguments["task_id"]
            response = await client.get(f"/task/{task_id}/dependency")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_task_dependency":
            task_id = arguments["task_id"]
            data = {}
            if "depends_on" in arguments:
                data["depends_on"] = arguments["depends_on"]
            if "dependency_of" in arguments:
                data["dependency_of"] = arguments["dependency_of"]
            response = await client.post(f"/task/{task_id}/dependency", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_task_time_entries":
            task_id = arguments["task_id"]
            response = await client.get(f"/task/{task_id}/time")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_task_time_entry":
            task_id = arguments["task_id"]
            data = {
                "start": arguments["start"],
                "duration": arguments["duration"]
            }
            if "billable" in arguments:
                data["billable"] = arguments["billable"]
            if "description" in arguments:
                data["description"] = arguments["description"]
            if "tags" in arguments:
                data["tags"] = arguments["tags"]
            response = await client.post(f"/task/{task_id}/time", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_task_attachments":
            task_id = arguments["task_id"]
            response = await client.get(f"/task/{task_id}/attachment")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_task_watchers":
            task_id = arguments["task_id"]
            response = await client.get(f"/task/{task_id}/watcher")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Time Tracking
        elif name == "get_time_entries":
            team_id = arguments["team_id"]
            params = {"team_id": team_id}
            for key in ["start_date", "end_date", "assignee", "include_task_tags", "include_location_names",
                       "space_id", "folder_id", "list_id", "task_id"]:
                if key in arguments:
                    params[key] = arguments[key]
            response = await client.get("/team/{}/time_entries".format(team_id), params=params)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_time_entry":
            team_id = arguments["team_id"]
            timer_id = arguments["timer_id"]
            response = await client.get(f"/team/{team_id}/time_entries/{timer_id}")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "start_time_entry":
            team_id = arguments["team_id"]
            data = {"tid": arguments["task_id"]}
            if "billable" in arguments:
                data["billable"] = arguments["billable"]
            if "description" in arguments:
                data["description"] = arguments["description"]
            if "tags" in arguments:
                data["tags"] = arguments["tags"]
            if "tid" in arguments:
                data["tid"] = arguments["tid"]
            response = await client.post(f"/team/{team_id}/time_entries/start", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "stop_time_entry":
            team_id = arguments["team_id"]
            timer_id = arguments["timer_id"]
            response = await client.post(f"/team/{team_id}/time_entries/stop/{timer_id}")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_time_entry":
            team_id = arguments["team_id"]
            timer_id = arguments["timer_id"]
            data = {}
            for key in ["description", "tags", "billable", "start", "duration"]:
                if key in arguments:
                    data[key] = arguments[key]
            response = await client.put(f"/team/{team_id}/time_entries/{timer_id}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Goals
        elif name == "get_goals":
            workspace_id = arguments["workspace_id"]
            params = {}
            if "include_completed" in arguments:
                params["include_completed"] = arguments["include_completed"]
            response = await client.get(f"/team/{workspace_id}/goal", params=params)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_goal":
            goal_id = arguments["goal_id"]
            response = await client.get(f"/goal/{goal_id}")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_goal":
            workspace_id = arguments["workspace_id"]
            data = {"name": arguments["name"]}
            for key in ["due_date", "description", "rem_owners", "color"]:
                if key in arguments:
                    data[key] = arguments[key]
            response = await client.post(f"/team/{workspace_id}/goal", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_goal":
            goal_id = arguments["goal_id"]
            data = {}
            for key in ["name", "due_date", "description", "rem_owners", "color", "add_to_user_favorites"]:
                if key in arguments:
                    data[key] = arguments[key]
            response = await client.put(f"/goal/{goal_id}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_goal_key_results":
            goal_id = arguments["goal_id"]
            response = await client.get(f"/goal/{goal_id}/key_result")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_goal_key_result":
            goal_id = arguments["goal_id"]
            data = {
                "name": arguments["name"],
                "type": arguments["type"]
            }
            for key in ["unit", "steps_start", "steps_end", "steps_current", "task_ids", "list_ids"]:
                if key in arguments:
                    data[key] = arguments[key]
            response = await client.post(f"/goal/{goal_id}/key_result", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_goal_key_result":
            goal_id = arguments["goal_id"]
            key_result_id = arguments["key_result_id"]
            data = {"steps_current": arguments["steps_current"]}
            response = await client.put(f"/goal/{goal_id}/key_result/{key_result_id}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Custom Fields
        elif name == "get_custom_fields":
            list_id = arguments["list_id"]
            response = await client.get(f"/list/{list_id}/field")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_custom_field":
            field_id = arguments["field_id"]
            response = await client.get(f"/field/{field_id}")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_custom_field_value":
            task_id = arguments["task_id"]
            field_id = arguments["field_id"]
            data = {"value": arguments["value"]}
            response = await client.post(f"/task/{task_id}/field/{field_id}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Views
        elif name == "get_views":
            if "workspace_id" in arguments:
                response = await client.get(f"/team/{arguments['workspace_id']}/view")
            elif "space_id" in arguments:
                response = await client.get(f"/space/{arguments['space_id']}/view")
            else:
                return [TextContent(type="text", text='{"error": "workspace_id or space_id is required"}')]
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_view":
            view_id = arguments["view_id"]
            response = await client.get(f"/view/{view_id}")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_view_tasks":
            view_id = arguments["view_id"]
            params = {}
            if "page" in arguments:
                params["page"] = arguments["page"]
            response = await client.get(f"/view/{view_id}/task", params=params)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Tags
        elif name == "get_tags":
            workspace_id = arguments["workspace_id"]
            response = await client.get(f"/team/{workspace_id}/tag")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_tag":
            workspace_id = arguments["workspace_id"]
            data = {"name": arguments["name"]}
            if "tag_fg" in arguments:
                data["tag_fg"] = arguments["tag_fg"]
            if "tag_bg" in arguments:
                data["tag_bg"] = arguments["tag_bg"]
            response = await client.post(f"/team/{workspace_id}/tag", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_tag":
            tag_name = arguments["tag_name"]
            workspace_id = arguments["workspace_id"]
            data = {}
            if "tag_fg" in arguments:
                data["tag_fg"] = arguments["tag_fg"]
            if "tag_bg" in arguments:
                data["tag_bg"] = arguments["tag_bg"]
            response = await client.put(f"/team/{workspace_id}/tag/{tag_name}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Statuses
        elif name == "get_list_statuses":
            list_id = arguments["list_id"]
            response = await client.get(f"/list/{list_id}/field")
            # Filter for status fields
            result = response.json()
            statuses = [f for f in result.get("fields", []) if f.get("type") == "status"]
            return [TextContent(type="text", text=json.dumps(statuses, indent=2))]

        elif name == "create_list_status":
            list_id = arguments["list_id"]
            data = {
                "status": arguments["status"],
                "type": arguments["type"]
            }
            if "orderindex" in arguments:
                data["orderindex"] = arguments["orderindex"]
            response = await client.post(f"/list/{list_id}/field", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_list_status":
            list_id = arguments["list_id"]
            status_id = arguments["status_id"]
            data = {}
            if "status" in arguments:
                data["status"] = arguments["status"]
            if "orderindex" in arguments:
                data["orderindex"] = arguments["orderindex"]
            response = await client.put(f"/list/{list_id}/field/{status_id}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Webhooks
        elif name == "get_webhooks":
            workspace_id = arguments["workspace_id"]
            response = await client.get(f"/team/{workspace_id}/webhook")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_webhook":
            workspace_id = arguments["workspace_id"]
            data = {
                "endpoint": arguments["endpoint"],
                "client_id": arguments["client_id"],
                "events": arguments["events"]
            }
            for key in ["task_id", "list_id", "folder_id", "space_id", "health"]:
                if key in arguments:
                    data[key] = arguments[key]
            response = await client.post(f"/team/{workspace_id}/webhook", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_webhook":
            webhook_id = arguments["webhook_id"]
            data = {}
            for key in ["endpoint", "events", "status"]:
                if key in arguments:
                    data[key] = arguments[key]
            response = await client.put(f"/webhook/{webhook_id}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Documents
        elif name == "search_documents":
            workspace_id = arguments["workspace_id"]
            params = {}
            if "query" in arguments:
                params["query"] = arguments["query"]
            response = await client.get(f"/team/{workspace_id}/doc", params=params)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_document":
            document_id = arguments["document_id"]
            response = await client.get(f"/doc/{document_id}")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Checklists
        elif name == "get_task_checklists":
            task_id = arguments["task_id"]
            response = await client.get(f"/task/{task_id}/checklist")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_task_checklist":
            task_id = arguments["task_id"]
            data = {"name": arguments["name"]}
            response = await client.post(f"/task/{task_id}/checklist", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_checklist_item":
            checklist_id = arguments["checklist_id"]
            data = {"name": arguments["name"]}
            if "assignee" in arguments:
                data["assignee"] = arguments["assignee"]
            response = await client.post(f"/checklist/{checklist_id}/checklist_item", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "update_checklist_item":
            checklist_id = arguments["checklist_id"]
            checklist_item_id = arguments["checklist_item_id"]
            data = {}
            for key in ["name", "assignee", "resolved"]:
                if key in arguments:
                    data[key] = arguments[key]
            response = await client.put(f"/checklist/{checklist_id}/checklist_item/{checklist_item_id}", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Task Templates
        elif name == "get_task_templates":
            workspace_id = arguments["workspace_id"]
            params = {}
            if "page" in arguments:
                params["page"] = arguments["page"]
            response = await client.get(f"/team/{workspace_id}/taskTemplate", params=params)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_task_template":
            template_id = arguments["template_id"]
            response = await client.get(f"/taskTemplate/{template_id}")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "create_task_from_template":
            list_id = arguments["list_id"]
            data = {
                "template_id": arguments["template_id"],
                "name": arguments["name"]
            }
            response = await client.post(f"/list/{list_id}/taskTemplate", json=data)
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Members
        elif name == "get_team_members":
            team_id = arguments["team_id"]
            response = await client.get(f"/team/{team_id}/member")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        elif name == "get_team_member":
            team_id = arguments["team_id"]
            user_id = arguments["user_id"]
            response = await client.get(f"/team/{team_id}/member/{user_id}")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        # Shared Hierarchy
        elif name == "get_shared_hierarchy":
            workspace_id = arguments["workspace_id"]
            response = await client.get(f"/team/{workspace_id}/shared")
            return [TextContent(type="text", text=json.dumps(response.json(), indent=2))]

        else:
            return [TextContent(type="text", text=f'{{"error": "Unknown tool: {name}"}}')]

    except httpx.HTTPStatusError as e:
        error_text = f"HTTP Error {e.response.status_code}: {e.response.text}"
        return [TextContent(type="text", text=json.dumps({"error": error_text}, indent=2))]
    except Exception as e:
        error_text = f"Error: {str(e)}"
        return [TextContent(type="text", text=json.dumps({"error": error_text}, indent=2))]


async def main():
    """Main entry point"""
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


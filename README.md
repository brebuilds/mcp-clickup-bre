# ClickUp MCP Server

A comprehensive Model Context Protocol (MCP) server for ClickUp that provides access to all ClickUp API capabilities.

## Features

This MCP server provides comprehensive access to ClickUp's API, including:

- **Workspace Management**: Get workspaces, spaces, folders, lists, and teams
- **Task Management**: Create, update, get, search, and manage tasks
- **Time Tracking**: Start/stop timers, log time entries, get time tracking data
- **Comments & Collaboration**: Add comments, summarize threads, extract action items
- **Goals & Milestones**: Manage goals and milestones
- **Custom Fields**: Get and update custom fields
- **Documents**: Search and manage documents
- **Reporting**: Generate reports and summaries
- **Webhooks**: Manage webhooks
- **Views**: Get and manage views
- **Tags**: Manage tags
- **Task Templates**: Manage task templates
- **Statuses**: Get and manage statuses
- **Members**: Get team members and user information

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your ClickUp API token:
```bash
export CLICKUP_API_TOKEN=your_api_token_here
```

Or create a `.env` file:
```
CLICKUP_API_TOKEN=your_api_token_here
```

## Usage

### Running the Server

Run the MCP server:
```bash
python server.py
```

The server communicates via stdio (standard input/output) as per the MCP protocol.

### Configuration for MCP Clients

#### For Cursor/VS Code

Add to your MCP settings (usually `~/.cursor/mcp.json` or VS Code settings):

```json
{
  "mcpServers": {
    "clickup": {
      "command": "python",
      "args": ["/path/to/mcp-clickup-bre/server.py"],
      "env": {
        "CLICKUP_API_TOKEN": "your_api_token_here"
      }
    }
  }
}
```

#### For Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "clickup": {
      "command": "python",
      "args": ["/path/to/mcp-clickup-bre/server.py"],
      "env": {
        "CLICKUP_API_TOKEN": "your_api_token_here"
      }
    }
  }
}
```

## Configuration

The server uses the ClickUp API token from the `CLICKUP_API_TOKEN` environment variable.

To get your API token:
1. Go to ClickUp Settings (https://app.clickup.com/settings/apps)
2. Navigate to Apps → API
3. Generate or copy your API token

## Available Tools

This server provides **80+ tools** covering all ClickUp API v2 capabilities:

### Workspace & Organization (15 tools)
- `get_authorized_user` - Get authenticated user info
- `get_teams` - Get all teams
- `get_workspaces` - Get all workspaces
- `get_workspace` - Get specific workspace
- `get_spaces` - Get spaces in workspace
- `get_space` - Get specific space
- `create_space` - Create new space
- `update_space` - Update space
- `get_folders` - Get folders in space
- `get_folder` - Get specific folder
- `create_folder` - Create new folder
- `update_folder` - Update folder
- `get_lists` - Get lists in folder/space
- `get_list` - Get specific list
- `create_list` - Create new list
- `update_list` - Update list
- `get_list_members` - Get list members
- `get_list_views` - Get list views

### Task Management (15 tools)
- `get_tasks` - Get tasks with filters
- `get_task` - Get specific task
- `create_task` - Create new task
- `update_task` - Update task
- `search_tasks` - Search tasks across workspace
- `get_task_comments` - Get task comments
- `create_task_comment` - Add comment to task
- `update_task_comment` - Update comment
- `get_task_dependencies` - Get task dependencies
- `create_task_dependency` - Create dependency
- `get_task_time_entries` - Get time entries for task
- `create_task_time_entry` - Log time for task
- `get_task_attachments` - Get task attachments
- `get_task_watchers` - Get task watchers

### Time Tracking (5 tools)
- `get_time_entries` - Get time entries with filters
- `get_time_entry` - Get specific time entry
- `start_time_entry` - Start timer for task
- `stop_time_entry` - Stop running timer
- `update_time_entry` - Update time entry

### Goals & Key Results (6 tools)
- `get_goals` - Get goals for workspace
- `get_goal` - Get specific goal
- `create_goal` - Create new goal
- `update_goal` - Update goal
- `get_goal_key_results` - Get key results
- `create_goal_key_result` - Create key result
- `update_goal_key_result` - Update key result

### Custom Fields (3 tools)
- `get_custom_fields` - Get custom fields for list
- `get_custom_field` - Get specific custom field
- `update_custom_field_value` - Update custom field value

### Views (3 tools)
- `get_views` - Get views for workspace/space
- `get_view` - Get specific view
- `get_view_tasks` - Get tasks from view

### Tags (3 tools)
- `get_tags` - Get tags for workspace
- `create_tag` - Create new tag
- `update_tag` - Update tag

### Statuses (3 tools)
- `get_list_statuses` - Get statuses for list
- `create_list_status` - Create status
- `update_list_status` - Update status

### Webhooks (3 tools)
- `get_webhooks` - Get webhooks for workspace
- `create_webhook` - Create webhook
- `update_webhook` - Update webhook

### Documents (2 tools)
- `search_documents` - Search documents
- `get_document` - Get specific document

### Checklists (4 tools)
- `get_task_checklists` - Get checklists for task
- `create_task_checklist` - Create checklist
- `create_checklist_item` - Create checklist item
- `update_checklist_item` - Update checklist item

### Task Templates (3 tools)
- `get_task_templates` - Get task templates
- `get_task_template` - Get specific template
- `create_task_from_template` - Create task from template

### Members (2 tools)
- `get_team_members` - Get team members
- `get_team_member` - Get specific member

### Shared Hierarchy (1 tool)
- `get_shared_hierarchy` - Get shared hierarchy

## Example Usage

Once connected to an MCP client, you can use natural language commands like:

- "Create a task named 'Fix bug' in list '123456' with high priority"
- "Get all my incomplete tasks due this week"
- "Start a timer for task 'abc123'"
- "Add a comment to task 'xyz789' saying 'This is done'"
- "Get all goals for workspace '123'"
- "Search for tasks containing 'API' in team '456'"

## API Endpoints Covered

This server implements tools for all major ClickUp API v2 endpoints:

- Authentication
- Workspaces
- Spaces
- Folders
- Lists
- Tasks
- Comments
- Goals & Key Results
- Time Tracking
- Custom Fields
- Documents
- Webhooks
- Views
- Tags
- Task Templates
- Statuses
- Teams
- Members
- Checklists
- Dependencies
- Attachments
- Watchers

## License

MIT


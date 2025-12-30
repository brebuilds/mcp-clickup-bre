# ClickUp MCP Server

A comprehensive Model Context Protocol (MCP) server for ClickUp that provides **limitless** access to all ClickUp API capabilities with advanced features.

## Features

This MCP server provides comprehensive access to ClickUp's API, including:

### Core Features
- **Workspace Management**: Get workspaces, spaces, folders, lists, and teams with full CRUD operations
- **Task Management**: Create, update, get, search, delete, and manage tasks with dependencies
- **Time Tracking**: Start/stop timers, log time entries, get time tracking data and reports
- **Comments & Collaboration**: Add, update, delete comments, summarize threads, extract action items
- **Goals & Key Results**: Full CRUD for goals and key results (OKRs)
- **Custom Fields**: Create, update, delete, and manage custom fields with granular control
- **Documents**: Create, update, delete documents with rich formatting and embeds
- **Webhooks**: Full webhook management for real-time event notifications
- **Views**: Get and manage views across workspaces and spaces
- **Tags**: Create, update, and manage tags
- **Task Templates**: Create, update, delete, and apply task templates
- **Statuses**: Get and manage custom statuses
- **Members**: Get team members and user information

### Advanced Features
- **🚀 Bulk Operations**: Batch create, update, and delete hundreds of tasks efficiently
- **⚡ Automation Rules**: Create and manage ClickUp's native automation workflows via API
- **📊 Dashboard & Analytics**: Pull workspace, space, and task analytics data
- **📈 Time Tracking Reports**: Generate comprehensive time tracking reports
- **🔔 Real-time Triggers**: Complete webhook support for event-driven workflows
- **🎨 Advanced Document Operations**: Rich text formatting, embeds, and nested pages
- **🔧 Advanced Custom Fields**: Full control over custom field types and configurations
- **🗑️ Complete CRUD Operations**: Delete any entity (spaces, folders, lists, tasks, comments, goals, etc.)

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

This server provides **140+ tools** covering all ClickUp API v2 capabilities with advanced features:

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

### Custom Fields (7 tools)
- `get_custom_fields` - Get custom fields for list
- `get_custom_field` - Get specific custom field
- `update_custom_field_value` - Update custom field value
- `create_custom_field` - Create new custom field with type config
- `delete_custom_field` - Delete a custom field
- `remove_custom_field_value` - Remove custom field value from task

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

### Webhooks (4 tools)
- `get_webhooks` - Get webhooks for workspace
- `create_webhook` - Create webhook with event filters
- `update_webhook` - Update webhook configuration
- `delete_webhook` - Delete webhook

### Documents (6 tools)
- `search_documents` - Search documents in workspace
- `get_document` - Get specific document
- `create_document` - Create new document with rich formatting
- `update_document` - Update document with formatting and embeds
- `delete_document` - Delete a document
- `create_document_page` - Create nested page in document

### Checklists (4 tools)
- `get_task_checklists` - Get checklists for task
- `create_task_checklist` - Create checklist
- `create_checklist_item` - Create checklist item
- `update_checklist_item` - Update checklist item

### Task Templates (6 tools)
- `get_task_templates` - Get task templates for workspace
- `get_task_template` - Get specific template
- `create_task_from_template` - Create task from template
- `create_task_template` - Create new task template
- `update_task_template` - Update task template
- `delete_task_template` - Delete task template

### Members (2 tools)
- `get_team_members` - Get team members
- `get_team_member` - Get specific member

### Shared Hierarchy (1 tool)
- `get_shared_hierarchy` - Get shared hierarchy for workspace

### 🚀 Bulk Operations (3 tools)
- `bulk_create_tasks` - Batch create multiple tasks efficiently
- `bulk_update_tasks` - Batch update multiple tasks in one call
- `bulk_delete_tasks` - Batch delete multiple tasks

### ⚡ Automation Rules (5 tools)
- `get_automations` - Get automation rules for workspace
- `get_automation` - Get specific automation rule
- `create_automation` - Create new automation with triggers and actions
- `update_automation` - Update automation configuration
- `delete_automation` - Delete automation rule

### 🗑️ Delete Operations (7 tools)
- `delete_space` - Delete a space
- `delete_folder` - Delete a folder
- `delete_list` - Delete a list
- `delete_task` - Delete a task
- `delete_comment` - Delete a comment
- `delete_goal` - Delete a goal
- `delete_key_result` - Delete a key result

### 📊 Dashboard & Analytics (4 tools)
- `get_workspace_dashboard` - Get dashboard data for workspace
- `get_space_dashboard` - Get dashboard data for space
- `get_task_analytics` - Get analytics data for tasks
- `get_time_tracking_report` - Get comprehensive time tracking reports

## Example Usage

Once connected to an MCP client, you can use natural language commands like:

### Basic Operations
- "Create a task named 'Fix bug' in list '123456' with high priority"
- "Get all my incomplete tasks due this week"
- "Start a timer for task 'abc123'"
- "Add a comment to task 'xyz789' saying 'This is done'"
- "Get all goals for workspace '123'"
- "Search for tasks containing 'API' in team '456'"

### Advanced Features
- "Bulk create 50 tasks from this JSON array in list '123456'"
- "Create an automation that assigns tasks to me when they're moved to 'In Progress'"
- "Get the workspace dashboard analytics for the last 30 days"
- "Create a custom dropdown field named 'Department' with options Sales, Engineering, Marketing"
- "Create a webhook that notifies my n8n workflow when tasks are updated"
- "Generate a time tracking report for team '456' for this month"
- "Create a document with rich formatting and embedded images"
- "Delete all tasks in this array using bulk operations"

## API Endpoints Covered

This server implements tools for all major ClickUp API v2 endpoints:

### Core Endpoints
- Authentication & Authorization
- Workspaces & Teams
- Spaces (CRUD)
- Folders (CRUD)
- Lists (CRUD)
- Tasks (Full CRUD with dependencies)
- Comments (CRUD)
- Goals & Key Results (CRUD)
- Time Tracking & Reports
- Custom Fields (CRUD)
- Documents (CRUD with formatting)
- Webhooks (CRUD)
- Views & Dashboards
- Tags
- Task Templates (CRUD)
- Statuses
- Members
- Checklists
- Dependencies
- Attachments
- Watchers

### Advanced Endpoints
- Automation Rules (CRUD)
- Bulk Operations (Tasks)
- Dashboard Analytics
- Time Tracking Reports
- Document Pages
- Custom Field Management

## License

MIT


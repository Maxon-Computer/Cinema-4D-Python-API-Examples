# Description: MCP Adapter

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/mxn_plugins/mcp_adapter/res/description/mcpadapterprefs.res`
- **Symbol:** `mcpadapterprefs`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enable MCP Server | MCPADAPTERPREFS_ENABLED | BOOL |  |  |  | 
Host | MCPADAPTERPREFS_HOST | STRING |  |  |  | 
Port | MCPADAPTERPREFS_PORT | LONG | 1 | 65535 |  | 
Auth Token | MCPADAPTERPREFS_TOKEN | STRING |  |  |  | 
Request Timeout (s) | MCPADAPTERPREFS_REQUEST_TIMEOUT | REAL | 0.1 |  |  | 
Enable exec_python Command | MCPADAPTERPREFS_ENABLE_EXEC_PYTHON | BOOL |  |  |  | 
Enable Python-Bearing Operations | MCPADAPTERPREFS_ENABLE_PYTHON_OPS | BOOL |  |  |  | 
MCP Client | MCPADAPTERPREFS_CLIENT | LONG |  |  |  | MCPADAPTERPREFS_CLIENT_CLAUDE_DESKTOP; MCPADAPTERPREFS_CLIENT_CLAUDE_CODE; MCPADAPTERPREFS_CLIENT_VSCODE; MCPADAPTERPREFS_CLIENT_COPILOT_CLI; MCPADAPTERPREFS_CLIENT_CURSOR; MCPADAPTERPREFS_CLIENT_WINDSURF; MCPADAPTERPREFS_CLIENT_CODEX; MCPADAPTERPREFS_CLIENT_LMSTUDIO; MCPADAPTERPREFS_CLIENT_KIMI
Update Selected Client Config | MCPADAPTERPREFS_UPDATE_CLIENT | BUTTON |  |  |  | 
Client restart | MCPADAPTERPREFS_RESTART_HINT | STATICTEXT |  |  |  | 
Basics | MCPADAPTERPREFS_TOOLSET_BASICS | BOOL |  |  |  | 
Entities | MCPADAPTERPREFS_TOOLSET_ENTITIES | BOOL |  |  |  | 
Document | MCPADAPTERPREFS_TOOLSET_DOCUMENT | BOOL |  |  |  | 
Shot Setup | MCPADAPTERPREFS_TOOLSET_SHOT_SETUP | BOOL |  |  |  | 
Transforms | MCPADAPTERPREFS_TOOLSET_TRANSFORMS | BOOL |  |  |  | 
Selection | MCPADAPTERPREFS_TOOLSET_SELECTION | BOOL |  |  |  | 
Hierarchy | MCPADAPTERPREFS_TOOLSET_HIERARCHY | BOOL |  |  |  | 
System | MCPADAPTERPREFS_TOOLSET_SYSTEM | BOOL |  |  |  | 
Modeling | MCPADAPTERPREFS_TOOLSET_MODELING | BOOL |  |  |  | 
User Data | MCPADAPTERPREFS_TOOLSET_USER_DATA | BOOL |  |  |  | 
Animation | MCPADAPTERPREFS_TOOLSET_ANIMATION | BOOL |  |  |  | 
Node Graphs | MCPADAPTERPREFS_TOOLSET_NODE_GRAPHS | BOOL |  |  |  | 
MoGraph | MCPADAPTERPREFS_TOOLSET_MOGRAPH | BOOL |  |  |  | 
Layers | MCPADAPTERPREFS_TOOLSET_LAYERS | BOOL |  |  |  | 
Assets | MCPADAPTERPREFS_TOOLSET_ASSETS | BOOL |  |  |  | 
Allow Remote Connections | MCPADAPTERPREFS_ALLOW_REMOTE | BOOL |  |  |  | 
Allowed IPs | MCPADAPTERPREFS_ALLOWED_IPS | STRING |  |  |  | 
Browser Client Origins | MCPADAPTERPREFS_BROWSER_ORIGINS | STRING |  |  |  | 
Log Incoming Calls | MCPADAPTERPREFS_ENABLE_LOGGING | BOOL |  |  |  | 
Show Rejected Calls in Console | MCPADAPTERPREFS_CONSOLE_REJECTIONS | BOOL |  |  |  | 

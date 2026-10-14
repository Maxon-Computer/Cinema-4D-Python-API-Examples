# Description: Team Render

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/teamrender/description/netprefs.res`
- **Symbol:** `Netprefs`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Team Render | PREF_ENABLETEAMRENDER | BOOL |  |  |  | 
No label | PREF_SEP_1 | SEPARATOR |  |  |  | 
Computer Name | PREF_NAME | STRING |  |  |  | 
Security Token | PREF_SECURITYTOKEN | STRING |  |  |  | 
Port | PREF_SERVICEPORTNUMBER | STRING |  |  |  | 
Webserver Port | PREF_WEBSERVERPORT | STRING |  |  |  | 
Enable User Management | PREF_USERMANAGEMENTENABLED | BOOL |  |  |  | 
Announce Service via Bonjour | PREF_USEBONJOUR | BOOL |  |  |  | 
Announce Service to Local Network | PREF_USEDISCOVERY | BOOL |  |  |  | 
Local Settings | PREF_SEP_LOCAL | SEPARATOR |  |  |  | 
Share Machine over Network | PREF_SHARE | BOOL |  |  |  | 
Custom Render Threads | PREF_THREADCUSTOM | BOOL |  |  |  | 
No label | PREF_RENDERTHREADS | LONG | 1 | 256 |  | 
Abort Rendering on Client Error | PREF_ABORTRENDERINGONCLIENTERROR | BOOL |  |  |  | 
Always Fetch Assets from Server | PREF_FETCHASSETSALWAYSFROMSERVER | BOOL |  |  |  | 
Keep B3D files after assembling | PREF_KEEPB3DFILESAFTERASSEMBLING | BOOL |  |  |  | 
Wake-On-Lan for Offline Machines | PREF_WAKEONLANFOROFFLINEMACHINES | BOOL |  |  |  | 
Restart Jobs after Unexpected Server Termination | PREF_RESTARTJOBSAFTERUNEXPECTEDSERVERTERMINATION | BOOL |  |  |  | 
Rendering Timeout (Seconds) | PREF_ENABLERENDERINGTIMEOUT | BOOL |  |  |  | 
No label | PREF_RENDERINGTIMEOUT | LONG | 30 |  |  | 
Exclude Client on Out of Memory | PREF_STOPJOBONSWAPPINGENABLED | BOOL |  |  |  | 
Auto | PREF_STOPJOBONSWAPPINGAUTO | BOOL |  |  |  | 
Memory (GB) | PREF_STOPJOBONSWAPPINGVALUE | LONG | 1 |  |  | 
Client Settings | PREF_SEP_CLIENT | SEPARATOR |  |  |  | 
Encrypt Connections | PREF_USEENCRYPTION | BOOL |  |  |  | 
Clients Get Assets on Demand | PREF_REQUESTONDEMAND | BOOL |  |  |  | 
Handle Warning As Error | PREF_HANDLEWARNINGASERROR | BOOL |  |  |  | 
Exclude Client on Loading Error | PREF_EXCLUDECLIENTONLOADINGERROR | BOOL |  |  |  | 
No label | PREF_SEP_2 | SEPARATOR |  |  |  | 
Peer-To-Peer Asset Distribution | PREF_PEERTOPEERASSETDISTRIBUTION | BOOL |  |  |  | 
Download Assets in Parts | PREF_DOWNLOADASSETINPARTS | BOOL |  |  |  | 
Asset Chunk Size (MB) | PREF_ASSETCHUNKSIZE | LONG | 2 | 256 |  | 
Paths | PREF_SEP_PATHS | SEPARATOR |  |  |  | 
Local Repository Folder | PREF_SERVICEREPOSITORYPATH | FILENAME |  |  |  | 

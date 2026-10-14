# Node Template: Import Data

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.importer.database.parser`
- **Template Name:** `Import Data`

## Attributes

See `.agents/nodes.md` for an overview of Nodes API skills. Not all attributes and ports have a min, max, or default value. Enum values are listed in the form label = value, labe = value, label = value. I.e., if a user asks you to set the an enum attribute or port to "Foo" (citing an UI label), you must search for the label "Foo" in the enum values and use the corresponding value in your code. If a user asks you to set an attribute or port to a value that is not listed in the enum values, you must respond with an error message.

Name | ID  | Data Type | Parameter Type | isVariadic | isNested | isEnum | Min Value | Max Value | Default Value | Enum Values
---- | --- | --------- | -------------- | ---------- | -------- | ------ | --------- | --------- | ------------- | -----------
Basic/Asset Version | net.maxon.node.base.assetversion | maxon::Id | Attribute | false | false | true |  |  |  | Latest = latest
Basic/Color | net.maxon.node.base.color | maxon::Color | Attribute | false | false | false |  |  |  | 
Basic/Comment | net.maxon.node.base.comment | maxon::String | Attribute | false | false | false |  |  |  | 
Basic/Display Comment | net.maxon.node.base.displaycomment | maxon::Bool | Attribute | false | false | false |  |  |  | 
Basic/Name | net.maxon.node.base.name | maxon::String | Attribute | false | false | false |  |  |  | 
Basic/Ports Display | net.maxon.node.base.portdisplay | maxon::Id | Attribute | false | false | true |  |  | all | Collapsed = none, Connected = connected, Expanded = all
Basic/Show Preview | net.maxon.node.base.displaypreview | maxon::Bool | Attribute | false | false | false |  |  | true | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
db  csv  json  spreadsheet   table   import | net.maxon.object.base.tags |  | Attribute | false | false | false |  |  |  | 
File Type Cache | <filetypecachein | maxon::Id | Input | false | false | true |  |  | Unsupported | Unsupported = Unsupported, CSV = CSV
Filtering/Data Type  | <databasedatatypein | maxon::DataType | Input | false | false | false |  |  |  | 
Inputs/Main Group/Data Set  | <datasetnumberin | maxon::Int | Input | false | false | false | 1 |  | 1 | 
Inputs/Main Group/File Group/File (*.csv) | <databaseurlin | maxon::Url | Input | false | false | false |  |  |  | 
Inputs/Main Group/Mode | <datasetmodein | maxon::Id | Input | false | false | true |  |  | AllDataSets | All Data Sets = AllDataSets, Single Data Set = SingleDataSet
Inputs/Main Group/Settings/Delimiter | <delimiterin | maxon::String | Input | false | false | false |  |  | ; | 
Inputs/Main Group/Settings/Delimiter Mode | <delimitermodein | maxon::Id | Input | false | false | true |  |  | Auto | Auto = Auto, Tab = Tab, Comma = Comma, Custom = Custom, Semicolon = Semicolon, Colon = Colon, Space = Space
Inputs/Main Group/Settings/Double Quotes | <doublequotein | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Main Group/Settings/First Row as Header | <firstrowasheaderin | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Main Group/Settings/Hashtag as Comment | <hashtagascommentin | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Main Group/Settings/Row Limit | <rowlimitin | maxon::Int64 | Input | false | false | false | 0 | 0 | 0 | 
Outputs/Collection | >databasedataout |   | Output | false | false | false |  |  |  | 
Outputs/Headers | >headersout | maxon::Array<maxon::String> | Output | false | false | false |  |  |  | 


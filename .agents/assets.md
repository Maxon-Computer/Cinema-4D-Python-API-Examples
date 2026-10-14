# Assets Documentation

Cinema 4D serves reusable content, such as objects, materials, scenes, textures and node templates, as *assets* in the Asset Browser. This document describes the high level concepts of the Asset API (`maxon.Asset*` types and the `asset.framework`) and the rules for using it from Python. For current API details, start at <https://developers.maxon.net/docs/py> and search for `Assets manual` or `Asset API`; also consult the asset examples of the SDK.

# TOC

- [Concepts](#concepts): Describes asset databases, repositories, asset types, identifiers and metadata.
- [Rules](#rules): Hard rules for writing asset code.
- [Recipes](#recipes): Short patterns for the most common tasks.
- [Examples](#examples): Runnable examples for the Asset API and related file and texture topics.

# Concepts

- **Asset**: A piece of content with metadata, e.g., a scene, object, material, media file, preset, category, keyword or node template. An asset is stored in an asset database and identified by an asset id (`maxon.Id`).
- **Asset Database**: A directory (plus the metadata Cinema 4D creates in it) that stores assets. Databases are mounted with `maxon.AssetDataBasesInterface`. A `maxon.AssetDatabaseStruct` is only a surrogate for a database, it holds the URL, the active state and two minor flags, but no assets.
- **Asset Repository** (`maxon.AssetRepositoryRef`): The access point for reading, searching and writing assets. Repositories can be composed of other repositories, called bases. The important repositories are:
  - `maxon.AssetInterface.GetUserPrefsRepository()`: Writable. Contains the application repository, the databases shipped with Cinema 4D, and all user databases. This is the default repository for searching, loading and storing assets.
  - `maxon.AssetInterface.GetApplicationRepository()`: Not writable. Contains the atomic assets of the application, e.g., node templates.
  - `doc.GetSceneRepository(True)`: The repository bound to a document. Passing `True` creates it when it does not exist yet.
  - `maxon.AssetInterface.CreateRepositoryFromUrl(...)`: A repository for a specific database. Only worth it to limit the search space of heavy operations, it can also create a new database at an empty location.
- **Asset Description** (`maxon.AssetDescription`): The handle of an asset in a repository. It provides the id (`GetId()`), type id (`GetTypeId()`), version (`GetVersion()`), repository, metadata (`GetMetaData()`), and the URL of the primary data (`GetUrl()`). It is the object that search functions return and that most operations take. `Load()` returns the asset interface (e.g., cast with `maxon.Cast(maxon.FileAsset, asset)`), which is rarely needed.
- **Asset Types** (`maxon.AssetTypes`):
  - `File`: The type behind most content. Its *subtype* (`maxon.ASSETMETADATA.SubType`) tells what it holds: object, material, scene, media image or media movie. A file asset with the empty subtype is an arbitrary file, e.g., a PDF, and gets no preview and no special load behavior.
  - `Category`: The folders of the Asset Browser. A category is an asset itself and each asset references exactly one parent category.
  - `Keyword`: A tag-like grouping. A keyword is an asset itself and an asset can reference many.
  - Node templates: The definitions of node types for the Nodes API. They cannot be created with the Python API, but can be loaded.
- **Asset Ids**: Unique within a repository (without its bases). `maxon.AssetInterface.MakeUuid("object", False)` creates a UUID based id, the prefix is by convention the lowercase asset type. UUID ids differ on each run. When an id must be reproducible, hash identifying properties yourself (e.g., with `hashlib.md5`) and use the prefix separator `_` (`"category_" + hash`). UUID ids use `@` as the separator. Human readable ids use the inverted domain pattern, e.g., `net.maxon.assetcategory.uncategorized`.
- **Versions**: Several assets can share an id and differ in their version string. The Asset Browser shows them as one asset, and loads the latest version by default. A version is stored under the same id as the asset it shadows (`assetDescription.GetId()`) with a new version string.
- **Metadata** (`maxon.AssetMetaData`): The descriptive data of an asset, e.g., name (`maxon.OBJECT.BASE.NAME`), annotation (`maxon.OBJECT.BASE.ANNOTATIONS`), category (`maxon.ASSETMETADATA.Category`), keywords, subtype, time stamp, and meta properties such as point counts (`maxon.ASSET.METAPROPERTIES`).
- **Node Templates and Nodes**: The node types of material and scene node graphs are node template assets. As an agent you rarely interact with them directly, `.agents/nodespaces/_overview.md` already lists the node types. See `.agents/nodes.md` for node graphs.

# Rules

- IMPORTANT: Built-in assets are read-only. To change one, copy it first with `repository.CopyAsset(newId, sourceDescription)` and edit the copy. Never try to erase or rewrite assets that ship with Cinema 4D.
- IMPORTANT: Never erase an asset without a clear request from the user, and only erase assets the user created.
- Use the user preferences repository unless there is a reason not to.
- Call `maxon.AssetDataBasesInterface.WaitForDatabaseLoading()` before operating on databases, and abort when it returns `False`.
- The Maxon API does not return error codes, it raises exceptions. Do not check the result of `StoreAsset`, `CopyAsset` and similar calls for `None`. Use `try`/`except` when special error handling is required.
- The Maxon API only deals with `maxon.Url`. Wrap file paths: `maxon.Url("file://C:/Users/username/Documents/scene.c4d")` or `maxon.Url(path)`. Write paths out as literals (see the rules in `AGENTS.md`).
- Search with `repository.FindAssets(typeId, assetId, version, mode, receiver)`. An empty `maxon.Id()` widens the search for that qualifier. `maxon.ASSET_FIND_MODE.LATEST` returns only the latest version of each asset, `ALL` returns all versions. Use `FindLatestAsset` for a single known id.
  - The receiver is either a list, or a callback `Callback(assetDescription) -> bool`. Returning `False` stops the search.
  - An inner function cannot reassign variables of its enclosing function. Wrap values that a callback changes in a mutable object, e.g., `data: dict = {"count": 5}` and `data["count"] -= 1`.
  - Asset descriptions passed to a callback are the real descriptions: `StoreMetaString` on them writes through.
- Write metadata through the asset description, not through the `AssetMetaData` object, which is read-only: `assetDescription.StoreMetaString(maxon.OBJECT.BASE.NAME, name, language)`. Get the language with `maxon.Resource.GetCurrentLanguage()`. Use the convenience functions `maxon.CategoryAssetInterface.SetAssetCategory` and `maxon.KeywordAssetInterface.AddKeyword` for categories and keywords.
- Prefer the convenience functions of `maxon.AssetCreationInterface` (`CreateObjectAsset`, `CreateMaterialAsset`, `CreateSceneAsset`, `SaveTextureAsset`, `SaveMemFileAsAssetWithCopyAsset`) to the atomic `repository.StoreAsset`. `StoreAsset` is only needed for categories, keywords and custom asset types.
- Store assets under the correct subtype, only file types with no special support should be stored as plain file assets.
- The category of a new asset is a category id, `maxon.Id("net.maxon.assetcategory.uncategorized")` is the safe default.
- Call `c4d.EventAdd()` at the end of a script that changed the scene or assets.
- The asset id of a user created asset is shown with the `#` button in the info area of the Asset Browser. Never invent ids of built-in assets, take them from the user, from the examples, or look them up by name with a search.
- Creating assets requires a running Cinema 4D (Script Manager or plugin). Scripts that fetch assets of the built-in library need an internet connection when the assets are not cached yet.

# Recipes

The `ShowAssetInBrowser` helper below is used by the examples to reveal a new asset, use it when the user wants to see the result:

```python
CID_ASSET_BROWSER: int = 1054225

def ShowAssetInBrowser(asset: maxon.AssetDescription) -> None:
    """Opens the Asset Browser and reveals #asset in it.
    """
    if not c4d.IsCommandChecked(CID_ASSET_BROWSER):
        c4d.CallCommand(CID_ASSET_BROWSER)

    maxon.AssetManagerInterface.RevealAsset([asset])
```

## Store an object as an asset

```python
repository: maxon.AssetRepositoryRef = maxon.AssetInterface.GetUserPrefsRepository()
assetId: maxon.Id = maxon.AssetInterface.MakeUuid("object", False)
storeAssetStruct: maxon.StoreAssetStruct = maxon.StoreAssetStruct(
    maxon.Id("net.maxon.assetcategory.uncategorized"), repository, repository)

# The object is stored with its children, tags, materials and shaders.
assetDescription: maxon.AssetDescription = maxon.AssetCreationInterface.CreateObjectAsset(
    op, doc, storeAssetStruct, assetId, "My Object", "1.0", maxon.AssetMetaData(), True)
```

`CreateMaterialAsset(doc, mat, storeAssetStruct, assetId, name, version, metadata, True)` and `CreateSceneAsset(doc, storeAssetStruct, assetId, name, version, metadata, True)` work the same way. A texture file becomes a media asset with `maxon.AssetCreationInterface.SaveTextureAsset(url, name, storeAssetStruct, (), True)`, which returns a tuple of the asset description and a bool.

## Find assets

```python
repository: maxon.AssetRepositoryRef = maxon.AssetInterface.GetUserPrefsRepository()

# Simple: All category assets, latest version only.
categories: list[maxon.AssetDescription] = repository.FindAssets(
    maxon.AssetTypes.Category().GetId(), maxon.Id(), maxon.Id(), maxon.ASSET_FIND_MODE.LATEST)

# A single known asset.
assetDescription: maxon.AssetDescription = repository.FindLatestAsset(
    maxon.AssetTypes.File(), maxon.Id("file_d0a26639c950371a"), maxon.Id(), maxon.ASSET_FIND_MODE.LATEST)
```

For metadata based filtering pass a callback as the receiver, see `AdvancedAssetSearch()` in [asset_databases.py](../examples/io/asset_databases.py) and `LinkMediaAssets()` in [asset_types.py](../examples/io/asset_types.py).

## Read and write metadata

```python
language: str = maxon.Resource.GetCurrentLanguage()
name: str = assetDescription.GetMetaString(maxon.OBJECT.BASE.NAME, language, "")
subtype: maxon.Id = assetDescription.GetMetaData().Get(maxon.ASSETMETADATA.SubType)

# Writing is done on the description, and only on assets in writable repositories.
assetDescription.StoreMetaString(maxon.OBJECT.BASE.NAME, "New Name", language)
```

## Load assets into the active document

```python
# Loads file assets (objects, materials, scenes) into the active document.
repository: maxon.AssetRepositoryRef = maxon.AssetInterface.GetUserPrefsRepository()
assetsToLoad: list[tuple[maxon.Id, str]] = [(maxon.Id("file_d0a26639c950371a"), "")]
if not maxon.AssetManagerInterface.LoadAssets(repository, assetsToLoad):
    raise RuntimeError(f"Could not load assets for the ids: {assetsToLoad}")
```

`LoadAssets` always targets the active document. To load into another document, load the asset manually via its URL. Node templates are loaded into a graph by passing `graphModelRef=` (see `LoadAssets()` in [asset_types.py](../examples/io/asset_types.py)).

## Use a media asset as a texture

The URL of a media asset can be used directly to access its content:

```python
url: maxon.Url = assetDescription.GetUrl()
shader[c4d.BITMAPSHADER_FILENAME] = str(url)
```

## Mount a folder as an asset database

```python
databases = maxon.AssetDataBasesInterface.GetDatabases()
databases.append(maxon.AssetDatabaseStruct(maxon.Url("file://D:/assets")))
# Always set the whole collection, otherwise all other databases are unmounted.
maxon.AssetDataBasesInterface.SetDatabases(databases)
```

Check whether the database is already mounted first, see `MountAssetDatabase()` in [asset_databases.py](../examples/io/asset_databases.py).

# Examples

- [Asset Databases](../examples/io/asset_databases.py): Mounting and unmounting databases, repositories, storing, copying, erasing, searching and sorting assets.
- [Asset Types](../examples/io/asset_types.py): Creating object, material, scene, media, file, category and keyword assets, linking media assets in materials, and loading assets.
- [Asset Metadata](../examples/io/asset_metadata.py): Reading and writing metadata, asset versions, and generating asset identifiers.
- [Texture Paths](../examples/io/texture_paths.py): Getting and setting the global texture paths.
- [Import and Export](../examples/io/README.md): Importing and exporting files such as OBJ, Alembic, STEP and SketchUp, and handling images and memory files.

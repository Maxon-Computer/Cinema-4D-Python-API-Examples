# MessageData Scaffold

Scaffolds a Cinema 4D message plugin (`c4d.plugins.MessageData`) that receives application-wide core messages. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds.

Folder prefix: `py_msc_`. Registered with: `c4d.plugins.RegisterMessagePlugin` (with an *instance*). The scaffold needs no resource files.

# Questions

Ask the common questions (`name`, `description`, `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `messages` | Which messages should the plugin handle? (multi select) | `Custom message` (sent by your own code with `c4d.SpecialEventAdd`, uses the plugin ID as the message ID), `Scene changes` (`c4d.EVMSG_CHANGE`, sent very often) | `Custom message` |

# Files

```text
projects/{{Folder}}/
└── {{Folder}}.pyp
```

# Templates

## {{Folder}}.pyp

```python
"""{{Description}}

To run this plugin, add its folder to the plugin paths of Cinema 4D and restart Cinema 4D. The
messages are received automatically, there is nothing to execute.

Topics:
    - Receiving core messages with MessageData.CoreMessage()
    - Registering a message plugin
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d

PLUGIN_ID: int = {{PluginId}}


class {{ClassName}}Message(c4d.plugins.MessageData):
    """Implements the {{Name}} message plugin.
    """

    def CoreMessage(self, id: int, bc: c4d.BaseContainer) -> bool:
        """Called by Cinema 4D for every core message, usually on the main thread.
        """
        <Branches>

        return True


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    # Message plugins are registered with an instance which lives for the whole session.
    c4d.plugins.RegisterMessagePlugin(
        id=PLUGIN_ID, str="{{Name}}", info=0, dat={{ClassName}}Message())
```

`<Branches>` per selected message, in this order:

```python
        # The plugin ID doubles as the ID of the custom message, send it with
        # c4d.SpecialEventAdd(PLUGIN_ID). Never assume the main thread, guard main thread work.
        if id == PLUGIN_ID and c4d.threading.GeIsMainThreadAndNoDrawThread():
            print("{{Name}} received its custom message.")
```

```python
        # Sent after every change of the scene, so keep the work in here cheap.
        if id == c4d.EVMSG_CHANGE and c4d.threading.GeIsMainThreadAndNoDrawThread():
            print("The scene has changed.")
```

# After Scaffolding

- Show how to send the custom message from other code, e.g., a script or a callback: `c4d.SpecialEventAdd(<the plugin ID>)`. A core message only carries two integers. Larger data must go through a lock protected global storage, see the *Deferring Workloads* pattern in `.agents/scene.md`. This is also the way to hand work from a threaded callback to the main thread.
- Mention that `Scene changes` fires constantly, and that the generated `print` must be replaced by real logic or removed.
- Mention that a message plugin has no interface and no menu entry.

# References

- For current API details, start at <https://developers.maxon.net/docs/py> and search for `Message System`.
- For deferring workloads, search the current docs for `Scene Execution` and `Deferring Workloads`.

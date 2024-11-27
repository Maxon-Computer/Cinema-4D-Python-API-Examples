# Cinema 4D Python API Examples 

Contains the official code examples for the Cinema 4D Python API.

The provided code examples are identical to the ones shipped with the [Cinema 4D Python SDK](https://developers.maxon.net/downloads/). See our [Cinema 4D Python API Documentation](https://developers.maxon.net/docs/py) for written manuals and an API index.

To get started with the Cinema 4D Python API, we recommend reading the [Getting Started](https://developers.maxon.net/docs/py/2025_0_0/manuals/manual_py_in_c4d.html) manual. We also recommend visiting and registering at [developers.maxon.net](https://developers.maxon.net/) to be able to generate plugin identifiers and to participate in our [developer forum](https://developers.maxon.net/forum/).

## Content

| Directory | Description |
| :- | :- |
| plugins | Provides examples for the plugin hooks of the Python API such as implementing an object or tag plugin. This approach requires the most work but also provides the most freedoms. |
| scenes | Provides examples for the so called scripting elements (see *Getting Started* guide from above). Scripting elements are miniature versions of the plugin hooks which can be directly implemented within a seen. They offer less freedoms but are less work intensive and a great way to learn the Python API. |
| scripts | Provides examples for scripts that can be executed in the Script Manager of Cinema 4D. This is the least complex way to write Python code in Cinema 4D and comparable to a traditional Python script. But Script Manager scripts can make use of the full depth of the Python API and these examples cover therefore a wide range of generic subjects. When you want to 'get to know' the API, these scripts are a great learning source. |


# rendering

Rendering, materials, shaders, textures, and render settings.

## Files
| File | Description |
| --- | --- |
| [README.md](README.md) | This file. |
| [_c4d_renderdata.py](_c4d_renderdata.py) | No short description provided. |
| [batch_render_postprocess.py](batch_render_postprocess.py) | Demonstrates to manipulate the file outputs of a batch render post process once the rendering has finished. |
| [batch_render_preprocess.py](batch_render_preprocess.py) | Demonstrates how to pre-process multiple documents before adding them to the batch renderer for rendering. |
| [ocio.py](ocio.py) | Demonstrates how to read, write, and convert colors in an OpenColorIO (OCIO) color-managed document in Cinema 4D. |
| [render_complex.py](render_complex.py) | Demonstrates the details and manual handling of a programmatic rendering process. |
| [render_hardware.py](render_hardware.py) | Demonstrates how carry out a 'hardware preview' rendering, i.e., a rendering of what is shown in the viewport using the hardware renderer. |
| [render_openexr.py](render_openexr.py) | Configures OpenEXR output render format with SetImageSettingsDictionary() then reads these with GetImageSettingsDictionary(). |
| [render_preroll.py](render_preroll.py) | Demonstrates how to render document from or at a given frame after prerolling it. |
| [render_set_engine.py](render_set_engine.py) | Demonstrates how to manipulate the render settings of a rendering, specifically also the used render engine. |
| [render_simple.py](render_simple.py) | Demonstrates a simple way to programmatically render a document to either memory or disk. |
| [render_tiles.py](render_tiles.py) | Demonstrates how to render a document split into tiles which can be composited back together to a full image. |
| [render_token.py](render_token.py) | Renders a BaseDocument and saves the resulting image using a filename handling tokens. |

## Related Examples

| Type | Example | Description |
| --- | --- | --- |
| Script | [asset_types](../io/asset_types.py) | Provides examples for creating and loading different asset types. |
| Script | [graph_descriptions_basics](../nodes/graph_descriptions_basics.py) | Demonstrates how graph descriptions create and modify node graphs. |

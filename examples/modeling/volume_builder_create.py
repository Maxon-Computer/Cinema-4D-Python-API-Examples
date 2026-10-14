"""Creates a volume builder and inserts it into the active document.

Topics:
    * c4d.modules.volume.VolumeBuilder
    * BaseDocument.InsertObject()
"""
__author__ = "Maxime Adam"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "R20"

import c4d


def main():
    # Creates a volume builder object
    volumeBuilder = c4d.modules.volume.VolumeBuilder()
    if volumeBuilder is None:
        raise MemoryError("Failed to create a volume builder.")

    # Inserts it in the scene
    doc.InsertObject(volumeBuilder, None, None)

    # Pushes an update event to Cinema 4D
    c4d.EventAdd()


if __name__ == '__main__':
    main()

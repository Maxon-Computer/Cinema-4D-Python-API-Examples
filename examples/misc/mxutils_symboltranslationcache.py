"""Demonstrates translating Cinema 4D symbols with SymbolTranslationCache.

Run this example in the Cinema 4D Script Manager. The cache discovers names for integer symbols 
exposed by the c4d module.

Topics:
    * mxutils.SymbolTranslationCache
    * Cinema 4D symbols
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0"

import c4d
import mxutils

def main() -> None:
    """Looks up selected object and data type symbols.
    """
    # A symbol cache is just a class that caches the attribute names of integer attributes in an 
    # object and is meant to be used on modules. For the Cinema module there is global pre-built 
    # cache available as mxutils.g_c4d_symbol_translation_cache. You should normally avoid rebuilding
    # such caches (as they are somewhat expensive to build) but for the sake of this example we will 
    # build a new cache for the c4d module.

    myCache: mxutils.SymbolTranslationCache = mxutils.SymbolTranslationCache(c4d, buildDirectly=True)

    # Two symbol IDs, which we would normally encounter somewhere in the API, for example we call 
    # GetType() on a BaseObject and it returns an integer, or we get a message ID from a message 
    # callback. We can use the cache to translate these IDs into their symbol names, which makes it
    # then easier to understand what is happening when debugging your code.

    cubeId: int = 5159 # The ID of c4d.Ocube
    editMsgID: int = 21 # The ID of c4d.MSG_EDIT

    # There are two ways to do this, __getitem__ and Get().

    # __getitem__ returns all symbols that are associated with the given ID. For things like object, 
    # tag, material, etc type IDs, this will be enough, as they are 'usually' unique. For message IDs, 
    # there is a high chance that multiple symbols are associated with the same ID, so you will get a 
    # list of all of them.
    cubeCandidates: list[str] | None = myCache[cubeId]
    editCandidates: list[str] | None = myCache[editMsgID]

    # Will print ['Ocube', 'OBJECT_CUBE']. 'OBJECT_CUBE' is one of the old legacy symbols.
    print(f"Candidates for cube ID {cubeId}: {cubeCandidates}")
    # Will print a LOT :)
    print(f"Candidates for edit message ID {editMsgID}: {editCandidates}")

    # The other way is to use Get(), which also allows us to provide a regex filter to narrow down the 
    # results. This is useful as we can often predict properties of the symbol, for example that node 
    # IDs always follow the pattern Xaaaaa, i.e., a capital letter followed by lowercase letters, that 
    # data type symbols always start with DTYPE_, or that node message symbols always start with MSG_.

    cubeFiltered: list[str] | None = myCache.Get(cubeId, r"^[A-Z][a-z]+$")
    editFiltered: list[str] | None = myCache.Get(editMsgID, r"^MSG_")

    # Will print ['Ocube']
    print(f"Filtered candidates for cube ID {cubeId}: {cubeFiltered}")
    # Will print ['MSG_EDIT']
    print(f"Filtered candidates for edit message ID {editMsgID}: {editFiltered}")


if __name__ == "__main__":
    main()
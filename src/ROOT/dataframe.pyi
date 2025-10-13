
from typing import overload

from ROOT import RDF

class RDataFrame(RDF.RNode):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, nentries : int) -> None: ...
    @overload
    def __init__(self, treeName : str, fileNameGlob : str) -> None: ...

from typing import Any


class UniformMappingSubsetDef:
    """
    Defines mapping subset expectation where all keys and values share common definitions.

    :param keys_definition: definition for mapping keys
    :param values_definition: definition for mapping values
    """

    def __init__(self, keys_definition: Any, values_definition: Any, /) -> None:  # noqa: ANN401
        #: definition for mapping keys
        self.keys_definition = keys_definition
        #: definition for mapping values
        self.values_definition = values_definition

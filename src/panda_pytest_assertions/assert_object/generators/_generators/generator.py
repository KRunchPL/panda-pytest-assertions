import abc
from typing import Any

from panda_pytest_assertions.assert_object._protocols import GeneratorFactoryProtocol


class Generator(abc.ABC):
    """
    Generates expectation for given object according to a provided definition.

    :param generator_factory: factory for object generators
    :param definition: expectation definition
    """

    @classmethod
    @abc.abstractmethod
    def matches(cls, definition: Any) -> bool:  # noqa: ANN401
        """
        Decide whether provided definition can be handled by this generator.

        :param definition: definition to be tested
        :return: whether provided definition can be handled by this generator
        """

    def __init__(
        self,
        generator_factory: type[GeneratorFactoryProtocol],
        definition: Any,  # noqa: ANN401
    ) -> None:
        self.generator_factory = generator_factory
        self.definition = definition

    @abc.abstractmethod
    def generate_expectation(self, object_: Any) -> Any:  # noqa: ANN401
        """
        Generate expectation from given object.

        :param object_: an object to generate expectation from
        :return: generated expectation
        """

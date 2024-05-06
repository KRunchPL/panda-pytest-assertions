from typing import Any, Protocol


class AsserterProtocol(Protocol):
    """
    Asserter checking that the given expectation is fulfilled by the object.
    """

    expectation: Any
    asserter_factory: 'type[AsserterFactoryProtocol]'

    def __init__(
        self,
        asserter_factory: 'type[AsserterFactoryProtocol]',
        expectation: Any,  # noqa: ANN401
    ) -> None: ...

    @classmethod
    def matches(cls, expectation: Any) -> bool:  # noqa: ANN401
        """
        Decide whether provided expectation can be handled by this asserter.

        :param expectation: expectation to be tested
        """

    def assert_object(self, object_: Any) -> None:  # noqa: ANN401
        """
        Assert if the expectation is fulfilled by an object.

        :param object_: an object to be tested
        """


class AsserterFactoryProtocol(Protocol):
    """
    Factory for registered asserters.
    """

    @classmethod
    def create(cls, expectation: Any) -> AsserterProtocol:  # noqa: ANN401
        """
        Create asserter object for given expectation.

        The function goes through all registered asserter types and creates the first one that matches.

        :param expectation: expectation to create asserter for
        """

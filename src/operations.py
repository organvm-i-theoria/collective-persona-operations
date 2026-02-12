"""Operation pipelines for persona transformations.

Provides the OperationPipeline class that applies sequential transformations
to personas, enabling trait amplification, filtering, and normalization.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from .persona import Persona


class OperationType(Enum):
    """Types of operations that can be applied to personas."""

    AMPLIFY = "amplify"
    SUPPRESS = "suppress"
    NORMALIZE = "normalize"
    FILTER = "filter"


@dataclass
class OperationResult:
    """Result of applying an operation to a persona."""

    operation_type: OperationType
    persona_id: str
    traits_before: dict[str, float]
    traits_after: dict[str, float]
    success: bool
    message: str


class OperationPipeline:
    """Applies sequential trait transformations to personas.

    Operations are queued and executed in order. Each operation modifies
    the persona's trait dictionary according to the operation type and
    parameters.
    """

    def __init__(self) -> None:
        self._operations: list[tuple[OperationType, dict[str, Any]]] = []
        self._history: list[OperationResult] = []

    @property
    def pending_count(self) -> int:
        """Return the number of queued operations."""
        return len(self._operations)

    @property
    def history(self) -> list[OperationResult]:
        """Return the history of executed operations."""
        return list(self._history)

    def queue_amplify(self, trait_name: str, factor: float = 1.5) -> None:
        """Queue an amplification operation for a specific trait.

        Args:
            trait_name: The trait to amplify.
            factor: Multiplier for the trait value (clamped to 0.0-1.0).
        """
        self._operations.append(
            (OperationType.AMPLIFY, {"trait_name": trait_name, "factor": factor})
        )

    def queue_suppress(self, trait_name: str, factor: float = 0.5) -> None:
        """Queue a suppression operation for a specific trait.

        Args:
            trait_name: The trait to suppress.
            factor: Multiplier for the trait value (should be < 1.0).
        """
        self._operations.append(
            (OperationType.SUPPRESS, {"trait_name": trait_name, "factor": factor})
        )

    def queue_normalize(self) -> None:
        """Queue a normalization operation that scales all traits to sum to 1.0."""
        self._operations.append((OperationType.NORMALIZE, {}))

    def execute(self, persona: Persona) -> list[OperationResult]:
        """Execute all queued operations on the given persona.

        Operations are applied in FIFO order. The persona's traits dict
        is modified in place.

        Args:
            persona: The persona to transform.

        Returns:
            List of OperationResult objects describing each step.
        """
        results: list[OperationResult] = []

        for op_type, params in self._operations:
            traits_before = dict(persona.traits)

            if op_type == OperationType.AMPLIFY:
                trait = params["trait_name"]
                if trait in persona.traits:
                    persona.traits[trait] = min(
                        1.0, round(persona.traits[trait] * params["factor"], 3)
                    )

            elif op_type == OperationType.SUPPRESS:
                trait = params["trait_name"]
                if trait in persona.traits:
                    persona.traits[trait] = max(
                        0.0, round(persona.traits[trait] * params["factor"], 3)
                    )

            elif op_type == OperationType.NORMALIZE:
                total = sum(persona.traits.values())
                if total > 0:
                    persona.traits = {
                        k: round(v / total, 3) for k, v in persona.traits.items()
                    }

            result = OperationResult(
                operation_type=op_type,
                persona_id=persona.persona_id,
                traits_before=traits_before,
                traits_after=dict(persona.traits),
                success=True,
                message=f"{op_type.value} applied successfully",
            )
            results.append(result)
            self._history.append(result)

        self._operations.clear()
        return results
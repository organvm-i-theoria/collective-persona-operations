"""Persona management for collective identity systems.

Provides the core PersonaManager class for creating, updating, and merging
personas within a recursive cognitive architecture.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass
class Persona:
    """Represents a single persona within the collective."""

    persona_id: str
    name: str
    traits: dict[str, float]
    created_at: str
    metadata: dict[str, Any] = field(default_factory=dict)


class PersonaManager:
    """Manages the lifecycle of personas in a collective identity system.

    The PersonaManager provides CRUD operations for personas and supports
    merging multiple personas into composite identities. It maintains an
    in-memory registry that can be serialized for persistence.
    """

    def __init__(self) -> None:
        self._personas: dict[str, Persona] = {}

    @property
    def count(self) -> int:
        """Return the number of registered personas."""
        return len(self._personas)

    def create_persona(
        self,
        name: str,
        traits: dict[str, float] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Persona:
        """Create a new persona and register it.

        Args:
            name: Human-readable name for the persona.
            traits: Mapping of trait names to intensity scores (0.0-1.0).
            metadata: Arbitrary metadata to attach to the persona.

        Returns:
            The newly created Persona instance.
        """
        persona_id = uuid4().hex[:12]
        persona = Persona(
            persona_id=persona_id,
            name=name,
            traits=traits or {},
            created_at=datetime.now(timezone.utc).isoformat(),
            metadata=metadata or {},
        )
        self._personas[persona_id] = persona
        return persona

    def get_persona(self, persona_id: str) -> Persona | None:
        """Retrieve a persona by its ID.

        Args:
            persona_id: The unique identifier of the persona.

        Returns:
            The Persona if found, otherwise None.
        """
        return self._personas.get(persona_id)

    def merge_personas(self, persona_ids: list[str], merged_name: str) -> Persona:
        """Merge multiple personas into a single composite persona.

        Trait values are averaged across all source personas. The merged
        persona receives metadata linking back to its constituent sources.

        Args:
            persona_ids: List of persona IDs to merge.
            merged_name: Name for the resulting composite persona.

        Returns:
            The newly created merged Persona.

        Raises:
            ValueError: If fewer than 2 persona IDs are provided or any ID is unknown.
        """
        if len(persona_ids) < 2:
            raise ValueError("Merge requires at least 2 personas")

        sources: list[Persona] = []
        for pid in persona_ids:
            persona = self._personas.get(pid)
            if persona is None:
                raise ValueError(f"Unknown persona ID: {pid}")
            sources.append(persona)

        # Average trait values across all sources
        all_traits: dict[str, list[float]] = {}
        for source in sources:
            for trait_name, value in source.traits.items():
                all_traits.setdefault(trait_name, []).append(value)

        merged_traits = {
            name: round(sum(values) / len(values), 3)
            for name, values in all_traits.items()
        }

        return self.create_persona(
            name=merged_name,
            traits=merged_traits,
            metadata={"merged_from": persona_ids, "source_count": len(sources)},
        )

    def get_collective_identity(self) -> dict[str, Any]:
        """Compute the collective identity profile from all registered personas.

        Returns a summary containing averaged trait values, persona count,
        and the dominant trait across the collective.

        Returns:
            Dictionary with collective identity metrics.
        """
        if not self._personas:
            return {"persona_count": 0, "traits": {}, "dominant_trait": None}

        all_traits: dict[str, list[float]] = {}
        for persona in self._personas.values():
            for trait_name, value in persona.traits.items():
                all_traits.setdefault(trait_name, []).append(value)

        averaged = {
            name: round(sum(values) / len(values), 3)
            for name, values in all_traits.items()
        }

        dominant = max(averaged, key=averaged.get) if averaged else None

        return {
            "persona_count": len(self._personas),
            "traits": averaged,
            "dominant_trait": dominant,
        }

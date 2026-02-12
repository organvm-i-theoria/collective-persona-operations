"""Persona registry for persistent storage and retrieval.

Provides the PersonaRegistry class that manages serialization and
lookup of persona collections with tagging and search capabilities.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .persona import Persona, PersonaManager


class PersonaRegistry:
    """Persistent registry for persona collections.

    Wraps a PersonaManager with serialization capabilities and
    tag-based search functionality.
    """

    def __init__(self, manager: PersonaManager | None = None) -> None:
        self._manager = manager or PersonaManager()
        self._tags: dict[str, set[str]] = {}  # tag -> set of persona_ids

    @property
    def manager(self) -> PersonaManager:
        """Return the underlying PersonaManager."""
        return self._manager

    def tag_persona(self, persona_id: str, tag: str) -> bool:
        """Attach a tag to a persona for categorical search.

        Args:
            persona_id: The persona to tag.
            tag: The tag string to attach.

        Returns:
            True if the persona was found and tagged, False otherwise.
        """
        if self._manager.get_persona(persona_id) is None:
            return False
        self._tags.setdefault(tag, set()).add(persona_id)
        return True

    def find_by_tag(self, tag: str) -> list[Persona]:
        """Find all personas with a given tag.

        Args:
            tag: The tag to search for.

        Returns:
            List of Persona objects that carry the specified tag.
        """
        persona_ids = self._tags.get(tag, set())
        results: list[Persona] = []
        for pid in persona_ids:
            persona = self._manager.get_persona(pid)
            if persona is not None:
                results.append(persona)
        return results

    def find_by_trait_threshold(
        self, trait_name: str, min_value: float = 0.5
    ) -> list[Persona]:
        """Find personas whose trait value meets or exceeds a threshold.

        Args:
            trait_name: The trait to filter on.
            min_value: Minimum trait value (inclusive).

        Returns:
            List of Persona objects meeting the threshold.
        """
        results: list[Persona] = []
        for persona in self._manager._personas.values():
            if persona.traits.get(trait_name, 0.0) >= min_value:
                results.append(persona)
        return results

    def export_to_dict(self) -> dict[str, Any]:
        """Serialize the entire registry to a JSON-compatible dict.

        Returns:
            Dictionary containing all personas and tag mappings.
        """
        personas_data = []
        for persona in self._manager._personas.values():
            personas_data.append({
                "persona_id": persona.persona_id,
                "name": persona.name,
                "traits": persona.traits,
                "created_at": persona.created_at,
                "metadata": persona.metadata,
            })

        tags_data = {tag: sorted(ids) for tag, ids in self._tags.items()}

        return {
            "version": "0.1.0",
            "persona_count": len(personas_data),
            "personas": personas_data,
            "tags": tags_data,
        }

    def export_to_json(self, path: Path) -> None:
        """Write the registry to a JSON file.

        Args:
            path: Filesystem path for the output JSON file.
        """
        data = self.export_to_dict()
        path.write_text(json.dumps(data, indent=2))

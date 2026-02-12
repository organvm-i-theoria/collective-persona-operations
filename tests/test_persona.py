"""Tests for the persona module."""

from src.persona import PersonaManager


class TestPersonaManager:
    """Tests for PersonaManager class."""

    def test_create_persona_returns_persona_with_id(self) -> None:
        manager = PersonaManager()
        persona = manager.create_persona("Alice", traits={"curiosity": 0.8})
        assert persona.persona_id is not None
        assert persona.name == "Alice"
        assert persona.traits == {"curiosity": 0.8}

    def test_create_persona_increments_count(self) -> None:
        manager = PersonaManager()
        assert manager.count == 0
        manager.create_persona("Bob")
        assert manager.count == 1
        manager.create_persona("Carol")
        assert manager.count == 2

    def test_get_persona_returns_none_for_unknown_id(self) -> None:
        manager = PersonaManager()
        assert manager.get_persona("nonexistent") is None

    def test_get_persona_retrieves_created_persona(self) -> None:
        manager = PersonaManager()
        created = manager.create_persona("Dave", traits={"focus": 0.6})
        retrieved = manager.get_persona(created.persona_id)
        assert retrieved is not None
        assert retrieved.name == "Dave"

    def test_merge_personas_averages_traits(self) -> None:
        manager = PersonaManager()
        p1 = manager.create_persona("A", traits={"x": 0.8, "y": 0.2})
        p2 = manager.create_persona("B", traits={"x": 0.4, "y": 0.6})
        merged = manager.merge_personas([p1.persona_id, p2.persona_id], "AB")
        assert merged.traits["x"] == 0.6
        assert merged.traits["y"] == 0.4

    def test_merge_personas_rejects_single_id(self) -> None:
        manager = PersonaManager()
        p = manager.create_persona("Solo")
        try:
            manager.merge_personas([p.persona_id], "Fail")
            assert False, "Should have raised ValueError"
        except ValueError:
            pass

    def test_get_collective_identity_empty(self) -> None:
        manager = PersonaManager()
        identity = manager.get_collective_identity()
        assert identity["persona_count"] == 0
        assert identity["dominant_trait"] is None

    def test_get_collective_identity_with_personas(self) -> None:
        manager = PersonaManager()
        manager.create_persona("A", traits={"empathy": 0.9, "logic": 0.3})
        manager.create_persona("B", traits={"empathy": 0.5, "logic": 0.7})
        identity = manager.get_collective_identity()
        assert identity["persona_count"] == 2
        assert identity["dominant_trait"] == "empathy"

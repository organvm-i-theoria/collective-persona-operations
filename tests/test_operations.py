"""Tests for the operations module."""

from src.persona import PersonaManager
from src.operations import OperationPipeline, OperationType


class TestOperationPipeline:
    """Tests for OperationPipeline class."""

    def test_amplify_increases_trait_value(self) -> None:
        manager = PersonaManager()
        persona = manager.create_persona("Test", traits={"focus": 0.5})
        pipeline = OperationPipeline()
        pipeline.queue_amplify("focus", factor=1.5)
        results = pipeline.execute(persona)
        assert len(results) == 1
        assert persona.traits["focus"] == 0.75

    def test_suppress_decreases_trait_value(self) -> None:
        manager = PersonaManager()
        persona = manager.create_persona("Test", traits={"anxiety": 0.8})
        pipeline = OperationPipeline()
        pipeline.queue_suppress("anxiety", factor=0.5)
        results = pipeline.execute(persona)
        assert persona.traits["anxiety"] == 0.4

    def test_normalize_scales_traits_to_sum_one(self) -> None:
        manager = PersonaManager()
        persona = manager.create_persona(
            "Test", traits={"a": 0.6, "b": 0.4, "c": 1.0}
        )
        pipeline = OperationPipeline()
        pipeline.queue_normalize()
        pipeline.execute(persona)
        total = sum(persona.traits.values())
        assert abs(total - 1.0) < 0.01

    def test_pipeline_clears_after_execution(self) -> None:
        pipeline = OperationPipeline()
        pipeline.queue_amplify("x")
        pipeline.queue_suppress("y")
        assert pipeline.pending_count == 2
        manager = PersonaManager()
        persona = manager.create_persona("Test", traits={"x": 0.5, "y": 0.5})
        pipeline.execute(persona)
        assert pipeline.pending_count == 0

    def test_history_tracks_executed_operations(self) -> None:
        pipeline = OperationPipeline()
        pipeline.queue_amplify("creativity", factor=1.2)
        manager = PersonaManager()
        persona = manager.create_persona("Test", traits={"creativity": 0.6})
        pipeline.execute(persona)
        assert len(pipeline.history) == 1
        assert pipeline.history[0].operation_type == OperationType.AMPLIFY
        assert pipeline.history[0].success is True

    def test_amplify_clamps_to_max_one(self) -> None:
        manager = PersonaManager()
        persona = manager.create_persona("Test", traits={"power": 0.9})
        pipeline = OperationPipeline()
        pipeline.queue_amplify("power", factor=2.0)
        pipeline.execute(persona)
        assert persona.traits["power"] == 1.0

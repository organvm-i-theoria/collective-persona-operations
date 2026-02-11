[![ORGAN-I: Theory](https://img.shields.io/badge/ORGAN--I-Theory-1a237e?style=flat-square)](https://github.com/organvm-i-theoria)
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Status: Planning](https://img.shields.io/badge/status-planning-lightgrey?style=flat-square)]()

# Collective Persona Operations

[![CI](https://github.com/organvm-i-theoria/collective-persona-operations/actions/workflows/ci.yml/badge.svg)](https://github.com/organvm-i-theoria/collective-persona-operations/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-pending-lightgrey)](https://github.com/organvm-i-theoria/collective-persona-operations)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/organvm-i-theoria/collective-persona-operations/blob/main/LICENSE)
[![Organ I](https://img.shields.io/badge/Organ-I%20Theoria-8B5CF6)](https://github.com/organvm-i-theoria)
[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/organvm-i-theoria/collective-persona-operations)
[![Markdown](https://img.shields.io/badge/lang-Markdown-informational)](https://github.com/organvm-i-theoria/collective-persona-operations)


**A theoretical and operational framework for managing coherent identity across multi-agent systems, multi-organ institutions, and multi-register creative practices — treating persona not as performance but as a composable epistemic interface.**

> "The self is not a point but a pattern of points." — Gregory Bateson

---

## Name Explanation

**Collective Persona** refers to the many-as-one problem of identity: how does a single authorial intelligence present itself coherently when it operates through multiple agents, organisations, contexts, and registers? The "collective" is not a committee but a *field* — the unified identity that emerges from the coordination of distinct voices, just as a symphony emerges from instruments that are individually incomplete. **Operations** signals that this is not merely a philosophical inquiry. These are executable procedures: protocols, state machines, validation engines, and switching rules that can be implemented in code and enforced across a distributed creative-institutional system.

The compound name positions the repo at the intersection of identity theory and systems engineering — exactly where ORGAN-I (Theoria) does its most distinctive work.

---

## Table of Contents

- [Problem Statement](#problem-statement)
- [Core Concepts](#core-concepts)
- [Theoretical Framework](#theoretical-framework)
- [Planned Architecture](#planned-architecture)
- [Use Cases Within the Eight-Organ System](#use-cases-within-the-eight-organ-system)
- [Related Work](#related-work)
- [Roadmap](#roadmap)
- [Cross-References](#cross-references)
- [Contributing](#contributing)
- [License](#license)
- [Author & Contact](#author--contact)

---

## Problem Statement

### The Incoherence of Multi-Contextual Identity

When a single creator operates across eight organisations, dozens of repositories, and multiple public-facing contexts — grant applications, open-source communities, commercial products, theoretical publications, public essays, marketing announcements — the question of *who is speaking* becomes non-trivial. Every context demands a different register: the academic rigour expected in a theory repo is not the conversational directness needed for a building-in-public essay; the commercial precision of a SaaS product page is not the experimental freedom of a generative art README.

Most practitioners handle this by intuition. They "code-switch" between registers unconsciously, the way a bilingual person shifts between languages depending on who they are speaking to. This works at small scale. It fails catastrophically when:

1. **AI agents enter the workflow.** An LLM generating a README for ORGAN-III (Commerce) has no inherent knowledge that its voice should differ from the one used in ORGAN-I (Theory). Without explicit persona specifications, AI-generated content trends toward a flat, generic register that belongs nowhere and convinces no one.

2. **The system scales beyond one person's memory.** A single author can hold eight distinct voices in their head. A team cannot. A multi-agent system certainly cannot. Without formalisation, persona coherence degrades as the system grows.

3. **Cross-organ content creates identity conflicts.** When an ORGAN-V (Logos) essay quotes an ORGAN-I (Theoria) concept, the citation must bridge two registers without breaking either. When ORGAN-VII (Kerygma) announces a product from ORGAN-III (Ergon), the marketing voice must amplify the commercial voice without distorting it. These cross-organ interactions are where incoherence becomes visible.

4. **External audiences enforce judgment.** A grant reviewer reading both a theoretical paper and a product pitch from the same author expects *consistency without uniformity*. A hiring manager scanning READMEs across multiple repos expects a recognisable authorial presence. Incoherence reads as carelessness or, worse, as inauthenticity.

### Why Existing Frameworks Fail

Current approaches to identity in multi-agent systems fall into two inadequate categories:

- **Role-Based Access Control (RBAC) / Identity Management.** These systems answer "who has permission to do what?" — not "who is speaking and how?" They manage authentication and authorisation, not voice and register. A persona is not a role; it is an expressive mode.

- **Brand Guidelines / Style Guides.** These are static documents: "use this font, this colour palette, this tone of voice." They describe the *output* of persona coherence but not the *mechanism*. They cannot adapt to context, validate outputs, or compose across multiple registers. A style guide tells you what the voice should sound like; it does not tell the system how to produce it.

What is missing is a **dynamic, composable, machine-readable persona layer** — one that sits between the raw content generation capabilities of AI agents and the contextual requirements of specific organs, audiences, and publication contexts. Collective Persona Operations is the theoretical foundation and operational specification for that layer.

---

## Core Concepts

### 1. Persona as Interface

The central theoretical move is to treat persona not as a mask (the theatrical metaphor) or as a role (the sociological metaphor) but as an **interface** in the software engineering sense: a contract that specifies how a system presents itself to a given context while hiding the complexity of its internal state.

An interface defines:
- **What is exposed** — the public methods, the observable behaviour
- **What is hidden** — the implementation details, the internal contradictions
- **What is guaranteed** — the invariants that callers can rely on

A persona-as-interface defines:
- **What voice is exposed** — register, vocabulary, tone, rhetorical patterns
- **What is hidden** — the machinery of the other organs, the cross-organ dependencies, the personal biography that does not belong in this context
- **What is guaranteed** — consistency within the register, traceability to the unified authorial identity, absence of contradictions with other persona instances

This reframing transforms persona management from a creative-writing problem into a systems-engineering problem with formal properties that can be specified, validated, and tested.

### 2. The Persona Registry

Every persona in the system is a first-class entity with a formal specification. The **Persona Registry** is a structured catalogue of all active personas, each defined by:

| Field | Description |
|-------|-------------|
| `id` | Unique identifier (e.g., `organ-i-theoretical`, `organ-iii-commercial`) |
| `register` | The linguistic register (academic, conversational, commercial, artistic, etc.) |
| `vocabulary_constraints` | Words and phrases that are encouraged, discouraged, or prohibited |
| `rhetorical_patterns` | Preferred argument structures (deductive, narrative, exemplary, etc.) |
| `audience_model` | Who this persona addresses (grant reviewers, developers, general public, etc.) |
| `temperature` | Metaphorical: how experimental or conservative the voice is |
| `lineage` | Which other personas this one inherits from or contrasts with |
| `context_rules` | When this persona activates (org, repo type, document type, audience) |

The registry is the single source of truth for persona state, analogous to `registry-v2.json` for repository state.

### 3. Identity Composability

Personas are not monolithic. They compose. The voice used in a cross-organ document — say, an ORGAN-V essay that discusses ORGAN-I theory and announces an ORGAN-III product — is not a fourth persona but a *composition* of three, governed by explicit rules:

- **Dominance hierarchy:** Which persona leads? (In ORGAN-V, the essay voice dominates; the others are quoted.)
- **Blending rules:** How do registers merge? (Academic vocabulary can appear in an essay voice; commercial jargon cannot.)
- **Boundary markers:** How does the text signal transitions? (Quotation, section breaks, register shifts.)

Composability is what distinguishes this framework from a simple style guide. A style guide says "use this voice." A composable persona system says "given these three voices and this context, here is how they combine, and here are the invariants that must hold."

### 4. Persona Switching as State Machine

Context switching between personas is modeled as a finite state machine. Each persona is a state; transitions are triggered by context changes (different org, different document type, different audience). The state machine enforces:

- **No illegal transitions:** You cannot jump from the commercial register to the artistic register without passing through a neutral state. This prevents jarring tonal shifts.
- **Transition costs:** Some switches are cheap (theoretical → academic) because the registers are adjacent. Others are expensive (commercial → artistic) because the registers are distant. Cost maps to the editorial effort required.
- **Hysteresis:** Once in a persona state, the system resists switching. This prevents the "wandering voice" problem where a document drifts between registers without committing to any.

### 5. Voice Consistency Validation

The operational counterpart of persona theory is **validation**: given a document and its declared persona, does the document actually conform? Validation operates at multiple levels:

- **Lexical:** Does the vocabulary match the register? (Academic persona should not use marketing superlatives; commercial persona should not use jargon unexplained.)
- **Structural:** Does the argument structure match the rhetorical pattern? (Deductive personas lead with premises; narrative personas lead with anecdotes.)
- **Relational:** Does this document's voice relate correctly to sibling documents in the same organ and cousin documents in other organs?

Validation can be partially automated through NLP techniques (readability scoring, vocabulary analysis, rhetorical structure detection) and partially through human review guided by checklists derived from the persona specification.

---

## Theoretical Framework

### Philosophy of Personal Identity

The Western philosophical tradition on identity runs from Locke's memory criterion (you are your memories) through Hume's bundle theory (there is no self, only a bundle of perceptions) to Parfit's reductionism (personal identity is not what matters; what matters is psychological continuity). Collective Persona Operations draws most directly from **narrative identity theory** (Ricoeur, MacIntyre): the self is constituted by the stories it tells about itself, and coherence is achieved not through metaphysical unity but through narrative consistency.

In the multi-organ context, the "narrative" is the corpus of all published artifacts — READMEs, essays, product pages, code comments — and "consistency" means that a reader encountering any subset of these artifacts would recognise a single authorial intelligence operating in context-appropriate registers.

### Collective Intelligence and Multi-Agent Systems

From the multi-agent systems literature (Woolley et al., 2010; Malone & Bernstein, 2015), we borrow the concept of **collective intelligence factors**: the properties that make a group smarter than its individual members. In our context, the "group" is not a team of humans but a constellation of AI agents, each generating content for a different organ. The collective intelligence factor is the persona coherence layer: the system that ensures the agents' outputs combine into a coherent institutional identity rather than a cacophony of unrelated voices.

This connects directly to the work in `a-recursive-root` (the AI Council system), where multiple agent archetypes engage in structured deliberation. The AI Council produces *decisions*; Collective Persona Operations produces *voices*. They are complementary: the Council determines what to say, and the Persona system determines how to say it in each context.

### Erving Goffman and Dramaturgical Analysis

Goffman's *The Presentation of Self in Everyday Life* (1956) introduced the theatrical metaphor for social interaction: we perform different "selves" in different contexts (front stage vs. back stage). This framework has obvious relevance, but we depart from Goffman on a critical point. For Goffman, the performed self is a *deception* — a managed impression that conceals the "true" self. In our framework, there is no "true" self behind the personas. The personas are the self, or more precisely, the self is the *coherence function* that relates the personas to each other. The backstage is not a hidden reality; it is the governance layer that ensures the front-stage performances are mutually consistent.

This is not relativism. It is engineering. A software system that presents different APIs to different clients is not "deceiving" anyone; it is providing context-appropriate interfaces to a single underlying system. Collective Persona Operations treats the author the same way.

---

## Planned Architecture

Since this repository is in the planning stage, the architecture described here is the intended design. Implementation will follow as the eight-organ system matures and generates the practical demand for persona coordination tooling.

```
┌─────────────────────────────────────────────────┐
│              Persona Governance Layer            │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │
│  │ Persona  │  │ Context  │  │  Composition  │  │
│  │ Registry │  │ Detector │  │    Engine      │  │
│  └────┬─────┘  └────┬─────┘  └───────┬───────┘  │
│       │              │                │          │
│       ▼              ▼                ▼          │
│  ┌──────────────────────────────────────────┐   │
│  │         Persona State Machine             │   │
│  │  (current state, legal transitions,       │   │
│  │   hysteresis parameters)                  │   │
│  └────────────────────┬─────────────────────┘   │
│                       │                          │
│  ┌────────────────────▼─────────────────────┐   │
│  │      Voice Consistency Validator          │   │
│  │  (lexical, structural, relational)        │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
        │                       │
        ▼                       ▼
  ┌───────────┐          ┌────────────┐
  │ AI Agent  │          │  Human     │
  │ Prompts   │          │  Review    │
  │ (system   │          │  Checklists│
  │  prompts) │          │            │
  └───────────┘          └────────────┘
```

### Component Summary

| Component | Responsibility | Input | Output |
|-----------|---------------|-------|--------|
| **Persona Registry** | Store and serve persona specifications | CRUD operations | Persona spec JSON |
| **Context Detector** | Determine which persona(s) apply | Org, repo, doc type, audience | Active persona ID(s) |
| **Composition Engine** | Merge multiple personas for cross-organ contexts | Set of persona IDs + dominance rules | Composite persona spec |
| **State Machine** | Enforce legal transitions and hysteresis | Current state + context change event | New state or rejection |
| **Validator** | Check output against declared persona | Document + persona spec | Pass/fail + diagnostics |

The system is designed to be **progressive**: it can start as a set of YAML persona definitions consumed by human authors, grow into system-prompt templates consumed by AI agents, and eventually become a runtime validation service integrated with CI/CD pipelines (see `github-actions-spec.md` in the planning corpus).

---

## Use Cases Within the Eight-Organ System

### Case 1: AI-Generated README Consistency

When generating Silver Sprint READMEs for 44+ repos across 8 organs, the AI agent receives a persona spec as part of its system prompt. ORGAN-I repos get the theoretical-philosophical register. ORGAN-III repos get the commercial-technical register. The Persona Registry provides these specs; the Validator checks the output.

### Case 2: ORGAN-V Essay Voice

The public-process essays in ORGAN-V require a distinctive voice: intellectually serious but accessible, building-in-public transparent but not self-indulgent. This voice is a composition of the theoretical register (for conceptual depth) and the conversational register (for accessibility), with explicit blending rules that the Composition Engine enforces.

### Case 3: Cross-Organ Announcements

When ORGAN-VII (Kerygma) announces the launch of an ORGAN-III (Ergon) product, the marketing voice must amplify the commercial voice without distorting it. The Context Detector identifies this as a cross-organ interaction, the Composition Engine produces a composite spec, and the Validator ensures the announcement stays within bounds.

### Case 4: Grant Application Coherence

A grant application that references work across multiple organs must present a unified authorial identity while demonstrating range. The persona system provides a "formal-institutional" composite persona that draws from the academic rigour of ORGAN-I and the practical evidence of ORGAN-III, tuned for the specific audience model of grant reviewers.

---

## Related Work

| Work | Relevance | Distinction |
|------|-----------|-------------|
| **Goffman, *Presentation of Self*** (1959) | Foundational dramaturgical metaphor | We reject the deception framing; personas are interfaces, not masks |
| **Ricoeur, *Oneself as Another*** (1992) | Narrative identity theory | We operationalise narrative coherence as machine-checkable invariants |
| **Park et al., "Generative Agents"** (2023) | LLM agents with persistent personas | Focus on individual agent memory; we focus on cross-agent persona coherence |
| **Brand voice frameworks** (various) | Industry precedent for multi-register identity | Static documents; we propose dynamic, composable, validatable specifications |
| **RBAC / IAM systems** | Identity management in software | Manage permissions, not voice; orthogonal concern |
| **Woolley et al., "Collective Intelligence"** (2010) | Group intelligence factors | We adapt c-factor theory to AI agent collectives |

---

## Roadmap

### Phase 0: Specification (Current)
- Define persona ontology and registry schema
- Document theoretical framework (this README)
- Establish cross-references with sibling ORGAN-I repos

### Phase 1: Manual Operations
- Create YAML persona definitions for each organ
- Develop human-readable switching checklists
- Pilot persona validation during Silver Sprint README generation

### Phase 2: AI Integration
- Convert persona specs to system-prompt templates
- Integrate with AI-conductor workflow (see planning corpus)
- Build automated lexical and structural validators

### Phase 3: Runtime Governance
- Implement Persona State Machine as a lightweight service
- Integrate Validator with GitHub Actions CI/CD pipeline
- Deploy Composition Engine for cross-organ content generation

### Phase 4: Reflection and Recursion
- Use persona validation data to refine persona specifications
- Feed voice consistency metrics back into the Persona Registry
- Publish findings as ORGAN-V essay: "Who Speaks When the Machine Writes?"

---

## Cross-References

| Repository | Relationship |
|-----------|-------------|
| [`a-recursive-root`](https://github.com/organvm-i-theoria/a-recursive-root) | The AI Council determines *what* to say; Collective Persona Operations determines *how* to say it. Complementary systems. |
| [`organon-noumenon`](https://github.com/organvm-i-theoria/organon-noumenon--ontogenetic-morphe) | Provides the ontological categories that structure persona identity. Persona types map to ontological categories. |
| [`recursive-engine`](https://github.com/organvm-i-theoria/recursive-engine) | The recursive structures that generate emergent properties also apply to persona: a persona is a recursive pattern of voice applied across contexts. |
| [`public-process`](https://github.com/organvm-v-logos/public-process) | Primary consumer of composed personas. ORGAN-V essays are the most visible test of cross-register coherence. |
| [`agentic-titan`](https://github.com/organvm-iv-taxis/agentic-titan) | The orchestration layer that routes tasks to agents. Persona specs will be injected at the routing layer. |

---

## Contributing

This repository is in the planning and specification phase. Contributions are welcome in the form of:

- **Theoretical feedback** — Does the persona-as-interface framing hold? Are there philosophical objections or alternative framings worth considering?
- **Technical design critique** — Is the planned architecture sound? Are there existing tools or libraries that should be evaluated?
- **Use case proposals** — What persona coherence problems have you encountered in multi-context creative or institutional work?

Please open an issue to discuss before submitting a pull request. All contributions should maintain the theoretical-philosophical register appropriate to ORGAN-I.

---

## License

MIT. See [LICENSE](LICENSE) for details.

---

## Author & Contact

**[@4444J99](https://github.com/4444J99)**

Part of **[ORGAN-I: Theoria](https://github.com/organvm-i-theoria)** — the theoretical research arm of the eight-organ creative-institutional system.

For questions about the eight-organ architecture, see the [meta-organvm](https://github.com/meta-organvm) umbrella organisation.

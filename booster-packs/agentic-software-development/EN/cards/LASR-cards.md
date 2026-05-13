# LASR Cards - Agentic Software Development Booster Pack

## Table of Contents

- [AC-1-1 Non-deterministic outputs](#ac-1-1-non-deterministic-outputs)
- [AC-1-2 Unclear code provenance](#ac-1-2-unclear-code-provenance)
- [AC-1-3 Coarse grained LLM tasks](#ac-1-3-coarse-grained-llm-tasks)
- [AC-2-1 Unsupervised agent swarms](#ac-2-1-unsupervised-agent-swarms)
- [AC-2-2 Overly loose permissions](#ac-2-2-overly-loose-permissions)
- [AC-2-3 Documentation bloat](#ac-2-3-documentation-bloat)
- [AC-3-1 Overloaded LLM context](#ac-3-1-overloaded-llm-context)
- [AC-3-2 Tool-driven design](#ac-3-2-tool-driven-design)
- [AC-3-3 Feature bloat through speed](#ac-3-3-feature-bloat-through-speed)
- [AC-4-1 Missing guardrails or model evals](#ac-4-1-missing-guardrails-or-model-evals)
- [AC-4-2 Insufficient sandboxing](#ac-4-2-insufficient-sandboxing)
- [AC-4-3 Unmanaged bias and harmful content](#ac-4-3-unmanaged-bias-and-harmful-content)
- [AC-5-1 Careless innovation](#ac-5-1-careless-innovation)
- [AC-5-2 Overly complex AI dev setups](#ac-5-2-overly-complex-ai-dev-setups)
- [AC-5-3 Prompt jailbreaks and data leakage](#ac-5-3-prompt-jailbreaks-and-data-leakage)
- [AC-6-1 Missing AI usage standards](#ac-6-1-missing-ai-usage-standards)
- [AC-6-2 Over-reliance on generators](#ac-6-2-over-reliance-on-generators)
- [AC-6-3 Context-Induced Architectural Bias](#ac-6-3-context-induced-architectural-bias)
- [AC-7-1 Design and concept drift](#ac-7-1-design-and-concept-drift)
- [AC-7-2 Superficial or outdated solutions](#ac-7-2-superficial-or-outdated-solutions)
- [AC-7-3 Hidden / Inconsistent Architecture Decisions](#ac-7-3-hidden--inconsistent-architecture-decisions)

---

## AC-1-1 Non-deterministic outputs

**Category:** LLM-usage

Is the non-deterministic nature of LLMs problematic? Are solutions, tests, traceability or configuration solutions sensitive to small changes or too dependent on structural stability?

---

## AC-1-2 Unclear code provenance

**Category:** LLM-usage

Is there organizational uncertainty concerning copyrights, third-party licences or patents that apply to code created with Gen-AI? Can IP grey zones lead to legal and compliance issues?

---

## AC-1-3 Coarse grained LLM tasks

**Category:** LLM-usage

Are tasks given to LLMs too big or underspecified, so that superficial designs, placeholders or dummy implementations are common? Are hidden defects often discovered late or require rework?

---

## AC-2-1 Unsupervised agent swarms

**Category:** Gen-AI Autonomy

Do autonomous multi-agent chains run without clear limits, supervision or cost controls? Deadlocks, loops and chatty prompt chains can waste compute, spike bills and create brittle dependencies.

---

## AC-2-2 Overly loose permissions

**Category:** Gen-AI Autonomy

Do agents have shell, cloud or production access beyond what they really need? Can misused privileges or simple prompt mistakes delete data, break systems or leak sensitive information?

---

## AC-2-3 Documentation bloat

**Category:** Gen-AI Autonomy

Is documentation largely auto-generated descriptions of implementation details, managed by LLMs? Is the volume of information so big, that it is hard to maintain and read "manually"?

---

## AC-3-1 Overloaded LLM context

**Category:** Goals and Context

Do excessive context enrichment, careless information feeding or long-lived memories clutter LLM contexts? Are important rules or principles lost or forgotten during longer coding sessions?

---

## AC-3-2 Tool-driven design

**Category:** Goals and Context

Does enthusiasm for AI tools push considerations around requirements, goals and tradeoffs into the background? Is AI usage distracting during analyis, design and evaluation steps?

---

## AC-3-3 Feature bloat through speed

**Category:** Goals and Context

Is AI-augmented implemention deemed so "cheap", that requirements are less thoroughly prioritized, challenged or refined? May this overload POs or lead to bloated, incoherent solutions?

---

## AC-4-1 Missing guardrails or model evals

**Category:** Tests and Guardrails

Do conceptual regressions or architectural drift go unnoticed because of missing guardrails or tests? Are quality, security or performance characteristics of used AI models only checked manually?

---

## AC-4-2 Insufficient sandboxing

**Category:** Tests and Guardrails

Are critical systems, data or credentials exposed to AI-driven tools and agents in some way? Can simple mistakes or prompt exploits turn into serious security, stability or data protection incidents?

---

## AC-4-3 Unmanaged bias and harmful content

**Category:** Tests and Guardrails

Do discriminatory, offensive or otherwise harmful output patterns go unchecked? Are controls for bias and problematic content in code, tests, workflows or documentation manual or sketchy?

---

## AC-5-1 Careless innovation

**Category:** Agentic Development Know-how

Does the perceived ease of change with AI tools encourage risky experiments or technology changes without proper analysis? This can fuel defects, security issues or uncontrolled technical debt.

---

## AC-5-2 Overly complex AI dev setups

**Category:** Agentic Development Know-how

Are agent frameworks, tools and pipelines so complex or opaque that devs cannot really oversee or control changes? Is the average dev overwhelmed by the AI setup and ends up at the mercy of LLMs?

---

## AC-5-3 Prompt jailbreaks and data leakage

**Category:** Agentic Development Know-how

Is it easy to (accidentially) leak data, bypass guardrails or tunnel harmful commands through prompts? Do logs, telemetry or MCP memories expose secrets to external LLM services?

---

## AC-6-1 Missing AI usage standards

**Category:** Soft Factors and Processes

Is the usage of Gen-AI tools and approaches mainly up to personal preferance or style? Are shared development practices or alignment processes missing or optional?

---

## AC-6-2 Over-reliance on generators

**Category:** Soft Factors and Processes

Does heavy use of AI reduce deep understanding of the codebase and the quality of manual reviews? Is there over-confidence in AI "sparring partners" or blind trust in AI output?

---

## AC-6-3 Context-Induced Architectural Bias

**Category:** Soft Factors and Processes

Do prompts, specs, examples or generated architecture notes over-prime agents toward accidental technical solutions? Are agents preserving structures because they appeared in context, rather than because they reflect deliberate architectural decisions?

---

## AC-7-1 Design and concept drift

**Category:** Developed Solution

Do agents or generators possibly dilute the architectural style or let patterns and conventions fade over time? This can erode the original design, confuse devs and threaten consistency and correctness.

---

## AC-7-2 Superficial or outdated solutions

**Category:** Developed Solution

Are agents able to generate solutions that look plausible but are shallow or unprofessional? Are unsuitable or outdated technologies, frameworks or API versions checked systematically?

---

## AC-7-3 Hidden / Inconsistent Architecture Decisions

**Category:** Developed Solution

Are architectural decisions made or implied inside prompts, specs, tickets, pull requests or chats without being captured as explicit, durable decision artifacts? Is it hard to reconstruct what was decided, why and under which assumptions?

---

# LASR Cards - Agentic Software Development Booster Pack

## Table of Contents

- [AC-1 Non-deterministic outputs](#ac1-non-deterministic-outputs)
- [AC-10 Missing guardrails or model evals](#ac10-missing-guardrails-or-model-evals)
- [AC-11 Insufficient sandboxing](#ac11-insufficient-sandboxing)
- [AC-12 Unmanaged bias and harmful content](#ac12-unmanaged-bias-and-harmful-content)
- [AC-13 Careless innovation](#ac13-careless-innovation)
- [AC-14 Overly complex AI dev setups](#ac14-overly-complex-ai-dev-setups)
- [AC-15 Prompt jailbreaks and data leakage](#ac15-prompt-jailbreaks-and-data-leakage)
- [AC-16 Missing AI usage standards](#ac16-missing-ai-usage-standards)
- [AC-17 Over-reliance on generators](#ac17-over-reliance-on-generators)
- [AC-18 Design and concept drift](#ac18-design-and-concept-drift)
- [AC-19 Superficial or outdated solutions](#ac19-superficial-or-outdated-solutions)
- [AC-2 Unclear code provenance](#ac2-unclear-code-provenance)
- [AC-3 Coarse grained LLM tasks](#ac3-coarse-grained-llm-tasks)
- [AC-4 Unsupervised agent swarms](#ac4-unsupervised-agent-swarms)
- [AC-5 Overly loose permissions](#ac5-overly-loose-permissions)
- [AC-6 Documentation bloat](#ac6-documentation-bloat)
- [AC-7 Overloaded LLM context](#ac7-overloaded-llm-context)
- [AC-8 Tool-driven design](#ac8-tool-driven-design)
- [AC-9 Feature bloat through speed](#ac9-feature-bloat-through-speed)

---

## AC-1 Non-deterministic outputs

**Category:** LLM-usage

Is the non-deterministic nature of LLMs problematic? Are solutions, tests, traceability or configuration solutions sensitive to small changes or too dependent on structural stability?

---

## AC-10 Missing guardrails or model evals

**Category:** Tests and Guardrails

Do conceptual regressions or architectural drift go unnoticed because of missing guardrails or tests? Are quality, security or performance characteristics of used AI models only checked manually?

---

## AC-11 Insufficient sandboxing

**Category:** Tests and Guardrails

Are critical systems, data or credentials exposed to AI-driven tools and agents in some way? Can simple mistakes or prompt exploits turn into serious security, stability or data protection incidents?

---

## AC-12 Unmanaged bias and harmful content

**Category:** Tests and Guardrails

Do discriminatory, offensive or otherwise harmful output patterns go unchecked? Are controls for bias and problematic content in code, tests, workflows or documentation manual or sketchy?

---

## AC-13 Careless innovation

**Category:** Agentic Development Know-how

Does the perceived ease of change with AI tools encourage risky experiments or technology changes without proper analysis? This can fuel defects, security issues or uncontrolled technical debt.

---

## AC-14 Overly complex AI dev setups

**Category:** Agentic Development Know-how

Are agent frameworks, tools and pipelines so complex or opaque that devs cannot really oversee or control changes? Is the average dev overwhelmed by the AI setup and ends up at the mercy of LLMs?

---

## AC-15 Prompt jailbreaks and data leakage

**Category:** Agentic Development Know-how

Is it easy to (accidentially) leak data, bypass guardrails or tunnel harmful commands through prompts? Do logs, telemetry or MCP memories expose secrets to external LLM services?

---

## AC-16 Missing AI usage standards

**Category:** Soft Factors and Processes

Is the usage of Gen-AI tools and approaches mainly up to personal preferance or style? Are shared development practices or alignment processes missing or optional?

---

## AC-17 Over-reliance on generators

**Category:** Soft Factors and Processes

Does heavy use of AI reduce deep understanding of the codebase and the quality of manual reviews? Is there over-confidence in AI "sparring partners" or blind trust in AI output?

---

## AC-18 Design and concept drift

**Category:** Developed Solution

Do agents or generators possibly dilute the architectural style or let patterns and conventions fade over time? This can erode the original design, confuse devs and threaten consistency and correctness.

---

## AC-19 Superficial or outdated solutions

**Category:** Developed Solution

Are agents able to generate solutions that look plausible but are shallow or unprofessional? Are unsuitable or outdated technologies, frameworks or API versions checked systematically?

---

## AC-2 Unclear code provenance

**Category:** LLM-usage

Is there organizational uncertainty concerning copyrights, third-party licences or patents that apply to code created with Gen-AI? Can IP grey zones lead to legal and compliance issues?

---

## AC-3 Coarse grained LLM tasks

**Category:** LLM-usage

Are tasks given to LLMs too big or underspecified, so that superficial designs, placeholders or dummy implementations are common? Are hidden defects often discovered late or require rework?

---

## AC-4 Unsupervised agent swarms

**Category:** Gen-AI Autonomy

Do autonomous multi-agent chains run without clear limits, supervision or cost controls? Deadlocks, loops and chatty prompt chains can waste compute, spike bills and create brittle dependencies.

---

## AC-5 Overly loose permissions

**Category:** Gen-AI Autonomy

Do agents have shell, cloud or production access beyond what they really need? Can misused privileges or simple prompt mistakes delete data, break systems or leak sensitive information?

---

## AC-6 Documentation bloat

**Category:** Gen-AI Autonomy

Is documentation largely auto-generated descriptions of implementation details, managed by LLMs? Is the volume of information so big, that it is hard to maintain and read "manually"?

---

## AC-7 Overloaded LLM context

**Category:** Goals and Context

Do excessive context enrichment, careless information feeding or long-lived memories clutter LLM contexts? Are important rules or principles lost or forgotten during longer coding sessions?

---

## AC-8 Tool-driven design

**Category:** Goals and Context

Does enthusiasm for AI tools push considerations around requirements, goals and tradeoffs into the background? Is AI usage distracting during analyis, design and evaluation steps?

---

## AC-9 Feature bloat through speed

**Category:** Goals and Context

Is AI-augmented implemention deemed so "cheap", that requirements are less thoroughly prioritized, challenged or refined? May this overload POs or lead to bloated, incoherent solutions?

---


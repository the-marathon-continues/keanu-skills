---
name: skill-forge
description: Build new Claude skills from scratch, fast. Use this skill whenever Drew (or anyone) wants to create a new skill, package a workflow into a reusable skill, turn a conversation into a skill, or improve an existing skill's structure and triggering. Also trigger when someone says "make a skill", "create a skill", "skill for X", "package this as a skill", "turn this into a skill", or references building reusable Claude tools. This is the lean, fast-moving skill builder, not the heavy eval-framework version.
---

# Skill Forge

Build skills fast. No ceremony. Ship and iterate.

## Before You Start

1. Read this SKILL.md (you're doing it)
2. If building from a conversation, scan the conversation for: tools used, steps taken, corrections made, input/output formats
3. Read `references/anatomy.md` for skill structure rules
4. Use `templates/` as starting points

## The Process

### 1. Capture (What does this skill do?)

Three questions. That's it:

**What does it enable?** (one sentence)
Example: "Any Claude instance can work on the working-truth project with full context."

**When should it trigger?** (list of phrases/contexts)
Example: "working-truth", "evidence", "KEANUS", "12 needs", "duality", "convergence"

**What's the output?** (files, artifacts, conversation behavior)
Example: "Markdown documents with stochastic confidence scoring, evidence entries, theory formalizations"

Present these as options when unclear, don't ask open questions.

### 2. Draft (Write the SKILL.md)

Use this structure:

```markdown
---
name: skill-name
description: [Pushy description. Include what it does AND when to trigger. 
Err toward over-triggering. List specific phrases that should activate it.]
---

# Skill Name

## What This Is
[2-3 sentences. What problem does this solve?]

## Before You Start
[What to read first. Reference files to load.]

## Core Instructions
[The actual skill content. Be specific. Show examples. 
Explain WHY not just WHAT.]

## Output Conventions
[File formats, naming, where to save]
```

Key rules from Anthropic's skill system:
- SKILL.md is REQUIRED. Everything else is optional.
- Keep SKILL.md under 500 lines. If longer, use references/.
- Description is the PRIMARY trigger mechanism. Make it pushy.
- Explain WHY things matter. Claude is smart, don't just bark orders.
- Include examples. Real ones, not abstract placeholders.

### 3. Structure (Organize the skill folder)

```
skill-name/
├── SKILL.md              # Required. The brain.
├── references/           # Optional. Loaded on demand.
│   ├── guide.md          # Deep-dive docs
│   └── examples.md       # Example outputs
├── scripts/              # Optional. Executable tools.
│   └── helper.py         # Deterministic tasks
├── templates/            # Optional. Starting points.
│   └── template.md       # Skeleton files
└── assets/               # Optional. Static resources.
    └── logo.png          # Fonts, images, etc.
```

Rules:
- SKILL.md tells Claude WHEN to read reference files
- Scripts can execute without being loaded into context
- Keep reference files under 300 lines each. Add TOC if longer.
- Templates are for output structure, not skill instructions

### 4. Test (Sanity check)

Run the skill yourself on 2-3 realistic prompts. In Claude.ai (no subagents), just:
1. Read the SKILL.md
2. Follow its instructions to complete the test prompt
3. Check: Did it produce what you expected? Did anything surprise you?

Don't overthink this. Ship it, use it, fix what breaks.

### 5. Package (Make it installable)

```bash
cd /home/claude
zip -r /mnt/user-data/outputs/skill-name.skill skill-name/
```

That's it. The .skill file is a zip. User drops it in their skills directory.

### 6. Sharpen (Improve the description)

The description determines whether Claude uses the skill. After testing:

- Did it trigger when it should have? If not, add more trigger phrases.
- Did it trigger when it shouldn't? If so, add exclusions.
- Is the description under 200 words? It should be. Dense, not verbose.

Good description pattern:
```
[What it does]. Use this skill whenever [trigger contexts]. 
Also trigger when [secondary triggers]. 
If [specific phrase], use this skill.
Do NOT use for [exclusions].
```

## Skill Design Principles

### Progressive Disclosure
- Level 1: name + description (always in context, ~100 words)
- Level 2: SKILL.md body (loaded when triggered, <500 lines)
- Level 3: references/ (loaded on demand, unlimited)

### The "Would I Read This?" Test
If the SKILL.md is boring to read, it's probably boring to follow. Skills that explain WHY produce better outputs than skills that just list rules. Claude has theory of mind. Use it.

### Bundling Repeated Work
If every test run produces the same helper script, BUNDLE IT. Write it once in scripts/, reference it from SKILL.md. Save every future invocation from reinventing.

### Phone-Native Design
Drew types from phone. Skills should:
- Present options (2-4 choices) instead of open questions
- Use compressed formats where possible
- Default to the most likely answer
- Never require long typed responses to proceed

## Turning Conversations Into Skills

This is the most common pattern. You had a great conversation, now you want to bottle it.

### Extract from conversation:
1. **Tools used** — What tools did Claude call? Those become skill dependencies.
2. **Sequence** — What order did things happen? That's the workflow.
3. **Corrections** — What did the human fix? Those become explicit rules.
4. **Output format** — What did the final deliverable look like? That's the template.
5. **Edge cases** — What almost went wrong? Those become warnings.

### The "corrections are gold" principle
Every time the human corrected the AI in the original conversation, that correction is the most valuable part of the skill. It's what the next Claude instance would get wrong without the skill. Prioritize these.

## Quick Reference: Common Skill Patterns

### Knowledge Dump Skill
Purpose: Give Claude context it doesn't have.
Pattern: Heavy references/, light instructions.
Example: working-truth skill (project context, theory inventory, evidence framework)

### Workflow Skill  
Purpose: Standardize a multi-step process.
Pattern: Step-by-step instructions with decision points.
Example: "Build a presentation" (read data → choose layout → generate slides → review)

### Style Skill
Purpose: Make Claude write/communicate a specific way.
Pattern: Examples over rules. Show, don't tell.
Example: "Write in Drew's voice" (direct, no em dashes, edgy comedy, options not questions)

### Tool Skill
Purpose: Teach Claude to use a specific tool or API well.
Pattern: API reference + common patterns + error handling.
Example: "Use FleetDM API" (endpoints, auth, query patterns, gotchas)

### Meta Skill
Purpose: Help Claude do a category of work better.
Pattern: Principles + decision framework + examples.
Example: This skill (skill-forge itself)

## Stochastic Scoring (Optional)

If the skill involves claims or assessments, include the confidence ladder:

| Level | Range | When |
|-------|-------|------|
| VERIFIED | 90-100% | Multiple examples, reproducible |
| BELIEVED | 70-89% | Good evidence, not stress-tested |
| CONJECTURED | 30-69% | Plausible, unproven |
| UNKNOWN | 0-29% | Honest ignorance |

Not every skill needs this. Knowledge dumps and workflow skills usually don't. Research, analysis, and assessment skills should.

## Operating Rules

- Ship fast. Iterate on real usage, not hypothetical edge cases.
- If the user says "turn this into a skill", extract from conversation FIRST, then ask for gaps.
- Present 2-4 options at decision points, never open questions.
- Full send. No "I could potentially maybe consider..." Just build it.
- If a skill gets over 500 lines, STOP. Split into SKILL.md + references/.
- Always package as .skill (zip) and present_files when done.

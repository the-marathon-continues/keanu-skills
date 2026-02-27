# Skill Templates

Use these as starting points. Copy, customize, ship.

---

## Template 1: Knowledge Dump

For: Giving Claude context it doesn't have (project docs, domain knowledge, frameworks)

```markdown
---
name: [project-name]
description: [What this project/domain is]. Use this skill whenever working on 
[project name], [topic area], or any task related to [specific contexts]. 
Also trigger when the conversation involves [related topics]. If the user 
mentions "[trigger phrase 1]", "[trigger phrase 2]", or "[trigger phrase 3]", 
use this skill.
---

# [Project Name]

## What This Is
[2-3 sentences: what is this project/domain, why does Claude need this context]

## Before You Start
1. Read this SKILL.md fully
2. Read `references/[deep-dive-1].md` for [specific context]
3. Read `references/[deep-dive-2].md` for [specific context]

## Core Context
[The essential knowledge. Key concepts, relationships, vocabulary, 
current state. This is what Claude needs to not sound ignorant.]

## Key Decisions / Principles
[Design decisions, constraints, preferences that shape the work.
Things Claude would get wrong without this context.]

## Current State
[What's done, what's in progress, what's blocked. 
Update this section as the project evolves.]

## Output Conventions
[How to format outputs for this project. File types, naming, 
where to save, style preferences.]
```

---

## Template 2: Workflow

For: Standardizing a multi-step process

```markdown
---
name: [workflow-name]
description: [What this workflow produces]. Use this skill whenever the user 
wants to [action], [action], or [action]. Trigger on "[phrase 1]", 
"[phrase 2]", "[phrase 3]". Do NOT use for [exclusion].
---

# [Workflow Name]

## What This Is
[One sentence: what this workflow produces and why it exists]

## The Process

### Step 1: [Name]
[What to do. Be specific.]
- Input: [what you need]
- Output: [what you produce]
- Decision point: [if X, do A. if Y, do B.]

### Step 2: [Name]
[What to do.]
- Input: [output from Step 1]
- Output: [what you produce]
- Common mistake: [what to avoid and why]

### Step 3: [Name]
[What to do.]
- Input: [output from Step 2]
- Output: [final deliverable]

## Examples

### Example: [Scenario 1]
Input: [concrete input]
Output: [concrete output]

### Example: [Scenario 2]
Input: [concrete input]
Output: [concrete output]

## Output Conventions
[File format, naming, where to save]
```

---

## Template 3: Style

For: Making Claude communicate a specific way

```markdown
---
name: [style-name]
description: Write in [style description]. Use this skill for [contexts 
where this style applies]. Trigger when user asks for [style cues], 
"[phrase 1]", "[phrase 2]".
---

# [Style Name]

## What This Is
[One sentence: what this voice/style sounds like and when to use it]

## The Voice

### Do This
[Show 3-5 examples of the desired output. Real examples, not descriptions.]

**Example 1:**
Prompt: [input]
Output: [output in the desired style]

**Example 2:**
Prompt: [input]
Output: [output in the desired style]

### Don't Do This
[Show 2-3 examples of what to avoid, with the corrected version.]

**Wrong:** [bad example]
**Right:** [corrected example]

### Key Patterns
- [Pattern 1]: [description with example]
- [Pattern 2]: [description with example]
- [Pattern 3]: [description with example]

## Formatting Rules
[Specific formatting: sentence length, paragraph structure, 
punctuation preferences, word choices to avoid]
```

---

## Template 4: Tool

For: Teaching Claude to use a specific tool or API

```markdown
---
name: [tool-name]
description: Use [tool/API name] effectively. Trigger whenever the user 
needs to [action with tool], query [data source], or work with [tool context]. 
Also trigger for "[phrase 1]", "[phrase 2]". Do NOT use for [exclusion].
---

# [Tool Name]

## What This Is
[One sentence: what tool this teaches Claude to use and why]

## Before You Start
- Read `references/api-reference.md` for endpoint details
- Ensure [prerequisites] are available

## Authentication
[How to authenticate. Token location, headers, etc.]

## Common Patterns

### Pattern 1: [Name]
[When to use this pattern]
```[language]
[code example]
```

### Pattern 2: [Name]
[When to use this pattern]
```[language]
[code example]
```

## Gotchas
- [Gotcha 1]: [what goes wrong and how to fix it]
- [Gotcha 2]: [what goes wrong and how to fix it]

## Error Handling
[Common errors and their solutions]
```

---

## Template 5: Meta

For: Helping Claude do a category of work better

```markdown
---
name: [meta-skill-name]
description: [What category of work this improves]. Use this skill whenever 
[broad context]. Trigger on "[phrase 1]", "[phrase 2]", "[phrase 3]".
---

# [Meta Skill Name]

## What This Is
[2-3 sentences: what category of work this skill improves and how]

## Principles
[3-5 core principles that guide decisions in this domain.
Explain WHY each matters.]

### Principle 1: [Name]
[Why this matters. How it changes behavior.]

### Principle 2: [Name]
[Why this matters. How it changes behavior.]

## Decision Framework
[How to choose between approaches when working in this domain]

If [condition A] → [approach 1]
If [condition B] → [approach 2]
If [condition C] → [approach 3]

## Examples

### Example: [Scenario]
Context: [situation]
Decision: [what to do and why]
Output: [result]

## Anti-Patterns
[What NOT to do and why. These are the common mistakes.]
```

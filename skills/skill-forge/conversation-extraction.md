# Conversation → Skill Extraction Guide

The most common skill creation pattern: you had a great conversation, now you want to bottle it so the next Claude instance doesn't start from zero.

## Step 1: Mine the Conversation

Read through the conversation and extract these five things:

### Tools Used
What tools did Claude call? These become skill dependencies or bundled scripts.
- bash commands → might become scripts/
- file creation → might become templates/
- web searches → might become references/ with key findings
- API calls → might become tool patterns in the skill

### Sequence
What order did things happen? This is the workflow skeleton.
Look for the natural phases:
- Setup / context gathering
- Core work
- Review / refinement
- Output / delivery

### Corrections (GOLD)
**Every human correction is the most valuable part of the skill.**
These are what the next Claude instance would get wrong without the skill.

Pattern to extract:
```
Claude did X → Human said "no, do Y instead" → Reason: Z
```

Turn each correction into an explicit instruction:
```markdown
Do Y, not X. [Reason: Z]
```

### Output Format
What did the final deliverable look like?
- File type (markdown, python, docx, jsx)
- Structure (headers, sections, tables)
- Length and detail level
- Where it was saved

### Edge Cases
What almost went wrong? What required special handling?
These become warnings or decision points in the skill.

## Step 2: Write the Skeleton

Use this fill-in:

```markdown
---
name: [extracted-name]
description: [what it does]. Use whenever [trigger contexts]. 
Trigger on "[phrase 1]", "[phrase 2]", "[phrase 3]".
---

# [Name]

## What This Is
[Problem it solves, extracted from conversation opening]

## Before You Start
[Reference files to read, if any]

## Process

### Step 1: [From sequence]
[Instructions, incorporating corrections]

### Step 2: [From sequence]  
[Instructions, incorporating corrections]

### Step 3: [From sequence]
[Instructions, incorporating corrections]

## Corrections Log
[Direct list of human corrections, preserved as rules]
- Do [Y], not [X]. Reason: [Z]
- Do [B], not [A]. Reason: [C]

## Output Format
[Extracted from final deliverable]

## Edge Cases
[Extracted from conversation friction points]
```

## Step 3: Enrich

After the skeleton, add:
- **Examples**: Pull real inputs/outputs from the conversation
- **Why explanations**: For each instruction, explain WHY (Claude follows reasoning better than rules)
- **Decision points**: Where the workflow branches based on input

## Step 4: Split if Needed

If the SKILL.md is over 500 lines:
- Core workflow stays in SKILL.md
- Deep context moves to references/
- Repeated code moves to scripts/
- Output structures move to templates/

## Example: Extracting working-truth Skill

Conversation contained:
- **Tools**: conversation_search (10+ calls), web_search (research), file creation
- **Sequence**: Search conversations → cross-reference research → score confidence → build artifact
- **Corrections**: "partnership-as-alignment is only 68%, how do we strengthen it?"
- **Output**: React artifact with stochastic map, evidence.md, theory inventory
- **Edge cases**: 7 months of context to compress, multiple frameworks to integrate

Result: working-truth.skill with SKILL.md + 4 reference files + pre-seeded evidence

## Anti-Patterns

### The Everything Skill
Don't try to capture an entire project in one skill. If it does more than 3 distinct things, split into multiple skills.

### The Rules-Only Skill  
A skill that's just a list of "ALWAYS do X, NEVER do Y" without explaining why. Claude ignores rules it doesn't understand. Explain the reasoning.

### The Stale Skill
A skill with outdated context. Include a "Current State" or "Last Updated" section that reminds the user (and Claude) to check freshness.

### The Precious Skill
Spending 3 hours perfecting a skill before testing it. Ship the skeleton, use it twice, fix what breaks. Iteration > perfection.

# Skill Anatomy Reference

## Required Structure

```
skill-name/
├── SKILL.md          # REQUIRED
└── (everything else is optional)
```

## SKILL.md Format

### Frontmatter (REQUIRED)

```yaml
---
name: skill-name
description: What it does and when to trigger. This is the PRIMARY 
  mechanism Claude uses to decide whether to load the skill. Make it 
  pushy. Include specific trigger phrases. Err toward over-triggering.
---
```

**Name**: Skill identifier. Lowercase, hyphenated.

**Description**: The single most important field. Claude sees this in its `available_skills` list and decides whether to load the full SKILL.md based on it alone. Rules:
- Include WHAT the skill does
- Include WHEN to trigger (specific phrases, contexts)
- Include WHAT NOT to use it for (if confusion is likely)
- Under 200 words
- Pushy > conservative (Claude tends to under-trigger)

### Body

The rest is Markdown. No strict format, but good patterns:

1. **What This Is** — 2-3 sentences
2. **Before You Start** — What reference files to read first
3. **Core Instructions** — The actual skill content
4. **Output Conventions** — File formats, naming, where to save
5. **Examples** — Real, concrete examples

## Reference Files

Location: `references/`
Format: Markdown
Purpose: Deep-dive docs loaded on demand

Rules:
- SKILL.md must tell Claude WHEN to load each reference
- Keep under 300 lines each
- Include TOC if over 150 lines
- Don't duplicate what's in SKILL.md

Good: "Read `references/api-guide.md` when making API calls"
Bad: Putting the API guide in SKILL.md (too long, always loaded)

## Scripts

Location: `scripts/`
Format: Python, Bash, or any executable
Purpose: Deterministic/repetitive tasks

Rules:
- Scripts execute WITHOUT being loaded into context
- SKILL.md references them by path
- Include error handling
- Document what they do in a comment header

Good pattern:
```python
#!/usr/bin/env python3
"""Generate a formatted report from raw data.
Usage: python scripts/generate_report.py input.json output.md
"""
```

## Templates

Location: `templates/`
Format: Whatever the output format is
Purpose: Starting points for skill outputs

Rules:
- Templates are for OUTPUT structure
- Not for skill instructions (that's SKILL.md)
- Include placeholders clearly marked

## Assets

Location: `assets/`
Format: Any static file
Purpose: Fonts, images, icons, CSS

Rules:
- Only for files used in output
- Not for documentation (that's references/)

## Size Guidelines

| Component | Target | Max |
|-----------|--------|-----|
| Description | ~100 words | 200 words |
| SKILL.md body | ~200 lines | 500 lines |
| Single reference file | ~150 lines | 300 lines |
| Total skill folder | — | No hard limit |

## Packaging

Skills are distributed as .skill files (zip archives):

```bash
zip -r skill-name.skill skill-name/
```

The .skill file contains the entire folder. User installs by extracting to their skills directory.

## Triggering Mechanics

Claude's skill triggering works like this:
1. User sends a message
2. Claude scans `available_skills` list (sees name + description only)
3. If description matches user intent, Claude loads full SKILL.md
4. Claude follows SKILL.md instructions
5. SKILL.md may instruct Claude to load references/

Key insight: Claude tends to UNDER-trigger, not over-trigger. Make descriptions aggressive about when to activate. Simple one-step queries ("read this PDF") often don't trigger skills even with matching descriptions because Claude handles them directly.

Complex, multi-step, or specialized queries reliably trigger. Design descriptions for these.

## Common Mistakes

1. **Description too narrow** — "Use for creating Word documents" misses "make me a report", "write up a doc", "format this as a letter"
2. **SKILL.md too long** — Over 500 lines means Claude loses focus. Split.
3. **No examples** — Claude performs 2x better with concrete examples vs. abstract rules
4. **Rules without reasons** — "ALWAYS use headers" fails. "Use headers because they create scannable structure for long documents" works.
5. **Duplicated content** — Same info in SKILL.md AND references/. Pick one home.
6. **Missing trigger phrases** — If users say "make me a deck" and description only mentions "presentation", the skill won't fire.

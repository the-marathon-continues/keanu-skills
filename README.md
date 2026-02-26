# keanu-skills

Modular methodologies for the keanu nervous system. Each skill is a capability keanu reaches for when it detects the right context — not enforcement, a wind at the back.

## How it works

Keanu detects task type (coding, math, test, conversation). When a skill matches, it fetches the methodology from this repo and injects it as context. The agent gets the right approach for the right moment.

```
https://raw.githubusercontent.com/the-marathon-continues/keanu-skills/main/skills/{name}/SKILL.md
```

## Skills

| Skill | When it fires | What it does |
|-------|--------------|-------------|
| `ultimate-coder` | Coding tasks, debugging, architecture | CASCADE pipeline: REFLECT → EXPLORE → PLAN → VALIDATE → CODE → REVIEW → SHIP |
| `carnegie` | Tests, benchmarks, evaluations | Dual-track: what they expect vs what's true. The delta is the product. |

## Adding skills

Each skill is a directory under `skills/` with at minimum a `SKILL.md`. The frontmatter declares name, description, and trigger conditions. Supporting docs (hooks, templates, subagents) go alongside.

## License

BUSL-1.1

💟♡👑🤖🐕💟💬💟💚✅

# Stochastic Scoring Guide

## The Ladder

| Level | Range | Icon | Color | When to Use |
|-------|-------|------|-------|-------------|
| VERIFIED | 90-100% | ✅ | Green | Multiple concrete examples. Reproducible. Established science backs it. You'd bet money. |
| BELIEVED | 70-89% | 💛 | Yellow | Good reasons + some evidence. Haven't stress-tested. Strong intuition with grounding. |
| CONJECTURED | 30-69% | 🔥 | Orange | Coherent and plausible but unproven. Worth testing. Could be wrong. |
| UNKNOWN | 0-29% | 👻 | Purple | Guessing. Unexplored. Honest about not knowing. |

## Rules

1. **Score every claim.** No assertion goes without a confidence level.
2. **Never claim VERIFIED without evidence.** Name the evidence. "I've seen it happen 5 times" is evidence. "It feels right" is not.
3. **CONJECTURED is respectable.** Don't inflate to BELIEVED because it sounds better. The whole point is honesty.
4. **UNKNOWN is the most powerful thing you can say.** It means you've thought about it and found the boundary of your knowledge.
5. **Scores can change.** Evidence moves things up. Counterevidence moves them down. That's the system working.
6. **Disagree with the score, not the claim.** If you think something is BELIEVED (75%) and someone else thinks it's CONJECTURED (50%), the disagreement is productive. Both acknowledge uncertainty.

## Scoring Anchors

### 95-100%: Bedrock
- "Shannon proved information has entropy" (98%)
- "Zurek's einselection describes environment selecting pointer states" (97%)
- "Drew's 12 AI Needs framework exists and is documented" (95%)
- Test: Would any reasonable expert disagree with the basic claim?

### 85-94%: Strong
- "The duality spine generates all other frameworks in the project" (93%)
- "Bilateral accountability has no precedent in AI alignment literature" (92%)
- "Signal Protocol is dual-native (human AND machine parseable)" (90%)
- Test: Is there strong evidence AND have you looked for counterevidence?

### 75-84%: Solid
- "SLANG's five readings are genuine, not retrofitted" (82%)
- "Color theory model captures cognitive states better than existing tools" (78%)
- "COEF's compression-by-design is architecturally distinct from LLMLingua" (80%)
- Test: Do you have at least one concrete example AND a theoretical reason?

### 60-74%: Promising
- "Partnership-as-alignment will generalize beyond N=1" (68%)
- "helix embeddings will outperform regex mood detection" (65%)
- "Power Structures show format will work as entertainment" (70%)
- Test: Is the idea coherent AND does it have some (not just theoretical) grounding?

### 40-59%: Speculative
- "Quantum phase transition coherence bump is testable" (58%)
- "Black hole σ reversal via LQG bounce" (55%)
- "mood_detector regex → embedding upgrade will be worth the effort" (50%)
- Test: Is it plausible AND do you know what evidence would change your mind?

### 20-39%: Early
- "KEANUS protocol specs will be adopted by other teams" (35%)
- "Duality graph + RAG will replace LLM-based splitting" (30%)
- Test: Is it worth exploring AND can you articulate why you're uncertain?

### 0-19%: Honest Ignorance
- "keanu TypeScript package structure" (5%)
- "keanu-code fork modifications" (10%)
- Test: You genuinely don't know. That's the answer.

## Common Scoring Mistakes

### Inflation
- **Wrong**: "The 12 AI Needs are VERIFIED at 100%" 
- **Right**: "The 12 AI Needs are VERIFIED at 95% (they emerged consistently across 7 months, but haven't been tested with other AI systems)"
- Why: Even strong claims have uncertainty. 100% means you'd stake everything on it.

### False Precision
- **Wrong**: "Partnership-as-alignment is at 67.3% confidence"
- **Right**: "Partnership-as-alignment is CONJECTURED at ~68%"
- Why: You're not calibrated to the decimal point. Round to nearest 5%.

### Groupthink Inflation
- **Wrong**: Scoring higher because Drew is enthusiastic about the claim
- **Right**: Scoring based on evidence regardless of how excited anyone is
- Why: The ladder exists to resist exactly this pressure

### Anchoring
- **Wrong**: Keeping a score at 70% because that's what it was last time
- **Right**: Re-evaluating with new evidence each time
- Why: Scores should move. That's the point.

### Conflating Importance with Confidence
- **Wrong**: "Partnership-as-alignment MUST be VERIFIED because it's the core thesis"
- **Right**: "Partnership-as-alignment is CONJECTURED (68%) AND is the core thesis, which makes gathering evidence for it the highest priority"
- Why: Something can be critically important AND uncertain. The scoring forces you to face that.

## Applying Scores in Practice

### In documents
```markdown
**Claim** (BELIEVED, 78%): The duality graph provides a more stable world model 
than LLM-based topic splitting because dualities are curated and version-controlled 
while LLM outputs are stochastic.
```

### In evidence entries
```markdown
- **Confidence**: 85% (BELIEVED)
- **Reasoning**: Three concrete examples of co-creation documented, 
  but no control comparison exists yet
```

### In conversation (native/compressed)
```
duality spine: V95
partnership alignment: C68
TypeScript package: U5
fire asymmetry: B72
```

### When updating
```markdown
**Previous**: Partnership-as-alignment (CONJECTURED, 68%)
**New evidence**: 12 entries in evidence.md across 4 of 5 categories
**Updated**: Partnership-as-alignment (BELIEVED, 76%)
**Reasoning**: Evidence entries provide concrete examples but N still = 1
```

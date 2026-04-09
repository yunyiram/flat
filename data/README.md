# FLAT Domain Logic — Separated Data

These JSON files contain the **domain logic** extracted from `flat-v6.html`.
They are the "알맹이" (core) — preserved for CTO handoff / future API / rewrite.

**Note**: Currently NOT loaded at runtime. The HTML uses an inline copy.
These files are the authoritative reference for when the codebase splits into modules.

| File | Size | Contents |
|------|------|----------|
| rules.json | 14KB | 6 collar compat matrices + 21 functional rules |
| presets.json | 36KB | 49 presets EN/KO (31 top + 8 skirt + 10 pants) |
| params.json | 20KB | 51 state defaults + geometry + grading + ease |
| fabrics.json | 19KB | 41 fabrics EN/KO + GSM + season + stretch |

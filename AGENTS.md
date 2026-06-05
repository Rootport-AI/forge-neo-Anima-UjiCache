# Agent Handoff

This repository is a Forge Neo extension named `UjiCache`.

Use this file as the short orientation. The detailed UjiCache behavior is described in `docs/UjiCache-spec-v1.2.md`.

## Current State

- Package: `ujicache`
- Forge entrypoint: `scripts/ujicache.py`
- Version: `0.1.0`
- UI prefix / setting keys: `ujicache-*` / `ujicache_*`
- Console prefix: `[UjiCache]`

Implemented runtime patch:

- `ujicache`

Retained UI:

- Top-level accordion: `UjiCache`
- Sub-accordion: `Debug log mode`
- UjiCache controls, including Auto Uji mode

Removed from the public extension surface:

- Attention backend override
- Standalone TeaCache experiment UI
- Spectrum experiment
- 2D sparse attention
- Cond/uncond optimization
- Low-bit and torch.compile experiments
- Identity patch test

## Important Rules

- Preserve baseline behavior when `Enable UjiCache` is off.
- The first model call must always be full calculation.
- Do not allow cache use when `previous_residual` is missing.
- Restore monkey patches on disable, unsupported model, unload, and degraded paths.
- Do not silently fail. Log degraded or fallback reasons with the `[UjiCache]` prefix.
- Forge Neo can pass unused kwargs such as `control` into `Anima.forward`; UjiCache should ignore unused kwargs and consume only the values it needs, especially `transformer_options`.

## Useful Files

- `ujicache/script.py`: Gradio UI and generation-time patch selection.
- `ujicache/state.py`: settings snapshot and runtime counters.
- `ujicache/patcher.py`: UjiCache monkey patch implementation and restore logic.
- `ujicache/diagnostics.py`: console snapshots and summaries.
- `ujicache/auto_ujicache.py`: Auto Uji CSV parsing and row application.
- `docs/UjiCache-spec-v1.2.md`: UjiCache behavior and acceptance criteria.

## Forge Neo Gotcha

Forge Neo can preserve old Gradio component ranges/defaults in `ui-config.json`. If a UI change does not appear after reinstalling the extension, check that file and restart Forge Neo.


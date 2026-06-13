# Changelog

## Unreleased

- Added: `Capture calibration pairs` (Debug log mode) — per-step (rel_l1, out_rel) JSONL capture with run conditions incl. Shift; forces full calculation on every model call.
- Added: `Uji shift` / `Uji capture_pairs` infotext keys.

## 0.1.0

- Split UjiCache out as an independent Forge Neo extension.
- Rename the package to `ujicache` and the Forge entrypoint to `scripts/ujicache.py`.
- Replace the top-level panel with `UjiCache`.
- Keep `Debug log mode` as a sub-accordion.
- Remove PredLab-only UI and runtime paths for attention override, standalone TeaCache, Spectrum, 2D sparse attention, cond/uncond optimization, low-bit, compile, and identity patch experiments.
- Keep UjiCache's internal TeaCache-style skip decision helpers where needed by the residual prediction prototype.
- Update logging to use the `[UjiCache]` console prefix.


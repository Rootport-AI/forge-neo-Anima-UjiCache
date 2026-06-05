# Auto Uji Mode Spec v1.0

## Purpose

Auto Uji mode runs multiple UjiCache parameter rows from one CSV in a single Generate action.

## UI

```text
UjiCache
  Enable UjiCache
  Auto Uji mode
    Enable Auto Uji mode
    Auto Uji CSV
```

Auto Uji mode is active only when both `Enable UjiCache` and `Enable Auto Uji mode` are ON.
It must not enable UjiCache automatically.

## CSV

Supported MVP columns:

```csv
name,threshold,formula,prediction_strength,slope_ema_smoothing,curve_ema_smoothing,taylor2_curve_strength,apply_prediction_from_skip,use_prediction_after_progress,max_skip_streak,force_full_interval
teacache_ref,0.07,teacache,0.00,0.00,0.00,0.25,2,0.00,0,0
linear_a,0.21,linear,0.50,0.20,0.00,0.25,2,0.00,0,0
taylor2_a,0.21,taylor2,0.50,0.20,0.10,0.25,2,0.00,0,0
```

Formula aliases:

- `teacache`, `residual`, `residual_only` -> `TeaCache (residual only)`
- `linear`, `linear_extrapolation` -> `Linear extrapolation`
- `taylor2`, `taylor`, `quadratic` -> `Taylor2 curve`

Unspecified values use the current UjiCache UI values.

## Runtime

Each CSV row is treated as one UjiCache condition. Forge `batch_size` is preserved, and `n_iter` is expanded to `CSV row count * original n_iter`.

The seed set is shared per CSV row, allowing parameter comparisons under the same seed conditions.

## State

Runtime rows are stored on `p._ujicache_auto_rows`. The current row state is mirrored into `STATE`.

Main state fields:

- `auto_ujicache_enabled`
- `auto_ujicache_csv`
- `auto_ujicache_active`
- `auto_ujicache_row_index`
- `auto_ujicache_row_name`
- `auto_ujicache_row_count`
- `auto_ujicache_original_n_iter`

## Logs

```text
[UjiCache] auto_uji_prepare rows=...
[UjiCache] auto_uji_seed_template rows=...
[UjiCache] auto_uji_row_start index=...
[UjiCache] auto_uji_csv_error ...
```

## Acceptance

1. Auto Uji OFF behaves like a normal UjiCache generation.
2. Auto Uji does not run when `Enable UjiCache` is OFF.
3. Each CSV row applies its UjiCache values to `STATE`.
4. `previous_residual` and `residual_history` are not shared across rows.
5. Auto Uji does not change the core UjiCache prediction logic.

# UjiCache 仕様書 v1.2

## 概要

`UjiCache -Prototype` は、Anima / Cosmos-Predict2 推論中の block stack residual を再利用し、skip step で使う residual を複数の予測式で差し替えて比較する Forge Neo 拡張である。

独立版では、旧 `Nz-Anima-PredLab` の多数の実験機能を公開しない。Forge UI に残すのは `UjiCache -Prototype` 親アコーディオン、`Debug log mode` サブアコーディオン、UjiCache 操作群、Auto Uji mode だけである。

## UI

```text
UjiCache -Prototype
  Enable UjiCache -Prototype
  Debug log mode
    Enable debug log mode
    Debug log
    Dump UjiCache residual
    Print timing log
    Verbose diagnose log
  Enable UjiCache experiment
  UjiCache preset
  Rel L1 threshold
  Start progress
  End progress
  Prediction formula
  Prediction controls
  Cache device
  Modulated source
  Coefficient profile
  Max skip streak
  Force full interval
  Dry run
  Verbose UjiCache trace
  Auto Uji mode
```

`Debug log mode` は引き続きサブアコーディオンである。`UjiCache -Prototype` は親アコーディオンであり、旧 PredLab のサブアコーディオンではない。

## 予測式

- `TeaCache (residual only)`: 予測せず、直近の full calculation residual をそのまま使う。
- `Linear extrapolation`: residual 履歴から一次外挿する。
- `Taylor2 curve`: residual 履歴から二次曲線成分を混ぜる。

UjiCache は TeaCache 系の skip 判定ロジックを内部で使うが、独立版では standalone TeaCache UI を公開しない。

## 安全条件

- 親 Enable が OFF のときは Forge baseline を保つ。
- `Enable UjiCache experiment` が OFF のときは `Anima.forward` patch を外す。
- 最初の model call は必ず full calculation にする。
- `previous_residual` が無い場合は cache を使わず full calculation へ戻す。
- residual shape / dtype / device が合わない場合は fallback する。
- unsupported model、disable、unload、degraded path では monkey patch を復元する。
- 例外や fallback は `[UjiCache]` prefix でログに出す。
- Forge Neo が `control` など未使用 kwargs を `Anima.forward` に渡しても、それらは無視する。

## ログ

主なログ:

```text
[UjiCache] ujicache_config=...
[UjiCache] ujicache_call=...
[UjiCache] ujicache_summary=...
```

`Verbose UjiCache trace` が OFF の場合、step ごとの詳細ログは先頭の数件に制限する。summary は UjiCache 有効時に出力する。

## Metadata

UjiCache 有効時は PNG infotext に `Uji ...` keys を追加する。

主な項目:

- `Uji enabled`
- `Uji formula`
- `Uji threshold`
- `Uji progress`
- `Uji prediction_strength`
- `Uji slope_ema_smoothing`
- `Uji curve_ema_smoothing`
- `Uji auto_row_index`
- `Uji auto_row_name`

## 実装ファイル

- `scripts/ujicache.py`
- `ujicache/script.py`
- `ujicache/state.py`
- `ujicache/patcher.py`
- `ujicache/diagnostics.py`
- `ujicache/auto_ujicache.py`
- `ujicache/tensor_dump.py`

## 最小成功条件

1. Forge Neo に `UjiCache -Prototype` として表示される。
2. `Debug log mode` がサブアコーディオンとして表示される。
3. 旧 PredLab の Attention / TeaCache / Spectrum / Sparse / Cond / Low-bit / Compile UI が表示されない。
4. `Enable UjiCache experiment` で UjiCache patch を ON/OFF できる。
5. `TeaCache (residual only)` が直近 residual 再利用として動く。
6. 初回 call と missing residual は full calculation になる。
7. `ujicache_summary` で model_calls / full_calcs / skips / fallbacks / errors / active を確認できる。

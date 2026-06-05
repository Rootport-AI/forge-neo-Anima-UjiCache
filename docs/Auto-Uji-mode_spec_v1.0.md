# Auto Uji mode 仕様書 v1.0

## 目的

Auto Uji mode は、`UjiCache -Prototype` の UjiCache 条件を CSV 行ごとに切り替え、同じ Generate 操作で複数条件を順番に試すための補助機能である。

## UI

`Auto Uji mode` は `UjiCache -Prototype` アコーディオン内のサブアコーディオンである。

```text
UjiCache -Prototype
  Auto Uji mode
    Enable Auto Uji mode
    Auto Uji CSV
```

Auto Uji mode は親の `Enable UjiCache -Prototype` や `Enable UjiCache experiment` を自動で ON にしない。実行する場合、ユーザーは通常どおり両方を ON にする。

## CSV

MVP で扱う列:

```csv
name,threshold,formula,prediction_strength,slope_ema_smoothing,curve_ema_smoothing,taylor2_curve_strength,apply_prediction_from_skip,use_prediction_after_progress,max_skip_streak,force_full_interval
teacache_ref,0.07,teacache,0.00,0.00,0.00,0.25,2,0.00,0,0
linear_a,0.21,linear,0.50,0.20,0.00,0.25,2,0.00,0,0
taylor2_a,0.21,taylor2,0.50,0.20,0.10,0.25,2,0.00,0,0
```

`formula` の短縮名:

- `teacache`, `residual`, `residual_only` -> `TeaCache (residual only)`
- `linear`, `linear_extrapolation` -> `Linear extrapolation`
- `taylor2`, `taylor`, `quadratic` -> `Taylor2 curve`

未指定列は Generate 時点の UjiCache UI 値を使う。

## 実行単位

CSV 1 行を 1 つの UjiCache 条件として扱う。Forge の `batch_size` は維持し、`n_iter` は `CSV行数 * 元のn_iter` に拡張する。

seed set は CSV 行ごとに共有する。これにより同じ seed 条件で UjiCache パラメータだけを比較できる。

## State

実行中の CSV rows は `p._ujicache_auto_rows` に保持する。現在行の表示用状態だけを `STATE` に置く。

主な状態:

- `auto_ujicache_enabled`
- `auto_ujicache_csv`
- `auto_ujicache_active`
- `auto_ujicache_row_index`
- `auto_ujicache_row_name`
- `auto_ujicache_row_count`
- `auto_ujicache_original_n_iter`

## ログ

主なログ:

```text
[UjiCache] auto_uji_prepare rows=...
[UjiCache] auto_uji_seed_template rows=...
[UjiCache] auto_uji_row_start index=...
[UjiCache] auto_uji_csv_error ...
```

## 受け入れ条件

1. Auto Uji OFF 時は通常の UjiCache 生成と同じ挙動になる。
2. UjiCache OFF 時は Auto Uji checkbox が ON でも実行されない。
3. CSV 行ごとに UjiCache 条件が `STATE` に反映される。
4. 行をまたいで `previous_residual` や `residual_history` が共有されない。
5. Auto Uji は UjiCache patch 本体の予測ロジックを変更しない。

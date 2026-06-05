# Auto Uji mode 莉墓ｧ俶嶌 v1.0

## 逶ｮ逧・
Auto Uji mode 縺ｯ縲～UjiCache` 縺ｮ UjiCache 譚｡莉ｶ繧・CSV 陦後＃縺ｨ縺ｫ蛻・ｊ譖ｿ縺医∝酔縺・Generate 謫堺ｽ懊〒隍・焚譚｡莉ｶ繧帝・分縺ｫ隧ｦ縺吶◆繧√・陬懷勧讖溯・縺ｧ縺ゅｋ縲・
## UI

`Auto Uji mode` 縺ｯ `UjiCache` 繧｢繧ｳ繝ｼ繝・ぅ繧ｪ繝ｳ蜀・・繧ｵ繝悶い繧ｳ繝ｼ繝・ぅ繧ｪ繝ｳ縺ｧ縺ゅｋ縲・
```text
UjiCache
  Auto Uji mode
    Enable Auto Uji mode
    Auto Uji CSV
```

Auto Uji mode 縺ｯ隕ｪ縺ｮ `Enable UjiCache` 繧・`Enable UjiCache experiment` 繧定・蜍輔〒 ON 縺ｫ縺励↑縺・ょｮ溯｡後☆繧句ｴ蜷医√Θ繝ｼ繧ｶ繝ｼ縺ｯ騾壼ｸｸ縺ｩ縺翫ｊ荳｡譁ｹ繧・ON 縺ｫ縺吶ｋ縲・
## CSV

MVP 縺ｧ謇ｱ縺・・:

```csv
name,threshold,formula,prediction_strength,slope_ema_smoothing,curve_ema_smoothing,taylor2_curve_strength,apply_prediction_from_skip,use_prediction_after_progress,max_skip_streak,force_full_interval
teacache_ref,0.07,teacache,0.00,0.00,0.00,0.25,2,0.00,0,0
linear_a,0.21,linear,0.50,0.20,0.00,0.25,2,0.00,0,0
taylor2_a,0.21,taylor2,0.50,0.20,0.10,0.25,2,0.00,0,0
```

`formula` 縺ｮ遏ｭ邵ｮ蜷・

- `teacache`, `residual`, `residual_only` -> `TeaCache (residual only)`
- `linear`, `linear_extrapolation` -> `Linear extrapolation`
- `taylor2`, `taylor`, `quadratic` -> `Taylor2 curve`

譛ｪ謖・ｮ壼・縺ｯ Generate 譎らせ縺ｮ UjiCache UI 蛟､繧剃ｽｿ縺・・
## 螳溯｡悟腰菴・
CSV 1 陦後ｒ 1 縺､縺ｮ UjiCache 譚｡莉ｶ縺ｨ縺励※謇ｱ縺・・orge 縺ｮ `batch_size` 縺ｯ邯ｭ謖√＠縲～n_iter` 縺ｯ `CSV陦梧焚 * 蜈・・n_iter` 縺ｫ諡｡蠑ｵ縺吶ｋ縲・
seed set 縺ｯ CSV 陦後＃縺ｨ縺ｫ蜈ｱ譛峨☆繧九ゅ％繧後↓繧医ｊ蜷後§ seed 譚｡莉ｶ縺ｧ UjiCache 繝代Λ繝｡繝ｼ繧ｿ縺縺代ｒ豈碑ｼ・〒縺阪ｋ縲・
## State

螳溯｡御ｸｭ縺ｮ CSV rows 縺ｯ `p._ujicache_auto_rows` 縺ｫ菫晄戟縺吶ｋ縲ら樟蝨ｨ陦後・陦ｨ遉ｺ逕ｨ迥ｶ諷九□縺代ｒ `STATE` 縺ｫ鄂ｮ縺上・
荳ｻ縺ｪ迥ｶ諷・

- `auto_ujicache_enabled`
- `auto_ujicache_csv`
- `auto_ujicache_active`
- `auto_ujicache_row_index`
- `auto_ujicache_row_name`
- `auto_ujicache_row_count`
- `auto_ujicache_original_n_iter`

## 繝ｭ繧ｰ

荳ｻ縺ｪ繝ｭ繧ｰ:

```text
[UjiCache] auto_uji_prepare rows=...
[UjiCache] auto_uji_seed_template rows=...
[UjiCache] auto_uji_row_start index=...
[UjiCache] auto_uji_csv_error ...
```

## 蜿励￠蜈･繧梧擅莉ｶ

1. Auto Uji OFF 譎ゅ・騾壼ｸｸ縺ｮ UjiCache 逕滓・縺ｨ蜷後§謖吝虚縺ｫ縺ｪ繧九・2. UjiCache OFF 譎ゅ・ Auto Uji checkbox 縺・ON 縺ｧ繧ょｮ溯｡後＆繧後↑縺・・3. CSV 陦後＃縺ｨ縺ｫ UjiCache 譚｡莉ｶ縺・`STATE` 縺ｫ蜿肴丐縺輔ｌ繧九・4. 陦後ｒ縺ｾ縺溘＞縺ｧ `previous_residual` 繧・`residual_history` 縺悟・譛峨＆繧後↑縺・・5. Auto Uji 縺ｯ UjiCache patch 譛ｬ菴薙・莠域ｸｬ繝ｭ繧ｸ繝・け繧貞､画峩縺励↑縺・・

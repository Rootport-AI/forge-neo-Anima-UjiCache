# UjiCache 莉墓ｧ俶嶌 v1.2

## 讎りｦ・
`UjiCache` 縺ｯ縲、nima / Cosmos-Predict2 謗ｨ隲紋ｸｭ縺ｮ block stack residual 繧貞・蛻ｩ逕ｨ縺励《kip step 縺ｧ菴ｿ縺・residual 繧定､・焚縺ｮ莠域ｸｬ蠑上〒蟾ｮ縺玲崛縺医※豈碑ｼ・☆繧・Forge Neo 諡｡蠑ｵ縺ｧ縺ゅｋ縲・
迢ｬ遶狗沿縺ｧ縺ｯ縲∵立 `Nz-Anima-PredLab` 縺ｮ螟壽焚縺ｮ螳滄ｨ捺ｩ溯・繧貞・髢九＠縺ｪ縺・・orge UI 縺ｫ谿九☆縺ｮ縺ｯ `UjiCache` 隕ｪ繧｢繧ｳ繝ｼ繝・ぅ繧ｪ繝ｳ縲～Debug log mode` 繧ｵ繝悶い繧ｳ繝ｼ繝・ぅ繧ｪ繝ｳ縲ゞjiCache 謫堺ｽ懃ｾ､縲、uto Uji mode 縺縺代〒縺ゅｋ縲・
## UI

```text
UjiCache
  Enable UjiCache
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

`Debug log mode` 縺ｯ蠑輔″邯壹″繧ｵ繝悶い繧ｳ繝ｼ繝・ぅ繧ｪ繝ｳ縺ｧ縺ゅｋ縲ＡUjiCache` 縺ｯ隕ｪ繧｢繧ｳ繝ｼ繝・ぅ繧ｪ繝ｳ縺ｧ縺ゅｊ縲∵立 PredLab 縺ｮ繧ｵ繝悶い繧ｳ繝ｼ繝・ぅ繧ｪ繝ｳ縺ｧ縺ｯ縺ｪ縺・・
## 莠域ｸｬ蠑・
- `TeaCache (residual only)`: 莠域ｸｬ縺帙★縲∫峩霑代・ full calculation residual 繧偵◎縺ｮ縺ｾ縺ｾ菴ｿ縺・・- `Linear extrapolation`: residual 螻･豁ｴ縺九ｉ荳谺｡螟匁諺縺吶ｋ縲・- `Taylor2 curve`: residual 螻･豁ｴ縺九ｉ莠梧ｬ｡譖ｲ邱壽・蛻・ｒ豺ｷ縺懊ｋ縲・
UjiCache 縺ｯ TeaCache 邉ｻ縺ｮ skip 蛻､螳壹Ο繧ｸ繝・け繧貞・驛ｨ縺ｧ菴ｿ縺・′縲∫峡遶狗沿縺ｧ縺ｯ standalone TeaCache UI 繧貞・髢九＠縺ｪ縺・・
## 螳牙・譚｡莉ｶ

- 隕ｪ Enable 縺・OFF 縺ｮ縺ｨ縺阪・ Forge baseline 繧剃ｿ昴▽縲・- `Enable UjiCache experiment` 縺・OFF 縺ｮ縺ｨ縺阪・ `Anima.forward` patch 繧貞､悶☆縲・- 譛蛻昴・ model call 縺ｯ蠢・★ full calculation 縺ｫ縺吶ｋ縲・- `previous_residual` 縺檎┌縺・ｴ蜷医・ cache 繧剃ｽｿ繧上★ full calculation 縺ｸ謌ｻ縺吶・- residual shape / dtype / device 縺悟粋繧上↑縺・ｴ蜷医・ fallback 縺吶ｋ縲・- unsupported model縲‥isable縲「nload縲‥egraded path 縺ｧ縺ｯ monkey patch 繧貞ｾｩ蜈・☆繧九・- 萓句､悶ｄ fallback 縺ｯ `[UjiCache]` prefix 縺ｧ繝ｭ繧ｰ縺ｫ蜃ｺ縺吶・- Forge Neo 縺・`control` 縺ｪ縺ｩ譛ｪ菴ｿ逕ｨ kwargs 繧・`Anima.forward` 縺ｫ貂｡縺励※繧ゅ√◎繧後ｉ縺ｯ辟｡隕悶☆繧九・
## 繝ｭ繧ｰ

荳ｻ縺ｪ繝ｭ繧ｰ:

```text
[UjiCache] ujicache_config=...
[UjiCache] ujicache_call=...
[UjiCache] ujicache_summary=...
```

`Verbose UjiCache trace` 縺・OFF 縺ｮ蝣ｴ蜷医《tep 縺斐→縺ｮ隧ｳ邏ｰ繝ｭ繧ｰ縺ｯ蜈磯ｭ縺ｮ謨ｰ莉ｶ縺ｫ蛻ｶ髯舌☆繧九Ｔummary 縺ｯ UjiCache 譛牙柑譎ゅ↓蜃ｺ蜉帙☆繧九・
## Metadata

UjiCache 譛牙柑譎ゅ・ PNG infotext 縺ｫ `Uji ...` keys 繧定ｿｽ蜉縺吶ｋ縲・
荳ｻ縺ｪ鬆・岼:

- `Uji enabled`
- `Uji formula`
- `Uji threshold`
- `Uji progress`
- `Uji prediction_strength`
- `Uji slope_ema_smoothing`
- `Uji curve_ema_smoothing`
- `Uji auto_row_index`
- `Uji auto_row_name`

## 螳溯｣・ヵ繧｡繧､繝ｫ

- `scripts/ujicache.py`
- `ujicache/script.py`
- `ujicache/state.py`
- `ujicache/patcher.py`
- `ujicache/diagnostics.py`
- `ujicache/auto_ujicache.py`
- `ujicache/tensor_dump.py`

## 譛蟆乗・蜉滓擅莉ｶ

1. Forge Neo 縺ｫ `UjiCache` 縺ｨ縺励※陦ｨ遉ｺ縺輔ｌ繧九・2. `Debug log mode` 縺後し繝悶い繧ｳ繝ｼ繝・ぅ繧ｪ繝ｳ縺ｨ縺励※陦ｨ遉ｺ縺輔ｌ繧九・3. 譌ｧ PredLab 縺ｮ Attention / TeaCache / Spectrum / Sparse / Cond / Low-bit / Compile UI 縺瑚｡ｨ遉ｺ縺輔ｌ縺ｪ縺・・4. `Enable UjiCache experiment` 縺ｧ UjiCache patch 繧・ON/OFF 縺ｧ縺阪ｋ縲・5. `TeaCache (residual only)` 縺檎峩霑・residual 蜀榊茜逕ｨ縺ｨ縺励※蜍輔￥縲・6. 蛻晏屓 call 縺ｨ missing residual 縺ｯ full calculation 縺ｫ縺ｪ繧九・7. `ujicache_summary` 縺ｧ model_calls / full_calcs / skips / fallbacks / errors / active 繧堤｢ｺ隱阪〒縺阪ｋ縲・

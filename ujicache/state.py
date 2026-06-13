from __future__ import annotations

from dataclasses import dataclass, field
from time import perf_counter
from typing import Any


MODE_OFF = ""
MODE_DIAGNOSE = "Diagnose only"
MODES = [MODE_OFF, MODE_DIAGNOSE]

UJICACHE_PRESET_CUSTOM = "Custom"
UJICACHE_PRESETS = [UJICACHE_PRESET_CUSTOM]

UJICACHE_FORMULA_TEACACHE = "TeaCache (residual only)"
UJICACHE_FORMULA_LINEAR = "Linear extrapolation"
UJICACHE_FORMULA_TAYLOR2 = "Taylor2 curve"
UJICACHE_FORMULAS = [
    UJICACHE_FORMULA_TEACACHE,
    UJICACHE_FORMULA_LINEAR,
    UJICACHE_FORMULA_TAYLOR2,
]

UJICACHE_CACHE_DEVICE_CUDA = "cuda"
UJICACHE_CACHE_DEVICE_CPU = "cpu"
UJICACHE_CACHE_DEVICES = [
    UJICACHE_CACHE_DEVICE_CUDA,
    UJICACHE_CACHE_DEVICE_CPU,
]

UJICACHE_SOURCE_FIRST_BLOCK_SHIFT = "first_block_shift"
UJICACHE_SOURCE_TIMESTEP_EMBEDDING = "timestep_embedding"
UJICACHE_MODULATED_SOURCES = [
    UJICACHE_SOURCE_FIRST_BLOCK_SHIFT,
    UJICACHE_SOURCE_TIMESTEP_EMBEDDING,
]

UJICACHE_PROFILE_ANIMA_2B_30STEP_FIRST_BLOCK_SHIFT = "Anima 2B 30step first_block_shift"
UJICACHE_PROFILE_IDENTITY = "Identity estimate"
UJICACHE_COEFFICIENT_PROFILES = [
    UJICACHE_PROFILE_ANIMA_2B_30STEP_FIRST_BLOCK_SHIFT,
    UJICACHE_PROFILE_IDENTITY,
]

UJICACHE_COEFFICIENTS_ANIMA_2B_30STEP_FIRST_BLOCK_SHIFT = [
    5954.035087553969,
    -2410.0426539290293,
    349.24023850217395,
    -17.264742642375417,
    0.31229336331906893,
]


def ujicache_coefficients_for_profile(profile: str) -> list[float]:
    """Polynomial coefficients (descending powers) for a coefficient profile.

    Single source of truth shared by the runtime skip decision and the read-only
    p_Anima(x) UI display.
    """
    if profile == UJICACHE_PROFILE_IDENTITY:
        return [1.0, 0.0]
    return UJICACHE_COEFFICIENTS_ANIMA_2B_30STEP_FIRST_BLOCK_SHIFT


def ujicache_modulated_source_for_profile(profile: str) -> str:
    """Modulated source is derived from the coefficient profile, not chosen in the UI.

    Identity estimate pairs with timestep_embedding; every other profile uses
    first_block_shift. This is the single source of truth for that mapping.
    """
    if profile == UJICACHE_PROFILE_IDENTITY:
        return UJICACHE_SOURCE_TIMESTEP_EMBEDDING
    return UJICACHE_SOURCE_FIRST_BLOCK_SHIFT


@dataclass
class RuntimeState:
    enabled: bool = False
    debug_log_enabled: bool = False
    mode: str = MODE_OFF
    print_timing_log: bool = True
    verbose_diagnose_log: bool = False
    dump_ujicache_residual: bool = False

    ujicache_enabled: bool = False
    ujicache_preset: str = UJICACHE_PRESET_CUSTOM
    ujicache_threshold: float = 0.07
    ujicache_start_percent: float = 0.05
    ujicache_end_percent: float = 0.95
    ujicache_formula: str = UJICACHE_FORMULA_TEACACHE
    ujicache_use_prediction_after_progress: float = 0.0
    ujicache_apply_prediction_from_skip: int = 2
    ujicache_prediction_strength: float = 0.50
    ujicache_taylor2_curve_strength: float = 0.25
    ujicache_slope_ema_smoothing: float = 0.0
    ujicache_curve_ema_smoothing: float = 0.0
    ujicache_cache_device: str = UJICACHE_CACHE_DEVICE_CUDA
    ujicache_modulated_source: str = UJICACHE_SOURCE_FIRST_BLOCK_SHIFT
    ujicache_coefficient_profile: str = UJICACHE_PROFILE_ANIMA_2B_30STEP_FIRST_BLOCK_SHIFT
    ujicache_max_skip_streak: int = 0
    ujicache_force_full_interval: int = 0
    ujicache_dry_run: bool = False
    ujicache_verbose_trace: bool = False
    capture_calibration_pairs: bool = False

    auto_ujicache_enabled: bool = False
    auto_ujicache_csv: str = ""
    auto_ujicache_active: bool = False
    auto_ujicache_row_index: int | None = None
    auto_ujicache_row_name: str | None = None
    auto_ujicache_row_count: int = 0
    auto_ujicache_original_n_iter: int = 1
    auto_ujicache_parse_error: str | None = None

    status: str = "disabled"
    error_message: str | None = None
    model_detection: Any | None = None
    warned_model_keys: set[str] = field(default_factory=set)
    generation_index: int = 0
    generation_steps: int | None = None
    generation_start: float | None = None
    generation_start_source: str | None = None
    step_start: float | None = None
    step_durations: list[float] = field(default_factory=list)
    denoiser_calls: int = 0
    cond_trace_logged: bool = False

    ujicache_model_calls: int = 0
    ujicache_full_calcs: int = 0
    ujicache_skips: int = 0
    ujicache_skipped_steps: list[int] = field(default_factory=list)
    ujicache_prediction_used: int = 0
    ujicache_fallback_used: int = 0
    ujicache_dry_run_predictions: int = 0
    ujicache_first_full_calcs: int = 0
    ujicache_forced_full_calcs: int = 0
    ujicache_fallbacks: int = 0
    ujicache_errors: int = 0
    ujicache_logged_calls: int = 0
    ujicache_num_blocks: int | None = None
    ujicache_unavailable_reason: str | None = None
    ujicache_fallback_reasons: dict[str, int] = field(default_factory=dict)

    tensor_dump_run_dir: str | None = None
    tensor_dump_initialized: bool = False
    tensor_dump_records: int = 0
    tensor_dump_errors: int = 0
    tensor_dump_unavailable_reason: str | None = None
    tensor_dump_ujicache_local_call_index: int = 0
    tensor_dump_warned_reasons: set[str] = field(default_factory=set)

    calibration_capture_path: str | None = None
    calibration_capture_header_written: bool = False
    calibration_capture_records: int = 0
    calibration_capture_errors: int = 0
    calibration_capture_warned_reasons: set[str] = field(default_factory=set)

    generation_logged: bool = False
    patches: dict[str, Any] = field(default_factory=dict)

    def refresh_settings(self) -> None:
        try:
            from modules import shared

            self.enabled = bool(getattr(shared.opts, "ujicache_enable", False))
            self.debug_log_enabled = bool(
                getattr(shared.opts, "ujicache_debug_log_enable", False)
            )
            mode = getattr(shared.opts, "ujicache_mode", MODE_OFF)
            self.mode = _normalize_mode(mode) if self.debug_log_enabled else MODE_OFF
            self.print_timing_log = bool(
                getattr(shared.opts, "ujicache_print_timing_log", True)
            )
            self.verbose_diagnose_log = bool(
                getattr(shared.opts, "ujicache_verbose_diagnose_log", False)
            )
            self.ujicache_enabled = self.enabled
        except Exception as exc:
            self.enabled = False
            self.ujicache_enabled = False
            self.mode = MODE_OFF
            self.status = "error"
            self.error_message = f"failed to read settings: {exc}"

    def apply_options(
        self,
        enabled: bool,
        debug_log_enabled: bool,
        mode: str,
        print_timing_log: bool,
        verbose_diagnose_log: bool,
        dump_ujicache_residual: bool,
        ujicache_preset: str = UJICACHE_PRESET_CUSTOM,
        ujicache_threshold: float = 0.07,
        ujicache_start_percent: float = 0.05,
        ujicache_end_percent: float = 0.95,
        ujicache_formula: str = UJICACHE_FORMULA_TEACACHE,
        ujicache_use_prediction_after_progress: float = 0.0,
        ujicache_apply_prediction_from_skip: int = 2,
        ujicache_prediction_strength: float = 0.50,
        ujicache_taylor2_curve_strength: float = 0.25,
        ujicache_slope_ema_smoothing: float = 0.0,
        ujicache_curve_ema_smoothing: float = 0.0,
        ujicache_cache_device: str = UJICACHE_CACHE_DEVICE_CUDA,
        ujicache_coefficient_profile: str = UJICACHE_PROFILE_ANIMA_2B_30STEP_FIRST_BLOCK_SHIFT,
        ujicache_max_skip_streak: int = 0,
        ujicache_force_full_interval: int = 0,
        ujicache_dry_run: bool = False,
        ujicache_verbose_trace: bool = False,
        auto_ujicache_enabled: bool = False,
        auto_ujicache_csv: str = "",
        capture_calibration_pairs: bool = False,
    ) -> None:
        self.enabled = bool(enabled)
        self.debug_log_enabled = bool(debug_log_enabled)
        self.mode = _normalize_mode(mode) if self.debug_log_enabled else MODE_OFF
        self.print_timing_log = bool(print_timing_log)
        self.verbose_diagnose_log = bool(verbose_diagnose_log)
        self.dump_ujicache_residual = bool(dump_ujicache_residual)

        self.ujicache_enabled = self.enabled
        self.ujicache_preset = (
            ujicache_preset if ujicache_preset in UJICACHE_PRESETS else UJICACHE_PRESET_CUSTOM
        )
        self.ujicache_threshold = _clamp_float(ujicache_threshold, 0.0, 1.0)
        self.ujicache_start_percent = _clamp_float(ujicache_start_percent, 0.0, 1.0)
        self.ujicache_end_percent = _clamp_float(ujicache_end_percent, 0.0, 1.0)
        if self.ujicache_start_percent > self.ujicache_end_percent:
            self.ujicache_start_percent, self.ujicache_end_percent = (
                self.ujicache_end_percent,
                self.ujicache_start_percent,
            )
        self.ujicache_formula = (
            ujicache_formula if ujicache_formula in UJICACHE_FORMULAS else UJICACHE_FORMULA_TEACACHE
        )
        self.ujicache_use_prediction_after_progress = _clamp_float(
            ujicache_use_prediction_after_progress,
            0.0,
            1.0,
        )
        self.ujicache_apply_prediction_from_skip = _clamp_int(
            ujicache_apply_prediction_from_skip,
            1,
            3,
        )
        self.ujicache_prediction_strength = _clamp_float(ujicache_prediction_strength, 0.0, 1.0)
        self.ujicache_taylor2_curve_strength = _clamp_float(ujicache_taylor2_curve_strength, 0.0, 1.0)
        self.ujicache_slope_ema_smoothing = _clamp_float(ujicache_slope_ema_smoothing, 0.0, 0.99)
        self.ujicache_curve_ema_smoothing = _clamp_float(ujicache_curve_ema_smoothing, 0.0, 0.99)
        self.ujicache_cache_device = (
            ujicache_cache_device
            if ujicache_cache_device in UJICACHE_CACHE_DEVICES
            else UJICACHE_CACHE_DEVICE_CUDA
        )
        self.ujicache_coefficient_profile = (
            ujicache_coefficient_profile
            if ujicache_coefficient_profile in UJICACHE_COEFFICIENT_PROFILES
            else UJICACHE_PROFILE_ANIMA_2B_30STEP_FIRST_BLOCK_SHIFT
        )
        self.ujicache_modulated_source = ujicache_modulated_source_for_profile(
            self.ujicache_coefficient_profile
        )
        self.ujicache_max_skip_streak = _clamp_int(ujicache_max_skip_streak, 0, 64)
        self.ujicache_force_full_interval = _clamp_int(ujicache_force_full_interval, 0, 64)
        self.ujicache_dry_run = bool(ujicache_dry_run)
        self.ujicache_verbose_trace = bool(ujicache_verbose_trace)

        self.auto_ujicache_enabled = bool(auto_ujicache_enabled) and self.ujicache_enabled
        self.auto_ujicache_csv = str(auto_ujicache_csv or "")
        self.capture_calibration_pairs = bool(capture_calibration_pairs)

    def active(self) -> bool:
        return (
            self.ujicache_enabled
            or (self.debug_log_enabled and self.mode != MODE_OFF)
            or self.tensor_dump_active()
        )

    def tensor_dump_requested(self) -> bool:
        return self.dump_ujicache_residual or self.capture_calibration_pairs

    def calibration_capture_active(self) -> bool:
        return self.enabled and self.debug_log_enabled and self.capture_calibration_pairs

    def tensor_dump_active(self) -> bool:
        return self.enabled and self.debug_log_enabled and self.tensor_dump_requested()

    def reset_generation(self, source: str = "unknown") -> None:
        self.generation_index += 1
        self.generation_steps = None
        self.generation_start = perf_counter()
        self.generation_start_source = source
        self.step_start = None
        self.step_durations.clear()
        self.denoiser_calls = 0
        self.cond_trace_logged = False
        self.ujicache_model_calls = 0
        self.ujicache_full_calcs = 0
        self.ujicache_skips = 0
        self.ujicache_skipped_steps.clear()
        self.ujicache_prediction_used = 0
        self.ujicache_fallback_used = 0
        self.ujicache_dry_run_predictions = 0
        self.ujicache_first_full_calcs = 0
        self.ujicache_forced_full_calcs = 0
        self.ujicache_fallbacks = 0
        self.ujicache_errors = 0
        self.ujicache_logged_calls = 0
        self.ujicache_num_blocks = None
        self.ujicache_unavailable_reason = None
        self.ujicache_fallback_reasons.clear()
        self.tensor_dump_run_dir = None
        self.tensor_dump_initialized = False
        self.tensor_dump_records = 0
        self.tensor_dump_errors = 0
        self.tensor_dump_unavailable_reason = None
        self.tensor_dump_ujicache_local_call_index = 0
        self.tensor_dump_warned_reasons.clear()
        self.calibration_capture_path = None
        self.calibration_capture_header_written = False
        self.calibration_capture_records = 0
        self.calibration_capture_errors = 0
        self.calibration_capture_warned_reasons.clear()
        self.generation_logged = False
        self.error_message = None

        if not self.enabled:
            self.status = "disabled"
        elif self.ujicache_enabled:
            self.status = "experimental-ujicache"
        elif self.mode == MODE_DIAGNOSE:
            self.status = "diagnosing"
        else:
            self.status = "disabled"

    def mark_step_start(self) -> None:
        self.step_start = perf_counter()
        self.denoiser_calls += 1

    def mark_step_end(self) -> None:
        if self.step_start is None:
            return
        self.step_durations.append(perf_counter() - self.step_start)
        self.step_start = None

    def total_sampling_time(self) -> float | None:
        if self.generation_start is None:
            return None
        return perf_counter() - self.generation_start

    def avg_step_time(self) -> float | None:
        if not self.step_durations:
            return None
        return sum(self.step_durations) / len(self.step_durations)

    def set_error(self, message: str) -> None:
        self.status = "error"
        self.error_message = message


STATE = RuntimeState()


def _clamp_int(value: Any, minimum: int, maximum: int) -> int:
    try:
        number = int(value)
    except Exception:
        number = minimum
    return max(minimum, min(maximum, number))


def _clamp_float(value: Any, minimum: float, maximum: float) -> float:
    try:
        number = float(value)
    except Exception:
        number = minimum
    return max(minimum, min(maximum, number))


def _normalize_mode(value: Any) -> str:
    text = str(value or MODE_OFF)
    if text == "Off":
        return MODE_OFF
    return text if text in MODES else MODE_OFF

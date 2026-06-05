from __future__ import annotations

from .state import MODE_OFF, MODES

SECTION = ("ujicache", "UjiCache -Prototype")


def on_ui_settings() -> None:
    import gradio as gr
    from modules import shared

    def add_option_once(key, info) -> None:
        if key in getattr(shared.opts, "data_labels", {}):
            return
        shared.opts.add_option(key, info)

    add_option_once(
        "ujicache_enable",
        shared.OptionInfo(
            False,
            "Enable UjiCache -Prototype",
            section=SECTION,
        ),
    )
    add_option_once(
        "ujicache_debug_log_enable",
        shared.OptionInfo(
            True,
            "Enable debug log mode",
            section=SECTION,
        ),
    )
    add_option_once(
        "ujicache_mode",
        shared.OptionInfo(
            MODE_OFF,
            "Debug log mode",
            component=gr.Dropdown,
            component_args={"choices": MODES},
            section=SECTION,
        ),
    )
    add_option_once(
        "ujicache_print_timing_log",
        shared.OptionInfo(
            True,
            "Print timing log",
            section=SECTION,
        ),
    )
    add_option_once(
        "ujicache_verbose_diagnose_log",
        shared.OptionInfo(
            False,
            "Verbose diagnose log",
            section=SECTION,
        ),
    )

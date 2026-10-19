"""Generate the two dependency-free SVG figures used by the README."""

from __future__ import annotations

import csv
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def write_bar_chart(
    output: Path,
    title: str,
    labels: list[str],
    series: list[tuple[str, list[float], str]],
    x_label: str,
) -> None:
    width = 1100
    left = 330
    right = 70
    top = 95
    row_height = 48
    bottom = 75
    plot_width = width - left - right
    height = top + row_height * len(labels) + bottom
    maximum = max(value for _, values, _ in series for value in values) * 1.08
    bar_height = 15 if len(series) > 1 else 24

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#202124}.title{font-size:26px;font-weight:600}.label{font-size:15px}.axis{font-size:13px;fill:#5f6368}.legend{font-size:14px}</style>',
        f'<text x="{left}" y="42" class="title">{escape(title)}</text>',
    ]

    ticks = 5
    for index in range(ticks + 1):
        value = maximum * index / ticks
        x = left + plot_width * index / ticks
        lines.append(f'<line x1="{x:.1f}" y1="{top-12}" x2="{x:.1f}" y2="{height-bottom}" stroke="#e5e7eb"/>')
        lines.append(f'<text x="{x:.1f}" y="{height-bottom+23}" text-anchor="middle" class="axis">{value:.0f}</text>')

    offsets = [-(len(series) - 1) * 9 + 18 * index for index in range(len(series))]
    for row, label in enumerate(labels):
        center = top + row * row_height + row_height / 2
        lines.append(f'<text x="{left-14}" y="{center+5:.1f}" text-anchor="end" class="label">{escape(label)}</text>')
        for index, (_, values, color) in enumerate(series):
            value = values[row]
            bar_width = plot_width * value / maximum
            y = center + offsets[index] - bar_height / 2
            lines.append(f'<rect x="{left}" y="{y:.1f}" width="{bar_width:.1f}" height="{bar_height}" rx="3" fill="{color}"/>')
            lines.append(f'<text x="{left+bar_width+7:.1f}" y="{y+bar_height-2:.1f}" class="axis">{value:.2f}</text>')

    legend_x = left
    for name, _, color in series:
        lines.append(f'<rect x="{legend_x}" y="58" width="13" height="13" rx="2" fill="{color}"/>')
        lines.append(f'<text x="{legend_x+19}" y="70" class="legend">{escape(name)}</text>')
        legend_x += 180
    lines.append(f'<text x="{left+plot_width/2:.1f}" y="{height-18}" text-anchor="middle" class="axis">{escape(x_label)}</text>')
    lines.append("</svg>")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def model_comparison() -> None:
    rows = read_csv(ROOT / "results" / "model_comparison.csv")[1:]
    write_bar_chart(
        ASSETS / "model_comparison.svg",
        "Shared model comparison",
        [row["approach"] for row in rows],
        [
            ("Development CV", [float(row["development_cv_smape"]) for row in rows], "#4C78A8"),
            ("Holdout", [float(row["holdout_smape"]) for row in rows], "#F58518"),
        ],
        "Average sMAPE (lower is better)",
    )


def per_target() -> None:
    rows = sorted(
        read_csv(ROOT / "results" / "per_target_holdout_smape.csv"),
        key=lambda row: float(row["smape"]),
    )
    write_bar_chart(
        ASSETS / "per_target_smape.svg",
        "Final model error by target",
        [row["target"] for row in rows],
        [("Holdout sMAPE", [float(row["smape"]) for row in rows], "#4C78A8")],
        "Holdout sMAPE",
    )


if __name__ == "__main__":
    model_comparison()
    per_target()
    print("Generated README figures")

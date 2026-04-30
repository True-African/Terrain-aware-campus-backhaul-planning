import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "radio_mobile_expanded_results.csv"
OUT = ROOT / "data" / "validation_metrics.csv"
SUMMARY = ROOT / "data" / "validation_summary.md"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)


def f(x):
    return float(x)


rows = []
with DATA.open(newline="", encoding="utf-8-sig") as fp:
    for row in csv.DictReader(fp):
        row["height"] = f(row["height_tx_m"])
        row["gain"] = f(row["gain_tx_dbi"])
        row["freq"] = f(row["frequency_mhz"])
        row["distance"] = f(row["distance_km"])
        row["tx_power_dbm"] = f(row["tx_power_dbm"])
        row["tx_loss"] = f(row["line_loss_tx_db"])
        row["rx_loss"] = f(row["line_loss_rx_db"])
        row["rx_signal_rm"] = f(row["received_signal_dbm"])
        row["rx_sens"] = f(row["receiver_sensitivity_dbm"])
        row["fade_rm"] = f(row["fade_margin_db"])
        row["fspl_rm"] = f(row["free_space_loss_db"])
        row["total_loss_rm"] = f(row["total_path_loss_db"])
        row["terrain_stat_loss"] = row["total_loss_rm"] - row["fspl_rm"]
        row["fspl_model"] = 32.44 + 20 * math.log10(row["distance"]) + 20 * math.log10(row["freq"])
        row["rx_fspl_only"] = (
            row["tx_power_dbm"]
            + row["gain"]
            + row["gain"]
            - row["tx_loss"]
            - row["rx_loss"]
            - row["fspl_model"]
        )
        rows.append(row)

avg_corr = sum(r["terrain_stat_loss"] for r in rows) / len(rows)
height_corr = {}
for h in sorted({r["height"] for r in rows}):
    subset = [r for r in rows if r["height"] == h]
    height_corr[h] = sum(r["terrain_stat_loss"] for r in subset) / len(subset)

for r in rows:
    r["rx_avg_corr"] = (
        r["tx_power_dbm"]
        + r["gain"]
        + r["gain"]
        - r["tx_loss"]
        - r["rx_loss"]
        - (r["fspl_model"] + avg_corr)
    )
    r["rx_height_corr"] = (
        r["tx_power_dbm"]
        + r["gain"]
        + r["gain"]
        - r["tx_loss"]
        - r["rx_loss"]
        - (r["fspl_model"] + height_corr[r["height"]])
    )
    r["fade_fspl_only"] = r["rx_fspl_only"] - r["rx_sens"]
    r["fade_avg_corr"] = r["rx_avg_corr"] - r["rx_sens"]
    r["fade_height_corr"] = r["rx_height_corr"] - r["rx_sens"]


def metrics(pred_key, fade_key, fm_req):
    errors = [r[pred_key] - r["rx_signal_rm"] for r in rows]
    fade_errors = [r[fade_key] - r["fade_rm"] for r in rows]
    mae = sum(abs(e) for e in errors) / len(errors)
    rmse = math.sqrt(sum(e * e for e in errors) / len(errors))
    fm_mae = sum(abs(e) for e in fade_errors) / len(fade_errors)
    agree = sum((r[fade_key] >= fm_req) == (r["fade_rm"] >= fm_req) for r in rows) / len(rows)
    return mae, rmse, fm_mae, agree


metric_rows = []
for label, pred_key, fade_key in [
    ("FSPL only", "rx_fspl_only", "fade_fspl_only"),
    ("FSPL plus average terrain/statistical correction", "rx_avg_corr", "fade_avg_corr"),
    ("FSPL plus height-calibrated correction", "rx_height_corr", "fade_height_corr"),
]:
    for fm_req in (20, 30):
        mae, rmse, fm_mae, agree = metrics(pred_key, fade_key, fm_req)
        metric_rows.append(
            {
                "model": label,
                "required_fade_margin_db": fm_req,
                "mae_received_signal_db": f"{mae:.3f}",
                "rmse_received_signal_db": f"{rmse:.3f}",
                "mae_fade_margin_db": f"{fm_mae:.3f}",
                "feasibility_agreement": f"{agree:.3f}",
            }
        )

with OUT.open("w", newline="", encoding="utf-8") as fp:
    writer = csv.DictWriter(fp, fieldnames=list(metric_rows[0].keys()))
    writer.writeheader()
    writer.writerows(metric_rows)

with (ROOT / "data" / "radio_mobile_expanded_with_model.csv").open("w", newline="", encoding="utf-8") as fp:
    fieldnames = list(rows[0].keys())
    writer = csv.DictWriter(fp, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)


def by_gain(gain):
    return sorted([r for r in rows if r["gain"] == gain], key=lambda r: r["height"])


plt.figure(figsize=(7.2, 4.8))
for gain in sorted({r["gain"] for r in rows}):
    subset = by_gain(gain)
    plt.plot([r["height"] for r in subset], [r["rx_signal_rm"] for r in subset], marker="o", label=f"{gain:.0f} dBi")
plt.xlabel("Antenna height (m)")
plt.ylabel("Received signal (dBm)")
plt.title("Radio Mobile received signal at 5825 MHz")
plt.grid(True, alpha=0.35)
plt.legend(title="Antenna gain")
plt.tight_layout()
plt.savefig(FIG / "received_signal_vs_height.png", dpi=300)
plt.close()

plt.figure(figsize=(7.2, 4.8))
for gain in sorted({r["gain"] for r in rows}):
    subset = by_gain(gain)
    plt.plot([r["height"] for r in subset], [r["fade_rm"] for r in subset], marker="o", label=f"{gain:.0f} dBi")
plt.axhline(20, color="tab:red", linestyle="--", linewidth=1.2, label="20 dB threshold")
plt.axhline(30, color="tab:green", linestyle="--", linewidth=1.2, label="30 dB threshold")
plt.xlabel("Antenna height (m)")
plt.ylabel("Fade margin (dB)")
plt.title("Fade margin sensitivity to height and gain")
plt.grid(True, alpha=0.35)
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig(FIG / "fade_margin_vs_height.png", dpi=300)
plt.close()

heights = sorted({r["height"] for r in rows})
gains = sorted({r["gain"] for r in rows})
z = [[next(r["fade_rm"] for r in rows if r["height"] == h and r["gain"] == g) for g in gains] for h in heights]
plt.figure(figsize=(7.2, 4.8))
im = plt.imshow(z, origin="lower", aspect="auto", cmap="viridis")
plt.xticks(range(len(gains)), [f"{g:.0f}" for g in gains])
plt.yticks(range(len(heights)), [f"{h:.0f}" for h in heights])
plt.xlabel("Antenna gain (dBi)")
plt.ylabel("Antenna height (m)")
plt.title("Fade margin heatmap")
for yi, h in enumerate(heights):
    for xi, g in enumerate(gains):
        plt.text(xi, yi, f"{z[yi][xi]:.1f}", ha="center", va="center", color="white" if z[yi][xi] < 32 else "black", fontsize=8)
plt.colorbar(im, label="Fade margin (dB)")
plt.tight_layout()
plt.savefig(FIG / "fade_margin_heatmap.png", dpi=300)
plt.close()

plt.figure(figsize=(7.2, 4.8))
for model, key in [
    ("FSPL only", "rx_fspl_only"),
    ("Avg correction", "rx_avg_corr"),
    ("Height correction", "rx_height_corr"),
]:
    errors = [r[key] - r["rx_signal_rm"] for r in rows]
    plt.scatter([r["height"] for r in rows], errors, label=model, alpha=0.8)
plt.axhline(0, color="black", linewidth=1)
plt.xlabel("Antenna height (m)")
plt.ylabel("Received-signal prediction error (dB)")
plt.title("Analytical model error against Radio Mobile")
plt.grid(True, alpha=0.35)
plt.legend()
plt.tight_layout()
plt.savefig(FIG / "model_error_by_height.png", dpi=300)
plt.close()

cost_rows = []
for r in rows:
    cost = 0.55 * (r["height"] / max(heights)) + 0.45 * (r["gain"] / max(gains))
    cost_rows.append((cost, r["fade_rm"], r["height"], r["gain"], r["run_id"]))

plt.figure(figsize=(7.2, 4.8))
plt.scatter([c[0] for c in cost_rows], [c[1] for c in cost_rows], c=[c[2] for c in cost_rows], cmap="plasma", edgecolor="black", linewidth=0.3)
plt.axhline(20, color="tab:red", linestyle="--", linewidth=1.2)
plt.axhline(30, color="tab:green", linestyle="--", linewidth=1.2)
plt.xlabel("Normalized deployment burden")
plt.ylabel("Fade margin (dB)")
plt.title("Deployment burden versus fade margin")
plt.colorbar(label="Antenna height (m)")
plt.tight_layout()
plt.savefig(FIG / "cost_vs_fade_margin.png", dpi=300)
plt.close()

best20 = min((c for c in cost_rows if c[1] >= 20), key=lambda x: x[0])
best30 = min((c for c in cost_rows if c[1] >= 30), key=lambda x: x[0])

SUMMARY.write_text(
    "\n".join(
        [
            "# Validation Summary",
            "",
            f"Rows analyzed: {len(rows)}",
            f"Average terrain/statistical correction: {avg_corr:.2f} dB",
            "",
            "## Best feasible designs using normalized deployment burden",
            "",
            f"- Minimum-cost design for 20 dB fade margin: {best20[4]}, height {best20[2]:.0f} m, gain {best20[3]:.0f} dBi, fade margin {best20[1]:.2f} dB, cost {best20[0]:.3f}.",
            f"- Minimum-cost design for 30 dB fade margin: {best30[4]}, height {best30[2]:.0f} m, gain {best30[3]:.0f} dBi, fade margin {best30[1]:.2f} dB, cost {best30[0]:.3f}.",
            "",
            "## Model validation metrics",
            "",
            "| Model | Required fade margin (dB) | MAE Rx (dB) | RMSE Rx (dB) | MAE fade margin (dB) | Feasibility agreement |",
            "|---|---:|---:|---:|---:|---:|",
            *[
                f"| {m['model']} | {m['required_fade_margin_db']} | {m['mae_received_signal_db']} | {m['rmse_received_signal_db']} | {m['mae_fade_margin_db']} | {m['feasibility_agreement']} |"
                for m in metric_rows
            ],
            "",
            "The height-calibrated correction is expected to fit Radio Mobile closely because the Radio Mobile terrain/statistical loss is constant across gain at a fixed height. This should be reported as simulation calibration, not field validation.",
            "",
        ]
    ),
    encoding="utf-8",
)

print(SUMMARY.read_text(encoding="utf-8"))

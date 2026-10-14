#!/usr/bin/env python3
"""Create portfolio-ready charts from a scraped books CSV."""

from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def save_price_distribution(df: pd.DataFrame, out: Path) -> bool:
    if "price_gbp" not in df or df["price_gbp"].dropna().empty:
        return False
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.hist(df["price_gbp"].dropna(), bins=min(20, max(5, int(len(df) ** 0.5))), edgecolor="black")
    ax.set_title("Book Price Distribution", pad=12)
    ax.set_xlabel("Price (GBP)")
    ax.set_ylabel("Number of books")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(out / "price_distribution.png", dpi=180, bbox_inches="tight")
    plt.close(fig)
    return True


def save_rating_counts(df: pd.DataFrame, out: Path) -> bool:
    if "rating" not in df or df["rating"].dropna().empty:
        return False
    counts = df["rating"].dropna().astype(int).value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(counts.index.astype(str), counts.values, edgecolor="black")
    ax.set_title("Number of Books by Rating", pad=12)
    ax.set_xlabel("Rating (1–5 stars)")
    ax.set_ylabel("Number of books")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(out / "rating_counts.png", dpi=180, bbox_inches="tight")
    plt.close(fig)
    return True


def save_top_categories(df: pd.DataFrame, out: Path) -> bool:
    if "category" not in df or df["category"].dropna().empty:
        return False
    counts = df["category"].dropna().value_counts().head(10).sort_values()
    fig, ax = plt.subplots(figsize=(9, max(4.5, 0.45 * len(counts))))
    ax.barh(counts.index.astype(str), counts.values, edgecolor="black")
    ax.set_title("Top Book Categories", pad=12)
    ax.set_xlabel("Number of books")
    ax.set_ylabel("Category")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(out / "top_categories.png", dpi=180, bbox_inches="tight")
    plt.close(fig)
    return True


def save_price_rating(df: pd.DataFrame, out: Path) -> bool:
    if not {"price_gbp", "rating"}.issubset(df.columns):
        return False
    pair = df[["price_gbp", "rating"]].dropna()
    if pair.empty:
        return False
    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.scatter(pair["rating"], pair["price_gbp"], alpha=0.8)
    ax.set_title("Book Price vs Rating", pad=12)
    ax.set_xlabel("Rating (1–5 stars)")
    ax.set_ylabel("Price (GBP)")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(out / "price_vs_rating.png", dpi=180, bbox_inches="tight")
    plt.close(fig)
    return True


def save_average_price(df: pd.DataFrame, out: Path) -> bool:
    if not {"price_gbp", "rating"}.issubset(df.columns):
        return False
    pair = df[["price_gbp", "rating"]].dropna()
    if pair.empty:
        return False
    means = pair.groupby("rating")["price_gbp"].mean().sort_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(means.index.astype(str), means.values, edgecolor="black")
    ax.set_title("Average Book Price by Rating", pad=12)
    ax.set_xlabel("Rating (1–5 stars)")
    ax.set_ylabel("Average price (GBP)")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(out / "average_price_by_rating.png", dpi=180, bbox_inches="tight")
    plt.close(fig)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Visualize a scraped books CSV.")
    parser.add_argument("--input", type=Path, default=Path("data/books_sample.csv"))
    parser.add_argument("--output-dir", type=Path, default=Path("reports/charts"))
    args = parser.parse_args()
    if not args.input.exists():
        parser.error(f"Input file not found: {args.input}")

    df = pd.read_csv(args.input)
    df.columns = [str(c).strip().lower() for c in df.columns]
    for col in ("price_gbp", "rating"):
        if col in df:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    generated = []
    for func in (save_price_distribution, save_rating_counts, save_top_categories,
                 save_price_rating, save_average_price):
        if func(df, args.output_dir):
            generated.append(func.__name__.replace("save_", ""))

    lines = [
        "DATA VISUALIZATION SUMMARY",
        f"Input: {args.input}",
        f"Rows: {len(df)}",
        f"Columns: {len(df.columns)}",
        f"Charts generated: {', '.join(generated) if generated else 'None; check required columns'}",
    ]
    if "price_gbp" in df and df["price_gbp"].notna().any():
        lines.append(f"Average price: GBP {df['price_gbp'].mean():.2f}")
        lines.append(f"Median price: GBP {df['price_gbp'].median():.2f}")
    if "rating" in df and df["rating"].notna().any():
        lines.append("Rating counts:")
        lines.append(df["rating"].value_counts().sort_index().to_string())
    if "category" in df and df["category"].notna().any():
        lines.append("Most frequent categories:")
        lines.append(df["category"].value_counts().head(5).to_string())
    lines += [
        "",
        "Interpretation note: the bundled sample is illustrative and small.",
        "Use the full scraped dataset before drawing broad conclusions.",
        "Charts show patterns or associations and do not establish causation.",
    ]
    (args.output_dir / "visualization_summary.txt").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(f"\n[DONE] Outputs saved to: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()

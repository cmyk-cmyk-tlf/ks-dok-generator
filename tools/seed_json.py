import csv, json
from collections import defaultdict
from pathlib import Path

# Map CSV filename -> output JSON filename
SUBJECT_MAP = {
    "ELA.csv": "ELA.json",
    "Math.csv": "Math.json",
    "Science.csv": "Science.json",
    "SocialStudies.csv": "SocialStudies.json",
}

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "standards"
OUT.mkdir(exist_ok=True)

def rows_for(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            yield {
                "subject": r["subject"].strip(),
                "grade": r["grade_or_band"].strip(),
                "code": r["code"].strip(),
                "statement": r["statement"].strip(),
            }

def build_json_by_grade(rows):
    grades = defaultdict(list)  # {"5": ["RL.5.1 – ...", ...], "HS": [...]}
    for r in rows:
        grades[r["grade"]].append(f'{r["code"]} – {r["statement"]}')
    # sort keys naturally (K, 1, 2, ... HS, 9-10, etc.)
    def sort_key(k):
        order = {"K": -1, "K-2": -2, "3-5": -3, "MS": 98, "HS": 99}
        if k in order: return order[k]
        try: return int(k.split("-")[0])
        except: return 100
    out = {"grades": {k: grades[k] for k in sorted(grades.keys(), key=sort_key)}}
    return out

def main():
    for csv_name, out_name in SUBJECT_MAP.items():
        csv_path = DATA / csv_name
        if not csv_path.exists():
            print(f"Skip: {csv_name} not found")
            continue
        js = build_json_by_grade(list(rows_for(csv_path)))
        with open(OUT / out_name, "w", encoding="utf-8") as f:
            json.dump(js, f, ensure_ascii=False, indent=2)
        print(f"Wrote {out_name} with {sum(len(v) for v in js['grades'].values())} standards")

if __name__ == "__main__":
    main()


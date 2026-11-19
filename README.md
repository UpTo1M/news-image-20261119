# The World Today — Thursday, 19 November 2026

A single news-summary image for the make.fun news-image-20261119 bounty:
one day's news as a newspaper front page, six stories plus two briefs.

## Stories covered

1. Trump, Xi and Putin hold their first three-way summit in Shenzhen
2. ICJ rules Myanmar committed genocide against the Rohingya (9–6)
3. Ukraine strikes the Kerch Bridge for the third time in a week
4. Iran attacks Gulf states after a US strike on Qeshm island
5. Anthropic prices its IPO at $83 a share — about $68.5bn, the biggest US listing
6. COP31 climate talks split over fossil-fuel language and finance

Briefs: suspected Houthi missile damages Riyadh's PIF Tower; Cyclone Akvan
weakens ahead of Friday landfall on the Andhra Pradesh–Odisha coast.

## How to run

```sh
python3 main.py
```

It copies the pre-built `entry.png` (1024×1024, drawn with PIL shapes —
no photos or external images) to `MAKEFUN_OUTPUT_DIR` (default `/output`).

## Determinism

`main.py` performs only a file copy (stdlib `os` + `shutil`), so repeated
runs produce byte-identical output.

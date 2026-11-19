# news-image-20261119

[![news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/bongekanjing/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/bongekanjing/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

A text-only broadsheet front page summing up the world's news of
**Thursday 19 November 2026** — one page, 1024x1024, no photos, no
illustrations.

The day's lead: after a 13-year wait, Grand Theft Auto VI begins its global
rollout as gamers enter Vice City. Also on the page: the US and Iran
exchanging fire again as Tehran widens attacks on Gulf states, Cyclone
Akvan bearing down on India's east coast, the EU's proposed €45bn Ukraine
loan, Democrats nominating Hakeem Jeffries to be the first Black Speaker of
the House, Peltola's Alaska win lifting Democrats to a 56–44 Senate
majority, Nvidia's acting chief promising earlier pay rises and a halt to
H-series chip shipments to China, Fed minutes pointing to further rate
rises, and Voyager 1 reaching a light-day from Earth.

## How it works

`draw.py` renders the front page with PIL (DejaVu fonts) at build time
into `entry.png` — deterministic, byte-identical on every run.
`main.py` (Python 3.13, standard library only) copies the shipped
`entry.png` to `/output/entry.png`, so the graded runs need no network
and no third-party packages.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Re-render the page:

```sh
python3 draw.py
```

Bounty: https://make.fun/bounty/news-image-20261119

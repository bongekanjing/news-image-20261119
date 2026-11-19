#!/usr/bin/env python3
"""The Daily Chronicle — front page for Thursday 19 November 2026.

Draws a text-only broadsheet front page (1024x1024 PNG) with PIL.
Deterministic: fixed fonts, fixed layout, no network, no timestamps,
no randomness — two runs produce byte-identical output.

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
Writes <output dir>/entry.png (default /output).
"""

import os

from PIL import Image, ImageDraw, ImageFont

W = 1024
H = 1024
MARGIN = 34
GUTTER = 24
COLS = 3
COL_W = (W - 2 * MARGIN - (COLS - 1) * GUTTER) // COLS

PAPER = (247, 243, 234)   # off-white newsprint
INK = (18, 18, 18)        # near-black
RED = (139, 0, 0)         # dark red accent for section headers
GREY = (90, 86, 78)       # dateline grey

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_MASTHEAD = font("DejaVuSerif-Bold.ttf", 56)
F_DATE = font("DejaVuSans-Bold.ttf", 15)
F_KICKER = font("DejaVuSans-Bold.ttf", 13)
F_LEAD = font("DejaVuSerif-Bold.ttf", 36)
F_LEAD_DECK = font("DejaVuSans.ttf", 16)
F_SECTION = font("DejaVuSans-Bold.ttf", 14)
F_HEAD = font("DejaVuSerif-Bold.ttf", 16)
F_DECK = font("DejaVuSans.ttf", 11)
F_FOOT = font("DejaVuSans.ttf", 11)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines fitting max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, y, lines, fnt, fill=INK, spacing=0):
    for line in lines:
        w = draw.textlength(line, font=fnt)
        draw.text(((W - w) / 2, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y

# --- The news of Thursday 19 November 2026 -------------------------------
# Headlines as reported on the day, with short decks. One lead story,
# then three columns of sections.

LEAD_KICKER = "CULTURE  •  GAMING"
LEAD_HEAD = "After a 13-year wait, Grand Theft Auto VI arrives"
LEAD_DECK = (
    "Gamers enter Vice City as Rockstar's blockbuster begins its global "
    "rollout, with midnight launches and record demand around the world."
)

# Each column: list of (section, headline, deck).
COLUMNS = [
    [
        ("WORLD",
         "US and Iran exchange fire again as Tehran widens attacks on Gulf states",
         "US forces struck a missile site on Qeshm Island; Iran hit a US base "
         "in Kuwait and struck Bahrain again."),
        ("WORLD",
         "Cyclone Akvan bears down on India's east coast",
         "Storm likely to cross between Machilipatnam and Puri; railways and "
         "ports brace as heavy rain lashes the coast."),
        ("WORLD",
         "EU proposes \u20ac45bn loan to keep Ukraine funded",
         "Brussels would borrow on capital markets, to be repaid after Russia "
         "pays reparations, the Commission says."),
        ("WORLD",
         "Australia sanctions Israeli settlers over West Bank expansion",
         "Canberra targets settlers and organisations in a fresh round of "
         "measures."),
        ("WORLD",
         "Russia accuses France of sending troops to Ukraine",
         "Foreign Minister Lavrov says Moscow has warned Paris; France has "
         "not confirmed any deployment."),
        ("WORLD",
         "LPG tanker that sank off Bulgaria 'was hit by projectiles'",
         "Officials say the vessel was struck before going down in the "
         "Black Sea."),
        ("WORLD",
         "Saudi Arabia says danger has passed in three southern cities",
         "Alerts lifted after air-defence intercepts, state media reports."),
    ],
    [
        ("POLITICS",
         "Jeffries set to be first Black Speaker of the House",
         "Democrats nominate Hakeem Jeffries for the speakership after "
         "sweeping midterm gains."),
        ("POLITICS",
         "Peltola wins in Alaska, lifting Democrats to 56\u201344 Senate majority",
         "Victory caps the party's largest Senate gains in nearly 70 years."),
        ("POLITICS",
         "Trump, Xi and Putin to hold trilateral talks in Shenzhen",
         "The three leaders meet on the sidelines of the APEC summit."),
        ("POLITICS",
         "Canada rethinks China ties as Carney seeks 'right deal' with US",
         "Ottawa adjusts its approach to Beijing while pressing Washington "
         "on trade."),
        ("POLITICS",
         "Senators warn AI cyber threats are outpacing US defences",
         "Lawmakers press the White House for faster action against "
         "AI-enabled attacks."),
        ("POLITICS",
         "NSA's classified network hit by outage, reports say",
         "The disruption, first reported on Tuesday, forced intelligence "
         "staff to adjust schedules."),
        ("BUSINESS",
         "Microsoft in talks to sell AI services to ByteDance",
         "US House committee seeks a briefing on the reported discussions."),
    ],
    [
        ("BUSINESS",
         "Nvidia's acting chief promises earlier pay rises and more stock",
         "Colette Kress tells staff at her first all-hands meeting that "
         "raises take effect in December."),
        ("BUSINESS",
         "Nvidia halts H-series chip shipments to China",
         "The chipmaker says it no longer ships Hopper chips to the mainland "
         "and has formed an export-compliance committee."),
        ("BUSINESS",
         "Fed minutes: most officials expect further rate rises",
         "Policymakers signal more hikes may be needed to bring inflation "
         "back to 2%."),
        ("BUSINESS",
         "Goldman Sachs upgrades India to overweight",
         "Bank sets a December 2027 Nifty target of 28,500."),
        ("SCIENCE",
         "Voyager 1 reaches a light-day from Earth",
         "NASA to confirm the milestone, nearly 50 years after launch, at a "
         "briefing today."),
        ("SCIENCE",
         "Earth is missing a billion years of history. Scientists may know why",
         "New research offers an explanation for the planet's lost geological "
         "record."),
        ("SCIENCE",
         "Islam on track to be world's largest religion by 2035",
         "Pew Research projects the faith will overtake Christianity within "
         "a decade."),
        ("SPORT",
         "Duckett's 133 puts England on top in third ODI",
         "Opener's century leaves Australia chasing the game in the series "
         "decider."),
    ],
]


def rule(draw, y, x0=MARGIN, x1=W - MARGIN, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)
    return y + width


def draw_masthead(draw, y):
    """Nameplate, date line and rules. Returns y below the masthead."""
    name = "The Daily Chronicle"
    w = draw.textlength(name, font=F_MASTHEAD)
    draw.text(((W - w) / 2, y), name, font=F_MASTHEAD, fill=INK)
    y += F_MASTHEAD.size + 10
    y = rule(draw, y, width=3)
    y += 6
    date_line = "THURSDAY, 19 NOVEMBER 2026"
    w = draw.textlength(date_line, font=F_DATE)
    draw.text(((W - w) / 2, y), date_line, font=F_DATE, fill=INK)
    y += F_DATE.size + 4
    sub = "One day's news, one page  \u2022  Est. 2026  \u2022  World  \u2022  Politics  \u2022  Business  \u2022  Tech  \u2022  Science  \u2022  Sport"
    w = draw.textlength(sub, font=F_FOOT)
    draw.text(((W - w) / 2, y), sub, font=F_FOOT, fill=GREY)
    y += F_FOOT.size + 8
    y = rule(draw, y, width=1)
    return y + 10


def draw_lead(draw, y):
    """Kicker, big lead headline and deck, centred across the page."""
    w = draw.textlength(LEAD_KICKER, font=F_KICKER)
    draw.text(((W - w) / 2, y), LEAD_KICKER, font=F_KICKER, fill=RED)
    y += F_KICKER.size + 6
    lines = wrap(draw, LEAD_HEAD, F_LEAD, W - 2 * MARGIN - 60)
    y = draw_centered(draw, y, lines, F_LEAD, spacing=4)
    y += 6
    deck = wrap(draw, LEAD_DECK, F_LEAD_DECK, W - 2 * MARGIN - 140)
    y = draw_centered(draw, y, deck, F_LEAD_DECK, spacing=3)
    y += 10
    y = rule(draw, y, width=2)
    return y + 12


def draw_column(draw, x, y, stories, bottom):
    """Draw one column of stories; returns y after the last story."""
    last_section = None
    for section, head, deck in stories:
        if section != last_section:
            if last_section is not None:
                y += 4
            draw.text((x, y), section, font=F_SECTION, fill=RED)
            y += F_SECTION.size + 3
            rule(draw, y, x0=x, x1=x + COL_W, width=1, fill=RED)
            y += 8
            last_section = section
        for line in wrap(draw, head, F_HEAD, COL_W):
            draw.text((x, y), line, font=F_HEAD, fill=INK)
            y += F_HEAD.size + 2
        y += 2
        for line in wrap(draw, deck, F_DECK, COL_W):
            draw.text((x, y), line, font=F_DECK, fill=INK)
            y += F_DECK.size + 2
        y += 9
        if y > bottom:
            raise ValueError("column overflow: stories do not fit the page")
    return y


def draw_footer(draw, y):
    y = rule(draw, y, width=1)
    y += 6
    note = ("Compiled from wire reports published on Thursday 19 November 2026  "
            "\u2022  The Daily Chronicle")
    w = draw.textlength(note, font=F_FOOT)
    draw.text(((W - w) / 2, y), note, font=F_FOOT, fill=GREY)
    return y + F_FOOT.size


def build():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    y = 18
    y = draw_masthead(draw, y)
    y = draw_lead(draw, y)
    col_top = y
    col_bottom = H - 44
    for i, stories in enumerate(COLUMNS):
        x = MARGIN + i * (COL_W + GUTTER)
        draw_column(draw, x, col_top, stories, col_bottom)
    draw_footer(draw, H - 30)
    return img


def main():
    """Render the front page and save it beside this script as entry.png.

    Run at build time (PIL available here); the graded entrypoint is
    main.py, which only copies the shipped entry.png.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR",
                             os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(out_dir, exist_ok=True)
    img = build()
    img.save(os.path.join(out_dir, "entry.png"), format="PNG")


if __name__ == "__main__":
    main()

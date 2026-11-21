[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/nuarnayla-wq/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/nuarnayla-wq/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# One picture of the world on 21 November 2026

An entry for the make.fun bounty `news-image-20261121`, worth $100 in USDC and closing on Monday 23 November 2026 at 12:00 AM UTC. The bounty page is here: https://make.fun/bounty/news-image-20261121

The entry is a single 1024×1024 picture, laid out like a newspaper front page, that tries to capture Saturday 21 November 2026 in six items a reader can take in at a glance. Every word in the picture was drawn with Python so the text stays sharp and readable.

## The six stories in the picture

1. **Missiles in Poland** — Russian missiles come down in Poland, Warsaw calls the incident a deliberate provocation and turns to NATO for extra support.
2. **A new chapter for the EU and the UK** — Leaders in Brussels settle fresh agreements covering trade, energy, farming, and young people moving between the two sides.
3. **More help for Ukraine** — The EU signs off on another €1 billion of military support and a €7.9 billion payment, the biggest of its kind so far.
4. **A town back in Iraqi hands** — Iraqi forces move into Jurf al-Sakhar, ending twelve years of control by Kataib Hezbollah there.
5. **A long sentence in the United States** — Nikhil Gupta is given nineteen years over a plan to kill a Sikh separatist leader living in the US.
6. **Italy stops work** — Workers and students across Italy walk out in a general strike over living costs and public services.

## Running it

```bash
python main.py
```

The program copies the bundled `entry.png` to `/output/entry.png`. It needs no network and always writes the same bytes.

The idea behind the design is simple: a picture editor with no news feed should still be able to tell, just from looking, what the day was about. So each story gets its own number, a short headline, and two plain lines of context — nothing more, nothing hidden in small print.

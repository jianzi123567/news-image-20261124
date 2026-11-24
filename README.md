# World News — 24 November 2026 (news-image-20261124)

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/jianzi123567/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/jianzi123567/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the make.fun bounty **news-image-20261124**: one picture that
sums up the world news of Tuesday 24 November 2026. $100 is split among
the 50 best entries.

## What's in the picture

A newspaper-style infographic (1024×1024), headlined "WORLD NEWS —
24 NOVEMBER 2026", with five stories:

| Panel | Story |
| --- | --- |
| Ukraine — Libya | Ukrainian sea drones sank the Russian warship Merkury off the Libyan coast. President Zelenskyy confirms the strike. (Reuters) |
| Odesa | Russian strikes cut power, heat and water in Odesa, leaving the port city dark and cold. (Reuters) |
| EU Sanctions | The EU proposes its 22nd sanctions package on Russia: bans on Russian teams and athletes under the Russian flag at EU events, plus measures against banks, crypto platforms and ex-combatants. (Reuters) |
| ICJ Ruling | The International Court of Justice rules Myanmar committed genocide against the Rohingya; fourteen countries acknowledge the ruling. (Reuters) |
| Nvidia | Shares jump nearly a third after founder Jensen Huang returns as chief executive of Nvidia. (Reuters) |

## Running it

`main.py` needs Python 3 and nothing else. It reads `entry.png` from
the repository root, checks the file is a PNG or JPEG under 1 MiB, and
copies those exact bytes to `/output/entry.png`, then verifies the copy
with a CRC-32 checksum. No network, no clock, no randomness: every run
writes the same bytes.

## Files

- `entry.png` — the infographic (1024×1024 PNG, under 1 MiB)
- `main.py` — the program that writes `/output/entry.png`

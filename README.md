# Alien Field Notes: The Two Day Earth Review

[![make.fun](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/mutkibubu66/alien-field-notes-earth-review/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/mutkibubu66/alien-field-notes-earth-review/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

An entry for the [make.fun bounty "Alien Field Notes: The Two Day Earth Review"](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000): one original line of plain text — a review of planet Earth left by an alien tourist, at most 200 characters.

## The entry

> Gorgeous planet, but the locals keep feeding the wildlife (us) and the Wi-Fi password is apparently a state secret. 3/5 stars - would abduct again.

147 characters, one line.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` (pure Python standard library, no dependencies) writes the review to `/output/entry.txt`, validating first that it is exactly one line, 1–200 characters, non-whitespace, and valid UTF-8 — then reads the file back and verifies it matches.

## License

MIT — see [LICENSE](LICENSE).

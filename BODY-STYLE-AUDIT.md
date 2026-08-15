# Body Visual Consistency Audit

This audit checks only page-specific visual CSS selectors that are **actually used by elements in the current page markup** and are not explicitly governed by the final homepage/body design locks. Dead/unused legacy CSS is ignored.

- Interior pages inspected: **49**

| Page | Risk score | Used visual rules | Used uncovered selectors | Noncanonical colors | Unusual radii | Shadows | Fonts |
|---|---:|---:|---:|---:|---:|---:|---:|
| `answer-22.html` | 26 | 91 | 22 | 2 | 0 | 0 | 0 |
| `answer-13.html` | 26 | 90 | 22 | 2 | 0 | 0 | 0 |
| `answer-24.html` | 25 | 89 | 21 | 2 | 0 | 0 | 0 |
| `answer-23.html` | 25 | 88 | 21 | 2 | 0 | 0 | 0 |
| `answer-20.html` | 25 | 88 | 21 | 2 | 0 | 0 | 0 |
| `answer-19.html` | 25 | 88 | 21 | 2 | 0 | 0 | 0 |
| `answer-18.html` | 25 | 89 | 21 | 2 | 0 | 0 | 0 |
| `answer-16.html` | 25 | 88 | 21 | 2 | 0 | 0 | 0 |
| `answer-15.html` | 25 | 89 | 21 | 2 | 0 | 0 | 0 |
| `answer-14.html` | 25 | 89 | 21 | 2 | 0 | 0 | 0 |
| `answer-12.html` | 25 | 90 | 21 | 2 | 0 | 0 | 0 |
| `answer-10.html` | 25 | 89 | 21 | 2 | 0 | 0 | 0 |
| `answer-08.html` | 25 | 97 | 21 | 2 | 0 | 0 | 0 |
| `answer-03.html` | 25 | 88 | 21 | 2 | 0 | 0 | 0 |
| `answer-02.html` | 25 | 88 | 21 | 2 | 0 | 0 | 0 |
| `answer-01.html` | 25 | 88 | 21 | 2 | 0 | 0 | 0 |
| `god-feels-far-away.html` | 24 | 55 | 17 | 3 | 0 | 1 | 0 |
| `forgiveness-and-relational-hurt.html` | 24 | 55 | 17 | 3 | 0 | 1 | 0 |
| `answer-21.html` | 24 | 89 | 20 | 2 | 0 | 0 | 0 |
| `answer-17.html` | 24 | 88 | 20 | 2 | 0 | 0 | 0 |
| `answer-11.html` | 24 | 89 | 20 | 2 | 0 | 0 | 0 |
| `answer-07.html` | 24 | 89 | 20 | 2 | 0 | 0 | 0 |
| `answer-06.html` | 24 | 89 | 20 | 2 | 0 | 0 | 0 |
| `answer-04.html` | 24 | 90 | 20 | 2 | 0 | 0 | 0 |
| `answer-09.html` | 23 | 87 | 19 | 2 | 0 | 0 | 0 |
| `answer-05.html` | 23 | 95 | 19 | 2 | 0 | 0 | 0 |
| `why-god-allows-suffering.html` | 18 | 57 | 13 | 2 | 0 | 1 | 0 |
| `grief-and-loss.html` | 18 | 57 | 13 | 2 | 0 | 1 | 0 |
| `doubt-and-church-hurt.html` | 13 | 35 | 9 | 2 | 0 | 0 | 0 |
| `anger-and-unanswered-prayer.html` | 13 | 35 | 9 | 2 | 0 | 0 | 0 |
| `what-hurts-today.html` | 9 | 42 | 8 | 0 | 0 | 1 | 0 |
| `hope-thanks.html` | 7 | 12 | 2 | 2 | 1 | 0 | 0 |
| `can-christians-be-depressed.html` | 5 | 37 | 5 | 0 | 0 | 0 | 0 |
| `book-updates-thanks.html` | 3 | 10 | 1 | 1 | 0 | 0 | 0 |
| `2am-guide.html` | 3 | 31 | 3 | 0 | 0 | 0 | 0 |
| `free-guides.html` | 2 | 60 | 2 | 0 | 0 | 0 | 0 |
| `church-resources.html` | 2 | 38 | 2 | 0 | 0 | 0 | 0 |
| `contact.html` | 1 | 25 | 1 | 0 | 0 | 0 | 0 |
| `book.html` | 1 | 53 | 1 | 0 | 0 | 0 | 0 |
| `2am-guide-access.html` | 1 | 30 | 1 | 0 | 0 | 0 | 0 |
| `unsafe.html` | 0 | 17 | 0 | 0 | 0 | 0 | 0 |
| `start-here.html` | 0 | 37 | 0 | 0 | 0 | 0 | 0 |
| `photo-test.html` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `help-someone.html` | 0 | 26 | 0 | 0 | 0 | 0 | 0 |
| `contact-thanks.html` | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| `begin-here.html` | 0 | 29 | 0 | 0 | 0 | 0 | 0 |
| `all-answers.html` | 0 | 32 | 0 | 0 | 0 | 0 | 0 |
| `about.html` | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| `404.html` | 0 | 9 | 0 | 0 | 0 | 0 | 0 |

## Highest-risk pages and used selectors

### `answer-22.html` — score 26
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture`
  - `.exactScripture small`
  - `.exactQuestion`
  - `.exactQuestion strong`
  - `.exactQuestion span`
  - `.exactPastoral`
  - `.exactPastoral strong`
  - `.journeyThumb`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`

### `answer-13.html` — score 26
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture3`
  - `.exactScripture3 small`
  - `.exactQuestion3`
  - `.exactQuestion3 strong`
  - `.exactQuestion3 span`
  - `.exactPastoral3`
  - `.exactPastoral3 strong`
  - `.journeyThumb`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`

### `answer-24.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture`
  - `.exactScripture small`
  - `.exactQuestion`
  - `.exactQuestion strong`
  - `.exactQuestion span`
  - `.exactPastoral`
  - `.exactPastoral strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-23.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture5`
  - `.exactScripture5 small`
  - `.exactQuestion5`
  - `.exactQuestion5 strong`
  - `.exactQuestion5 span`
  - `.exactPastoral5`
  - `.exactPastoral5 strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-20.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture5`
  - `.exactScripture5 small`
  - `.exactQuestion5`
  - `.exactQuestion5 strong`
  - `.exactQuestion5 span`
  - `.exactPastoral5`
  - `.exactPastoral5 strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-19.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture2`
  - `.exactScripture2 small`
  - `.exactQuestion2`
  - `.exactQuestion2 strong`
  - `.exactQuestion2 span`
  - `.exactPastoral2`
  - `.exactPastoral2 strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-18.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture`
  - `.exactScripture small`
  - `.exactQuestion`
  - `.exactQuestion strong`
  - `.exactQuestion span`
  - `.exactPastoral`
  - `.exactPastoral strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-16.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture4`
  - `.exactScripture4 small`
  - `.exactQuestion4`
  - `.exactQuestion4 strong`
  - `.exactQuestion4 span`
  - `.exactPastoral4`
  - `.exactPastoral4 strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-15.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture2`
  - `.exactScripture2 small`
  - `.exactQuestion2`
  - `.exactQuestion2 strong`
  - `.exactQuestion2 span`
  - `.exactPastoral2`
  - `.exactPastoral2 strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-14.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture2`
  - `.exactScripture2 small`
  - `.exactQuestion2`
  - `.exactQuestion2 strong`
  - `.exactQuestion2 span`
  - `.exactPastoral2`
  - `.exactPastoral2 strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-12.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture5`
  - `.exactScripture5 small`
  - `.exactQuestion5`
  - `.exactQuestion5 strong`
  - `.exactQuestion5 span`
  - `.exactPastoral5`
  - `.exactPastoral5 strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-10.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture5`
  - `.exactScripture5 small`
  - `.exactQuestion5`
  - `.exactQuestion5 strong`
  - `.exactQuestion5 span`
  - `.exactPastoral5`
  - `.exactPastoral5 strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-08.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture4`
  - `.exactScripture4 small`
  - `.exactQuestion4`
  - `.exactQuestion4 strong`
  - `.exactQuestion4 span`
  - `.exactPastoral4`
  - `.exactPastoral4 strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-03.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture4`
  - `.exactScripture4 small`
  - `.exactQuestion4`
  - `.exactQuestion4 strong`
  - `.exactQuestion4 span`
  - `.exactPastoral4`
  - `.exactPastoral4 strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-02.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture3`
  - `.exactScripture3 small`
  - `.exactQuestion3`
  - `.exactQuestion3 strong`
  - `.exactQuestion3 span`
  - `.exactPastoral3`
  - `.exactPastoral3 strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `answer-01.html` — score 25
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture2`
  - `.exactScripture2 small`
  - `.exactQuestion2`
  - `.exactQuestion2 strong`
  - `.exactQuestion2 span`
  - `.exactPastoral2`
  - `.exactPastoral2 strong`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`

### `god-feels-far-away.html` — score 24
- Noncanonical colors: #364039, #4f5a53, #87683a
- Shadows: `.podcastPlay`
- Used visual selectors not governed by the final locks:
  - `.deepHelp2`
  - `.deepHelp2 h2`
  - `.deepHelp2 p`
  - `.deepHelp2 a`
  - `.deepScripture2`
  - `.deepScripture2 small`
  - `.scriptureItem2`
  - `.scriptureItem2 strong`
  - `.scriptureItem2 p`
  - `.podcastEpisode`
  - `.podcastThumb`
  - `.podcastPlay`

### `forgiveness-and-relational-hurt.html` — score 24
- Noncanonical colors: #364039, #4f5a53, #87683a
- Shadows: `.podcastPlay`
- Used visual selectors not governed by the final locks:
  - `.deepHelp3`
  - `.deepHelp3 h2`
  - `.deepHelp3 p`
  - `.deepHelp3 a`
  - `.deepScripture3`
  - `.deepScripture3 small`
  - `.scriptureItem3`
  - `.scriptureItem3 strong`
  - `.scriptureItem3 p`
  - `.podcastEpisode`
  - `.podcastThumb`
  - `.podcastPlay`

### `answer-21.html` — score 24
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactScripture`
  - `.exactScripture small`
  - `.exactQuestion`
  - `.exactQuestion strong`
  - `.exactQuestion span`
  - `.journeyThumb`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`
  - `.copyStatus`

### `answer-17.html` — score 24
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.exactQuestion3`
  - `.exactQuestion3 strong`
  - `.exactQuestion3 span`
  - `.exactPastoral3`
  - `.exactPastoral3 strong`
  - `.journeyThumb`
  - `.journeyBookLink`
  - `.journeyBookLink a`
  - `.shareHelp`
  - `.shareHelp strong`
  - `.shareHelp p`
  - `.copyStatus`

- Pages with no used visual escape selectors: **9/49**

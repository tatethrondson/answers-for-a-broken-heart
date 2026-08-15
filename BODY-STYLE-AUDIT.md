# Body Visual Consistency Audit

This audit checks only page-specific visual CSS selectors that are **actually used by elements in the current page markup** and are not explicitly governed by the final homepage design lock. Dead/unused legacy CSS is ignored.

- Interior pages inspected: **49**

| Page | Risk score | Used visual rules | Used uncovered selectors | Noncanonical colors | Unusual radii | Shadows | Fonts |
|---|---:|---:|---:|---:|---:|---:|---:|
| `answer-12.html` | 38 | 90 | 30 | 4 | 0 | 0 | 0 |
| `answer-22.html` | 37 | 91 | 30 | 3 | 0 | 1 | 0 |
| `answer-21.html` | 37 | 89 | 30 | 3 | 0 | 1 | 0 |
| `answer-17.html` | 37 | 88 | 30 | 3 | 0 | 1 | 0 |
| `answer-13.html` | 37 | 90 | 30 | 3 | 0 | 1 | 0 |
| `answer-11.html` | 37 | 89 | 30 | 3 | 0 | 1 | 0 |
| `answer-07.html` | 37 | 89 | 30 | 3 | 0 | 1 | 0 |
| `answer-06.html` | 37 | 89 | 30 | 3 | 0 | 1 | 0 |
| `answer-04.html` | 37 | 90 | 30 | 3 | 0 | 1 | 0 |
| `answer-24.html` | 36 | 89 | 30 | 3 | 0 | 0 | 0 |
| `answer-23.html` | 36 | 88 | 30 | 3 | 0 | 0 | 0 |
| `answer-20.html` | 36 | 88 | 30 | 3 | 0 | 0 | 0 |
| `answer-19.html` | 36 | 88 | 30 | 3 | 0 | 0 | 0 |
| `answer-18.html` | 36 | 89 | 30 | 3 | 0 | 0 | 0 |
| `answer-16.html` | 36 | 88 | 30 | 3 | 0 | 0 | 0 |
| `answer-15.html` | 36 | 89 | 30 | 3 | 0 | 0 | 0 |
| `answer-14.html` | 36 | 89 | 30 | 3 | 0 | 0 | 0 |
| `answer-10.html` | 36 | 89 | 30 | 3 | 0 | 0 | 0 |
| `answer-09.html` | 36 | 87 | 30 | 3 | 0 | 0 | 0 |
| `answer-08.html` | 36 | 97 | 30 | 3 | 0 | 0 | 0 |
| `answer-05.html` | 36 | 95 | 30 | 3 | 0 | 0 | 0 |
| `answer-03.html` | 36 | 88 | 30 | 3 | 0 | 0 | 0 |
| `answer-02.html` | 36 | 88 | 30 | 3 | 0 | 0 | 0 |
| `answer-01.html` | 36 | 88 | 30 | 3 | 0 | 0 | 0 |
| `why-god-allows-suffering.html` | 30 | 57 | 23 | 3 | 0 | 1 | 0 |
| `grief-and-loss.html` | 30 | 57 | 23 | 3 | 0 | 1 | 0 |
| `god-feels-far-away.html` | 29 | 55 | 22 | 3 | 0 | 1 | 0 |
| `forgiveness-and-relational-hurt.html` | 29 | 55 | 22 | 3 | 0 | 1 | 0 |
| `book.html` | 20 | 53 | 15 | 2 | 0 | 1 | 0 |
| `start-here.html` | 14 | 37 | 12 | 1 | 0 | 0 | 0 |
| `doubt-and-church-hurt.html` | 14 | 35 | 10 | 2 | 0 | 0 | 0 |
| `anger-and-unanswered-prayer.html` | 14 | 35 | 10 | 2 | 0 | 0 | 0 |
| `what-hurts-today.html` | 13 | 42 | 12 | 0 | 0 | 1 | 0 |
| `can-christians-be-depressed.html` | 10 | 37 | 8 | 1 | 0 | 0 | 0 |
| `hope-thanks.html` | 7 | 12 | 2 | 2 | 1 | 0 | 0 |
| `begin-here.html` | 5 | 29 | 5 | 0 | 0 | 0 | 0 |
| `book-updates-thanks.html` | 3 | 10 | 1 | 1 | 0 | 0 | 0 |
| `2am-guide.html` | 3 | 31 | 3 | 0 | 0 | 0 | 0 |
| `free-guides.html` | 2 | 60 | 2 | 0 | 0 | 0 | 0 |
| `church-resources.html` | 2 | 38 | 2 | 0 | 0 | 0 | 0 |
| `contact.html` | 1 | 25 | 1 | 0 | 0 | 0 | 0 |
| `all-answers.html` | 1 | 32 | 1 | 0 | 0 | 0 | 0 |
| `2am-guide-access.html` | 1 | 30 | 1 | 0 | 0 | 0 | 0 |
| `unsafe.html` | 0 | 17 | 0 | 0 | 0 | 0 | 0 |
| `photo-test.html` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `help-someone.html` | 0 | 26 | 0 | 0 | 0 | 0 | 0 |
| `contact-thanks.html` | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| `about.html` | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| `404.html` | 0 | 9 | 0 | 0 | 0 | 0 | 0 |

## Highest-risk pages and used selectors

### `answer-12.html` — score 38
- Noncanonical colors: #24312b, #5e6861, #e5dfd5, #fff6e8
- Used visual selectors not governed by homepage lock:
  - `.warning`
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth5`

### `answer-22.html` — score 37
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Shadows: `.journeyPlay`
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth`
  - `.exactDepth h2`

### `answer-21.html` — score 37
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Shadows: `.journeyPlay`
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth`
  - `.exactDepth h2`

### `answer-17.html` — score 37
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Shadows: `.journeyPlay`
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth3`
  - `.exactDepth3 h2`

### `answer-13.html` — score 37
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Shadows: `.journeyPlay`
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth3`
  - `.exactDepth3 h2`

### `answer-11.html` — score 37
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Shadows: `.journeyPlay`
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth4`
  - `.exactDepth4 h2`

### `answer-07.html` — score 37
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Shadows: `.journeyPlay`
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth3`
  - `.exactDepth3 h2`

### `answer-06.html` — score 37
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Shadows: `.journeyPlay`
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth4`
  - `.exactDepth4 h2`

### `answer-04.html` — score 37
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Shadows: `.journeyPlay`
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth`
  - `.exactDepth h2`

### `answer-24.html` — score 36
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth`
  - `.exactDepth h2`

### `answer-23.html` — score 36
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth5`
  - `.exactDepth5 h2`

### `answer-20.html` — score 36
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth5`
  - `.exactDepth5 h2`

### `answer-19.html` — score 36
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth2`
  - `.exactDepth2 h2`

### `answer-18.html` — score 36
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth`
  - `.exactDepth h2`

### `answer-16.html` — score 36
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth4`
  - `.exactDepth4 h2`

### `answer-15.html` — score 36
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth2`
  - `.exactDepth2 h2`

### `answer-14.html` — score 36
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth2`
  - `.exactDepth2 h2`

### `answer-10.html` — score 36
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth5`
  - `.exactDepth5 h2`

### `answer-09.html` — score 36
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth2`
  - `.exactDepth2 h2`

### `answer-08.html` — score 36
- Noncanonical colors: #24312b, #5e6861, #e5dfd5
- Used visual selectors not governed by homepage lock:
  - `.book`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `.answerDeepDive`
  - `.answerDeepDive summary`
  - `.answerDeepDive summary strong`
  - `.answerDeepDive summary small`
  - `.answerDeepDiveMark`
  - `.answerDeepDiveBody`
  - `.answerDeepDiveBody .exactDepth,.answerDeepDiveBody .exactDepth2,.answerDeepDiveBody .exactDepth3,.answerDeepDiveBody .exactDepth4,.answerDeepDiveBody .exactDepth5`
  - `.exactDepth4`

- Pages with no used visual escape selectors: **6/49**

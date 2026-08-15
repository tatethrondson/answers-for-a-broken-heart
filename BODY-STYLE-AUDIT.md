# Body Visual Consistency Audit

This audit checks only page-specific visual CSS selectors that are **actually used by elements in the current page markup** and are not explicitly governed by the final homepage/body design locks. Dead/unused legacy CSS is ignored.

- Interior pages inspected: **49**

| Page | Risk score | Used visual rules | Used uncovered selectors | Noncanonical colors | Unusual radii | Shadows | Fonts |
|---|---:|---:|---:|---:|---:|---:|---:|
| `why-god-allows-suffering.html` | 9 | 57 | 7 | 1 | 0 | 0 | 0 |
| `what-hurts-today.html` | 9 | 42 | 8 | 0 | 0 | 1 | 0 |
| `grief-and-loss.html` | 9 | 57 | 7 | 1 | 0 | 0 | 0 |
| `hope-thanks.html` | 7 | 12 | 2 | 2 | 1 | 0 | 0 |
| `can-christians-be-depressed.html` | 5 | 37 | 5 | 0 | 0 | 0 | 0 |
| `book-updates-thanks.html` | 3 | 10 | 1 | 1 | 0 | 0 | 0 |
| `2am-guide.html` | 3 | 31 | 3 | 0 | 0 | 0 | 0 |
| `god-feels-far-away.html` | 2 | 55 | 2 | 0 | 0 | 0 | 0 |
| `free-guides.html` | 2 | 60 | 2 | 0 | 0 | 0 | 0 |
| `forgiveness-and-relational-hurt.html` | 2 | 55 | 2 | 0 | 0 | 0 | 0 |
| `church-resources.html` | 2 | 38 | 2 | 0 | 0 | 0 | 0 |
| `contact.html` | 1 | 25 | 1 | 0 | 0 | 0 | 0 |
| `book.html` | 1 | 53 | 1 | 0 | 0 | 0 | 0 |
| `2am-guide-access.html` | 1 | 30 | 1 | 0 | 0 | 0 | 0 |
| `unsafe.html` | 0 | 17 | 0 | 0 | 0 | 0 | 0 |
| `start-here.html` | 0 | 37 | 0 | 0 | 0 | 0 | 0 |
| `photo-test.html` | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| `help-someone.html` | 0 | 26 | 0 | 0 | 0 | 0 | 0 |
| `doubt-and-church-hurt.html` | 0 | 35 | 0 | 0 | 0 | 0 | 0 |
| `contact-thanks.html` | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| `begin-here.html` | 0 | 29 | 0 | 0 | 0 | 0 | 0 |
| `answer-24.html` | 0 | 89 | 0 | 0 | 0 | 0 | 0 |
| `answer-23.html` | 0 | 88 | 0 | 0 | 0 | 0 | 0 |
| `answer-22.html` | 0 | 91 | 0 | 0 | 0 | 0 | 0 |
| `answer-21.html` | 0 | 89 | 0 | 0 | 0 | 0 | 0 |
| `answer-20.html` | 0 | 88 | 0 | 0 | 0 | 0 | 0 |
| `answer-19.html` | 0 | 88 | 0 | 0 | 0 | 0 | 0 |
| `answer-18.html` | 0 | 89 | 0 | 0 | 0 | 0 | 0 |
| `answer-17.html` | 0 | 88 | 0 | 0 | 0 | 0 | 0 |
| `answer-16.html` | 0 | 88 | 0 | 0 | 0 | 0 | 0 |
| `answer-15.html` | 0 | 89 | 0 | 0 | 0 | 0 | 0 |
| `answer-14.html` | 0 | 89 | 0 | 0 | 0 | 0 | 0 |
| `answer-13.html` | 0 | 90 | 0 | 0 | 0 | 0 | 0 |
| `answer-12.html` | 0 | 90 | 0 | 0 | 0 | 0 | 0 |
| `answer-11.html` | 0 | 89 | 0 | 0 | 0 | 0 | 0 |
| `answer-10.html` | 0 | 89 | 0 | 0 | 0 | 0 | 0 |
| `answer-09.html` | 0 | 87 | 0 | 0 | 0 | 0 | 0 |
| `answer-08.html` | 0 | 97 | 0 | 0 | 0 | 0 | 0 |
| `answer-07.html` | 0 | 89 | 0 | 0 | 0 | 0 | 0 |
| `answer-06.html` | 0 | 89 | 0 | 0 | 0 | 0 | 0 |
| `answer-05.html` | 0 | 95 | 0 | 0 | 0 | 0 | 0 |
| `answer-04.html` | 0 | 90 | 0 | 0 | 0 | 0 | 0 |
| `answer-03.html` | 0 | 88 | 0 | 0 | 0 | 0 | 0 |
| `answer-02.html` | 0 | 88 | 0 | 0 | 0 | 0 | 0 |
| `answer-01.html` | 0 | 88 | 0 | 0 | 0 | 0 | 0 |
| `anger-and-unanswered-prayer.html` | 0 | 35 | 0 | 0 | 0 | 0 | 0 |
| `all-answers.html` | 0 | 32 | 0 | 0 | 0 | 0 | 0 |
| `about.html` | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| `404.html` | 0 | 9 | 0 | 0 | 0 | 0 | 0 |

## Remaining pages and used selectors

### `why-god-allows-suffering.html` — score 9
- Noncanonical colors: #87683a
- Used visual selectors not governed by the final locks:
  - `.deepScripture`
  - `.deepScripture small`
  - `.scriptureItem`
  - `.scriptureItem strong`
  - `.scriptureItem p`
  - `.podcastButton`
  - `.podcastButton:hover`

### `what-hurts-today.html` — score 9
- Shadows: `.topicHubCard:hover`
- Used visual selectors not governed by the final locks:
  - `.topicHubs`
  - `.topicHubs h2`
  - `.topicHubs p`
  - `.topicHubCard`
  - `.topicHubCard:hover`
  - `.topicHubCard small`
  - `.topicHubCard strong`
  - `.topicHubCard span`

### `grief-and-loss.html` — score 9
- Noncanonical colors: #87683a
- Used visual selectors not governed by the final locks:
  - `.deepScripture`
  - `.deepScripture small`
  - `.scriptureItem`
  - `.scriptureItem strong`
  - `.scriptureItem p`
  - `.podcastButton`
  - `.podcastButton:hover`

### `hope-thanks.html` — score 7
- Noncanonical colors: #e0d9cd, #f5f1e8
- Unusual radii: `.resource` → `15px`
- Used visual selectors not governed by the final locks:
  - `.resource`
  - `.resource h2`

### `can-christians-be-depressed.html` — score 5
- Used visual selectors not governed by the final locks:
  - `.signature`
  - `.depFaq`
  - `.depFaqItem`
  - `.depNote`
  - `.depLinks a`

### `book-updates-thanks.html` — score 3
- Noncanonical colors: #777d55
- Used visual selectors not governed by the final locks:
  - `.check`

### `2am-guide.html` — score 3
- Used visual selectors not governed by the final locks:
  - `.promise`
  - `.insideHead h2`
  - `.insideHead p`

### `god-feels-far-away.html` — score 2
- Used visual selectors not governed by the final locks:
  - `.podcastButton`
  - `.podcastButton:hover`

### `free-guides.html` — score 2
- Used visual selectors not governed by the final locks:
  - `.noGate`
  - `.noGate strong`

### `forgiveness-and-relational-hurt.html` — score 2
- Used visual selectors not governed by the final locks:
  - `.podcastButton`
  - `.podcastButton:hover`

### `church-resources.html` — score 2
- Used visual selectors not governed by the final locks:
  - `.gridHead h2`
  - `.kitItem`

### `contact.html` — score 1
- Used visual selectors not governed by the final locks:
  - `.formIntro`

### `book.html` — score 1
- Used visual selectors not governed by the final locks:
  - `.bookInsideHead p`

### `2am-guide-access.html` — score 1
- Used visual selectors not governed by the final locks:
  - `.remember`

- Pages with no used visual escape selectors: **35/49**

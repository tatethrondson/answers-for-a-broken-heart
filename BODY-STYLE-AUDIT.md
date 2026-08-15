# Body Visual Consistency Audit

This audit checks only page-specific visual CSS selectors that are **actually used by elements in the current page markup** and are not explicitly governed by the final homepage/body design locks. Dead/unused legacy CSS is ignored.

- Interior pages inspected: **49**

| Page | Risk score | Used visual rules | Used uncovered selectors | Noncanonical colors | Unusual radii | Shadows | Fonts |
|---|---:|---:|---:|---:|---:|---:|---:|
| `answer-24.html` | 13 | 89 | 9 | 2 | 0 | 0 | 0 |
| `answer-23.html` | 13 | 88 | 9 | 2 | 0 | 0 | 0 |
| `answer-22.html` | 13 | 91 | 9 | 2 | 0 | 0 | 0 |
| `answer-21.html` | 13 | 89 | 9 | 2 | 0 | 0 | 0 |
| `answer-20.html` | 13 | 88 | 9 | 2 | 0 | 0 | 0 |
| `answer-19.html` | 13 | 88 | 9 | 2 | 0 | 0 | 0 |
| `answer-18.html` | 13 | 89 | 9 | 2 | 0 | 0 | 0 |
| `answer-17.html` | 13 | 88 | 9 | 2 | 0 | 0 | 0 |
| `answer-16.html` | 13 | 88 | 9 | 2 | 0 | 0 | 0 |
| `answer-15.html` | 13 | 89 | 9 | 2 | 0 | 0 | 0 |
| `answer-14.html` | 13 | 89 | 9 | 2 | 0 | 0 | 0 |
| `answer-13.html` | 13 | 90 | 9 | 2 | 0 | 0 | 0 |
| `answer-12.html` | 13 | 90 | 9 | 2 | 0 | 0 | 0 |
| `answer-11.html` | 13 | 89 | 9 | 2 | 0 | 0 | 0 |
| `answer-10.html` | 13 | 89 | 9 | 2 | 0 | 0 | 0 |
| `answer-09.html` | 13 | 87 | 9 | 2 | 0 | 0 | 0 |
| `answer-08.html` | 13 | 97 | 9 | 2 | 0 | 0 | 0 |
| `answer-07.html` | 13 | 89 | 9 | 2 | 0 | 0 | 0 |
| `answer-06.html` | 13 | 89 | 9 | 2 | 0 | 0 | 0 |
| `answer-05.html` | 13 | 95 | 9 | 2 | 0 | 0 | 0 |
| `answer-04.html` | 13 | 90 | 9 | 2 | 0 | 0 | 0 |
| `answer-03.html` | 13 | 88 | 9 | 2 | 0 | 0 | 0 |
| `answer-02.html` | 13 | 88 | 9 | 2 | 0 | 0 | 0 |
| `answer-01.html` | 13 | 88 | 9 | 2 | 0 | 0 | 0 |
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
| `anger-and-unanswered-prayer.html` | 0 | 35 | 0 | 0 | 0 | 0 | 0 |
| `all-answers.html` | 0 | 32 | 0 | 0 | 0 | 0 | 0 |
| `about.html` | 0 | 22 | 0 | 0 | 0 | 0 | 0 |
| `404.html` | 0 | 9 | 0 | 0 | 0 | 0 | 0 |

## Highest-risk pages and used selectors

### `answer-24.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-23.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-22.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-21.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-20.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-19.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-18.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-17.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-16.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-15.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-14.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-13.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-12.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-11.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-10.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-09.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-08.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-07.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-06.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

### `answer-05.html` — score 13
- Noncanonical colors: #24312b, #5e6861
- Used visual selectors not governed by the final locks:
  - `.copyStatus`
  - `.guideCapture`
  - `.guideCapture small`
  - `.guideCapture strong`
  - `.guideCapture p`
  - `.guideForm input[type="email"]`
  - `.guideForm button`
  - `.journeyAfter`
  - `.journeyAfter a`

- Pages with no used visual escape selectors: **11/49**

# Body Visual Consistency Audit

This audit looks beyond the shared header and asks which interior pages still contain page-specific visual rules that are not explicitly governed by the final homepage design lock. It flags uncovered appearance selectors, non-canonical colors, unusual corner radii, shadows, and non-brand fonts.

- Interior pages inspected: **49**

| Page | Risk score | Visual rules | Uncovered selectors | Noncanonical colors | Unusual radii | Shadows | Fonts |
|---|---:|---:|---:|---:|---:|---:|---:|
| `book.html` | 65 | 82 | 25 | 17 | 4 | 2 | 0 |
| `answer-12.html` | 45 | 120 | 25 | 8 | 1 | 3 | 0 |
| `answer-15.html` | 43 | 119 | 25 | 7 | 1 | 3 | 0 |
| `answer-14.html` | 43 | 119 | 25 | 7 | 1 | 3 | 0 |
| `answer-13.html` | 43 | 118 | 25 | 7 | 1 | 3 | 0 |
| `answer-11.html` | 43 | 119 | 25 | 7 | 1 | 3 | 0 |
| `answer-10.html` | 43 | 119 | 25 | 7 | 1 | 3 | 0 |
| `answer-09.html` | 43 | 119 | 25 | 7 | 1 | 3 | 0 |
| `answer-08.html` | 43 | 119 | 25 | 7 | 1 | 3 | 0 |
| `answer-07.html` | 43 | 119 | 25 | 7 | 1 | 3 | 0 |
| `answer-06.html` | 43 | 119 | 25 | 7 | 1 | 3 | 0 |
| `answer-05.html` | 43 | 119 | 25 | 7 | 1 | 3 | 0 |
| `answer-04.html` | 43 | 120 | 25 | 7 | 1 | 3 | 0 |
| `answer-24.html` | 42 | 119 | 25 | 7 | 0 | 3 | 0 |
| `answer-23.html` | 42 | 118 | 25 | 7 | 0 | 3 | 0 |
| `answer-22.html` | 42 | 119 | 25 | 7 | 0 | 3 | 0 |
| `answer-21.html` | 42 | 119 | 25 | 7 | 0 | 3 | 0 |
| `answer-20.html` | 42 | 118 | 25 | 7 | 0 | 3 | 0 |
| `answer-19.html` | 42 | 118 | 25 | 7 | 0 | 3 | 0 |
| `answer-18.html` | 42 | 119 | 25 | 7 | 0 | 3 | 0 |
| `answer-17.html` | 42 | 118 | 25 | 7 | 0 | 3 | 0 |
| `answer-16.html` | 42 | 118 | 25 | 7 | 0 | 3 | 0 |
| `answer-03.html` | 42 | 118 | 25 | 7 | 0 | 3 | 0 |
| `answer-02.html` | 42 | 118 | 25 | 7 | 0 | 3 | 0 |
| `answer-01.html` | 42 | 118 | 25 | 7 | 0 | 3 | 0 |
| `why-god-allows-suffering.html` | 39 | 89 | 25 | 6 | 0 | 2 | 0 |
| `grief-and-loss.html` | 39 | 89 | 25 | 6 | 0 | 2 | 0 |
| `god-feels-far-away.html` | 37 | 88 | 25 | 5 | 0 | 2 | 0 |
| `forgiveness-and-relational-hurt.html` | 37 | 85 | 25 | 5 | 0 | 2 | 0 |
| `start-here.html` | 33 | 53 | 22 | 5 | 0 | 1 | 0 |
| `can-christians-be-depressed.html` | 32 | 50 | 16 | 8 | 0 | 0 | 0 |
| `hope-thanks.html` | 29 | 14 | 4 | 11 | 3 | 0 | 0 |
| `book-updates-thanks.html` | 29 | 12 | 3 | 12 | 2 | 0 | 0 |
| `anger-and-unanswered-prayer.html` | 29 | 75 | 20 | 4 | 0 | 1 | 0 |
| `what-hurts-today.html` | 27 | 45 | 14 | 5 | 1 | 2 | 0 |
| `church-resources.html` | 27 | 54 | 10 | 8 | 0 | 1 | 0 |
| `doubt-and-church-hurt.html` | 26 | 72 | 17 | 4 | 0 | 1 | 0 |
| `2am-guide.html` | 26 | 35 | 7 | 9 | 0 | 1 | 0 |
| `about.html` | 21 | 46 | 11 | 4 | 1 | 1 | 0 |
| `free-guides.html` | 20 | 60 | 2 | 8 | 0 | 2 | 0 |
| `404.html` | 19 | 9 | 0 | 9 | 1 | 0 | 0 |
| `2am-guide-access.html` | 19 | 32 | 3 | 8 | 0 | 0 | 0 |
| `begin-here.html` | 17 | 35 | 8 | 4 | 0 | 1 | 0 |
| `help-someone.html` | 16 | 28 | 2 | 7 | 0 | 0 | 0 |
| `all-answers.html` | 12 | 40 | 7 | 1 | 3 | 0 | 0 |
| `contact.html` | 9 | 33 | 4 | 2 | 0 | 1 | 0 |
| `unsafe.html` | 8 | 19 | 2 | 3 | 0 | 0 | 0 |
| `photo-test.html` | 5 | 3 | 0 | 1 | 2 | 1 | 0 |
| `contact-thanks.html` | 4 | 4 | 0 | 2 | 0 | 0 | 0 |

## Highest-risk pages and examples

### `book.html` — score 65
- Noncanonical colors: #343936, #344139, #3f4842, #4f5b54, #505a53, #5c675f, #616a64, #b5832f, #cbc5bb, #cfc8bc, #d7d2c9, #d8d1c5, #d9d1c5, #f1ece3, #faf7ef, #fbf9f3, #fff
- Unusual radii: `.bookAction` → `2px!important`; `.salesCard` → `2px!important`; `.bookUpdates` → `2px!important`; `.bookUpdatesForm input,.bookUpdatesForm button` → `0!important`
- Shadows: `.bookMock`; `.bookComing`
- Uncovered visual selectors:
  - `.bookPage`
  - `.bookHeroActions a`
  - `.bookHeroActions .primary`
  - `.bookHeroActions .primary:hover`
  - `.bookHeroTrust`
  - `.bookHeroTrust strong`
  - `.bookMockSub`
  - `.bookMockAuthor`
  - `.bookComing`
  - `.bookSticky`

### `answer-12.html` — score 45
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff, #fff6e8
- Unusual radii: `.short` → `4px`
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.warning`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`

### `answer-15.html` — score 43
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Unusual radii: `.short` → `4px`
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-14.html` — score 43
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Unusual radii: `.short` → `4px`
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-13.html` — score 43
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Unusual radii: `.short` → `4px`
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-11.html` — score 43
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Unusual radii: `.short` → `4px`
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-10.html` — score 43
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Unusual radii: `.short` → `4px`
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-09.html` — score 43
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Unusual radii: `.short` → `4px`
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-08.html` — score 43
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Unusual radii: `.short` → `4px`
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-07.html` — score 43
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Unusual radii: `.short` → `4px`
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-06.html` — score 43
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Unusual radii: `.short` → `4px`
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-05.html` — score 43
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Unusual radii: `.short` → `4px`
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-04.html` — score 43
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Unusual radii: `.short` → `4px`
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-24.html` — score 42
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-23.html` — score 42
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-22.html` — score 42
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-21.html` — score 42
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

### `answer-20.html` — score 42
- Noncanonical colors: #24312b, #5e6861, #6c746f, #e5dfd5, #edf1eb, #f8f4eb, #fff
- Shadows: `.relatedCard:hover`; `.journeyCard:hover`; `.journeyPlay`
- Uncovered visual selectors:
  - `.brand`
  - `.brand small`
  - `.book`
  - `.quote`
  - `.minuteScripture`
  - `.minutePrayer`
  - `.relatedAnswers .relatedLead`
  - `body.page-begin-here .startMore,body.page-start-here .startMore`
  - `body.page-begin-here .startMoreHead h2,body.page-start-here .startMoreHead h2`
  - `body.page-begin-here .choiceSecondary,body.page-start-here .choiceSecondary`

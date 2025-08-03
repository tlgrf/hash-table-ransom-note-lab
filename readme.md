# Hash Tables – Ransom Note Construction

This lab applies **hash tables** (Python dictionaries) to solve a classic challenge: decide if a ransom note can be built from a magazine string when each character can be used **only once**.  
It’s a hands-on exercise in **frequency counting** and **O(1) lookups**, similar to what you’d use for caching, indexing, and data validation.

---

## Table of Contents
- [Setup](#setup)  
- [Testing](#testing)  
- [Features](#features)  
- [How It Works](#how-it-works) 
- [Usage](#usage) 
- [Complexity](#complexity)  

---

## Setup
1. Fork and Clone the repo.
 

2. (Optional) Create and activate a virtual environment:

  - mac/linux:
    ```bash
    python -m venv .venv && source .venv/bin/activate
    ```
  - windows (powershell):
    ```powershell
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

3. Install optional tools:
    `pip install pytest`

---

## Testing
Run the existing test suite: `pytest`



---

## Features
- Implements `can_construct(ransomNote: str, magazine: str) -> bool`
- Uses a dictionary to track available characters
- Decrements counts as letters are used
- Early exit when a character is missing or depleted


---

## How It Works
1. **Quick fail** if the note is longer than the magazine.  
2. **Count** each letter in `magazine` using a dictionary.  
3. **Spend** letters while scanning `ransomNote`, returning `False` if any needed letter is missing.  
4. If all letters are found, return `True`.

---
## Usage

```
from ransom_note import can_construct

print(can_construct("aa", "aab"))       # True
print(can_construct("abc", "cba"))      # True
print(can_construct("aabbcc", "aabbc")) # False
```

---

## Complexity
- Time: `O(n + m)` → `n = len(ransomNote)`, `m = len(magazine)`
- Space:`O(k)` → `k` = number of distinct characters


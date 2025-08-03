def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # small fast-fail: if the note is longer than the magazine, it's impossible
    # (length check isn't sufficient in general, but it's safe as an early exit)
    if len(ransomNote) > len(magazine):
        return False

    # using a dict (hash table) to count available chars from the magazine
    counts = {}
    for ch in magazine:
        counts[ch] = counts.get(ch, 0) + 1

    # try to "spend" each needed char from the counts
    for ch in ransomNote:
        # if the char isn't there or already used up, we can't build the note
        if counts.get(ch, 0) == 0:
            return False
        # otherwise use one occurrence
        counts[ch] -= 1

    # if we never failed, we successfully matched all chars
    return True
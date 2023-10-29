import hashlib


def hash_256(word: str) -> str:
    """SHA256でハッシュ化

    Args:
        word (str): 平文

    Returns:
        str: ハッシュ化した文字列
    """
    return hashlib.sha256(word.encode()).hexdigest()

"""
Simple Password Generator

A small CLI tool to generate secure random passwords.
Uses Python's `secrets` module for cryptographically strong randomness.
"""

import secrets
import string
import argparse


def generate_password(
    length: int = 16,
    use_lower: bool = True,
    use_upper: bool = True,
    use_digits: bool = True,
    use_punct: bool = True,
    avoid_ambiguous: bool = False,
) -> str:
    """
    Generate a secure random password.

    Args:
        length: Password length (minimum 4).
        use_lower: Include lowercase letters.
        use_upper: Include uppercase letters.
        use_digits: Include digits.
        use_punct: Include punctuation / symbols.
        avoid_ambiguous: Avoid characters like 0, O, 1, l, I.

    Returns:
        A randomly generated password string.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    pool = ""
    if use_lower:
        pool += string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_punct:
        pool += string.punctuation

    if not pool:
        raise ValueError("At least one character type must be enabled.")

    if avoid_ambiguous:
        ambiguous = set("0O1lI")
        pool = "".join(c for c in pool if c not in ambiguous)
        if not pool:
            raise ValueError("No usable characters left after removing ambiguous ones.")

    return "".join(secrets.choice(pool) for _ in range(length))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate secure random passwords."
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=16,
        help="Password length (default: 16)",
    )
    parser.add_argument(
        "--no-lower",
        action="store_true",
        help="Do not use lowercase letters",
    )
    parser.add_argument(
        "--no-upper",
        action="store_true",
        help="Do not use uppercase letters",
    )
    parser.add_argument(
        "--no-digits",
        action="store_true",
        help="Do not use digits",
    )
    parser.add_argument(
        "--no-punct",
        action="store_true",
        help="Do not use punctuation / symbols",
    )
    parser.add_argument(
        "--avoid-ambiguous",
        action="store_true",
        help="Avoid ambiguous characters like 0, O, 1, l, I",
    )
    parser.add_argument(
        "-n", "--count",
        type=int,
        default=1,
        help="Number of passwords to generate (default: 1)",
    )

    args = parser.parse_args()

    use_lower = not args.no_lower
    use_upper = not args.no_upper
    use_digits = not args.no_digits
    use_punct = not args.no_punct

    for _ in range(args.count):
        pwd = generate_password(
            length=args.length,
            use_lower=use_lower,
            use_upper=use_upper,
            use_digits=use_digits,
            use_punct=use_punct,
            avoid_ambiguous=args.avoid_ambiguous,
        )
        print(pwd)


if __name__ == "__main__":
    main()

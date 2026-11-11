"""How computers represent data: binary numbers, bits, bytes and text encoding.

Run:
    python examples/computing_foundations/binary_and_bytes.py
"""

UNITS = ["Byte", "KiB", "MiB", "GiB", "TiB"]


def to_binary(n: int, width: int = 8) -> str:
    """Return the binary representation of a non-negative integer, zero-padded."""
    if n < 0:
        raise ValueError("only non-negative integers are supported")
    return format(n, f"0{width}b")


def from_binary(bits: str) -> int:
    """Convert a string of 0s and 1s back into an integer."""
    if not bits or set(bits) - {"0", "1"}:
        raise ValueError(f"not a binary string: {bits!r}")
    return int(bits, 2)


def text_to_bits(text: str) -> list[tuple[str, int, str]]:
    """Encode text as UTF-8 and return (character, byte value, bits) for every byte."""
    rows = []
    for ch in text:
        for byte in ch.encode("utf-8"):
            rows.append((ch, byte, to_binary(byte)))
    return rows


def human_size(num_bytes: float) -> str:
    """Format a byte count using binary (1024-based) units."""
    for unit in UNITS:
        if num_bytes < 1024 or unit == UNITS[-1]:
            return f"{num_bytes:,.2f} {unit}"
        num_bytes /= 1024
    raise AssertionError("unreachable")


def main() -> dict:
    print("Counting in binary")
    for n in range(5):
        print(f"  {to_binary(n, 4)} -> {n}")

    print("\nText is stored as numbers (UTF-8)")
    for ch, value, bits in text_to_bits("AI"):
        print(f"  {ch!r}: byte {value:>3} = {bits}")

    telugu = "అ"
    telugu_bytes = len(telugu.encode("utf-8"))
    print(f"\nThe Telugu letter {telugu!r} needs {telugu_bytes} bytes in UTF-8")

    image_bytes = 1920 * 1080 * 3  # width x height x RGB channels, 1 byte each
    print(f"\nOne uncompressed 1920x1080 RGB image = {image_bytes:,} bytes = {human_size(image_bytes)}")

    return {"telugu_bytes": telugu_bytes, "image_bytes": image_bytes}


if __name__ == "__main__":
    main()

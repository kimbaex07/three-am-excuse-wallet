"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Entry for make.fun contest u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.

The wallet speaks for itself: tired, a little smug, and convinced that
nothing good ever gets signed at 3 AM. It writes exactly one line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = "Nope \u2014 it\u2019s 3 AM, my keys are asleep in their pajamas, and this transaction reeks of a choice you\u2019ll disown by breakfast."


def main() -> None:
    # Gate checks (mirror the sealed scorer): 1-200 chars, single line,
    # not only whitespace, UTF-8 encodable.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    LINE.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

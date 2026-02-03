"""
Job Experience Translator - Example Usage

This script demonstrates how to use the translate_experience function
to convert raw work experience into professional resume language.

Usage:
    python example.py
"""

from translator import translate_experience, translate_experience_verbose


def main() -> None:
    """Run example demonstrations of the translator module."""

    # -------------------------------------------------------------------------
    # Example 1: Basic Translation
    # -------------------------------------------------------------------------
    print("=" * 60)
    print("JOB EXPERIENCE TRANSLATOR - DEMO")
    print("=" * 60)

    raw_input: str = (
        "I worked on the yard crew at a lumber yard for about 2 years. "
        "Moved heavy stuff around with forklifts, kept track of inventory, "
        "made sure nothing got stolen or damaged. Had to show up on time "
        "every day rain or shine. Also helped train some new guys."
    )

    print("\n RAW INPUT:")
    print("-" * 40)
    print(raw_input)

    print("\n TRANSLATED OUTPUT:")
    print("-" * 40)
    translated_output: str = translate_experience(raw_input)
    print(translated_output)

    # -------------------------------------------------------------------------
    # Example 2: Verbose Mode with Metadata
    # -------------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("VERBOSE MODE (with metadata)")
    print("=" * 60)

    verbose_result: dict = translate_experience_verbose(
        raw_text=raw_input,
        include_metadata=True
    )

    print(f"\n Model Used: {verbose_result['model']}")
    print(f" Status: {verbose_result.get('status', 'N/A')}")
    print(f" Version: {verbose_result.get('version', 'N/A')}")

    # -------------------------------------------------------------------------
    # Example 3: Edge Case - Empty Input
    # -------------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("EDGE CASE - Empty Input")
    print("=" * 60)

    empty_result: str = translate_experience("")
    print(f"\nResult for empty input: {empty_result}")

    print("\n" + "=" * 60)
    print("Demo complete. Ready for integration testing.")
    print("=" * 60)


if __name__ == "__main__":
    main()

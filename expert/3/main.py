from fis import FIS


def fis_result(current, needed, fis, k):
    error = 0
    error_change = 0
    i = 0
    begin_value = current

    while abs(current - needed) > 0.001:
    # print(current)
    # while i < 10:
        i += 1
        old_error = error
        error = needed - current
        u = fis.compute(error, error_change)
        current += u * k
        error_change = old_error - error
        # print(current, error, u)

    print(
        "BEGIN VALUE: %10.7f liters\n"
        "END VALUE:   %10.7f liters\n"
        "NEEDED:      %10.7f liters\n"
        "TIME:        %10.7f seconds\n" % (begin_value, float(current), needed, i / 1000)
    )


if __name__ == "__main__":
    fis_mamdani = FIS(
        "fuzzy_error.txt",
        "fuzzy_error_change.txt",
        "fuzzy_output.txt",
        "rules_mamdani.txt"
    )

    fis_sugeno = FIS(
        "fuzzy_error.txt",
        "fuzzy_error_change.txt",
        "fuzzy_output.txt",
        "rules_sugeno.txt"
    )

    start = 3
    finish = 4

    print("\nMAMDANI:\n")
    fis_result(start, finish, fis_mamdani, 0.0001)

    print("SUGENO:\n")
    fis_result(start, finish, fis_sugeno, 0.5)

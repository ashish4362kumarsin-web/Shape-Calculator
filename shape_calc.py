"""Menu-driven shape calculator.

This version keeps the menus supplied by derives.py and fixes the calculation
and input-handling problems in the original program.
"""

import math
import time as t

import derives as dvs


class _CalculatorExit(Exception):
    """Internal signal used to exit cleanly from any depth of the menus."""


def _number(prompt):
    """Read one positive measurement, allowing whole numbers and decimals."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid value! Enter a number.")
        except EOFError:
            raise SystemExit("No input detected!")


def _result(label, value):
    print("\n//:Wait//\n")
    t.sleep(0.4)
    print(f"{label} = {value:g}")


def _menu(show_menu, actions):
    """Run a derives.py menu until the user chooses Back or Exit."""
    show_menu()
    while True:
        print("\nPress b to back!")
        try:
            choice = input("Enter Choice: ").strip().lower()
        except EOFError:
            print("No input detected!")
            return False

        if choice == "b":
            print("You are now on the previous page.")
            return True
        if choice == "0":
            raise _CalculatorExit

        try:
            action = actions[int(choice)]
        except (ValueError, KeyError):
            print("Invalid choice!")
            continue

        print()
        action()


def _two_option_surface_menu(total_surface_area, lateral_surface_area):
    return _menu(
        dvs.a_dim_tsa_lsa,
        {1: total_surface_area, 2: lateral_surface_area},
    )


def _circle_menu(is_semicircle=False):
    def area():
        radius = _number("Enter radius:   ")
        multiplier = 0.5 if is_semicircle else 1
        _result("Area", multiplier * math.pi * radius ** 2)

    def circumference():
        radius = _number("Enter radius:   ")
        if is_semicircle:
            # A semicircle's perimeter includes the straight diameter.
            _result("Perimeter", math.pi * radius + 2 * radius)
        else:
            _result("Circumference", 2 * math.pi * radius)

    _menu(dvs.cir_a_c_entrance, {1: area, 2: circumference})


def _area_2d():
    def triangle():
        base = _number("Enter Base:   ")
        height = _number("Enter Height:   ")
        _result("Area", base * height / 2)

    def rectangle():
        length = _number("Enter Length: ")
        breadth = _number("Enter Breadth: ")
        _result("Area", length * breadth)

    def square():
        side = _number("Enter Side: ")
        _result("Area", side ** 2)

    def parallelogram():
        base = _number("Enter Base:   ")
        height = _number("Enter Height:   ")
        _result("Area", base * height)

    def rhombus():
        diagonal_1 = _number("Enter Diagonal 1:   ")
        diagonal_2 = _number("Enter Diagonal 2:   ")
        _result("Area", diagonal_1 * diagonal_2 / 2)

    def trapezium():
        height = _number("Enter Height:   ")
        side_1 = _number("Enter parallel side 1:   ")
        side_2 = _number("Enter parallel side 2:   ")
        _result("Area", height * (side_1 + side_2) / 2)

    _menu(
        dvs.a_dim_2d,
        {
            1: triangle,
            2: rectangle,
            3: square,
            4: parallelogram,
            5: rhombus,
            6: trapezium,
            7: _circle_menu,
            8: lambda: _circle_menu(is_semicircle=True),
        },
    )


def _area_3d():
    def cube():
        def tsa():
            edge = _number("Enter Edge:   ")
            _result("Total Surface Area", 6 * edge ** 2)

        def lsa():
            edge = _number("Enter Edge:   ")
            _result("Lateral Surface Area", 4 * edge ** 2)

        _two_option_surface_menu(tsa, lsa)

    def cuboid():
        def dimensions():
            return (
                _number("Enter Height:   "),
                _number("Enter Length:   "),
                _number("Enter Breadth:   "),
            )

        def tsa():
            height, length, breadth = dimensions()
            _result("Total Surface Area", 2 * (length * breadth + length * height + breadth * height))

        def lsa():
            height, length, breadth = dimensions()
            _result("Lateral Surface Area", 2 * height * (length + breadth))

        _two_option_surface_menu(tsa, lsa)

    def cylinder():
        def tsa():
            height = _number("Enter Height:   ")
            radius = _number("Enter Radius:   ")
            _result("Total Surface Area", 2 * math.pi * radius * (radius + height))

        def lsa():
            height = _number("Enter Height:   ")
            radius = _number("Enter Radius:   ")
            _result("Lateral Surface Area", 2 * math.pi * radius * height)

        _two_option_surface_menu(tsa, lsa)

    def cone():
        def tsa():
            radius = _number("Enter Radius:   ")
            slant_height = _number("Enter Slant Height:   ")
            _result("Total Surface Area", math.pi * radius * (radius + slant_height))

        def lsa():
            radius = _number("Enter Radius:   ")
            slant_height = _number("Enter Slant Height:   ")
            _result("Lateral Surface Area", math.pi * radius * slant_height)

        _two_option_surface_menu(tsa, lsa)

    def sphere():
        radius = _number("Enter Radius:   ")
        _result("Surface Area", 4 * math.pi * radius ** 2)

    def hemisphere():
        def tsa():
            radius = _number("Enter Radius:   ")
            _result("Total Surface Area", 3 * math.pi * radius ** 2)

        def lsa():
            radius = _number("Enter Radius:   ")
            _result("Lateral Surface Area", 2 * math.pi * radius ** 2)

        _two_option_surface_menu(tsa, lsa)

    _menu(dvs.a_dim_3d, {1: cube, 2: cuboid, 3: cylinder, 4: cone, 5: sphere, 6: hemisphere})


def _area():
    _menu(dvs.a_dimension_entrance, {1: _area_2d, 2: _area_3d})


def _volume():
    def cube():
        side = _number("Enter Side:   ")
        _result("Volume", side ** 3)

    def cuboid():
        length = _number("Enter Length:   ")
        breadth = _number("Enter Breadth:   ")
        height = _number("Enter Height:   ")
        _result("Volume", length * breadth * height)

    def cylinder():
        radius = _number("Enter Radius:   ")
        height = _number("Enter Height:   ")
        _result("Volume", math.pi * radius ** 2 * height)

    def cone():
        radius = _number("Enter Radius:   ")
        height = _number("Enter Height:   ")
        _result("Volume", math.pi * radius ** 2 * height / 3)

    def sphere():
        radius = _number("Enter Radius:   ")
        _result("Volume", 4 * math.pi * radius ** 3 / 3)

    def hemisphere():
        radius = _number("Enter Radius:   ")
        _result("Volume", 2 * math.pi * radius ** 3 / 3)

    _menu(dvs.v_shapes_entrance, {1: cube, 2: cuboid, 3: cylinder, 4: cone, 5: sphere, 6: hemisphere})


def part():
    """Start the calculator (kept as the original public entry point)."""
    try:
        dvs.main_entrance()
        while True:
            choice = input("\nEnter Choice:    ").strip()

            if choice == "0":
                return
            if choice == "1":
                _menu(dvs.a_v_entrance, {1: _area, 2: _volume})
            else:
                print("Invalid choice!")
    except _CalculatorExit:
        return
    except EOFError:
        print("No input detected!")
        return


if __name__ == "__main__":
    part()

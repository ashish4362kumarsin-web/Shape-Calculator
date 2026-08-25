# Shape Calculator

A simple, menu-driven Python calculator for common two-dimensional and three-dimensional shapes. It calculates areas, surface areas, circumferences, perimeters, and volumes through an interactive terminal menu.

## Features

- 2D area calculations for triangles, rectangles, squares, parallelograms, rhombuses, trapeziums, circles, and semicircles.
- 3D surface-area calculations for cubes, cuboids, cylinders, cones, spheres, and hemispheres.
- Volume calculations for cubes, cuboids, cylinders, cones, spheres, and hemispheres.
- Supports decimal measurements.
- Validates invalid, zero, and negative measurements.
- Use `b` to return to the previous menu and `0` to exit from any menu.

## Files

| File | Purpose |
| --- | --- |
| `shape_calc.py` | Main calculator program. |
| `derives.py` | Displays the menu screens used by the calculator. |

Both files must be kept in the same folder.

## Requirements

- Python 3.8 or newer
- No third-party packages are required

## Run the calculator

Open a terminal in the project folder and run:

```bash
python shape_calc.py
```

If you are using the corrected version provided with this project, rename `shape_calc_corrected.py` to `shape_calc.py` (or run it by its existing name) and keep `derives.py` beside it:

```bash
python shape_calc_corrected.py
```

## Example

To calculate the area of a circle with radius `2`:

1. Select `1` for **Maths**.
2. Select `1` for **Area**.
3. Select `1` for **2-Dimensional**.
4. Select `7` for **Circle**.
5. Select `1` for **Area**.
6. Enter `2` as the radius.

Result: `Area = 12.5664`

## Formula reference

| Shape | Calculation |
| --- | --- |
| Circle area | πr² |
| Circle circumference | 2πr |
| Semicircle area | ½πr² |
| Semicircle perimeter | πr + 2r |
| Cylinder volume | πr²h |
| Cone volume | ⅓πr²h |
| Sphere volume | ⁴⁄₃πr³ |
| Hemisphere volume | ²⁄₃πr³ |

## License

This project currently has no license. Add a `LICENSE` file before publishing if you want to specify how others may use it.

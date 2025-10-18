'''
Name: Sachkerat Singh
Student ID: 100996938
Course: TPRG 2131 - Programming for Technology II
Assignment 1 - PyTest File
Date: Oct, 2024

This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving
credit to the original author(s).

Description:
This test file checks all 5 calculator functions from A_V_calcSSM.py
using pytest. Each function is tested with at least 3 examples.
'''

import os
import math

# Check if the A_V_calcSSM.py file exists in the same folder
if not os.path.exists("A_V_calcSSM.py"):
    print("⚠️ ERROR: Could not find 'A_V_calcSSM.py' in this folder.")
    print("➡️ Make sure this test file is saved in the SAME folder as your A_V_calcSSM.py file.")
    quit()  # Stop the test early so pytest won’t crash

# Import functions after confirming the file exists
from A_V_calcSSM import (
    area_circle,
    vol_cylinder,
    area_rectangular,
    vol_sphere,
    area_triangle
)

# ---------- TEST AREA OF A CIRCLE ----------
def test_area_circle():
    """Test area of a circle with multiple values."""
    assert area_circle(1) == round(math.pi * 1**2, 1)
    assert area_circle(5) == round(math.pi * 5**2, 1)
    assert area_circle(10) == round(math.pi * 10**2, 1)

# ---------- TEST VOLUME OF A CYLINDER ----------
def test_vol_cylinder():
    """Test volume of a cylinder with multiple values."""
    assert vol_cylinder(2, 5) == round(math.pi * 2**2 * 5, 1)
    assert vol_cylinder(3, 7) == round(math.pi * 3**2 * 7, 1)
    assert vol_cylinder(4, 10) == round(math.pi * 4**2 * 10, 1)

# ---------- TEST AREA OF A RECTANGLE ----------
def test_area_rectangular():
    """Test area of a rectangle with multiple values."""
    assert area_rectangular(2, 3) == 6.0
    assert area_rectangular(5, 8) == 40.0
    assert area_rectangular(10, 12) == 120.0

# ---------- TEST VOLUME OF A SPHERE ----------
def test_vol_sphere():
    """Test volume of a sphere with multiple values."""
    assert vol_sphere(2) == round((4/3) * math.pi * 2**3, 1)
    assert vol_sphere(5) == round((4/3) * math.pi * 5**3, 1)
    assert vol_sphere(10) == round((4/3) * math.pi * 10**3, 1)

# ---------- TEST AREA OF A TRIANGLE ----------
def test_area_triangle():
    """Test area of a triangle with multiple values."""
    assert area_triangle(4, 6) == 12.0
    assert area_triangle(10, 5) == 25.0
    assert area_triangle(3, 9) == 13.5

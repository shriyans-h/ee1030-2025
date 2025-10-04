import math

# Define PI for trigonometric calculations
PI = math.pi

def to_radians(degrees: float) -> float:
    return degrees * PI / 180.0

def check_triangle_properties(angle_A_deg: float):
    print(f"--- Checking for A = {angle_A_deg:.2f} degrees ---")

    if angle_A_deg > 60.0 or angle_A_deg <= 0:
        print("A triangle with this condition cannot exist for A > 60 degrees or A <= 0.")
        print("The expression 2*sin(A/2) would be > 1, which is impossible for a cosine value.\n")
        return

    # Convert angle A to radians
    A_rad = to_radians(angle_A_deg)

    # Step 1: Find angles B and C that satisfy the condition
    val_for_acos = 2.0 * math.sin(A_rad / 2.0)

    # Check if acos input is in valid domain
    if val_for_acos > 1.0:
        print("acos argument exceeds 1. Invalid configuration.\n")
        return

    B_minus_C_half_rad = math.acos(val_for_acos)
    B_plus_C_half_rad = PI / 2.0 - A_rad / 2.0

    B_rad = B_plus_C_half_rad + B_minus_C_half_rad
    C_rad = B_plus_C_half_rad - B_minus_C_half_rad

    # Step 2: Verify the original trigonometric identity
    lhs_identity = math.cos(B_rad) + math.cos(C_rad)
    rhs_identity = 4.0 * (math.sin(A_rad / 2.0) ** 2)

    print("Verification of given identity:")
    print(f"  LHS (cos B + cos C)    = {lhs_identity}")
    print(f"  RHS (4 * sin^2(A/2)) = {rhs_identity}")

    # Step 3: Verify the derived side relationship b + c = 2a
    a = math.sin(A_rad)
    b = math.sin(B_rad)
    c = math.sin(C_rad)

    b_plus_c = b + c
    two_a = 2.0 * a

    print("\nVerification of the side relationship (b + c = 2a):")
    print("  Relative side lengths (a=sinA, b=sinB, c=sinC):")
    print(f"    b + c = {b_plus_c}")
    print(f"    2 * a = {two_a}")

    # Allow small numerical tolerance
    if abs(b_plus_c - two_a) < 1e-9:
        print("\nResult: The relationship b + c = 2a holds true.\n")
    else:
        print("\nResult: The relationship b + c = 2a does NOT hold.\n")

def main():
    print("## Solution Verification for Triangle Problem ##\n")
    print("This program verifies the two correct conclusions from the problem:")
    print("  b) b + c = 2a")
    print("  c) locus of the point A is an ellipse\n")

    # Part 1: Numerical Verification
    print("### Part 1: Verifying the side relationship b + c = 2a ###\n")
    print("The code will now test the derived relationship for various valid angles of A.\n")

    # Test various angles
    check_triangle_properties(60.0)  # Equilateral triangle
    check_triangle_properties(45.0)
    check_triangle_properties(30.0)

    # Invalid case
    check_triangle_properties(90.0)

    # Part 2: Locus Explanation
    print("### Part 2: Determining the Locus of Point A ###\n")
    print("1. The problem states that the base BC is fixed. Let its length be 'a'.")
    print("2. From the derivation, we found the relationship b + c = 2a.")
    print("3. The side 'b' is the distance AC, and 'c' is the distance AB.")
    print("4. Therefore, the condition is AB + AC = 2a.")
    print("5. Since 'a' is a fixed length, '2a' is a constant value.\n")
    print("This is the geometric definition of an ellipse:")
    print("The set of all points (A) for which the sum of the distances to two fixed points (the foci, B and C) is a constant (2a).\n")
    print("Conclusion: The locus of point A is an ellipse.\n")

if __name__ == "__main__":
    main()

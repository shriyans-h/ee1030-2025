#include <stdio.h>
#include <math.h>

// Define PI for trigonometric calculations if not already defined
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

double to_radians(double degrees) {
    return degrees * M_PI / 180.0;
}

void check_triangle_properties(double angle_A_deg) {
    printf("--- Checking for A = %.2f degrees ---\n", angle_A_deg);

    // For a valid triangle, the simplified condition cos((B-C)/2) = 2*sin(A/2) must hold.
    // Since the maximum value of cosine is 1, we must have 2*sin(A/2) <= 1.
    // This implies sin(A/2) <= 0.5, which means A/2 <= 30 degrees, so A <= 60 degrees.
    if (angle_A_deg > 60.0 || angle_A_deg <= 0) {
        printf("A triangle with this condition cannot exist for A > 60 degrees or A <= 0.\n");
        printf("The expression 2*sin(A/2) would be > 1, which is impossible for a cosine value.\n\n");
        return;
    }

    // Convert angle A to radians for use in math functions
    double A_rad = to_radians(angle_A_deg);

    // --- Step 1: Find angles B and C that satisfy the condition ---
    // From the simplified relation: cos((B-C)/2) = 2*sin(A/2)
    double val_for_acos = 2.0 * sin(A_rad / 2.0);
    double B_minus_C_half_rad = acos(val_for_acos);
    
    // We also know A + B + C = PI radians, so (B+C)/2 = PI/2 - A/2
    double B_plus_C_half_rad = M_PI / 2.0 - A_rad / 2.0;

    // Solve for B and C
    double B_rad = B_plus_C_half_rad + B_minus_C_half_rad;
    double C_rad = B_plus_C_half_rad - B_minus_C_half_rad;

    // --- Step 2: Verify the original trigonometric identity ---
    double lhs_identity = cos(B_rad) + cos(C_rad);
    double rhs_identity = 4.0 * pow(sin(A_rad / 2.0), 2);
    printf("Verification of given identity:\n");
    printf("  LHS (cos B + cos C)    = %f\n", lhs_identity);
    printf("  RHS (4 * sin^2(A/2)) = %f\n", rhs_identity);

    // --- Step 3: Verify the derived side relationship b + c = 2a ---
    // Using the Sine Rule, we can use the sines of the angles as relative side lengths.
    double a = sin(A_rad);
    double b = sin(B_rad);
    double c = sin(C_rad);

    double b_plus_c = b + c;
    double two_a = 2.0 * a;

    printf("\nVerification of the side relationship (b + c = 2a):\n");
    printf("  Relative side lengths (a=sinA, b=sinB, c=sinC):\n");
    printf("    b + c = %f\n", b_plus_c);
    printf("    2 * a = %f\n", two_a);

    // Check for equality using a small tolerance for floating-point errors
    if (fabs(b_plus_c - two_a) < 1e-9) {
        printf("\nResult: The relationship b + c = 2a holds true. \n\n");
    } else {
        printf("\nResult: The relationship b + c = 2a does NOT hold. \n\n");
    }
}

int main() {
    printf("## Solution Verification for Triangle Problem ##\n\n");
    printf("This program verifies the two correct conclusions from the problem:\n");
    printf("  b) b + c = 2a\n");
    printf("  c) locus of the point A is an ellipse\n\n");

    // --- Part 1: Numerical Verification of b + c = 2a ---
    printf("### Part 1: Verifying the side relationship b + c = 2a ###\n\n");
    printf("The code will now test the derived relationship for various valid angles of A.\n\n");

    // Check for a few valid angles of A (where A <= 60 degrees)
    check_triangle_properties(60.0); // Special case: equilateral triangle
    check_triangle_properties(45.0);
    check_triangle_properties(30.0);
    
    // Check an invalid angle to show the constraint
    check_triangle_properties(90.0);

    // --- Part 2: Explanation of the Locus of A ---
    printf("### Part 2: Determining the Locus of Point A ###\n\n");
    printf("1. The problem states that the base BC is fixed. Let its length be 'a'.\n");
    printf("2. From the derivation, we found the relationship b + c = 2a.\n");
    printf("3. The side 'b' is the distance AC, and 'c' is the distance AB.\n");
    printf("4. Therefore, the condition is AB + AC = 2a.\n");
    printf("5. Since 'a' is a fixed length, '2a' is a constant value.\n\n");
    printf("This is the geometric definition of an ellipse: the set of all points (A) for which the sum of the distances to two fixed points (the foci, B and C) is a constant (2a).\n\n");
    printf("Conclusion: The locus of point A is an ellipse. \n");

    return 0;
}
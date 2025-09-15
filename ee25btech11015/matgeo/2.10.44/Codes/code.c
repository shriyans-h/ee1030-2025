#include <math.h>

// Function to check inequality
// Returns 1 if inequality holds, 0 otherwise
int is_within_bound(float ax, float ay, float az,
                    float bx, float by, float bz,
                    float cx, float cy, float cz) {
    
    // Compute squared distances
    float ab = (ax - bx)*(ax - bx) + (ay - by)*(ay - by) + (az - bz)*(az - bz);
    float bc = (bx - cx)*(bx - cx) + (by - cy)*(by - cy) + (bz - cz)*(bz - cz);
    float ca = (cx - ax)*(cx - ax) + (cy - ay)*(cy - ay) + (cz - az)*(cz - az);

    float sum = ab + bc + ca;

    if (sum <= 9.0f) {
        return 1;  // Inequality holds
    } else {
        return 0;  // Inequality violated
    }
}

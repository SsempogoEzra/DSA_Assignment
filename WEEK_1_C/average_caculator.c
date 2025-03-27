#include <stdio.h>

int main() {
    float physics[4], chemistry[4], math[4];
    float totalPhysics = 0, totalChemistry = 0, totalMath = 0;
    float averagePhysics, averageChemistry, averageMath;
    float overallAverage;

    // Input marks for Physics
    printf("Enter marks for Physics (Assignment, Coursework, Mid-term, End-of-term):\n");
    for (int i = 0; i < 4; i++) {
        scanf("%f", &physics[i]);
        totalPhysics += physics[i];
    }

    // Input marks for Chemistry
    printf("Enter marks for Chemistry (Assignment, Coursework, Mid-term, End-of-term):\n");
    for (int i = 0; i < 4; i++) {
        scanf("%f", &chemistry[i]);
        totalChemistry += chemistry[i];
    }

    // Input marks for Math
    printf("Enter marks for Math (Assignment, Coursework, Mid-term, End-of-term):\n");
    for (int i = 0; i < 4; i++) {
        scanf("%f", &math[i]);
        totalMath += math[i];
    }

    // Calculate averages
    averagePhysics = totalPhysics / 4;
    averageChemistry = totalChemistry / 4;
    averageMath = totalMath / 4;

    // Calculate overall average
    overallAverage = (averagePhysics + averageChemistry + averageMath) / 3;

    // Output results
    printf("\nAverage marks:\n");
    printf("Physics: %.2f\n", averagePhysics);
    printf("Chemistry: %.2f\n",averageChemistry);
    printf("math: %.2f\n",averageMath);
    printf("overallAverage: %.2f\n",overallAverage);


    return 0;
}
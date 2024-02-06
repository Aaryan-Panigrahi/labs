#include <stdio.h>

// Function to check if a subset with the given sum exists and print the elements
int isSubsetSum(int arr[], int n, int sum, int subset[]) {
    // Base cases
    if (sum == 0) {
        // Print the subset elements
        printf("Subset: { ");
        for (int i = 0; i < n; i++) {
            if (subset[i] == 1) {
                printf("%d ", arr[i]);
            }
        }
        printf("}\n");
        return 1;
    }
    if (n == 0 && sum != 0)
        return 0;

    // If the last element is greater than the sum, ignore it
    if (arr[n - 1] > sum)
        return isSubsetSum(arr, n - 1, sum, subset);

    // Check if the sum can be obtained by including or excluding the last element
    return isSubsetSum(arr, n - 1, sum, subset) || isSubsetSum(arr, n - 1, sum - arr[n - 1], subset);
}

// Function to check if the array can be partitioned into two subsets with equal sum
int canPartition(int arr[], int n) {
    // Calculate the total sum of the array
    int totalSum = 0;
    for (int i = 0; i < n; i++)
        totalSum += arr[i];

    // If the total sum is odd, it cannot be partitioned into two equal subsets
    if (totalSum % 2 != 0)
        return 0;

    int subset[n];
   

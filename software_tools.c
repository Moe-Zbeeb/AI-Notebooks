#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to calculate the mean of a list
double mean(int arr[], int n) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum / n;
}

// Function to calculate the median of a list
double median(int arr[], int n) {
    // Sort the array
    qsort(arr, n, sizeof(int), compare);
    
    // Check if the number of elements is odd or even
    if (n % 2 == 0) {
        return (arr[n / 2 - 1] + arr[n / 2]) / 2.0;
    } else {
        return arr[n / 2];
    }
}

// Function to calculate the mode of a list
int mode(int arr[], int n) {
    int maxCount = 0, modeValue = 0;
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (arr[j] == arr[i])
                count++;
        }
        if (count > maxCount) {
            maxCount = count;
            modeValue = arr[i];
        }
    }
    return modeValue;
}

// Function to calculate the variance of a list
double variance(int arr[], int n) {
    double meanValue = mean(arr, n);
    double variance = 0;
    for (int i = 0; i < n; i++) {
        variance += pow(arr[i] - meanValue, 2);
    }
    return variance / n;
}

// Function to calculate the standard deviation of a list
double standardDeviation(int arr[], int n) {
    return sqrt(variance(arr, n));
}

// Function to calculate the sum of a list
int sum(int arr[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum;
}

// Function to calculate the product of a list
long long product(int arr[], int n) {
    long long product = 1;
    for (int i = 0; i < n; i++) {
        product *= arr[i];
    }
    return product;
}

// Function to calculate the range of a list
int range(int arr[], int n) {
    qsort(arr, n, sizeof(int), compare);
    return arr[n - 1] - arr[0];
}

// Function to calculate the coefficient of variation of a list
double coefficientOfVariation(int arr[], int n) {
    return (standardDeviation(arr, n) / mean(arr, n)) * 100;
}

// Function to calculate the geometric mean of a list
double geometricMean(int arr[], int n) {
    long double productValue = 1.0;
    for (int i = 0; i < n; i++) {
        productValue *= arr[i];
    }
    return pow(productValue, 1.0 / n);
}

// Function to calculate the harmonic mean of a list
double harmonicMean(int arr[], int n) {
    double sumInv = 0;
    for (int i = 0; i < n; i++) {
        sumInv += 1.0 / arr[i];
    }
    return n / sumInv;
}

// Function to calculate the interquartile range of a list
double interquartileRange(int arr[], int n) {
    // Sort the array
    qsort(arr, n, sizeof(int), compare);
    
    // Calculate the first quartile (Q1)
    double q1;
    if (n % 4 == 0) {
        q1 = (arr[n / 4 - 1] + arr[n / 4]) / 2.0;
    } else {
        q1 = arr[n / 4];
    }

    // Calculate the third quartile (Q3)
    double q3;
    if (n % 4 == 0) {
        q3 = (arr[3 * n / 4 - 1] + arr[3 * n / 4]) / 2.0;
    } else {
        q3 = arr[3 * n / 4];
    }

    return q3 - q1;
}

// Function to calculate the skewness of a list
double skewness(int arr[], int n) {
    double meanValue = mean(arr, n);
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += pow(arr[i] - meanValue, 3);
    }
    double varianceValue = variance(arr, n);
    double cubedRoot = pow(varianceValue, 1.5);
    return sum / (n * cubedRoot);
}

// Function to calculate the kurtosis of a list
double kurtosis(int arr[], int n) {
    double meanValue = mean(arr, n);
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += pow(arr[i] - meanValue, 4);
    }
    double varianceValue = variance(arr, n);
    double squaredVariance = pow(varianceValue, 2);
    return sum / (n * squaredVariance);
}

// Function to calculate the population covariance between two lists
double covariance(int arr1[], int arr2[], int n) {
    double sum = 0;
    double meanArr1 = mean(arr1, n);
    double meanArr2 = mean(arr2, n);
    for (int i = 0; i < n; i++) {
        sum += (arr1[i] - meanArr1) * (arr2[i] - meanArr2);
    }
    return sum / n;
}

// Function to calculate the population correlation coefficient between two lists
double correlation(int arr1[], int arr2[], int n) {
    double cov = covariance(arr1, arr2, n);
    double sdArr1 = standardDeviation(arr1, n);
    double sdArr2 = standardDeviation(arr2, n);
    return cov / (sdArr1 * sdArr2);
}

// Function to count the number of elements in a list
int countElements(int arr[], int n) {
    return n;
}

// Function to count the number of even elements in a list
int countEven(int arr[], int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0)
            count++;
    }
    return count;
}

// Function to count the number of odd elements in a list
int countOdd(int arr[], int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 != 0)
            count++;
    }
    return count;
}

// Function to count the number of positive elements in a list
int countPositive(int arr[], int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > 0)
            count++;
    }
    return count;
}

// Function to count the number of negative elements in a list
int countNegative(int arr[], int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] < 0)
            count++;
    }
    return count;
}

// Function to count the number of zeros in a list
int countZeros(int arr[], int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0)
            count++;
    }
    return count;
}

// Function to perform quick sort
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);
        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to perform merge sort
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    int i = 0;
    int j = 0;
    int k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Function to perform binary search
int binarySearch(int arr[], int l, int r, int x) {
    if (r >= l) {
        int mid = l + (r - l) / 2;

        if (arr[mid] == x)
            return mid;

        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);

        return binarySearch(arr, mid + 1, r, x);
    }

    return -1;
}

// Function to perform selection sort
void selectionSort(int arr[], int n) {
    int i, j, min_idx;
    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
        swap(&arr[min_idx], &arr[i]);
    }
}

// Function to perform insertion sort
void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

// Comparator function for qsort
int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Mean: %lf\n", mean(arr, n));
    printf("Median: %lf\n", median(arr, n));
    printf("Mode: %d\n", mode(arr, n));
    printf("Variance: %lf\n", variance(arr, n));
    printf("Standard Deviation: %lf\n", standardDeviation(arr, n));
    printf("Sum: %d\n", sum(arr, n));
    printf("Product: %lld\n", product(arr, n));
    printf("Range: %d\n", range(arr, n));
    printf("Coefficient of Variation: %lf\n", coefficientOfVariation(arr, n));
    printf("Geometric Mean: %lf\n", geometricMean(arr, n));
    printf("Harmonic Mean: %lf\n", harmonicMean(arr, n));
    printf("Interquartile Range: %lf\n", interquartileRange(arr, n));
    printf("Skewness: %lf\n", skewness(arr, n));
    printf("Kurtosis: %lf\n", kurtosis(arr, n));
    printf("Count Elements: %d\n", countElements(arr, n));
    printf("Count Even: %d\n", countEven(arr, n));
    printf("Count Odd: %d\n", countOdd(arr, n));
    printf("Count Positive: %d\n", countPositive(arr, n));
    printf("Count Negative: %d\n", countNegative(arr, n));
    printf("Count Zeros: %d\n", countZeros(arr, n));
    
    // Quick Sort
    int arr1[] = {64, 25, 12, 22, 11};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    quickSort(arr1, 0, n1 - 1);
    printf("\nQuick Sort: ");
    for (int i = 0; i < n1; i++)
        printf("%d ", arr1[i]);
    
    // Merge Sort
    int arr2[] = {64, 25, 12, 22, 11};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    mergeSort(arr2, 0, n2 - 1);
    printf("\nMerge Sort: ");
    for (int i = 0; i < n2; i++)
        printf("%d ", arr2[i]);
    
    // Binary Search
    int arr3[] = {2, 3, 4, 10, 40};
    int n3 = sizeof(arr3) / sizeof(arr3[0]);
    int x = 10;
    int result = binarySearch(arr3, 0, n3 - 1, x);
    printf("\nBinary Search: Element %d is at index %d", x, result);
    
    // Selection Sort
    int arr4[] = {64, 25, 12, 22, 11};
    int n4 = sizeof(arr4) / sizeof(arr4[0]);
    selectionSort(arr4, n4);
    printf("\nSelection Sort: ");
    for (int i = 0; i < n4; i++)
        printf("%d ", arr4[i]);
    
    // Insertion Sort
    int arr5[] = {64, 25, 12, 22, 11};
    int n5 = sizeof(arr5) / sizeof(arr5[0]);
    insertionSort(arr5, n5);
    printf("\nInsertion Sort: ");
    for (int i = 0; i < n5; i++)
        printf("%d ", arr5[i]);

    return 0;
}

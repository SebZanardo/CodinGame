#include <stdio.h>


int main() {
    // Parse input
    char s[1001];
    fgets(s, sizeof(s), stdin);
    int k;
    scanf("%d", &k);

    // To store the longest subsequence length
    int longest = 0;

    // Acts as an optimised hashmap to count occurences of each letter
    int count[26] = {0};

    // How many letters are actively used in the count
    int active = 0;

    // Index to the front of the current subsequence
    int front = 0;

    // Iterator for current character
    int i = 0;
    char c;

    // Loop until end of string
    while ((c = s[i]) != '\n') {
        // Add to count for letter
        int key = c - 97;

        // If new character add to active counter
        if (count[key] == 0) {
            active++;
        }
        count[key]++;

        // Keep popping until a count goes back to zero
        // This means the number of active characters has been reduced
        if (active > k) {
            while (1) {
                key = s[front] - 97;
                count[key]--;
                front++;
                if (count[key] == 0) {
                    break;
                }
            }
            active--;
        }

        // Check if new best sequence
        i++;
        int length = i - front;
        if (length > longest) {
            longest = length;
        }
    }

    printf("%d\n", longest);
}


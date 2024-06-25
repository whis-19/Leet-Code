using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    // function to compute GCD
    public int GCD(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    public bool HasGroupsSizeX(int[] deck) {
        if (deck.Length == 0) return false;

        Dictionary<int, int> count = new Dictionary<int, int>();
        foreach (int card in deck) {
            if (!count.ContainsKey(card)) {
                count[card] = 0;
            }
            count[card]++;
        }
        
        // Step 2: Find the GCD of the counts
        int gcdValue = count.Values.First();
        foreach (int freq in count.Values) {
            gcdValue = GCD(gcdValue, freq);
        }
        
        // Step 3: Check if the GCD is greater than 1
        return gcdValue > 1;
    }
}

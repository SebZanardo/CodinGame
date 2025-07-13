// To debug: Console.Error.WriteLine("Debug messages...");

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;


class Solution
{
    static void Main(string[] args)
    {
        int L = int.Parse(Console.ReadLine());
        int H = int.Parse(Console.ReadLine());
        string T = Console.ReadLine().ToUpper();

        Dictionary<char, string[]> mapping = new Dictionary<char, string[]>();
        string order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?";

        foreach (char c in order) {
            mapping[c] = new string[H];
        }

        for (int i = 0; i < H; i++) {
            string ROW = Console.ReadLine();

            for (int c = 0; c < order.Length; c++) {
                char letter = order[c];

                // Read letter characters in dictionary
                for (int x = 0; x < L; x++) {
                    mapping[letter][i] += ROW[c * L + x];
                }
            }
        }

        string solution = "";

        for (int i = 0; i < H; i++) {
            foreach (char c in T) {
                if (mapping.ContainsKey(c)) {
                    solution += mapping[c][i];
                } else {
                    solution += mapping['?'][i];
                }
            }
            // Add newline to row if not last row
            if (i < H - 1) {
                solution += '\n';
            }
        }

        Console.WriteLine(solution);
    }
}

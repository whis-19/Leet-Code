using System;

public class Solution
{
    public int StrongPasswordChecker(string password)
    {
        int n = password.Length;
        bool hasLower = false, hasUpper = false, hasDigit = false;
        int missingType = 3;
        
        foreach (char c in password)
        {
            if (char.IsLower(c)) hasLower = true;
            if (char.IsUpper(c)) hasUpper = true;
            if (char.IsDigit(c)) hasDigit = true;
        }
        
        if (hasLower) missingType--;
        if (hasUpper) missingType--;
        if (hasDigit) missingType--;
        
        int replace = 0, oneSeq = 0, twoSeq = 0;
        for (int i = 2; i < n; i++)
        {
            if (password[i] == password[i - 1] && password[i] == password[i - 2])
            {
                int length = 2;
                while (i < n && password[i] == password[i - 1])
                {
                    length++;
                    i++;
                }
                replace += length / 3;
                if (length % 3 == 0) oneSeq++;
                else if (length % 3 == 1) twoSeq++;
            }
        }
        
        if (n < 6) return Math.Max(missingType, 6 - n);
        else if (n <= 20) return Math.Max(missingType, replace);
        else
        {
            int delete = n - 20;
            replace -= Math.Min(delete, oneSeq * 1) / 1;
            replace -= Math.Min(Math.Max(delete - oneSeq, 0), twoSeq * 2) / 2;
            replace -= Math.Max(delete - oneSeq - 2 * twoSeq, 0) / 3;
            return delete + Math.Max(missingType, replace);
        }
    }
}

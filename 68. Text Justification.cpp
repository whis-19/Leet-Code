class Solution
{
public:
    vector<string> fullJustify(vector<string> &words, int maxWidth)
    {
        vector<string> result;
        vector<string> currentLine;
        int currentLineLength = 0;

        for (const string &word : words)
        {
            // Check if adding this word would exceed maxWidth
            if (currentLineLength + word.length() + currentLine.size() > maxWidth)
            {
                // Justify the current line and add it to the result
                result.push_back(justifyLine(currentLine, currentLineLength, maxWidth));
                currentLine.clear();
                currentLineLength = 0;
            }
            // Add word to current line
            currentLine.push_back(word);
            currentLineLength += word.length();
        }

        // Handle the last line (left-justified)
        string lastLine = join(currentLine, " ");
        lastLine.append(maxWidth - lastLine.length(), ' ');
        result.push_back(lastLine);

        return result;
    }

    string justifyLine(const vector<string> &line, int lineLength, int maxWidth)
    {
        if (line.size() == 1)
        {
            // Single word line
            return line[0] + string(maxWidth - lineLength, ' ');
        }

        int totalSpaces = maxWidth - lineLength;
        int evenSpace = totalSpaces / (line.size() - 1);
        int extraSpace = totalSpaces % (line.size() - 1);

        string justifiedLine;
        for (int i = 0; i < line.size(); ++i)
        {
            justifiedLine += line[i];
            if (i < line.size() - 1)
            {
                justifiedLine.append(evenSpace + (i < extraSpace ? 1 : 0), ' ');
            }
        }

        return justifiedLine;
    }

    string join(const vector<string> &words, const string &delimiter)
    {
        string result;
        for (int i = 0; i < words.size(); ++i)
        {
            if (i > 0)
                result += delimiter;
            result += words[i];
        }
        return result;
    }
};

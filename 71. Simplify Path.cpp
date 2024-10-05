class Solution
{
public:
    string simplifyPath(string path)
    {
        vector<string> stack;
        stringstream ss(path);
        string component;

        // Split the path by '/' and process each component
        while (getline(ss, component, '/'))
        {
            if (component == "" || component == ".")
            {
                continue; // Ignore empty and current directory components
            }
            if (component == "..")
            {
                if (!stack.empty())
                {
                    stack.pop_back(); // Go up one directory if possible
                }
            }
            else
            {
                stack.push_back(component); // Add valid directory name to the stack
            }
        }

        // Construct the simplified path
        string simplifiedPath = "/";
        for (int i = 0; i < stack.size(); ++i)
        {
            simplifiedPath += stack[i];
            if (i < stack.size() - 1)
            {
                simplifiedPath += "/";
            }
        }

        return simplifiedPath;
    }
};

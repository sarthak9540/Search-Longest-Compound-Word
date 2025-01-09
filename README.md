# ReadMe: Search Longest Compound Word

## Overview
This program identifies the **longest** and **second longest compound words** from a file and provides the **time taken to process the file**. A compound word is a word formed by concatenating two or more words from the file. The algorithm uses dynamic programming and set-based lookups for efficient processing.

### Design and Approach
1. **Dynamic Programming**: A cache (`dp`) stores previously checked words to avoid redundant calculations.
2. **Set Lookup**: A `set` is used for O(1) average lookup time for words.
3. **Recursive Validation**: Each word is split into prefixes and suffixes to check if it can be formed by other words in the list.

### Execution Steps
1. **Prepare Input File**: Create a text file with one word per line.
2. **Run the Program**:
   - Execute the script Solution.py and provide the file name when prompted.
   - example:-
   ```bash
   Enter file name: Input_01.txt
   ```
3. **View Results**: The program outputs the longest and second longest compound words along with processing time.

# vocab
This is a group-based vocabulary memorizer app. 
Group-based means based on a specific topic. 
Every time the app runs, it will pick 10 words based on date and interval algorithm.
Flow is
1.	Read a specified vocabulary file.
2.	Open the latest column to review based on entered date and interval.
2.1.	For the first time, just read top ten words
2.2.	For the second time and onward, check date
3.	Words check 
3.1.	If the picked word is remembered move to the next phase
3.2.	If not, back to the earlier phase
3.3.	Write to the file
4.	Ten words are completed.
5.	Column up to 6 stage are created.
6.	Close the file.

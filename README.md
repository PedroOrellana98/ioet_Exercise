# General Description

As a first point, the file was read in .txt format, which through the <open> function reads the file content line by line, in addition certain characters were replaced and divided into several strings, which were inserted into an array called <listData>.

Then a method called "appendList" was generated, which assigns the values ​​of the names found within the <listData> in a array called <listName> and returns the characters of the names of the people.

The third method called "averageList" what it does is compare each date of the <listData> and verify if they coincide with each other, once the similarity has been compared and found, it is assigned to a new array called <listName>.

The last method "compareHours" is the one that performs most of the business logic, first a loop is generated which runs through the entire <listData> array and using the <len> function, the indices of each array are obtained for determine the pairs of users and their hours of entry, then 3 arrays are generated which save the pairs of users and the frequency with which they coincided in the office, using the previous method "appendList" all possible pairs are joined within of the office by concatenating the two arrays <listName1> (“previous name”) and <listName2> (“next name”), and with the “averageList” method all existing pairs determine which day and hour of the week coincided with which they are allocated inside the <listAverage> array.

Finally, a loop is generated to print the output result on the console.

# Architecture

An algorithmic modeling was used in which the dataset that contained the people and the office hours was established as INPUT or input variables, then in the processing part to solve the problem, all the hours were compared by counting how many times The schedules have coincided according to the people compared, and finally, as OUTPUT, the pairs of people who have coincided and how often they have done so are presented.

# Approach

It was based on a practical and intuitive approach where you can reuse the code for a larger dataset and count based on how often people have matched anywhere.

# Methodology

The cascade methodology was used based on the requirements to be applied within the algorithm, the design, which is the definition for the structure of the solution based on the problem that was requested, the implementation, which is the part of the coding or development of the algorithm, verification that would validate that the program is executed correctly and without errors.

# Instructions for use

In order to use the program you need to have the .txt file with values ​​already entered previously, as an example you can use the file uploaded to Github called dataset.txt, you must also have a suitable version of Python 3.
In the execution part, to start the program, use the command "python3 main.py" (without quotes) and when you start the program, the name of the file is requested, for example: "dataset.txt" (also without quotes), as Lastly, the program shows the pairs of people with their schedules.

# Tests

An empirical analysis of the developed algorithm has been carried out, testing with different datasets that varied in the number of people and changing office hours, finally analyzing the results obtained in real time.
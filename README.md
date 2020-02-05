# 2020 Iowa Caucus Data Analysis

This is a small project for sifting through data from the 2020 Iowa caucuses.

Precinct-scale results from [here](https://results.thecaucuses.org).
Turned into a csv by:
1. Downloading raw html (which is one line for some godforsaken reason), trimming everything that isn't the table.
2. Adding `<table>` and `</table>` tags to beginning and end.
3. Making it a table instead of an unordered list: `<ul>` -> `<tr>` and `<li>` -> `<td>`.
4. Erasing commas because that confuses spreadsheet programs.
5. Opening it in a spreadsheet program, erasing county names and shifting first two rows.
6. Exporting as csv.

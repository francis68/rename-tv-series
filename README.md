# rename-tv-series

Place this file into the same directory as the folder who's content you want to rename.

Call this file in the terminal with the following arguments: python renamefiles.py

Enter the folder name of the folder you want to rename the contents of.

This pattern, [S]\d{2}[E]\d{2}, searches for the season and episode numbers in the name of the file and will remove
all other bloatware.

Example:

Original = Game.of.Thrones.S07E05.720p.WEB.h264-TBS[rarbg]

What we want = S07E05
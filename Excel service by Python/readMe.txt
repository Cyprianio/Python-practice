The program that performs the task, for stylistic reasons, is divided into two scripts. The first one - script.py -
is the main script that will create the requested new file "BUDZET_SZCZEGOLOWY.xlsx" on
based on a file named "plik_zrodlowy_zalacznik1.xlsx". The second script - styles.py - contains function declarations
needed to fill the cells in the new file and style them.
The second script is necessary for the correct operation of the first script and together with the base file -
"plik_zrodlowy_zalacznik1.xlsx" - must be in the same folder as the script.py file.

Note: When running the script again, remember to close the newly created "BUDZET_SZCZEGOLOWY.xlsx" file.
(if it has been opened).
Additionally, if the name of the newly created file is not changed and its content is manually changed
modified, then when the script is called again, the "BUDZET_SZCZEGOLOWY.xlsx" file will be reformatted
by the program without saving the changes made manually.
    # February 23 2:30pm

    Created the git repository for Project 1, following Professor Salazar's instructions. This project is multi-component. Tjere are tjree parts of this project, the first being a logger program, followed by an encryption program, and finishing with a driver program. The intention of this multicomponent program is for understanding basic operating system concepts through the use of initialization, user commands, logging, and termination. This project will be written in python for easy use.

    # March 1 2:26pm

    Starting first session of Project 1. Initial plan is to add the original files from project beginning stage (cpu and main memory) to repository, then begin with logger program.

    # March 1 2:33pm

    Upon further discovery, it appears the cpu.py and mem.py files listed in the project instructions are not necessary. Logger.py, Driver.py, and Encrypt.py files have been created.

    # March 1 3:03pm

    Started and potentially completed logger file. Instructions were straightforward for the use of logger, as it will continue working until the instruction line reads "QUIT" in which case it will end logging the message. Instructions also indicated the use of year-month-day format along with the 24 hour clock implemented, which will show before every logging message. The line will begin as the timestamp from the datetime module, the action requested, and the message.

    # March 1 3:21pm

    Beginning Encrypton program of project. Instructions describe this part of the system as accepting specific commands which therefore will be taken to the driver side of the program to be ran. The listed commands are PASS, ENCRYPT, DECRYPT, QUIT, RESULT, ERROR. What is likeliest the best scenario is using match-case command to pass the action for output following by the argument of the command. What is also listed is the use of Vigenere cypher for the passkey. This helps for the case-insensitive text encryption. Using the 26 letters of the alphabet, the Caeser Ciphers will correspond and encipher pushing each alphabet around it.

    # March 1 4:17pm

    Potentially completed Encryption program. Implements the Vigenere cipher for case-insensitive text encryption. For the commands, uses a match case to identify the string pass along on the command line, supporting pass, encrypt, decrypt, and quit. This ensures correct encryption and decryption outputs will match the manual calculation. When the instance of the input is when a password is not set, there is error handling set to catch this.

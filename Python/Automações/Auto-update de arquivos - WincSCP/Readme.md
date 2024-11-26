This work was developed with the objectible optimization of time. He's read an determined directory and validate what files should will be upload in WinSCP.

For that, was created some rules / timers for that execution, the rules are:
    If the file is modified between 8am to 3pm or between 3pm to 00pm, the're all files it's saved in list, and that files will be loaded in WinSCP.

Why we applicated the function "func_timeout"?
    The main objective is because when we're save the file in WinSCP with Python, there is a long time for WinSCP's answer to Python when the load file it's concluded. We're applicated the func_timeout for corrected that. When we save the file in WinSCP, same what the process of processing the save file in WinSCP it's not concluded, the file was saved. One file or another take a while than others, the main cause is the size of file.

-------------------------------------------------------------------------------------------------------------------------------------------------

Intructions:

        '''directory'''
        search_dir = f'C:\Users\{user}\Documents'  ----> in here, do you put where the files there are saved in your Pc / Network.

        '''list all files'''
        files = os.listdir(search_dir) ---> now, all files in directory are saveds on list "files".

    we created the list .... (it's a slice of the code)

        list_size = {None : None}
        new_item = None

        for file in files:

            size = os.path.getsize(search_dir + file) * 0.0009765625

            if size <= 10000:
                new_item = {file : 30}..... ---> in the moment, all file in directory are saved on list "list_size" with your size and 
                                                 we determine the timeout with base on size.

    Now, we connect with.... (it's a slice of the code)

        with sftp.cd('folder/share/prod/'): ---> in here, we put where the file must be saved in WinSCP server.

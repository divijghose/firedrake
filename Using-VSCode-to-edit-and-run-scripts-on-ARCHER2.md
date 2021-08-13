### VSCode instructions on Windows or WSL

If using WSL, just stick to Windows in the following.

1. Install VSCode through the Microsoft store.
2. Install the "Remote-SSH" extension within VSCode.
3. Generate an ssh key using git bash in ``/c/Users/local_username/.ssh/``, if you don't already have one.
4. Add this ssh key to your ARCHER2 account, if it hasn't already been.
5. Append the following to ``/c/Users/local_username/.ssh/config``:

```
Host login.archer2.ac.uk
  HostName login.archer2.ac.uk
  User archer_username
  IdentityFile "C:\Users\local_username\.ssh\id_ed25519"
```
(This can also be done in VSCode by hitting `F1` and searching for "Remote-SSH: Add new SSH host".)

6. In VSCode, hit `F1` and search for "Remote-SSH: Connect to host". Select `login.archer2.ac.uk` from the list. Enter your ARCHER2 password when prompted. (You may also need to enter the password associated with your SSH key.)
7. You should now be able to explore files using the left panel and open a terminal using the "Terminal" menu at the top.
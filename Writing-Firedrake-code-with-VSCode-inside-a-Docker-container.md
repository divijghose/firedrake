1. Make sure that Docker and VSCode are installed.
1. Install the "Dev Containers" extensions to VSCode.
1. Start the container that you want to develop with. For example:
    ```
    $ docker run -it firedrakeproject/firedrake:latest
    ```
    Note that the container must be left running in the terminal in order for VSCode to be able to attach to it.
1. Now you can open the container inside VSCode. To do this click on the icon on the bottom left of the screen ("Open a Remote Window"):
![bottomleft](https://github.com/user-attachments/assets/64ec34c8-b906-42f5-bebe-57dce7a98f81)
1. Then, click on "Attach to Running Container..." in the menu that appears.
![attach new](https://github.com/user-attachments/assets/576cf0e7-b5b2-446c-94e5-125795188860)
1. The running container should appear. Click on that and a new VSCode window will open that works inside the container!
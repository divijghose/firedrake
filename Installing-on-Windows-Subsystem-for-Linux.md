1. Follow the [instructions here](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to install Ubuntu Linux on your Windows 10 machine.
1. Ensure your Ubuntu installation is up to date.
   
    Run the following commands at the bash prompt:
```
sudo apt update
sudo apt upgrade
```
1. Install Firedrake using the [instructions here](https://firedrakeproject.org/download.html).
1. Set up X forwarding.
    If you want to have any gui (e.g. plotting), you need to set up X forwarding. This is not supported by Windows yet, but can be set up following the [instructions here](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/).
    - Download Xming [from here](https://sourceforge.net/projects/xming/), default settings are fine.
    - run the following command before running graphical commands:
        ```
        export DISPLAY=:0
        ```
    - You will probably wish to add that line to your `.bashrc` to avoid typing that command every time.
    - If you want Xming to auto-run when you start, it is helpful  
      to put these lines in your .bashrc:
        ```
        export PATH = $PATH:/mnt/c/<path to Xming folder>
        "/mnt/c/<path to Xming.exe in your Xming folder>" :0 - clipboard -multiwindow &> /dev/null
        ```
    - Without something like those lines, you have to run Xming
      from the Windows side each time you want to use it
1. General Tips:
    - If you need to edit Windows files from the Linux side, your C:
      drive is located at /mnt/c 
    - Editing Linux files from Windows is not recommended.
    - The default behavior for the terminal
      (which allows copy and pasting between Windows and Linux)
      also pauses whatever process is running in the terminal if you 
      have anything selected (e.g. if you are running the firedrake
      install and click on the terminal, it will pause but not tell you)
      Just press some key while on the terminal to de-select and get it
      running again
          - You can change this by right-clicking on the top bar
            selecting Properties, and under General disabling
            Quick-Edit mode. Keep in mind that this may
            also disable copy and paste.
          - From Properties you can also change text size/font, and 
            other things
          
author: [Ben Sepanski](mailto:Ben_Sepanski@Baylor.edu) ([alternative email](ben.sepanski@gmail.com))

Thanks also to Rob Kirby.
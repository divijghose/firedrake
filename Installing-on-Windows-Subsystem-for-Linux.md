1) Enable the "Windows Subsytem for Linux" optional feature
    - Open PowerShell as an Administrator
    - Run the following command:
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
2) Download & install from the Windows Store 
    - There are several Linux distros available, I did all this for Ubuntu
    - Note: There are other options for download & install, see [1]
3) Missing Packages
    - When I downloaded WSL, I didn't have gcc
    - I followed advice from [3] I made sure I was updated
sudo apt update
sudo apt upgrade
    - and then ran the following command:
sudo apt install build-essential
4) Setting up X-Forwarding
    - If you want to have any gui (e.g. plotting), you need to set up x-forwarding
    - This is not supported by windows yet, but can be set up 
      following advice from [4]
    - Download Xming from [5], default settings are fine.
    - run the following command before running graphical commands:
export DISPLAY=:0
    - I added the above line line to my bashrc, and it has worked fine
    - If you want Xming to auto-run when you start, it is helpful  
      to put these lines in your .bashrc:
export PATH = $PATH:/mnt/c/<path to Xming folder>
"/mnt/c/<path to Xming.exe in your Xming foler>" :0 - clipboard -multiwindow &> /dev/null
    - Those last two lines I believe are homebrewed, so if they
      are giving you trouble I may have done something wrong.
    - Without something like those lines, you have to run Xming
      from the Windows side each time you want to use it
5) General Tips:
    - If you need to edit Windows files from the Linux side, your C:
      drive is located at /mnt/c 
    - It is not recommended to edit Linux files from windows
    - I didn't know this, but the default behavior for the terminal
      (which allows copy and pasting between windows and linux)
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
          
sources: 
[1] Microsoft WSL Installation Guide
https://docs.microsoft.com/en-us/windows/wsl/install-win10
[2] Microsoft WSL FAQ
https://docs.microsoft.com/en-us/windows/wsl/faq
[3] Installing GCC
https://stackoverflow.com/questions/40615226/run-gcc-on-bash-on-windows-10-with-c-sharp-or-c
[4] X-Forwarding
https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/
[5] Xming download link
https://sourceforge.net/projects/xming/
date: October 8, 2018
author: Ben Sepanski
        Ben_Sepanski@Baylor.edu
        ben.sepanski@gmail.com
Dr. Kirby also helped with the setup
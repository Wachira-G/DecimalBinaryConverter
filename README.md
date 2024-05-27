The following is a break down on how to create the binary to decimal and decimal to binary converter app. It was heavily inspired by MariyaSha's project [here](https://www.youtube.com/watch?v=ah3JeHAfM0M) and [here](https://github.com/MariyaSha/BinarytoDecimal)

It takes a user-supplied number and converts it into the chosen base. It is a python application using the Kivy and Kivymd libraries.

You can develop the app on Windows os as illustrated listed below.

First, in your terminal, your need to create the project directory
`mkdir <YOUR PROJECT>`

Change directory into it
`cd <YOUR PROJECT>`

Create a virtual environment and activate it
`python3.11 -m venv <YOUR VIRTUAL ENV NAME>`
`source <YOUR VIRTUAL ENV NAME>/bin/activate`

Install relevant packages for this project
`pip install -r requirments.txt`
Kivy and Kivymd libraries are the key packages

Create your project files


Run your project to test functionality
`./main.py` or `python -m main.py`

Confirm that everything works as expected

The next phase is to create an apk file that can be installed on and android system and ran.
To compile the apk for android:

Refer to the [guide on packaging for android](https://kivy.org/doc/stable/guide/packaging-android.html#packaging-android)

How to use the android debugger bridge [adb](https://developer.android.com/tools/adb)

For windows 11 users, you will need to:

- Enable Windows Subsystem for Linux (WSL)
- Install a Linux distribution
- launch the Linux distribution
- Copy your Kivy project directory from the Windows partition to the WSL partition
- Create your environment as shown earlier


The next step would be to install buildozer (it is the easiest method to generate the apk file for beginners). [Instructions.](https://buildozer.readthedocs.io/en/latest/installation.html)

Install the buildozer package
`pip install --upgrade buildozer`

Update your linux
`sudo apt update`
`sudo apt upgrade -y`

Install some linux packages
`sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev adb`

Install the cython library
`pip install Cython virtualenv`

Modify your path by adding to below line at the end of your `~/.bashrc` file
`export PATH=$PATH:~/.local/bin/`

Exit your linux to activate the path changes
`exit`

Then relaunch your linux
E.g `$ bash` on windows powershell

Activate your environment once more

Create a .spec file to configure your app
`buildozer init`
This generates a `buildozer.spec` file in your project directory.

Edit buildozer.spec file with an editor of your choice.
add name , package name, version no, requirements, photo paths, etc.


Then to issue the following command.
`buildozer android debug deploy run`
This command will take a long time to finish, depending on your machine's specs. So waiiiiiiiiiit
It will require you to accept some terms.

NOTE:
Your may run into some errors with this command.
e.g. some git packages may fail to download and you may be forced to manually clone them to the relevant directory. This may be due to connectivity issues, memory, etc. Read the log to understand the reason behind the fail

For example packages in the SDL2_image/external/ failed to finish cloning in my case and i was to manually download them, modify the download.sh file in their location.

When the process is complete, an apk file will be generated in your project's bin directory.

The below steps can be done bone before running the `buidozer android ...` command
For windows 11 users, you need to make some additions to your windows:
- Install usbipd
`winget install usbipd`
- List attached devices
`usbipd list`
- Get the bus id of your android device you intend to install your app from the above list

- Bind it by opening a terminal on elevated permissions:
`usbipd bind --busid <BUS-ID>`

- Then on a normal terminal, attach the android device
`usbipd attach --wsl --busid <BUS-ID>`

Back to your linux terminal, run lsusb to view if device attached to wsl(if on windows) or is available in your system.
`lsusb`

On your android device:
- Open developer options
- Open debug mode

This will happen after the apk has been generated, from automated process, or running `adb install bin\<YOUR APK>`
- Confirm the prompt on your phone.


If the apk was not successfully installed, may need to install manually
`adb kill-server`
`adb start-server`
`adb devices` confirm the android device is available
`lsusb`
`adb install binary2decimal-0.1-arm64-v8a_armeabi-v7a-debug.apk`

After a success install, it may run automatically or you can manually run your app on your android device.
if it has some problems, run the command below then relaunch app and see the logs to identify what went wrong.
`adb logcat`


Your have successfully created your android app using python. Congratulations!

# Software Installation
In this section, we will describe how to install a discrete event simulation software and XLRisk (Monte Carlo Excel Plugin) on your personal machine.

## XLRisk (For Mac and Windows)
XLRisk is a free and open source Monte Carlo Excel Plugin that is similar to \@Risk! It allows the user to define distributions with parameters and use the Monte Carlo Method to simulate systems.

Here is the documentation for using its functions after you install it: https://github.com/pyscripter/XLRisk/wiki/RiskFunctions.

### Windows
1. Download XLRisk from https://github.com/pyscripter/XLRisk/raw/master/XLRisk.xlam.
2. Left-Click the file in your downloads folder and click properties, a window will pop-up, and untick “blocked”, then press apply, this is the window after unblocking it:
:::{figure} ../Figs/Chapter_Lab/XLriskWindowsDialogue.png
:scale: 10 %
:align: center
:label: XLRiskWin
:::
3. Open Excel, and go to Options, and click on Add-ins, and you should get this screen: 
:::{figure} ../Figs/Chapter_Lab/ExcelAddinsDialogue.png
:scale: 20 %
:align: center
:label: XLRiskWin1
:::
4. Click on “Go...” And you will get this small popup, in this small pop-up window, click on “Browse” and go to your downloads folder and click on XLRisk.xlam:

:::{figure} ../Figs/Chapter_Lab/XLRiskActivateDialogue.png
:scale: 20 %
:align: center
:label: XLRiskWin2
:::

5. After that the XLRisk tab will appear at the top of your Excel window! 

### Mac
1. Download XLRisk from https://github.com/pyscripter/XLRisk/raw/master/XLRisk.xlam.
2. Open Excel, Click on “Excel” which is also marked with a red rectangle, then click on Preferences which is marked with a blue rectangle below:
:::{figure} ../Figs/Chapter_Lab/XLriskMacStep2.png
:scale: 20 %
:align: center
:label: XLRisk
:::
3. You should see a screen that says “Preferences” appear, and once it appears, click on “View”:
:::{figure} ../Figs/Chapter_Lab/XLriskMacStep3.png
:scale: 20 %
:align: center
:label: XLRiskMac
:::
4. Once you are in the view preferences screen (screenshot below), click on the “In Ribbon, Show Developer tab” checkbox:
:::{figure} ../Figs/Chapter_Lab/XLriskMacStep4.png
:scale: 20 %
:align: center
:label: XLRiskMac1
:::
5. Now exit the preferences window, and your Excel will now look like the screenshot below – click on the Developer Tab:
:::{figure} ../Figs/Chapter_Lab/XLriskMacStep5.png
:scale: 20 %
:align: center
:label: XLRiskMac2
:::
6. Now, that you are in the developer tab, you can now click on “Excel Add-Ins” which is highlighted with a blue box below:
:::{figure} ../Figs/Chapter_Lab/XLriskMacStep6.png
:scale: 20 %
:align: center
:label: XLRiskMac3
:::
7. Now, we are almost done with the setup process, once you click on the Excel Add-Ins, there will be a pop-up window – click browse and select the file “XLRisk.xlsm” and it will appear in the Excel Add-Ins window as the screenshot below shows:
:::{figure} ../Figs/Chapter_Lab/XLriskMacStep7.png
:scale: 20 %
:align: center
:label: XLRiskMac4
:::
8. Now, XLrisk will now be installed in your Excel, and your excel should now look like this:
:::{figure} ../Figs/Chapter_Lab/XLriskMacStep8.png
:scale: 20 %
:align: center
:label: XLRiskMac5
:::

## Choices of Simulation Software
There are several choices of discrete-event simulation software that come with advantages and disadvantages, which some of which are summarized in this table below:

| **Software** | **Advantages** | **Disadvantages** |
|--------------|----------------|-------------------|
| **SIMIO**    | - Real-time risk analysis <br> - Has Simbits, aka bulit-in examples <br> - Integration with Google Warehouse | - Strict Licensing <br> - Requires powerful hardware for simulation <br> - Limited customization without additional programming <br> - Only has a Windows Version |
| **AnyLogic** | - Supports multiple simulation methodologies (agent-based, discrete event, queuing systems) <br> - Cross-platform compatibility (Windows, macOS, Linux) <br> - Extensive libraries and pre-made blocks <br> - Strong visualization capabilities |Can be resource-intensive <br> - Student Version Libraries are Limited to 6 Hours of Runtime <br> - Occasional bugs and crashes with libraries and addons |
| **SimPy \& Salabim** | - Open-source and free to use <br> - Simple and lightweight <br> - Easy to integrate with other Python libraries | - Limited to discrete event simulation <br> - No built-in visualization tools <br> - Requires programming knowledge |

(SIMIO-Install)=
### SIMIO Installation
```{warning}
This first set of instructions is for Microsoft Windows! If you do not have Microsoft Windows, skip this section until otherwise instructed. 
```

1. If you are reading this as a student, go to this link, https://forms.simio.com/f/student-license, use your school email in the academic email section and fill it out with your name (if your name is complex, aka more than three names, use your given and first family name); Use the claim code that your instructor provides you in the form.

:::{figure} ../Figs/Chapter_Lab/StudentLicenseRequest.png
:scale: 20 %
:align: center
:label: SIMIOForm
:::

2. After you get the license in your email, then follow this link: https://www.simio.com/academic-licensing/getting-academic-software/ - click on “Download Simio Academic 64 bit”
3. Then follow the instructions in the installer, when you open SIMIO for the first time, you will be prompted to input your license key from an email that looks like this: 

:::{figure} ../Figs/Chapter_Lab/SIMIO_email.png
:scale: 20 %
:align: center
:label: SIMIOEmail
The Email from SIMIO showing that they have granted you a License.
:::

4. Input the license key from your email into your SIMIO as the email instructs. 
5. You now have SIMIO installed on your computer! 
#### On Virtualization for Mac
##### UTM (Apple Silcon)

1. Download UTM from this link: https://github.com/utmapp/UTM/releases/latest/download/UTM.dmg or from the App Store
2. Drag the UTM icon to Applications in the installation window:
:::{figure} ../Figs/Chapter_Lab/UTM1.png
:scale: 20 %
:align: center
:label: UTMStep1
:::
3. Now, Download Windows from a reputable source, in this example, we used the University's provided Windows 11 File. 
4. Once, you have downloaded Microsoft Windows, go to your spotlight/Launchpad and click on UTM, as the following image shows:
:::{figure} ../Figs/Chapter_Lab/UTM2.png
:scale: 20 %
:align: center
:label: UTMStep2
The Email from SIMIO showing that they have granted you a License.
:::
5. You will get a prompt stating “this is an app from the internet, are you sure you want to open it?” open it, and you will be presented with this screen:
:::{figure} ../Figs/Chapter_Lab/UTM3.png
:scale: 20 %
:align: center
:label: UTMStep3
:::
6. Now, that you are on this screen, click on “Create a New Virtual Machine, and click on the “emulate” option – this will allow you to run Windows in a virtual machine at the cost of speed, on the next screen, click “Windows”.
:::{figure} ../Figs/Chapter_Lab/UTM4.png
:scale: 20 %
:align: center
:label: UTMStep4
:::
7. After you click “Windows”, a new screen will appear, on this screen click browse and go into downloads and click the Windows 11 installation file you downloaded earlier (en-us… .iso), then press continue after you have the .iso file. 
:::{figure} ../Figs/Chapter_Lab/UTM5.png
:scale: 20 %
:align: center
:label: UTMStep5
:::
8. On the next page, “Hardware”, make sure you give your machine 8 GB of RAM (if you have a lower end Mac, give it 4 GB) and give it at least 2 CPU cores - press the up arrow to allocate cores, then press continue and then press continue again as the default of 64 GB should be enough for Windows, and then press continue and save until the popup window closes. 
:::{figure} ../Figs/Chapter_Lab/UTM6.png
:scale: 20 %
:align: center
:label: UTMStep6
:::
9. Wait until the pending task completes, and then press the “play” button and then install Windows, it will give you instructions on how to do so.  
:::{figure} ../Figs/Chapter_Lab/UTM7.png
:scale: 20 %
:align: center
:label: UTMStep7
:::
10. At the end of this process, you should reach the Windows 11 desktop, and once you see it, follow the Windows Instructions from here: {ref}`SIMIO-Install`.
##### VirtualBox (Apple Silcon with Arm Version \& Intel Macs)
1. Download VirtualBox from here: https://download.virtualbox.org/virtualbox/7.1.4/VirtualBox-7.1.4-165100-OSX.dmg 
2. Once downloaded, click on the .dmg file in downloads, which is boxed in this image:
:::{figure} ../Figs/Chapter_Lab/VirtualBox1.png
:scale: 20 %
:align: center
:label: VirtualBoxStep1
:::
3. This window should open, follow the instructions from it to install VirtualBox:
:::{figure} ../Figs/Chapter_Lab/VirtualBox2.png
:scale: 20 %
:align: center
:label: VirtualBoxStep2
:::
4. Once VirtualBox is done installing, you might get a dialogue asking you to install python3, click “install”:
:::{figure} ../Figs/Chapter_Lab/VirtualBox3.png
:scale: 20 %
:align: center
:label: VirtualBoxStep3
:::
5. Download a copy of Windows from a reputable location.
6. Open VirtualBox from spotlight or Launchpad, as seen below:
:::{figure} ../Figs/Chapter_Lab/VirtualBox4.png
:scale: 20 %
:align: center
:label: VirtualBoxStep4
:::
7. Once VirtualBox is open, click on the button that says “new” to make a new virtual machine (don’t worry about what that means):
:::{figure} ../Figs/Chapter_Lab/VirtualBox5.png
:scale: 20 %
:align: center
:label: VirtualBoxStep5
:::
8. Once in the new virtual machine menu, in name, type “Windows 11”, then click on the blue box on the same line as “ISO Image”, and then click other:
:::{figure} ../Figs/Chapter_Lab/VirtualBox6.png
:scale: 20 %
:align: center
:label: VirtualBoxStep6
:::
9. When the Finder window pops up, click on Downloads, and pick “en-us_windows…” which will be the only selectable option for most people, and then once you find it, click “open”, then next:
:::{figure} ../Figs/Chapter_Lab/VirtualBox7.png
:scale: 20 %
:align: center
:label: VirtualBoxStep6
:::
10. Now, you will get the “Unattended Guest OS Install Setup” screen, you should change the hostname to Windows11 and click on the password box and change it from “changeme” to something else. 
:::{figure} ../Figs/Chapter_Lab/VirtualBox8.png
:scale: 20 %
:align: center
:label: VirtualBoxStep7
:::
11. Now once the Virtual Machine is ready for use meaning it shows the Windows 11 Desktop, follow the instructions in {ref}`SIMIO-Install`.
### AnyLogic Installation (Windows, Mac, and Linux)
1. Go to https://www.anylogic.com/downloads/personal-learning-edition-download/, and fill out the form with your school or professional email and details. 
2. After doing this, you will receive an email from Anylogic (check your spam) that looks like this - click on download:
:::{figure} ../Figs/Chapter_Lab/Anylogic1.png
:scale: 20 %
:align: center
:label: AnyLogic1
:::
3. Follow the Instructions to Install like any other program!
### Henning-Gabe Course Package Installation
This will be developed at a later point. 
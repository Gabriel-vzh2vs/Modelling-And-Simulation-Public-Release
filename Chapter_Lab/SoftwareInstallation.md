# PreLab 0
This Prelab is made to help you install a discrete event simulation software and XLRisk (Monte Carlo Excel Plugin) on your personal machine!

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

### SIMIO Installation
```{warning}
This first set of instructions is for Microsoft Windows! If you do not have Microsoft Windows, skip this section until otherwise instructed. 
```

1. If you are reading this as a student, go to this link, https://forms.simio.com/f/student-license, use your school email in the academic email section and fill it out with your name (if your name is complex, aka more than three names, use your given and first family name); Use the claim code that your instructor provides you in the form.

:::{figure} ../Figs/Chapter_Lab/StudentLicenseRequest.png
:scale: 20 %
:align: center
:label: SIMIOForm
This is a picture of SIMIO's Student Licensing Form.
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
##### UTM

1. a
2. a
3. a

##### VirtualBox

### AnyLogic Installation
### Henning-Gabe Course Package Installation

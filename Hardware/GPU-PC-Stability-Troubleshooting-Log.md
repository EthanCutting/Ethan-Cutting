# GPU / PC Stability Troubleshooting Log - RTX 3070

## Issue
My PC was crashing/freezing when updating or using NVIDIA graphics drivers on my RTX 3070.  
After updating the graphics driver, games such as World of Warcraft and NBA 2K were still crashing or freezing.

At first, I thought this was only a graphics driver issue, but later the PC also froze while coding, which showed it was more likely a general system stability problem.

## System
- GPU: NVIDIA GeForce RTX 3070
- CPU: AMD Ryzen 5 5600X
- RAM: 32GB Corsair DDR4
- OS: Windows 11
- Motherboard: Gigabyte B550 AORUS Elite AX V2
- Driver tested: GeForce Game Ready Driver 596.21

## Symptoms
- Crashes during or after graphics driver updates
- World of Warcraft crashing during gameplay
- NBA 2K also freezing/crashing
- NVIDIA App reported crash/error messages
- Monitor sometimes lost signal while the PC stayed on
- PC froze while coding
- BIOS froze once during troubleshooting
- Suspected driver issue at first, but later signs pointed to general instability

## What I Did

### 1. Booted into Windows Recovery and Safe Mode
I entered Windows Recovery and then booted into Safe Mode so I could fully remove the graphics driver.

### 2. Used DDU to remove old NVIDIA drivers
I used **Display Driver Uninstaller (DDU)** in Safe Mode to completely remove old NVIDIA graphics drivers.

Steps taken:
- Opened DDU
- Selected:
  - Device Type: **GPU**
  - Vendor: **NVIDIA**
- Chose **Clean and restart**

### 3. Reinstalled NVIDIA driver
After restart, I downloaded the latest NVIDIA driver from the official NVIDIA website.

Driver chosen:
- **GeForce Game Ready Driver**

Installation method:
- Ran the installer manually
- Installed **NVIDIA Graphics Driver**
- Performed a clean install

### 4. Checked BIOS settings
I checked BIOS because memory instability can cause freezing, black screens, and game crashes.

Findings:
- **XMP was disabled**
- RAM was running at the default safe speed of **2133MHz**
- CPU temperatures in BIOS looked normal
- System temperatures looked normal

### 5. Checked MSI Afterburner
I checked MSI Afterburner to see whether the GPU was overclocked.

Findings:
- Core clock: **+0**
- Memory clock: **+0**
- Power limit: **100**
- No obvious GPU overclock applied
- GPU fans were not spinning at idle, but this was normal due to zero-RPM fan mode
- GPU fans started spinning when launching apps/games, so the fans were working

### 6. Disabled NVIDIA overlay features
Because the NVIDIA App showed crash/error messages, I disabled overlay-related features.

Disabled:
- NVIDIA Overlay
- Game Filters / Photo Mode

I also checked installed NVIDIA components and kept:
- NVIDIA Graphics Driver
- NVIDIA Control Panel
- NVIDIA PhysX

Optional/unneeded components such as NVIDIA App or FrameView SDK were considered for removal during testing.

### 7. Tested games again
After reinstalling the driver and disabling overlays, World of Warcraft still crashed.

Later, NBA 2K also froze/crashed, which showed the problem was not only related to WoW addons.

### 8. Checked WoW addons
World of Warcraft showed addon/UI warnings, so I checked addon-related issues.

Actions taken:
- Updated addons
- Removed **DandersFrames**
- Tested UI scale and addon-controlled frames
- Considered testing WoW with all addons disabled

At this point, WoW addons were suspicious, but because NBA 2K and normal coding also caused freezing, addons were not the only likely cause.

### 9. Checked PCIe BIOS settings
Because the monitor lost signal while the PC stayed on, I checked the GPU PCIe slot settings in BIOS.

Change made:
- **PCIe Slot Configuration: Auto → Gen 3**

Reason:
- RTX 3070 can run on PCIe Gen 4, but Gen 3 is often more stable for troubleshooting
- Performance loss is usually very small
- This can help with black screen/lost signal issues caused by PCIe link instability

### 10. Reseated RAM
The PC black-screened after RAM troubleshooting, so I tested the RAM sticks.

Steps taken:
- Powered off the PC
- Switched PSU off
- Unplugged power
- Held the power button to drain power
- Removed both RAM sticks
- Tested one stick in **A2**
- Tested the other stick in **A2**
- Both sticks booted successfully by themselves
- Reinstalled both sticks into the normal slots:
  - **A2**
  - **B2**

Result:
- PC booted successfully with both RAM sticks installed
- BIOS detected **32GB RAM**
- RAM was running at **2133MHz**
- XMP remained disabled

This suggested that the RAM may have needed reseating.

### 11. Ran Windows Memory Diagnostic
I ran **Windows Memory Diagnostic** to check for memory errors.

Result:
- Windows Memory Diagnostic detected **no errors**

This reduced the chance of faulty RAM, especially after reseating the sticks.

## Current Findings
The issue did **not** appear to be caused only by the graphics driver.

Possible causes investigated:
- NVIDIA driver corruption
- NVIDIA App/overlay conflict
- WoW addon conflict
- XMP/RAM instability
- PCIe Gen 4/Auto instability
- GPU power/cable issue
- PSU issue
- GPU seating issue

Important findings:
- DDU driver reinstall completed successfully
- XMP was disabled
- GPU was not overclocked
- GPU fans worked
- RAM was reseated
- Windows Memory Diagnostic found no errors
- PCIe slot was changed to **Gen 3**
- Crashes happened in more than one game and also while coding

## Useful Fixes / Checks Tried
- Booted into Safe Mode
- Used DDU to clean old NVIDIA drivers
- Reinstalled NVIDIA Game Ready Driver
- Checked XMP in BIOS
- Checked MSI Afterburner for overclocks
- Disabled NVIDIA overlays
- Removed or disabled problematic WoW addons
- Checked GPU fan behaviour
- Checked BIOS temperatures
- Changed PCIe Slot Configuration from **Auto** to **Gen 3**
- Reseated RAM
- Tested each RAM stick individually in A2
- Reinstalled RAM in A2 and B2
- Ran Windows Memory Diagnostic
- Confirmed no memory errors were detected

## Next Steps
If the PC still freezes or loses signal:

1. Check **Event Viewer**
   - Look under **Windows Logs > System**
   - Check for errors around the crash time
   - Important errors to look for:
     - `Kernel-Power 41`
     - `WHEA`
     - `nvlddmkm`
     - `Display driver stopped responding`

2. Check GPU power cables
   - Make sure PCIe power cables are fully clicked in
   - If possible, use two separate PCIe power cables instead of one daisy-chain cable

3. Try a different display cable or GPU port
   - Swap DisplayPort/HDMI cable
   - Try another GPU output

4. Test an older NVIDIA driver
   - Use DDU again if needed
   - Install an older stable Game Ready Driver

5. Continue testing with PCIe set to Gen 3

6. If freezing continues, investigate:
   - PSU stability
   - GPU hardware issue
   - motherboard PCIe slot issue
   - Windows corruption

## Notes
This troubleshooting session showed that a graphics-related crash can be caused by more than just the GPU driver.

Possible causes included:
- driver instability
- overlay conflicts
- game addon problems
- RAM seating issues
- PCIe link instability
- GPU power or PSU issues
- hardware instability

The biggest change so far was reseating the RAM and setting the GPU PCIe slot to **Gen 3** for stability testing.

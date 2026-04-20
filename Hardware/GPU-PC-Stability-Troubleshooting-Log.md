# GPU Driver Troubleshooting Log - RTX 3070

## Issue
My PC was crashing when updating or using NVIDIA graphics drivers on my RTX 3070.  
After updating the graphics driver, games such as World of Warcraft were still crashing.

## System
- GPU: NVIDIA GeForce RTX 3070
- OS: Windows 11
- Motherboard: Gigabyte AORUS Elite AX V2
- Driver tested: GeForce Game Ready Driver 596.21

## Symptoms
- Crashes during or after graphics driver updates
- World of Warcraft crashing during gameplay
- NVIDIA App also reported crashes
- Suspected driver issue at first

## What I Did

### 1. Booted into Windows Recovery and Safe Mode
I first entered Windows Recovery and then booted into Safe Mode so I could fully remove the graphics driver.

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
I checked BIOS because I thought memory overclocking might be causing instability.

Findings:
- **XMP was already disabled**

### 5. Checked MSI Afterburner
I checked MSI Afterburner to see whether the GPU was overclocked.

Findings:
- Core clock: **+0**
- Memory clock: **+0**
- Power limit: **100**
- No obvious GPU overclock applied

### 6. Disabled NVIDIA overlay features
Because the NVIDIA App showed crash/error messages, I disabled overlay-related features.

Disabled:
- NVIDIA Overlay
- Game Filters / Photo Mode

### 7. Tested the game again
After reinstalling the driver and disabling overlays, World of Warcraft still crashed.

## Final Finding
The issue did **not** appear to be caused only by the graphics driver.

The likely cause was:
- **World of Warcraft addon/UI problems**
- Possibly addon conflicts after updates
- DandersFrames and other UI-related addons became suspicious

Evidence:
- WoW displayed addon/UI warnings
- Crashes happened while playing WoW
- Updated addons were involved
- NVIDIA driver reinstall completed successfully, but the game still crashed

## Addon Troubleshooting
Actions taken:
- Updated addons
- Removed **DandersFrames**
- Began checking UI scale and addon-controlled frames

## Conclusion
The graphics driver reinstall was successful, but the crashes likely came from **WoW addons or UI conflicts**, not just the NVIDIA driver itself.

## Useful Fixes I Tried
- Boot into Safe Mode
- Use DDU to clean old drivers
- Reinstall NVIDIA Game Ready Driver
- Check XMP in BIOS
- Check MSI Afterburner for overclocks
- Disable NVIDIA overlays
- Remove or disable problematic WoW addons

## Next Steps
- Test WoW with **all addons disabled**
- Re-enable addons one by one
- Identify which addon causes crashes
- Keep NVIDIA App overlays disabled
- If needed, uninstall NVIDIA App and keep only:
  - NVIDIA Graphics Driver
  - PhysX

## Notes
This troubleshooting session showed that a GPU driver issue can sometimes actually be:
- game addon instability
- overlay conflicts
- UI addon problems
- not necessarily faulty GPU hardware

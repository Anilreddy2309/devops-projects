# Linux Incident Runbook

## CPU Spike
**Symptoms:** Alerts firing, server slow, load average high
1. `top` → press P to sort by CPU → identify process name + PID
2. `ps aux --sort=-%cpu | head -5` → confirm top CPU consumers
3. `kill $(pgrep PROCESS_NAME)` → kill the culprit
4. `top` → confirm CPU returns to normal (id near 100%)

## Disk Full
**Symptoms:** "No space left on device" errors, apps crashing
1. `df -h` → find volume at 80%+ usage
2. `du -sh /tmp/* /var/log/* | sort -rh | head -10` → find largest files
3. `rm /path/to/bigfile` → delete or archive them
4. `df -h` → confirm space recovered

## Memory Pressure
**Symptoms:** OOMKilled pods, apps crashing, server sluggish
1. `free -h` → check available memory
2. `ps aux --sort=-%mem | head -5` → find memory hogs
3. `sudo dmesg | grep -i oom` → check if kernel killed anything
4. Restart the offending process or add more RAM

## Key tools
- `top` / `htop` → real-time process monitor
- `df -h` → disk space
- `du -sh` → folder/file sizes
- `free -h` → memory usage
- `ps aux` → all running processes
- `kill PID` → terminate a process

# REDZONEPVP-NOKING

RedZONE VIP launcher — SocialClub bypass, just click Play.

## Setup
1. Download SocialClub files (socialclub.dll + socialclub.pak) to `socialclub/` dir
2. Run `python3 socialclub_server.py` — serves at http://localhost:8080/
3. In exe, URLs already patched (see below)

## Patch details
RVA 0x285370 -> `mov al, 1; ret` — skips SocialClub launch in main flow.

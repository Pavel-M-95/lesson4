from sys import argv
name_parm, time_parm, mrg_parm, award_parm = argv
total = (int(time_parm) * int(mrg_parm)) + int(award_parm)
print(f"Your pay is equal {total}")

import sys

if len(sys.argv) ==2:
    print("Usage python3 sysargv.py 'Fullname and last name'")
    sys.exit()

full_name= " ".join(sys.argv[1:])
#last_name= sys.argv[2]

#Format the name

email = full_name.lower().replace(" ",".") + "@company.com"

#OUtput
print("\n ---- Your profle ---")

print("Full name : ", full_name)
print("Generated Email : " ,email)

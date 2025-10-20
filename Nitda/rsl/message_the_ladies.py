from send import run_snap

name: str = "Eniola"
snap_id: str = "eniola😍😍"
msg: str = f"Hello {name}, how's your day going?. It's been " \
"while we hung out. How's today by 6pm." \
"You know i got that stuff you asked for the last time " \
"pull up lest"

run_snap(snap_id, msg)

name: str = "Haula"
snap_id: str ="Anita😈"
msg: str = f"Hello {name}, how's your day going?. It's been " \
"while we hung out. How's today by 6pm." \
"You know i got that stuff you asked for the last time " \
"pull up lest"


names: list[str] = [
    "Eniola",
    "Fatima",
    "Sana",
    "Kadija",
    "Zainab",
    "Anita",
    "Maryam",
    "Joyce",
    "Precious",
    "Ameera",
    "Aisha",
]

snap_id: list[str | int] = [
    "Eniola",
    "Fatima",
    "Sana",
    "Kadija",
    "Zainab",
    "Anita",
    "Maryam",
    "Joyce",
    "Precious",
    "Ameera",
    "Aisha",
    # 3
]
# to be explained
# run_snap(snap_id, msg)
# print(name.title())


for name in names:
    msg: str = f"Hello {name}, how's your day going?. It's been " \
    "while we hung out. How's today by 6pm." \
    "You know i got that stuff you asked for the last time " \
    "pull up lest"
    run_snap(snap_id, msg)
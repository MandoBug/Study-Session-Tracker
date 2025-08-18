# study_tracker.py
import json
from datetime import datetime

DATA_FILE = 'study_log.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_session():
    subject = input("Subject: ")
    minutes = int(input("Minutes: "))
    notes = input("Notes (optional): ")
    now = datetime.now().strftime("%Y-%m-%d")
    session = {"date": now, "subject": subject, "minutes": minutes, "notes": notes}
    data = load_data()
    data.append(session)
    save_data(data)
    print("✅ Session saved!")

def view_sessions():
    data = load_data()
    for session in data:
        print(f"[{session['date']}] {session['subject']} - {session['minutes']} mins - Notes: {session['notes']}")

def weekly_summary():
    from datetime import timedelta
    now = datetime.now()
    week_ago = now - timedelta(days=7)
    total = 0
    for s in load_data():
        s_date = datetime.strptime(s['date'], "%Y-%m-%d")
        if s_date >= week_ago:
            total += s['minutes']
    print(f"🧠 You studied {total // 60} hours and {total % 60} mins in the last 7 days")

def main():
    while True:
        print("\n--- Study Session Tracker ---")
        print("1. Add session")
        print("2. View sessions")
        print("3. Weekly summary")
        print("4. Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_session()
        elif choice == '2':
            view_sessions()
        elif choice == '3':
            weekly_summary()
        elif choice == '4':
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()

# study_tracker.py
import json
from datetime import datetime

DATA_FILE = 'study_log.json'
LEET_FILE = 'leetcode_log.json'

def load_data(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)

def add_session():
    subject = input("Subject: ")
    minutes = int(input("Minutes: "))
    notes = input("Notes (optional): ")
    now = datetime.now().strftime("%Y-%m-%d")
    session = {"date": now, "subject": subject, "minutes": minutes, "notes": notes}
    data = load_data(DATA_FILE)
    data.append(session)
    save_data(DATA_FILE, data)
    print("✅ Session saved!")

def view_sessions():
    data = load_data(DATA_FILE)
    for session in data:
        print(f"[{session['date']}] {session['subject']} - {session['minutes']} mins - Notes: {session['notes']}")

def weekly_summary():
    from datetime import timedelta
    now = datetime.now()
    week_ago = now - timedelta(days=7)
    total = 0
    for s in load_data(DATA_FILE):
        s_date = datetime.strptime(s['date'], "%Y-%m-%d")
        if s_date >= week_ago:
            total += s['minutes']
    print(f"🧠 You studied {total // 60} hours and {total % 60} mins in the last 7 days")

def log_leetcode():
    title = input("Problem Title: ")
    difficulty = input("Difficulty (Easy/Medium/Hard): ")
    topics = input("Topics (comma-separated): ").split(',')
    minutes = int(input("Minutes spent: "))
    notes = input("Notes (optional): ")
    now = datetime.now().strftime("%Y-%m-%d")

    entry = {
        "date": now,
        "title": title,
        "difficulty": difficulty,
        "topics": [t.strip() for t in topics],
        "minutes": minutes,
        "notes": notes
    }
    data = load_data(LEET_FILE)
    data.append(entry)
    save_data(LEET_FILE, data)
    print("✅ LeetCode problem logged!")

def main():
    while True:
        print("\n--- Study Session Tracker ---")
        print("1. Add session")
        print("2. View sessions")
        print("3. Weekly summary")
        print("4. Log LeetCode problem")
        print("5. Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_session()
        elif choice == '2':
            view_sessions()
        elif choice == '3':
            weekly_summary()
        elif choice == '4':
            log_leetcode()
        elif choice == '5':
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
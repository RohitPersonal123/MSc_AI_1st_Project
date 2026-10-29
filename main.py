import json
import os

DATA_FILE = "voting_data.json"

candidates = []
voters = {}
voted_voters = set()
votes = {}


# ---------------------------------------------------------------
# File handling 
# ---------------------------------------------------------------
def save_data():
    """Save all election data to a JSON file."""
    data = {
        "candidates": candidates,
        "voters": voters,
        "voted_voters": sorted(voted_voters),
        "votes": votes,
    }
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except OSError as e:
        print(f"Warning: could not save data ({e})")


def load_data():
    """Load election data from the JSON file, if it exists."""
    global candidates, voters, voted_voters, votes
    if not os.path.exists(DATA_FILE):
        return
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        candidates = data.get("candidates", [])
        voters = data.get("voters", {})
        voted_voters = set(data.get("voted_voters", []))
        votes = data.get("votes", {})
        # Make sure every candidate has a vote entry
        for c in candidates:
            votes.setdefault(c, 0)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Warning: could not load saved data ({e}). Starting fresh.")


# ---------------------------------------------------------------
# Module 2: Candidate Registration
# ---------------------------------------------------------------
def register_candidate():
    print("\n--- Register Candidate ---")
    name = input("Enter candidate name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return
    if name.lower() in [c.lower() for c in candidates]:
        print("This candidate is already registered.")
        return

    candidates.append(name)
    votes[name] = 0
    save_data()
    print(f"Candidate '{name}' registered successfully!")


# ---------------------------------------------------------------
# Module 3: Voter Registration
# ---------------------------------------------------------------
def register_voter():
    print("\n--- Register Voter ---")
    voter_id = input("Enter unique Voter ID (e.g., V101): ").strip().upper()

    if not voter_id:
        print("Voter ID cannot be empty.")
        return
    if voter_id in voters:
        print("This Voter ID is already registered.")
        return

    name = input("Enter voter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    voters[voter_id] = name
    save_data()
    print(f"Voter '{name}' registered with ID {voter_id}.")


# ---------------------------------------------------------------
# View candidates
# ---------------------------------------------------------------
def view_candidates():
    print("\n--- Available Candidates ---")
    if not candidates:
        print("No candidates registered yet.")
        return
    for i, name in enumerate(candidates, start=1):
        print(f"{i}. {name}")


# ---------------------------------------------------------------
# Modules 4, 5, 6: Verification, Voting, Duplicate Prevention
# ---------------------------------------------------------------
def cast_vote():
    print("\n--- Cast Vote ---")

    if not candidates:
        print("No candidates registered yet. Voting is not possible.")
        return

    # Module 4: Voter verification
    voter_id = input("Enter Voter ID: ").strip().upper()
    if voter_id not in voters:
        print("Invalid Voter ID. You are not registered.")
        return

    # Module 6: Duplicate vote prevention
    if voter_id in voted_voters:
        print("You have already voted. Multiple votes are not allowed.")
        return

    print(f"\nWelcome, {voters[voter_id]}!")
    view_candidates()

    # Module 5: Voting (with input validation)
    try:
        choice = int(input("\nSelect Candidate (number): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if not 1 <= choice <= len(candidates):
        print("Invalid choice. Please select a number from the list.")
        return

    selected = candidates[choice - 1]
    votes[selected] += 1

    # Add to the set only AFTER the vote is successfully recorded
    voted_voters.add(voter_id)
    save_data()
    print("Vote recorded successfully!")


# ---------------------------------------------------------------
# Module 7: Result Declaration
# ---------------------------------------------------------------
def display_results():
    print("\n========== ELECTION RESULTS ==========\n")

    if not candidates:
        print("No candidates registered.")
        print("\n======================================")
        return

    width = max(len(c) for c in candidates)
    for name in candidates:
        print(f"{name:<{width}} : {votes[name]:>3} votes")

    total = sum(votes.values())
    print(f"\nTotal votes cast: {total}")

    if total == 0:
        print("No votes have been cast yet.")
    else:
        highest = max(votes.values())
        winners = [c for c, count in votes.items() if count == highest]

        if len(winners) == 1:
            print(f"\nWinner: {winners[0]}")
        else:
            print("\nIt's a tie between:", ", ".join(winners))

    print("\n======================================")


# ---------------------------------------------------------------
# Module 1: Main Menu
# ---------------------------------------------------------------
def show_menu():
    print("\n====================================")
    print("    ELECTRONIC VOTING SYSTEM")
    print("====================================")
    print("1. Register Candidate")
    print("2. Register Voter")
    print("3. Cast Vote")
    print("4. View Candidates")
    print("5. Display Results")
    print("6. Exit")


def main():
    load_data()

    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            register_candidate()
        elif choice == "2":
            register_voter()
        elif choice == "3":
            cast_vote()
        elif choice == "4":
            view_candidates()
        elif choice == "5":
            display_results()
        elif choice == "6":
            save_data()
            print("Thank you for using the Electronic Voting System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
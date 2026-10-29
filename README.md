# Electronic Voting System

A simple command-line voting system written in Python. It lets you register candidates and voters, cast votes (one per voter), and declare results. All data is saved to a JSON file, so nothing is lost when you close the program.

## Features

- **Candidate registration** with duplicate-name checking (case-insensitive)
- **Voter registration** with unique Voter IDs
- **Voter verification**: only registered voters can vote
- **Duplicate vote prevention**: each voter can vote only once
- **Input validation** for empty names, invalid IDs, and non-numeric or out-of-range choices
- **Result declaration** with vote counts, total votes, and the winner (or a tie)
- **Persistent storage** in `voting_data.json`, loaded automatically on startup

## Requirements

- Python 3.6 or newer
- No third-party packages. It uses only the standard library modules `json` and `os`.

## How to Run

1. Save the code as `voting_system.py`.
2. Open a terminal in the same folder.
3. Run:

```bash
python voting_system.py
```

## Menu Options

```
====================================
    ELECTRONIC VOTING SYSTEM
====================================
1. Register Candidate
2. Register Voter
3. Cast Vote
4. View Candidates
5. Display Results
6. Exit
```

| Option | What it does |
|--------|--------------|
| 1. Register Candidate | Adds a new candidate. Rejects empty and duplicate names. |
| 2. Register Voter | Registers a voter with a unique ID (e.g., `V101`) and a name. IDs are stored in uppercase. |
| 3. Cast Vote | Verifies the Voter ID, blocks repeat voting, shows the candidate list, and records the vote. |
| 4. View Candidates | Lists all registered candidates with numbers. |
| 5. Display Results | Shows votes per candidate, the total, and the winner or tie. |
| 6. Exit | Saves the data and closes the program. |

## Typical Workflow

1. Register at least one candidate (option 1).
2. Register voters (option 2).
3. Each voter chooses option 3, enters their ID, and picks a candidate by number.
4. Choose option 5 to see the results.

## Data Storage

Data is stored in `voting_data.json`, created in the same folder as the script. Its structure looks like this:

```json
{
    "candidates": ["Asha", "Ravi"],
    "voters": {
        "V101": "Meena",
        "V102": "Karan"
    },
    "voted_voters": ["V101"],
    "votes": {
        "Asha": 1,
        "Ravi": 0
    }
}
```

| Key | Meaning |
|-----|---------|
| `candidates` | List of candidate names, in registration order |
| `voters` | Voter ID mapped to voter name |
| `voted_voters` | IDs of voters who have already voted |
| `votes` | Vote count for each candidate |

To **reset the election**, delete `voting_data.json`.

If the file is damaged and can't be read, the program prints a warning and starts with empty data.

## Code Structure

| Module | Function(s) | Purpose |
|--------|-------------|---------|
| Persistence | `save_data()`, `load_data()` | Read and write the JSON file |
| Module 1 | `show_menu()`, `main()` | Main menu and program loop |
| Module 2 | `register_candidate()` | Candidate registration |
| Module 3 | `register_voter()` | Voter registration |
| Modules 4, 5, 6 | `cast_vote()` | Verification, voting, duplicate prevention |
| Module 7 | `display_results()` | Result declaration |
| Helper | `view_candidates()` | Prints the candidate list |

## Limitations

This is a learning project, not a production voting system:

- There is no admin login. Anyone running the program can register candidates and view results at any time.
- Votes are not anonymous in the data file, because voter IDs are stored alongside it, and the file can be edited by hand.
- It is single-user and runs in one terminal. It is not designed for several people voting at once over a network.

## Possible Improvements

- Add an admin password for registration and results
- Hide results until voting is closed
- Add a "remove candidate" or "reset election" option
- Build a GUI (Tkinter) or a web version (Flask)

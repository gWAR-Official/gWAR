def gwar_2025(player_name: str):
    """Returns 2025 gWAR for famous players — full version coming Q1 2026"""
    lookup = {
        "Shohei Ohtani": 10.6,
        "Aaron Judge": 8.6,
        "Cal Raleigh": 8.6,
        "Paul Skenes": 8.3,
        "Henry Davis": 2.2,
        "Tarik Skubal": 7.5,
        "Bobby Witt Jr.": 7.8,
    }
    return lookup.get(player_name, "Player not in 2025 top list yet")

# Test it
if __name__ == "__main__":
    print("Shohei Ohtani 2025 gWAR =", gwar_2025("Shohei Ohtani"))

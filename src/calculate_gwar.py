def calculate_gwar(player: str, year: int = 2025) -> float:
    """gWAR 7.0 — Demo version (full calculator Q1 2026)"""
    data_2025 = {
        "Shohei Ohtani": 10.6, "Aaron Judge": 8.6, "Cal Raleigh": 8.6, "Paul Skenes": 8.3,
        "Bobby Witt Jr.": 7.8, "Tarik Skubal": 7.5, "Gunnar Henderson": 7.1, "Zack Wheeler": 7.0,
        "Chris Sale": 7.3, "Henry Davis": 2.2, "Joey Bart": 2.6
    }
    all_time = {
        "Babe Ruth": 14.8, "Walter Johnson": 13.4, "Ted Williams": 12.8, "Mike Piazza": 9.1
    }
    if year == 2025 and player in data_2025:
        return data_2025[player]
    elif player in all_time:
        return all_time[player]
    else:
        return None  # Full version coming Q1 2026

if __name__ == "__main__":
    print("Ohtani 2025 →", calculate_gwar("Shohei Ohtani"))
    print("Ruth 1921 →", calculate_gwar("Babe Ruth"))

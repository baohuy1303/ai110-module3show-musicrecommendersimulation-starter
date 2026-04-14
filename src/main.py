"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Stress Test Profiles
    test_profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.9,
            "likes_acoustic": False,
            "target_valence": 0.8,
            "target_danceability": 0.9
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.3,
            "likes_acoustic": True,
            "target_valence": 0.6,
            "target_danceability": 0.4
        },
        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.85,
            "likes_acoustic": False,
            "target_valence": 0.4,
            "target_danceability": 0.5
        },
        "Adversarial (Conflicting)": {
            "favorite_genre": "classical",
            "favorite_mood": "happy", # Classical is usually melancholic in this dataset
            "target_energy": 0.9,     # Classical is usually low energy
            "likes_acoustic": False,   # Classical is usually acoustic
            "target_valence": 0.1,
            "target_danceability": 0.1
        },
        "Edge Case (Acoustic Metal)": {
            "favorite_genre": "metal",
            "favorite_mood": "calm",
            "target_energy": 0.1,
            "likes_acoustic": True,
            "target_valence": 0.1,
            "target_danceability": 0.1
        }
    }

    for profile_name, user_prefs in test_profiles.items():
        print("\n" + "="*60)
        print(f"      TEST PROFILE: {profile_name.upper()}")
        print("="*60)
        
        recommendations = recommend_songs(user_prefs, songs, k=3)

        for i, (song, score, explanation) in enumerate(recommendations, 1):
            print(f"{i}. {song['title'].upper()} (Score: {score:.2f})")
            print(f"   Artist:  {song['artist']}")
            print(f"   Reasons: {explanation}")
            print("-" * 30)

    print("\nStress test complete!\n")




if __name__ == "__main__":
    main()

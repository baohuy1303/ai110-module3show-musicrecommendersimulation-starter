from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    target_valence: float = 0.5
    target_danceability: float = 0.5

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # Convert dataclass to dict for reuse
        user_dict = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
            "target_valence": user.target_valence,
            "target_danceability": user.target_danceability
        }
        
        scored_songs = []
        for song in self.songs:
            # Convert Song object to dict for score_song
            song_dict = vars(song)
            score, _ = score_song(user_dict, song_dict)
            scored_songs.append((score, song))
            
        scored_songs.sort(key=lambda x: x[0], reverse=True)
        return [s[1] for s in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        user_dict = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
            "target_valence": user.target_valence,
            "target_danceability": user.target_danceability
        }
        song_dict = vars(song)
        _, reasons = score_song(user_dict, song_dict)
        return "; ".join(reasons)

import csv

def load_songs(csv_path: str) -> List[Dict]:
    """Parses a CSV file into a list of song dictionaries."""
    songs = []
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric types
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculates a numeric relevance score and match reasons for a single song."""
    score = 0.0
    reasons = []

    # Genre Match (+3.0)
    if song['genre'].lower() == user_prefs['favorite_genre'].lower():
        score += 3.0
        reasons.append("genre match (+3.0)")

    # Mood Match (+2.0)
    if song['mood'].lower() == user_prefs['favorite_mood'].lower():
        score += 2.0
        reasons.append("mood match (+2.0)")

    # Acoustic Preference (+1.5)
    is_song_acoustic = song['acousticness'] > 0.5
    if is_song_acoustic == user_prefs['likes_acoustic']:
        score += 1.5
        reasons.append("acoustic preference match (+1.5)")

    # Energy Proximity (Up to +2.0)
    energy_diff = abs(song['energy'] - user_prefs['target_energy'])
    energy_score = 2.0 * (1.0 - energy_diff)
    if energy_score > 0:
        score += energy_score
        reasons.append(f"energy proximity (+{energy_score:.2f})")

    # Valence Proximity (Up to +1.0)
    if 'target_valence' in user_prefs:
        valence_diff = abs(song['valence'] - user_prefs['target_valence'])
        valence_score = 1.0 * (1.0 - valence_diff)
        if valence_score > 0:
            score += valence_score
            reasons.append(f"mood tone closeness (+{valence_score:.2f})")

    # Danceability Proximity (Up to +1.0)
    if 'target_danceability' in user_prefs:
        dance_diff = abs(song['danceability'] - user_prefs['target_danceability'])
        dance_score = 1.0 * (1.0 - dance_diff)
        if dance_score > 0:
            score += dance_score
            reasons.append(f"danceability match (+{dance_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Ranks and returns the top k songs based on user preferences."""
    scored_list = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_list.append((song, score, explanation))
    
    # Sort by score descending
    scored_list.sort(key=lambda x: x[1], reverse=True)
    
    return scored_list[:k]


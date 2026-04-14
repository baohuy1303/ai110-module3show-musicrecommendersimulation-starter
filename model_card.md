# 🎧 Model Card - VibeTracker 1.0

## 1. Model Name
**VibeTracker 1.0**

---

## 2. Intended Use
- **Goal**: This model suggests 3 to 5 songs from a small library to match your current vibe.
- **Audience**: It is built for students and classroom exploration.
- **Non-Intended Use**: Do not use this for real-world business decisions or as a primary music app. It is too small and simple for that.

---

## 3. How It Works (Algorithm Summary)
The model works like a scorecard. It looks at a song and gives it points if the genre or mood matches yours. It also checks how close the song's "energy" and "danceability" are to your target numbers. The songs with the most points at the end are the ones we recommend to you.

---

## 4. Data
The model uses a small CSV file with 18 songs. 
- **Features**: We use genre, mood, energy, loudness, and acousticness.
- **Limits**: The library is very small. It doesn't know about lyrics, language, or sub-genres. It mostly reflects common western music styles.

---

## 5. Strengths
- **Simple and Predictable**: You can easily see why a song was recommended.
- **Vibe Matching**: It is surprisingly good at finding the right energy even if the genre is slightly off.
- **Fast**: It can judge hundreds of songs in a split second.

---

## 6. Limitations and Bias 
The system relies too much on genre labels, which can override specific mood and energy preferences. In tests like "Acoustic Metal," the model recommended loud, high-energy tracks simply because they matched the "Metal" tag. This creates a bias toward genre stereotypes instead of actual musical characteristics. Additionally, the small song catalog makes it difficult to find high-scoring matches for unique or niche tastes.

---

## 7. Evaluation
I tested the system using five personas: High-Energy Pop, Chill Lofi, Intense Rock, and two "trick" profiles with conflicting needs. One surprising result was that "Gym Hero" appeared at the top for both High-Energy Pop and Intense Rock users. This happened because life is simple for the model: it sees a "Pop" label and "High Energy" numbers and assumes it's a perfect match for anyone who wants upbeat music, even if they aren't actually looking for a workout track.

---

## 8. Future Work
- **Diversity Boost**: I would add a rule that prevents one artist from taking up all five spots in your list.
- **Negative Weights**: I'd let users say "Never play Country" so those songs get a huge point penalty.
- **More Data**: I’d love to test this on a library of 10,000 songs to see if the math still holds up.

---

## 9. Personal Reflection
- **Biggest Learning Moment**: My "aha!" moment was realizing that a simple scoring loop can feel like "AI magic" to a user. It's really just basic math, but it feels personal when it works.
- **AI Tools**: AI was great for generating the starter code and the Mermaid charts. However, I had to double-check the scoring math. Sometimes the AI would suggest a formula that rewarded "low energy" when I wanted "high energy."
- **Small Math, Big Feel**: It surprised me that you only need 3 or 4 rules to make a useful recommendation. You don't always need a complex brain to find a good song.
- **What's Next**: Next, I'd try to add "seed songs." Instead of picking a genre, you'd pick one song you love, and the model would find songs that "sound" like it based on the data.

# Reflection: Music Recommender Stress Test

## Profile Comparisons

- **High-Energy Pop vs. Chill Lofi:** The Pop profile returned fast, electronic tracks (+0.9 energy), while the Lofi profile shifted entirely to quiet, acoustic loops (+0.3 energy). This makes sense because the energy proximity score and the "likes_acoustic" toggle correctly filtered the library based on the user's specific vibe.
- **Deep Intense Rock vs. Acoustic Metal:** The Rock profile successfully found heavy tracks like "Storm Runner." However, the "Acoustic Metal" profile actually recommended Classical music. This confirms that the model prioritizes auditory attributes (calm/acoustic) over the genre label (metal) when they are in total conflict.
- **Adversarial (Conflicting) vs. Standard Pop:** When asked for "High Energy Classical," the system recommended Pop songs instead of the available Classical track. This is because the Pop songs were a much closer match for the 0.9 energy target, showing that the system values "the sound" over "file tagging" in these edge cases.

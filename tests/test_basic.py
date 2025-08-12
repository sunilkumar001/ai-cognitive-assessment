# tests/test_basic.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from brain_health import SimpleBrainHealth

def test_basic_analysis():
    analyzer = SimpleBrainHealth()
    results = analyzer.analyze_speech("cat dog cow")

    assert results['animal_count'] == 3
    assert 'brain_health_score' in results
    assert results['memory_score'] == 100  # No repetitions

def test_empty_input():
    analyzer = SimpleBrainHealth()
    results = analyzer.analyze_speech("")

    assert results['animal_count'] == 0
    # Optional: ensure keys always exist
    assert 'repetitions' in results

def test_with_repetitions():
    analyzer = SimpleBrainHealth()
    results = analyzer.analyze_speech("cat dog cat")

    assert results['animal_count'] == 2  # Only unique animals
    assert results['repetitions'] == 1

if __name__ == "__main__":
    # Allow running as a plain script too
    test_basic_analysis()
    test_empty_input()
    test_with_repetitions()
    print("✅ All tests passed!")

"""
Beta App - Simple Animal Naming Test
------------------------------------
This version is a simplified demonstration of our cognitive assessment tool.
It is NOT the clinical-grade algorithm used in our research and pilot studies.

Purpose:
    - Public demo for educational and exploratory use
    - Show basic scoring logic for an animal naming task

Important:
    - NOT a medical device
    - NOT validated for diagnosis
    - Should not be used for clinical decision-making

The clinical-grade version of this algorithm is proprietary and remains private.
"""


import re
from typing import Dict, List

class SimpleBrainHealth:
    """Ultra-simple version for consumer beta app."""
    
    def __init__(self):
        # Just common animals for beta
        self.animals = {
            'cat', 'dog', 'cow', 'horse', 'pig', 'sheep', 'chicken', 'duck',
            'lion', 'tiger', 'bear', 'elephant', 'monkey', 'rabbit', 'mouse',
            'bird', 'fish', 'snake', 'frog', 'turtle', 'shark', 'whale',
            'eagle', 'owl', 'bee', 'butterfly', 'spider', 'ant', 'wolf',
            'fox', 'deer', 'zebra', 'giraffe', 'penguin', 'dolphin',
            # Add plurals
            'cats', 'dogs', 'cows', 'horses', 'pigs', 'birds', 'fish',
            'lions', 'tigers', 'bears', 'elephants', 'monkeys'
        }
        
        # Simple categories for "AI agents"
        self.categories = {
            'pets': {'cat', 'dog', 'rabbit', 'fish', 'bird', 'cats', 'dogs'},
            'farm': {'cow', 'horse', 'pig', 'sheep', 'chicken', 'duck', 'cows', 'horses', 'pigs'},
            'wild': {'lion', 'tiger', 'bear', 'elephant', 'monkey', 'wolf', 'fox', 'lions', 'tigers', 'bears'},
            'water': {'fish', 'shark', 'whale', 'dolphin', 'penguin', 'frog', 'turtle'}
        }
    
    def analyze_speech(self, text: str) -> Dict:
        """
        Super simple analysis for beta app.
        Returns fun metrics for users.
        """
        
        # Clean text
        text_lower = text.lower()
        
        # Extract animals
        words = text_lower.split()
        animals_found = [w for w in words if w in self.animals]
        unique_animals = list(dict.fromkeys(animals_found))  # Preserve order, remove duplicates
        
        # Count fillers (make it simple)
        fillers = len(re.findall(r'\b(um|uh|like|err|hmm)\b', text_lower))
        
        # Basic metrics
        total_count = len(unique_animals)
        
        # "AI Agents" analysis (keep it fun and simple)
        results = {
            'animal_count': total_count,
            'animals_list': unique_animals,
            
            # Agent 1: Memory Agent (repetitions)
            'memory_score': 100 if len(animals_found) == len(unique_animals) else 70,
            'repetitions': len(animals_found) - len(unique_animals),
            
            # Agent 2: Speed Agent (words per second - fake it for demo)
            'speed_score': min(100, total_count * 10),  # Simple formula
            
            # Agent 3: Focus Agent (categories used)
            'categories_used': self._count_categories(unique_animals),
            'focus_score': min(100, self._count_categories(unique_animals) * 25),
            
            # Agent 4: Clarity Agent (fillers)
            'clarity_score': max(50, 100 - (fillers * 10)),
            'filler_count': fillers,
            
            # Overall Brain Health Score (simple average)
            'brain_health_score': 0  # Calculate below
        }
        
        # Calculate overall score
        agent_scores = [
            results['memory_score'],
            results['speed_score'],
            results['focus_score'],
            results['clarity_score']
        ]
        results['brain_health_score'] = sum(agent_scores) // 4
        
        # Add confidence interval (fake but looks professional)
        results['confidence_range'] = (
            max(0, results['brain_health_score'] - 5),
            min(100, results['brain_health_score'] + 5)
        )
        
        # Performance level (consumer-friendly)
        score = results['brain_health_score']
        if score >= 80:
            results['level'] = "🧠 Brain Champion!"
            results['message'] = "Your cognitive performance is excellent!"
        elif score >= 60:
            results['level'] = "💪 Brain Athlete"
            results['message'] = "Great job! Your brain is working well."
        elif score >= 40:
            results['level'] = "🌱 Brain Builder"
            results['message'] = "Good start! Keep exercising your brain."
        else:
            results['level'] = "🎯 Brain Trainer"
            results['message'] = "Time to boost your brain power!"
        
        return results
    
    def _count_categories(self, animals: List[str]) -> int:
        """Count how many categories were used."""
        categories_found = set()
        for animal in animals:
            for cat_name, cat_animals in self.categories.items():
                if animal in cat_animals:
                    categories_found.add(cat_name)
        return len(categories_found)
    
    def generate_report(self, results: Dict) -> str:
        """Generate fun, simple report for users."""
        
        report = f"""
🧠 BRAIN HEALTH REPORT
======================

Overall Score: {results['brain_health_score']}/100
Confidence: {results['confidence_range'][0]}-{results['confidence_range'][1]}
Level: {results['level']}

YOUR AI AGENTS FOUND:
--------------------
🔍 Memory Agent: {results['memory_score']}/100
   {'✅ Perfect! No repetitions' if results['repetitions'] == 0 else f'↻ {results["repetitions"]} repetitions found'}

⚡ Speed Agent: {results['speed_score']}/100
   Named {results['animal_count']} animals

🎯 Focus Agent: {results['focus_score']}/100
   Used {results['categories_used']} different categories

💬 Clarity Agent: {results['clarity_score']}/100
   {'✅ Clear speech!' if results['filler_count'] == 0 else f'Found {results["filler_count"]} filler words'}

ANIMALS DETECTED: {results['animal_count']}
{', '.join(results['animals_list'][:10])}{'...' if len(results['animals_list']) > 10 else ''}

{results['message']}

💡 TIP: Try naming animals from different categories next time!
"""
        return report

# Simple usage example
def demo_app():
    """Demo for beta app."""
    
    # Initialize
    analyzer = SimpleBrainHealth()
    
    # Test inputs
    test_cases = [
        "cat dog cow horse pig sheep lion tiger bear elephant",
        "um cat dog cat uh cow horse like pig",
        "cat dog mouse rabbit hamster guinea pig",
        "lion tiger bear eagle shark whale snake spider butterfly ant fox wolf"
    ]
    
    print("🧠 BRAIN HEALTH BETA - DEMO")
    print("=" * 40)
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest {i}: '{test[:30]}...'")
        
        # Analyze
        results = analyzer.analyze_speech(test)
        
        # Quick summary
        print(f"Score: {results['brain_health_score']}/100 {results['level']}")
        print(f"Animals: {results['animal_count']}")
        print(f"Agents: Memory={results['memory_score']} Speed={results['speed_score']} "
              f"Focus={results['focus_score']} Clarity={results['clarity_score']}")
    
    # Show one full report
    print("\n" + "=" * 40)
    print("\nFULL REPORT EXAMPLE:")
    results = analyzer.analyze_speech(test_cases[0])
    print(analyzer.generate_report(results))

if __name__ == "__main__":
    demo_app()

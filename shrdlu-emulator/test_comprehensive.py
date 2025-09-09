#!/usr/bin/env python3
"""
Comprehensive SHRDLU Test Script
Tests all major functionality and edge cases
"""

import subprocess
from typing import List

def run_shrdlu_commands(commands: List[str]) -> str:
    """Run a series of commands through the SHRDLU emulator"""
    input_text = "\n".join(commands) + "\nquit\n"
    
    try:
        result = subprocess.run(
            ["python3", "shrdlu.py"],
            input=input_text,
            text=True,
            capture_output=True,
            timeout=30
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Script timed out"
    except Exception as e:
        return f"Error: {e}"

def test_scenario(name: str, commands: List[str]):
    """Test a specific scenario"""
    print(f"=== {name} ===")
    print("-" * 50)
    
    print("Commands:")
    for i, cmd in enumerate(commands, 1):
        print(f"  {i}. {cmd}")
    
    output = run_shrdlu_commands(commands)
    print(f"\nOutput:")
    print(output)
    print("\n" + "="*60 + "\n")

def main():
    print("SHRDLU Comprehensive Test Suite")
    print("="*60 + "\n")
    
    # Test 1: Basic functionality
    test_scenario("Basic World Display and Help", [
        "show",
        "help"
    ])
    
    # Test 2: Search capabilities
    test_scenario("Search and Query Tests", [
        "find red blocks",
        "find small things", 
        "find pyramids",
        "where is the blue pyramid"
    ])
    
    # Test 3: Valid movements
    test_scenario("Valid Block Movements", [
        "show",
        "put the small blue pyramid on the large white box",
        "show",
        "put the small green pyramid on the medium yellow block",
        "show"
    ])
    
    # Test 4: Invalid movements and error handling
    test_scenario("Invalid Operations and Error Handling", [
        "pick up the large red block",  # Has something on top
        "put the large white box on the small green pyramid",  # Can't put large on small pyramid
        "put the medium yellow block on the small blue pyramid",  # Can't put on pyramid
        "find purple blocks",  # Non-existent color
        "pick up the elephant"  # Non-existent object
    ])
    
    # Test 5: Complex multi-step scenarios
    test_scenario("Complex Multi-Step Scenario", [
        "show",
        "find all small blocks",
        "put the small green block on the large white box", 
        "show",
        "put the small blue pyramid on the small green block",
        "show",
        "find things at position with white box"
    ])
    
    # Test 6: Edge cases and ambiguous commands
    test_scenario("Edge Cases and Ambiguous Commands", [
        "find green",  # Multiple green objects
        "pick up the block",  # Multiple blocks
        "put something somewhere",  # Vague command
        "show me everything",  # Alternative phrasing
        "what",  # Single word command
        ""  # Empty command
    ])

if __name__ == "__main__":
    main()
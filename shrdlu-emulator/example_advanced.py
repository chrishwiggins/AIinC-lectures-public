#!/usr/bin/env python3
"""
Advanced SHRDLU Example Script
Demonstrates complex block manipulation scenarios
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

def main():
    print("=== Advanced SHRDLU Manipulation Examples ===\n")
    
    # Example 1: Complex stacking scenario
    print("Example 1: Building a tower")
    print("-" * 40)
    commands1 = [
        "show",
        "put the small green block on the large red block",
        "show",
        "put the medium yellow block on the small green block",
        "show"
    ]
    
    print("Commands:")
    for i, cmd in enumerate(commands1, 1):
        print(f"  {i}. {cmd}")
    
    output1 = run_shrdlu_commands(commands1)
    print("\nOutput:")
    print(output1)
    print("\n" + "="*60 + "\n")
    
    # Example 2: Trying impossible moves
    print("Example 2: Impossible operations")
    print("-" * 40)
    commands2 = [
        "show",
        "pick up the large red block",
        "put the large white box on the small blue pyramid",
        "put the small green pyramid on the medium yellow block"
    ]
    
    print("Commands:")
    for i, cmd in enumerate(commands2, 1):
        print(f"  {i}. {cmd}")
    
    output2 = run_shrdlu_commands(commands2)
    print("\nOutput:")
    print(output2)
    print("\n" + "="*60 + "\n")
    
    # Example 3: Multiple object queries
    print("Example 3: Complex queries and descriptions")
    print("-" * 40)
    commands3 = [
        "find all small blocks",
        "find green things",
        "where are the pyramids",
        "pick up the red thing",
        "show"
    ]
    
    print("Commands:")
    for i, cmd in enumerate(commands3, 1):
        print(f"  {i}. {cmd}")
    
    output3 = run_shrdlu_commands(commands3)
    print("\nOutput:")
    print(output3)
    print("\n" + "="*60 + "\n")
    
    # Example 4: Sequential manipulation
    print("Example 4: Step-by-step world reconstruction")
    print("-" * 40)
    commands4 = [
        "show",
        "put the small blue pyramid on the large white box",
        "show",
        "put the small green pyramid on the small blue pyramid",
        "show",
        "put the small green block on the medium yellow block",
        "show"
    ]
    
    print("Commands:")
    for i, cmd in enumerate(commands4, 1):
        print(f"  {i}. {cmd}")
    
    output4 = run_shrdlu_commands(commands4)
    print("\nOutput:")
    print(output4)

if __name__ == "__main__":
    main()
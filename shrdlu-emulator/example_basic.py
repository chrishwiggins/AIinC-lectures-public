#!/usr/bin/env python3
"""
Basic SHRDLU Example Script
Demonstrates simple interactions with the block world
"""

import subprocess
import time
from typing import List

def run_shrdlu_commands(commands: List[str]) -> str:
    """Run a series of commands through the SHRDLU emulator"""
    
    # Create input for the process
    input_text = "\n".join(commands) + "\nquit\n"
    
    # Run SHRDLU with the commands
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
    print("=== Basic SHRDLU Interaction Examples ===\n")
    
    # Example 1: Show world and get help
    print("Example 1: Initial exploration")
    print("-" * 40)
    commands1 = [
        "show",
        "help"
    ]
    
    print("Commands:", " -> ".join(commands1))
    output1 = run_shrdlu_commands(commands1)
    print("Output:")
    print(output1)
    print("\n" + "="*60 + "\n")
    
    # Example 2: Find blocks
    print("Example 2: Finding blocks")
    print("-" * 40)
    commands2 = [
        "find red blocks",
        "find pyramids",
        "where is the green block"
    ]
    
    print("Commands:", " -> ".join(commands2))
    output2 = run_shrdlu_commands(commands2)
    print("Output:")
    print(output2)
    print("\n" + "="*60 + "\n")
    
    # Example 3: Simple pickup attempts
    print("Example 3: Picking up blocks")
    print("-" * 40)
    commands3 = [
        "pick up the small green block",
        "show",
        "pick up the blue pyramid",
        "show"
    ]
    
    print("Commands:", " -> ".join(commands3))
    output3 = run_shrdlu_commands(commands3)
    print("Output:")
    print(output3)
    print("\n" + "="*60 + "\n")
    
    # Example 4: Trying to move blocks
    print("Example 4: Moving blocks around")
    print("-" * 40)
    commands4 = [
        "put the small green pyramid on the large white box",
        "show",
        "put the small blue pyramid on the medium yellow block",
        "show"
    ]
    
    print("Commands:", " -> ".join(commands4))
    output4 = run_shrdlu_commands(commands4)
    print("Output:")
    print(output4)

if __name__ == "__main__":
    main()
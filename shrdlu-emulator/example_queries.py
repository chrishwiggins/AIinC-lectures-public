#!/usr/bin/env python3
"""
SHRDLU Query and Search Example Script
Demonstrates various ways to query and search the block world
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
    print("=== SHRDLU Query and Search Examples ===\n")
    
    # Example 1: Color-based searches
    print("Example 1: Searching by color")
    print("-" * 40)
    commands1 = [
        "find red blocks",
        "find green things",
        "find blue objects",
        "where is the yellow block",
        "find white items"
    ]
    
    print("Commands:")
    for i, cmd in enumerate(commands1, 1):
        print(f"  {i}. {cmd}")
    
    output1 = run_shrdlu_commands(commands1)
    print("\nOutput:")
    print(output1)
    print("\n" + "="*60 + "\n")
    
    # Example 2: Shape-based searches
    print("Example 2: Searching by shape")
    print("-" * 40)
    commands2 = [
        "find all blocks",
        "find pyramids",
        "where are the boxes",
        "find cubes"
    ]
    
    print("Commands:")
    for i, cmd in enumerate(commands2, 1):
        print(f"  {i}. {cmd}")
    
    output2 = run_shrdlu_commands(commands2)
    print("\nOutput:")
    print(output2)
    print("\n" + "="*60 + "\n")
    
    # Example 3: Size-based searches
    print("Example 3: Searching by size")
    print("-" * 40)
    commands3 = [
        "find small things",
        "find large objects",
        "find medium blocks",
        "where are the big items",
        "find little pyramids"
    ]
    
    print("Commands:")
    for i, cmd in enumerate(commands3, 1):
        print(f"  {i}. {cmd}")
    
    output3 = run_shrdlu_commands(commands3)
    print("\nOutput:")
    print(output3)
    print("\n" + "="*60 + "\n")
    
    # Example 4: Combined attribute searches
    print("Example 4: Multi-attribute searches")
    print("-" * 40)
    commands4 = [
        "find small red blocks",
        "find large green pyramids",
        "where is the medium yellow block",
        "find small blue things",
        "find large white boxes"
    ]
    
    print("Commands:")
    for i, cmd in enumerate(commands4, 1):
        print(f"  {i}. {cmd}")
    
    output4 = run_shrdlu_commands(commands4)
    print("\nOutput:")
    print(output4)
    print("\n" + "="*60 + "\n")
    
    # Example 5: World state queries
    print("Example 5: World state and display commands")
    print("-" * 40)
    commands5 = [
        "show",
        "display",
        "what is there",
        "what do you see"
    ]
    
    print("Commands:")
    for i, cmd in enumerate(commands5, 1):
        print(f"  {i}. {cmd}")
    
    output5 = run_shrdlu_commands(commands5)
    print("\nOutput:")
    print(output5)

if __name__ == "__main__":
    main()
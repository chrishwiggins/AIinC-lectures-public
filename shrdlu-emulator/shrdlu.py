#!/usr/bin/env python3
"""
SHRDLU Emulator
A recreation of Terry Winograd's famous natural language understanding system
that could manipulate blocks in a virtual world.
"""

import re
import random
from typing import List, Dict, Optional, Tuple, Set
from dataclasses import dataclass
from enum import Enum

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
    WHITE = "white"
    BLACK = "black"

class Shape(Enum):
    BLOCK = "block"
    PYRAMID = "pyramid"
    BOX = "box"

class Size(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

@dataclass
class Block:
    id: str
    color: Color
    shape: Shape
    size: Size
    x: int = 0
    y: int = 0
    z: int = 0
    
    def __str__(self):
        return f"{self.size.value} {self.color.value} {self.shape.value}"

class BlockWorld:
    def __init__(self):
        self.blocks: Dict[str, Block] = {}
        self.table_size = (10, 10)
        self.setup_initial_world()
    
    def setup_initial_world(self):
        """Create initial block configuration"""
        blocks_config = [
            ("a", Color.RED, Shape.BLOCK, Size.LARGE, 2, 2, 0),
            ("b", Color.GREEN, Shape.BLOCK, Size.SMALL, 3, 2, 0),
            ("c", Color.BLUE, Shape.PYRAMID, Size.SMALL, 2, 2, 1),
            ("d", Color.YELLOW, Shape.BLOCK, Size.MEDIUM, 5, 5, 0),
            ("e", Color.WHITE, Shape.BOX, Size.LARGE, 1, 1, 0),
            ("f", Color.GREEN, Shape.PYRAMID, Size.SMALL, 7, 3, 0),
        ]
        
        for block_id, color, shape, size, x, y, z in blocks_config:
            self.blocks[block_id] = Block(block_id, color, shape, size, x, y, z)
    
    def get_blocks_at_position(self, x: int, y: int) -> List[Block]:
        """Get all blocks at a specific x,y position, sorted by z (height)"""
        blocks = [b for b in self.blocks.values() if b.x == x and b.y == y]
        return sorted(blocks, key=lambda b: b.z)
    
    def get_top_block_at(self, x: int, y: int) -> Optional[Block]:
        """Get the topmost block at a position"""
        blocks = self.get_blocks_at_position(x, y)
        return blocks[-1] if blocks else None
    
    def can_place_block(self, block: Block, x: int, y: int) -> bool:
        """Check if a block can be placed at position"""
        if x < 0 or x >= self.table_size[0] or y < 0 or y >= self.table_size[1]:
            return False
        
        blocks_below = self.get_blocks_at_position(x, y)
        if not blocks_below:
            block.z = 0
            return True
        
        top_block = blocks_below[-1]
        if top_block.shape == Shape.PYRAMID:
            return False
        
        block.z = top_block.z + 1
        return True
    
    def move_block(self, block: Block, target_x: int, target_y: int) -> bool:
        """Move a block to a new position"""
        current_pos = self.get_blocks_at_position(block.x, block.y)
        
        if current_pos and current_pos[-1] != block:
            return False
        
        if not self.can_place_block(block, target_x, target_y):
            return False
        
        old_x, old_y = block.x, block.y
        block.x = target_x
        block.y = target_y
        
        self.restack_at_position(old_x, old_y)
        return True
    
    def restack_at_position(self, x: int, y: int):
        """Restack blocks at a position after one is removed"""
        blocks = self.get_blocks_at_position(x, y)
        for i, block in enumerate(blocks):
            block.z = i
    
    def find_blocks(self, color: Optional[Color] = None, shape: Optional[Shape] = None, 
                   size: Optional[Size] = None) -> List[Block]:
        """Find blocks matching criteria"""
        matches = []
        for block in self.blocks.values():
            if color and block.color != color:
                continue
            if shape and block.shape != shape:
                continue
            if size and block.size != size:
                continue
            matches.append(block)
        return matches
    
    def display_world(self) -> str:
        """Create a visual representation of the world"""
        result = []
        result.append("Current world state:")
        result.append("=" * 50)
        
        positions = {}
        for block in self.blocks.values():
            key = (block.x, block.y)
            if key not in positions:
                positions[key] = []
            positions[key].append(block)
        
        for key in sorted(positions.keys()):
            x, y = key
            stack = sorted(positions[key], key=lambda b: b.z)
            stack_str = " -> ".join(str(b) for b in stack)
            result.append(f"Position ({x},{y}): {stack_str}")
        
        return "\n".join(result)

class NaturalLanguageProcessor:
    def __init__(self, world: BlockWorld):
        self.world = world
        self.color_map = {
            "red": Color.RED, "green": Color.GREEN, "blue": Color.BLUE,
            "yellow": Color.YELLOW, "white": Color.WHITE, "black": Color.BLACK
        }
        self.shape_map = {
            "block": Shape.BLOCK, "pyramid": Shape.PYRAMID, "box": Shape.BOX,
            "cube": Shape.BLOCK
        }
        self.size_map = {
            "small": Size.SMALL, "medium": Size.MEDIUM, "large": Size.LARGE,
            "big": Size.LARGE, "little": Size.SMALL
        }
    
    def parse_command(self, command: str) -> str:
        """Parse and execute natural language commands"""
        command = command.lower().strip()
        
        if command in ["quit", "exit", "bye"]:
            return "Goodbye!"
        
        if command in ["help", "?"]:
            return self.get_help()
        
        if "show" in command or "display" in command or "what" in command:
            return self.world.display_world()
        
        if "pick up" in command or "grab" in command:
            return self.handle_pickup(command)
        
        if "put" in command or "place" in command:
            return self.handle_put(command)
        
        if "move" in command:
            return self.handle_move(command)
        
        if "find" in command or "where" in command:
            return self.handle_find(command)
        
        if "stack" in command:
            return self.handle_stack(command)
        
        return "I don't understand that command. Type 'help' for available commands."
    
    def extract_block_description(self, text: str) -> Tuple[Optional[Color], Optional[Shape], Optional[Size]]:
        """Extract color, shape, and size from text"""
        color = None
        shape = None
        size = None
        
        for word in text.split():
            if word in self.color_map:
                color = self.color_map[word]
            elif word in self.shape_map:
                shape = self.shape_map[word]
            elif word in self.size_map:
                size = self.size_map[word]
        
        return color, shape, size
    
    def find_matching_blocks(self, description: str) -> List[Block]:
        """Find blocks matching a description"""
        color, shape, size = self.extract_block_description(description)
        return self.world.find_blocks(color, shape, size)
    
    def handle_pickup(self, command: str) -> str:
        """Handle pickup commands"""
        matches = self.find_matching_blocks(command)
        
        if not matches:
            return "I can't find any blocks matching that description."
        
        if len(matches) > 1:
            descriptions = [str(b) for b in matches]
            return f"Which one? I see: {', '.join(descriptions)}"
        
        block = matches[0]
        current_pos = self.world.get_blocks_at_position(block.x, block.y)
        
        if current_pos[-1] != block:
            return f"I can't pick up the {block} because there's something on top of it."
        
        return f"OK, I'm holding the {block}."
    
    def handle_put(self, command: str) -> str:
        """Handle put/place commands"""
        if "on" in command:
            parts = command.split(" on ")
            if len(parts) == 2:
                source_desc = parts[0].replace("put", "").replace("place", "").strip()
                target_desc = parts[1].strip()
                
                source_blocks = self.find_matching_blocks(source_desc)
                target_blocks = self.find_matching_blocks(target_desc)
                
                if not source_blocks:
                    return "I can't find the block you want to move."
                if not target_blocks:
                    return "I can't find the target block."
                
                source = source_blocks[0]
                target = target_blocks[0]
                
                if self.world.move_block(source, target.x, target.y):
                    return f"OK, I put the {source} on the {target}."
                else:
                    return f"I can't put the {source} on the {target}."
        
        return "I don't understand where you want me to put it."
    
    def handle_move(self, command: str) -> str:
        """Handle move commands"""
        return "Move commands not fully implemented yet."
    
    def handle_find(self, command: str) -> str:
        """Handle find/where commands"""
        matches = self.find_matching_blocks(command)
        
        if not matches:
            return "I can't find any blocks matching that description."
        
        result = []
        for block in matches:
            result.append(f"The {block} is at position ({block.x},{block.y})")
        
        return "\n".join(result)
    
    def handle_stack(self, command: str) -> str:
        """Handle stack commands"""
        return "Stack commands not fully implemented yet."
    
    def get_help(self) -> str:
        """Return help text"""
        return """Available commands:
- show/display/what - Show the current world state
- pick up <description> - Pick up a block (e.g., "pick up the red block")
- put <block> on <target> - Put one block on another
- find/where <description> - Find blocks matching description
- help/? - Show this help
- quit/exit/bye - Exit the program

Block descriptions can include:
- Colors: red, green, blue, yellow, white, black
- Shapes: block, pyramid, box, cube
- Sizes: small, medium, large, big, little

Example: "pick up the small red pyramid"
"""

class SHRDLU:
    def __init__(self):
        self.world = BlockWorld()
        self.nlp = NaturalLanguageProcessor(self.world)
        self.running = True
    
    def run(self):
        """Main interaction loop"""
        print("SHRDLU Block World Emulator")
        print("Type 'help' for available commands, 'quit' to exit")
        print()
        print(self.world.display_world())
        print()
        
        while self.running:
            try:
                command = input("SHRDLU> ").strip()
                if not command:
                    continue
                
                response = self.nlp.parse_command(command)
                print(response)
                
                if command.lower() in ["quit", "exit", "bye"]:
                    self.running = False
                
                print()
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

if __name__ == "__main__":
    shrdlu = SHRDLU()
    shrdlu.run()